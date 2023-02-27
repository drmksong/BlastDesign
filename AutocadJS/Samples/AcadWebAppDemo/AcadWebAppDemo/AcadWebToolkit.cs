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
using Amazon.SimpleDB.Model;
using Amazon.SimpleDB;
using System.Runtime.Serialization.Json;
using System.IO;
using System.Text;
using Amazon.S3.Model;
using Amazon.S3;

namespace AcadWebAppDemo
{
    public class AcadWebToolkit
    {
        /////////////////////////////////////////////////////////////////////////////
        // Checks if SimpleDb domain exists
        //
        /////////////////////////////////////////////////////////////////////////////
        public static bool HasDomain(AmazonSimpleDB sdbClient, string domain)
        {
            try
            {
                ListDomainsResponse sdbListDomainsResponse =
                    sdbClient.ListDomains(new ListDomainsRequest());

                if (sdbListDomainsResponse.IsSetListDomainsResult())
                {
                    ListDomainsResult listDomainsResult =
                        sdbListDomainsResponse.ListDomainsResult;

                    foreach (String str in listDomainsResult.DomainName)
                    {
                        if (str == domain)
                            return true;
                    }
                }

                return false;
            }
            catch
            {
                return false;
            }
        }

        /////////////////////////////////////////////////////////////////////////////
        // Creates SimpleDb Domain
        //
        /////////////////////////////////////////////////////////////////////////////
        public static bool CreateDomain(AmazonSimpleDB sdbClient, string domain)
        {
            try
            {
                CreateDomainRequest request = new CreateDomainRequest()
                    .WithDomainName(domain);

                CreateDomainResponse response = sdbClient.CreateDomain(request);

                return true;
            }
            catch
            {
                return false;
            }
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        public static T ToObjectFromJSON<T>(string jsonString)
        {
            var serializer = new DataContractJsonSerializer(typeof(T));

            using (var memoryStream =
                new MemoryStream(Encoding.Unicode.GetBytes(jsonString)))
            {
                var newObject = (T)serializer.ReadObject(memoryStream);
                memoryStream.Close();

                return newObject;
            }
        }

        /////////////////////////////////////////////////////////////////////////////
        // Checks if S3 bucket exists
        //
        /////////////////////////////////////////////////////////////////////////////
        public static bool HasBucket(AmazonS3 s3Client, string bucketName)
        {
            try
            {
                using (ListBucketsResponse response = s3Client.ListBuckets())
                {
                    foreach (S3Bucket bucket in response.Buckets)
                    {
                        if (bucket.BucketName == bucketName)
                            return true;
                    }
                }

                return false;
            }
            catch (AmazonS3Exception amazonS3Exception)
            {
                return false;
            }
        }

        /////////////////////////////////////////////////////////////////////////////
        // creates S3 bucket
        //
        /////////////////////////////////////////////////////////////////////////////
        public static bool CreateBucket(AmazonS3 s3Client, string bucketName)
        {
            try
            {
                PutBucketRequest request = new PutBucketRequest()
                    .WithBucketName(bucketName);

                s3Client.PutBucket(request);

                return true;
            }
            catch (AmazonS3Exception amazonS3Exception)
            {
                return false;
            }
        }
    }
}