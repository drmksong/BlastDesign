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
using Amazon;
using Amazon.SimpleDB.Model;
using System.Web.Script.Serialization;

namespace AcadWebAppDemo
{
    public class AcadWebViewService
    {
        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        [DataContract]
        public class AcadViewProperties
        {
            [DataMember]
            public string Name;

            [DataMember]
            public double[] Position;

            [DataMember]
            public double[] Target;

            [DataMember]
            public double[] UpVector;

            [DataMember]
            public double FieldHeight;

            [DataMember]
            public double FieldWidth;

            [DataMember]
            public int Projection;

            public AcadViewProperties(
                string name,
                double[] pos,
                double[] target,
                double[] up,
                double fieldHeight,
                double fieldWidth,
                int projection)
            {
                Name = name;

                Position = pos;

                Target = target;

                UpVector = up;

                FieldHeight = fieldHeight;

                FieldWidth = fieldWidth;

                Projection = projection;
            }
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        static string _domainName = "AcadWebDemoViews";

        static AmazonSimpleDB _sdbClient;

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        static AcadViewProperties DbItemToDbView(Item item)
        {
            string name = string.Empty;

            double[] pos = new double[3];
            double[] target = new double[3];
            double[] up = new double[3];

            double fieldHeight = 0;
            double fieldHWidth = 0;

            int projection = 0;

            foreach (Amazon.SimpleDB.Model.Attribute attribute in item.Attribute)
            {
                switch (attribute.Name)
                {
                    case "Name":
                        name = attribute.Value;
                        break;

                    case "PosX":
                        pos[0] = double.Parse(attribute.Value);
                        break;

                    case "PosY":
                        pos[1] = double.Parse(attribute.Value);
                        break;

                    case "PosZ":
                        pos[2] = double.Parse(attribute.Value);
                        break;

                    case "TargetX":
                        target[0] = double.Parse(attribute.Value);
                        break;

                    case "TargetY":
                        target[1] = double.Parse(attribute.Value);
                        break;

                    case "TargetZ":
                        target[2] = double.Parse(attribute.Value);
                        break;

                    case "UpX":
                        up[0] = double.Parse(attribute.Value);
                        break;

                    case "UpY":
                        up[1] = double.Parse(attribute.Value);
                        break;

                    case "UpZ":
                        up[2] = double.Parse(attribute.Value);
                        break;

                    case "FieldHeight":
                        fieldHeight = double.Parse(attribute.Value);
                        break;

                    case "FieldWidth":
                        fieldHWidth = double.Parse(attribute.Value);
                        break;

                    case "Projection":
                        projection = int.Parse(attribute.Value);
                        break;

                    default:
                        break;
                }
            }

            return new AcadViewProperties(
                name,
                pos,
                target,
                up,
                fieldHeight,
                fieldHWidth,
                projection);
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        public static bool SaveView(string viewProps)
        {
            try
            {
                if (!AcadWebToolkit.HasDomain(_sdbClient, _domainName))
                    return false;

                AcadViewProperties view =
                    AcadWebToolkit.ToObjectFromJSON<AcadViewProperties>(
                        viewProps.Replace("\n", ""));

                PutAttributesRequest sDbRequest = new PutAttributesRequest()
                    .WithDomainName(_domainName)
                    .WithItemName(view.Name)
                    .WithAttribute(new ReplaceableAttribute()
                        .WithName("Name")
                        .WithValue(view.Name))

                    .WithAttribute(new ReplaceableAttribute()
                        .WithName("PosX")
                        .WithValue(view.Position[0].ToString()))
                    .WithAttribute(new ReplaceableAttribute()
                        .WithName("PosY")
                        .WithValue(view.Position[1].ToString()))
                    .WithAttribute(new ReplaceableAttribute()
                        .WithName("PosZ")
                        .WithValue(view.Position[2].ToString()))

                    .WithAttribute(new ReplaceableAttribute()
                        .WithName("TargetX")
                        .WithValue(view.Target[0].ToString()))
                    .WithAttribute(new ReplaceableAttribute()
                        .WithName("TargetY")
                        .WithValue(view.Target[1].ToString()))
                    .WithAttribute(new ReplaceableAttribute()
                        .WithName("TargetZ")
                        .WithValue(view.Target[2].ToString()))

                    .WithAttribute(new ReplaceableAttribute()
                        .WithName("UpX")
                        .WithValue(view.UpVector[0].ToString()))
                    .WithAttribute(new ReplaceableAttribute()
                        .WithName("UpY")
                        .WithValue(view.UpVector[1].ToString()))
                    .WithAttribute(new ReplaceableAttribute()
                        .WithName("UpZ")
                        .WithValue(view.UpVector[2].ToString()))

                    .WithAttribute(new ReplaceableAttribute()
                        .WithName("FieldHeight")
                        .WithValue(view.FieldHeight.ToString()))
                    .WithAttribute(new ReplaceableAttribute()
                        .WithName("FieldWidth")
                        .WithValue(view.FieldWidth.ToString()))
                    .WithAttribute(new ReplaceableAttribute()
                        .WithName("Projection")
                        .WithValue(view.Projection.ToString()));

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
        public static string LoadView(string viewName)
        {
            try
            {
                String expression =
                    "Select " +
                    "Name, " +

                    "PosX, " +
                    "PosY, " +
                    "PosZ, " +

                    "TargetX, " +
                    "TargetY, " +
                    "TargetZ, " +

                    "UpX, " +
                    "UpY, " +
                    "UpZ, " +

                    "FieldHeight, " +
                    "FieldWidth, " +
                    "Projection " +

                    "From " + _domainName +
                    " Where Name = '" + viewName + "'";

                SelectRequest request = new SelectRequest()
                    .WithSelectExpression(expression);

                SelectResponse response = _sdbClient.Select(request);

                if (!response.IsSetSelectResult())
                    return null;

                SelectResult result = response.SelectResult;

                if (result.Item.Count < 1)
                    return null;

                AcadViewProperties view = DbItemToDbView(result.Item[0]);

                JavaScriptSerializer serializer =
                    new JavaScriptSerializer();

                return serializer.Serialize(view);
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
        public static string GetViews()
        {
            try
            {
                String expression =
                    "Select " +
                    "Name, " +

                    "PosX, " +
                    "PosY, " +
                    "PosZ, " +

                    "TargetX, " +
                    "TargetY, " +
                    "TargetZ, " +

                    "UpX, " +
                    "UpY, " +
                    "UpZ, " +

                    "FieldHeight, " +
                    "FieldWidth, " +
                    "Projection " +

                    "From " + _domainName;

                SelectRequest request = new SelectRequest()
                    .WithSelectExpression(expression);

                SelectResponse response = _sdbClient.Select(request);

                if (!response.IsSetSelectResult())
                    return null;

                List<AcadViewProperties> views = new List<AcadViewProperties>();

                SelectResult result = response.SelectResult;

                foreach (Item item in result.Item)
                    views.Add(DbItemToDbView(item));

                JavaScriptSerializer serializer =
                    new JavaScriptSerializer();

                return serializer.Serialize(views.ToArray());
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
        public static bool ClearViews()
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
        }
    }
}