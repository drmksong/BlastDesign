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
using Autodesk.AutoCAD.Runtime;
using Autodesk.AutoCAD.ApplicationServices;
using Autodesk.AutoCAD.DatabaseServices;
using Autodesk.AutoCAD.Geometry;
using Autodesk.AutoCAD.EditorInput;
using System.Runtime.InteropServices;
using System.Collections.Generic;
using Newtonsoft.Json;
using System.Globalization;

[assembly: CommandClass(typeof(AcadJsToolkit.Callbacks))]

namespace AcadJsToolkit
{
    public class Callbacks
    {
        //"{
        //      \"functionName\":\"EntToString\",
        //      \"invokeAsCommand\":false,
        //      \"functionParams\":
        //          {\"args\":
        //              [
        //                  {\"objectId\":\"7f66c605dc0\",\"gsMarker\":\"0\"},
        //                  {\"objectId\":\"7f66c605dd0\",\"gsMarker\":\"0\"}
        //              ],
        //          \"contextID\":2},
        //      \"onComplete\":\"EntToString_complete\",
        //      \"onError\":\"EntToString_error\"}"

        public class AcadArgsRead
        {
            public string functionName;
            public bool invokeAsCommand;
            public FunctionParams functionParams;

            public class FunctionParams
            {
                public Arg[] args;
                public int contextID;

                public class Arg
                {
                    public string objectId;
                    public int gsMarker;
                }
            }

            public string onComplete;
            public string onError;

            public ObjectId[] GetObjectIds()
            {
                List<ObjectId> ids = new List<ObjectId>();

                foreach (FunctionParams.Arg arg in functionParams.args)
                {
                    IntPtr oldId = (IntPtr)long.Parse(
                        arg.objectId, NumberStyles.HexNumber);

                    ObjectId id = new ObjectId(oldId);

                    ids.Add(id);
                }

                return ids.ToArray();
            }
        }

        [JavaScriptCallback("EntToString")]
        public string EntToString(string jsonArgs)
        {
            Document doc = Application.DocumentManager.MdiActiveDocument;
            Editor ed = doc.Editor;

            try 
            {
                var args = JsonConvert.DeserializeObject<AcadArgsRead>(jsonArgs);

                ObjectId[] ids = args.GetObjectIds();

                string ents = JsToolkit.Ents2String(ids);

                string jsonRes = "{\"retCode\":0, \"result\":\"" + ents + "\"}";

                return jsonRes;
            }
            catch (System.Exception ex)
            {
                ed.WriteMessage("\n Error reading entities...");

                string jsonRes = "{\"retCode\":-1, \"result\":\"" + "false" + "\"}";

                return jsonRes;
            }
        }

        //"{
        //      \"functionName\":\"StringToEnt\",
        //      \"invokeAsCommand\":true,
        //      \"functionParams\":
        //          {
        //              \"args\":\"-1*(8754959506896)|0*LINE|330*(8754959497712)|5*1D5|100*AcDbEntity|67*0|410*Model|8*0|100*AcDbLine|10*(41.3013764411391,40.4131187458543,0)|11*(48.1569453387673,33.1609856571364,0)|210*(0,0,1)!-1*(8754959506880)|0*LINE|330*(8754959497712)|5*1D4|100*AcDbEntity|67*0|410*Model|8*0|100*AcDbLine|10*(37.268688847087,12.2909582891659,0)|11*(41.3013764411391,40.4131187458543,0)|210*(0,0,1)\",
        //              \"contextID\":2
        //          },
        //      \"onComplete\":\"StringToEnt_complete\",
        //      \"onError\":\"StringToEnt_error\"
        //}"

        public class AcadArgsWrite
        {
            public string functionName;
            public bool invokeAsCommand;
            public FunctionParams functionParams;

            public class FunctionParams
            {
                public string args;
                public int contextID;
            }

            public string onComplete;
            public string onError;
        }

        [JavaScriptCallback("StringToEnt")]
        public string StringToEnt(string jsonArgs)
        {
            Document doc = Application.DocumentManager.MdiActiveDocument;
            Editor ed = doc.Editor;

            try 
            {
                var args = JsonConvert.DeserializeObject<AcadArgsWrite>(jsonArgs);

                using (doc.LockDocument())
                {
                    bool res = JsToolkit.String2Ents(args.functionParams.args);

                    string jsonRes = "{\"retCode\":0, \"result\":\"" + res.ToString() + "\"}";

                    return jsonRes;
                }
            }
            catch(System.Exception ex)
            {
                ed.WriteMessage("\n Error creating entities...");

                string jsonRes = "{\"retCode\":-1, \"result\":\"" + "false" + "\"}"; 

                return jsonRes;
            }
        }
    }
}
