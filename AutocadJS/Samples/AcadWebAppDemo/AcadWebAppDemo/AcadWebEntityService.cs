// (C) Copyright 2002-2013 by Autodesk, Inc. 
//
// Permission to use, copy, modify, and distribute this software in
// object code form for any purpose and without fee is hereby granted, 
// provided that the above copyright notice appears in all copies and 
// that both that copyright notice and the limited warranty and
// restricted rights notice below appear in all supporting 
// documentation.
//
// AUTODESK PROVIDES THIS PROGRAM "AS IS" AND WITH ALL FAULTS. 
// AUTODESK SPECIFICALLY DISCLAIMS ANY IMPLIED WARRANTY OF
// MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE.  AUTODESK, INC. 
// DOES NOT WARRANT THAT THE OPERATION OF THE PROGRAM WILL BE
// UNINTERRUPTED OR ERROR FREE.
//
// Use, duplication, or disclosure by the U.S. Government is subject to 
// restrictions set forth in FAR 52.227-19 (Commercial Computer
// Software - Restricted Rights) and DFAR 252.227-7013(c)(1)(ii)
// (Rights in Technical Data and Computer Software), as applicable.
//
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Runtime.Serialization;
using Amazon.SimpleDB;
using Amazon.SimpleDB.Model;
using System.Web.Script.Serialization;
using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using System.IO;

namespace AcadWebAppDemo
{
    public class AcadWebEntityService
    {
        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        [DataContract]
        public class AcadEntityProperties
        {
            [DataMember]
            public string GroupName;

            [DataMember]
            public string DxfData;

            public AcadEntityProperties(
                string groupName,
                string dxfData)
            {
                GroupName = groupName;

                DxfData = dxfData;
            }
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        static string _domainName = "AcadWebDemoEntities";
        static string _bucketName = "AcadWebDemoEntities";

        static AmazonSimpleDB _sdbClient;
        static AmazonS3 _s3Client;

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        static AcadEntityProperties DbItemToDbEnt(Item item, string data)
        {
            string group = string.Empty;

            foreach (Amazon.SimpleDB.Model.Attribute attribute in item.Attribute)
            {
                switch (attribute.Name)
                {
                    case "GroupName":
                        group = attribute.Value;
                        break;

                    default:
                        break;
                }
            }

            return new AcadEntityProperties(group, data);
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        public static bool SaveEntities(string entProps)
        {
            try
            {
                if (!AcadWebToolkit.HasDomain(_sdbClient, _domainName))
                    return false;

                AcadEntityProperties props =
                    AcadWebToolkit.ToObjectFromJSON<AcadEntityProperties>(
                        entProps.Replace("\n", ""));


                string s3Key = props.GroupName;

                PutObjectRequest s3Request = new PutObjectRequest();

                s3Request.WithBucketName(_bucketName)
                       .WithKey(s3Key)
                       .WithContentBody(props.DxfData);

                S3Response response = _s3Client.PutObject(s3Request);
                response.Dispose();


                PutAttributesRequest sDbRequest = new PutAttributesRequest()
                    .WithDomainName(_domainName)
                    .WithItemName(props.GroupName)

                    .WithAttribute(new ReplaceableAttribute()
                        .WithName("GroupName")
                        .WithValue(props.GroupName));
                 
                PutAttributesResponse sDbResponse =
                    _sdbClient.PutAttributes(sDbRequest);

                return true;
            }
            catch (Exception ex)
            {
                return false;
            }
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        public static string LoadGroup(string groupName)
        {
            try
            {
                String expression =
                    "Select " +
                    "GroupName " +
                    "From " + _domainName +
                    " Where GroupName = '" + groupName + "'";

                SelectRequest request = new SelectRequest()
                    .WithSelectExpression(expression);

                SelectResponse response = _sdbClient.Select(request);

                if (!response.IsSetSelectResult())
                    return null;

                SelectResult result = response.SelectResult;

                if (result.Item.Count < 1)
                    return null;


                GetObjectRequest s3Request = new GetObjectRequest()
                   .WithBucketName(_bucketName)
                   .WithKey(groupName);

                using (GetObjectResponse s3Response = _s3Client.GetObject(s3Request))
                {
                    using (StreamReader reader = new StreamReader(s3Response.ResponseStream))
                    {
                        string data = reader.ReadToEnd();

                         AcadEntityProperties props = DbItemToDbEnt(result.Item[0], data);

                        JavaScriptSerializer serializer =
                            new JavaScriptSerializer();

                        return serializer.Serialize(props);
                    }
                }
            }
            catch (Exception ex)
            {
                return null;
            }
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        public static string GetEntities()
        {
            try
            {
                String expression =
                    "Select " +
                    "GroupName, " +
                    "DxfData " +
                    "From " + _domainName;

                SelectRequest request = new SelectRequest()
                    .WithSelectExpression(expression);

                SelectResponse response = _sdbClient.Select(request);

                if (!response.IsSetSelectResult())
                    return null;

                List<AcadEntityProperties> props = new List<AcadEntityProperties>();

                SelectResult result = response.SelectResult;

                foreach (Item item in result.Item)
                    props.Add(DbItemToDbEnt(item, string.Empty));

                JavaScriptSerializer serializer =
                    new JavaScriptSerializer();

                return serializer.Serialize(props.ToArray());
            }
            catch (Exception ex)
            {
                return null;
            }
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        public static bool ClearEntities()
        {
            try
            {
                string expression =
                    "Select * From " + _domainName;

                SelectRequest sDbRequest = new SelectRequest()
                    .WithSelectExpression(expression);

                SelectResponse sDbResponse = _sdbClient.Select(sDbRequest);

                if (!sDbResponse.IsSetSelectResult())
                    return false;

                SelectResult result = sDbResponse.SelectResult;

                foreach (Item item in result.Item)
                {
                    DeleteObjectRequest s3Request = new DeleteObjectRequest()
                        .WithBucketName(_bucketName)
                        .WithKey(item.Name);

                    DeleteObjectResponse s3Response = _s3Client.DeleteObject(s3Request);
                    s3Response.Dispose();

                    DeleteAttributesRequest deleteRequest =
                        new DeleteAttributesRequest()
                        .WithDomainName(_domainName)
                        .WithItemName(item.Name);

                    _sdbClient.DeleteAttributes(deleteRequest);
                }

                return true;
            }
            catch (Exception ex)
            {
                return true;
            }
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        public static void OnPageLoad(object sender, EventArgs e)
        {
            AmazonSimpleDBConfig dbConfig = new AmazonSimpleDBConfig();

            _sdbClient = AWSClientFactory.CreateAmazonSimpleDBClient(
                "*** Your AWS Access Key Here ***",
                "*** Your AWS Secret Key Here ***",
                dbConfig);

            if (!AcadWebToolkit.HasDomain(_sdbClient, _domainName))
                AcadWebToolkit.CreateDomain(_sdbClient, _domainName);

            AmazonS3Config s3Config = new AmazonS3Config();

            _s3Client = AWSClientFactory.CreateAmazonS3Client(
                "*** Your AWS Access Key Here ***",
                "*** Your AWS Secret Key Here ***",
                s3Config);

            if (!AcadWebToolkit.HasBucket(_s3Client, _bucketName))
                AcadWebToolkit.CreateBucket(_s3Client, _bucketName);
        }
    }
}