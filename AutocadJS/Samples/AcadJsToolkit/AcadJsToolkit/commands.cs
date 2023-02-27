// (C) Copyright 2013 by  
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

[assembly: CommandClass(typeof(AcadJsToolkit.AcadCommands))]

namespace AcadJsToolkit
{
    public class Imports
    {
        public struct ads_name
        {
            public IntPtr a;
            public IntPtr b;
        };

        [DllImport("acdb19.dll", CallingConvention = CallingConvention.Cdecl,                        
           EntryPoint = "?acdbGetAdsName@@YA?AW4ErrorStatus@Acad@@AAY01JVAcDbObjectId@@@Z")]
        static extern int acdbGetAdsName32(ref ads_name name, ObjectId objId);

         [DllImport("acdb19.dll", CallingConvention = CallingConvention.Cdecl,                        
           EntryPoint = "?acdbGetAdsName@@YA?AW4ErrorStatus@Acad@@AEAY01_JVAcDbObjectId@@@Z")]
        static extern int acdbGetAdsName64(ref ads_name name, ObjectId objId);

        public static int acdbGetAdsName(ref ads_name name, ObjectId objId)
        {
             if (Marshal.SizeOf(IntPtr.Zero) > 4)
                return acdbGetAdsName64(ref name, objId);

            return acdbGetAdsName32(ref name, objId);
        }
        
        [DllImport("accore.dll", 
            CharSet = CharSet.Unicode, 
            CallingConvention = CallingConvention.Cdecl, 
            EntryPoint = "acdbEntGet")]
        public static extern System.IntPtr acdbEntGet(ref ads_name ename);

        [DllImport("accore.dll", 
            CharSet = CharSet.Unicode, 
            CallingConvention = CallingConvention.Cdecl, 
            EntryPoint = "acdbEntMake")]
        public static extern int acdbEntMake(System.IntPtr rb);

        public enum DataType
        { 
            RTNONE =    5000, /* No result */
            RTREAL =    5001, /*Real number */
            RTPOINT =   5002, /* 2D point X and Y only */
            RTSHORT =   5003, /* Short integer */
            RTANG =     5004, /* Angle */
            RTSTR =     5005, /* String */
            RTENAME =   5006, /* Entity name */
            RTPICKS =   5007, /* Pick set */
            RTORINT =   5008, /* Orientation */
            RT3DPOINT = 5009, /* 3D point - X, Y, and Z */
            RTLONG =    5010, /* Long integer */
            RTVOID =    5014, /* Blank symbol */
            RTLB =      5016, /* list begin */
            RTLE  =     5017, /* list end */
            RTDOTE =    5018, /* dotted pair */
            RTNIL =     5019, /* nil */
            RTDXF0 =    5020, /* DXF code 0 for ads_buildlist only */
            RTT =       5021, /* T atom */
            RTRESBUF =  5023, /* resbuf */
            RTMODELESS =5027, /* interrupted by modeless dialog */
            RTNEG1      = -1,
            RTNEG4      = -4
        }
    }

    public class AcadCommands
    {
        public string Ent2String(ObjectId id) 
        {
            try
            {
                Imports.ads_name name = new Imports.ads_name();

                int result = Imports.acdbGetAdsName(ref name, id);

                ResultBuffer rb = new ResultBuffer();
                Autodesk.AutoCAD.Runtime.Interop.AttachUnmanagedObject(
                    rb,
                    Imports.acdbEntGet(ref name),
                    true);

                ResultBufferEnumerator iter = rb.GetEnumerator();

                string res = string.Empty;

                bool next = iter.MoveNext();

                while (next)
                {
                    TypedValue TmpVal = (TypedValue)iter.Current;

                    next = iter.MoveNext();

                    string strValue = (TmpVal.Value != null ? TmpVal.Value.ToString() : "*Nothing*");

                    res += TmpVal.TypeCode.ToString() + "*" + strValue + (next ? "|" : "");
                }

                return res;
            }
            catch
            {
                return null;
            }
        }

        public string Ents2String(ObjectId[] ids)
        {
            string res = string.Empty;

            foreach (ObjectId id in ids)
            {
                string ent = Ent2String(id);

                if (ent != null)
                    res += (res != string.Empty ? "!" : "") + ent;
            }

            return res;
        }

        Imports.DataType dxfCodeToDataType(int dxfCode)
        {
            if ((dxfCode >= 0) && (dxfCode <= 9))
                return Imports.DataType.RTSTR;
            else if ((dxfCode >= 10) && (dxfCode <= 17))
                return Imports.DataType.RT3DPOINT;
            else if ((dxfCode >= 38) && (dxfCode <= 59))
                return Imports.DataType.RTREAL;
            else if ((dxfCode >= 60) && (dxfCode <= 79))
                return Imports.DataType.RTSHORT;
            else if ((dxfCode >= 90) && (dxfCode <= 99))
                return Imports.DataType.RTLONG;
            else if ((dxfCode == 100) ||
                (dxfCode == 101) ||
                (dxfCode == 102) ||
                (dxfCode == 105))
                return Imports.DataType.RTSTR;
            else if ((dxfCode >= 110) && (dxfCode <= 119))
                return Imports.DataType.RT3DPOINT;
            else if ((dxfCode >= 140) && (dxfCode <= 149))
                return Imports.DataType.RTREAL;
            else if ((dxfCode >= 170) && (dxfCode <= 179))
                return Imports.DataType.RTSHORT;
            else if ((dxfCode >= 210) && (dxfCode <= 219))
                return Imports.DataType.RT3DPOINT;
            else if ((dxfCode >= 270) && (dxfCode <= 299))
                return Imports.DataType.RTSHORT;
            else if ((dxfCode >= 300) && (dxfCode <= 309))
                return Imports.DataType.RTSTR;
            else if ((dxfCode >= 310) && (dxfCode <= 369))
                return Imports.DataType.RTENAME;
            else if ((dxfCode >= 370) && (dxfCode <= 379))
                return Imports.DataType.RTSHORT;
            else if ((dxfCode >= 380) && (dxfCode <= 389))
                return Imports.DataType.RTSHORT;
            else if ((dxfCode >= 390) && (dxfCode <= 399))
                return Imports.DataType.RTENAME;
            else if ((dxfCode >= 400) && (dxfCode <= 409))
                return Imports.DataType.RTSHORT;
            else if ((dxfCode >= 410) && (dxfCode <= 419))
                return Imports.DataType.RTSTR;
            else if ((dxfCode >= 999) && (dxfCode <= 1009))
                return Imports.DataType.RTSTR;
            else if ((dxfCode >= 1010) && (dxfCode <= 1013))
                return Imports.DataType.RT3DPOINT;
            else if ((dxfCode >= 1038) && (dxfCode <= 1059))
                return Imports.DataType.RTREAL;
            else if ((dxfCode >= 1060) && (dxfCode <= 1070))
                return Imports.DataType.RTSHORT;
            else if ((dxfCode == 1071))
                return Imports.DataType.RTLONG;
            else if ((dxfCode == -1))
                return Imports.DataType.RTNEG1;
            else if ((dxfCode == -4))
                return Imports.DataType.RTNEG4;
            else
                return Imports.DataType.RTNONE;
        }

        TypedValue GenerateTypedValue(string codeStr, string valueStr)
        {
            try
            {
                int dxfCode = int.Parse(codeStr);

                Imports.DataType dataType = dxfCodeToDataType(dxfCode);

                switch (dataType)
                {
                    case Imports.DataType.RTSHORT:

                        short vshort = short.Parse(valueStr);
                        return new TypedValue(dxfCode, vshort);

                    case Imports.DataType.RTLONG:

                        long vlong = long.Parse(valueStr);
                        return new TypedValue(dxfCode, vlong);

                    case Imports.DataType.RTREAL:

                        double vdbl = double.Parse(valueStr);
                        return new TypedValue(dxfCode, vdbl);

                    case Imports.DataType.RTSTR:

                        return new TypedValue(dxfCode, valueStr);

                    case Imports.DataType.RT3DPOINT:

                        string p3d = valueStr.Substring(1, valueStr.Length - 2);

                        string[] coords3d = p3d.Split(new char[] { ',' });

                        double x1 = double.Parse(coords3d[0]);
                        double y1 = double.Parse(coords3d[1]);
                        double z1 = double.Parse(coords3d[2]);

                        return new TypedValue(dxfCode, new Point3d(x1, y1, z1));

                    case Imports.DataType.RTPOINT:

                        string p2d = valueStr.Substring(1, valueStr.Length - 2);

                        string[] coords2d = p2d.Split(new char[] { ',' });

                        double x2 = double.Parse(coords2d[0]);
                        double y2 = double.Parse(coords2d[1]);

                        return new TypedValue(dxfCode, new Point2d(x2, y2));

                    case Imports.DataType.RTNEG4:

                        return new TypedValue(dxfCode, valueStr);

                    case Imports.DataType.RTNEG1:
                    case Imports.DataType.RTENAME:

                        string idStr1 = valueStr.Substring(1, valueStr.Length - 2);

                        IntPtr oldId1 = (IntPtr)long.Parse(idStr1);

                        ObjectId id1 = new ObjectId(oldId1);

                        return new TypedValue(dxfCode, id1);

                    case Imports.DataType.RTPICKS:

                        string idStr2 = valueStr.Substring(1, valueStr.Length - 2);

                        IntPtr oldId2 = (IntPtr)long.Parse(idStr2);

                        ObjectId id2 = new ObjectId(oldId2);

                        return new TypedValue(dxfCode, id2);

                    default:
                        break;
                }

                return new TypedValue(dxfCode);
            }
            catch(System.Exception ex)
            {
                Document doc = Application.DocumentManager.MdiActiveDocument;
                Editor ed = doc.Editor;

                ed.WriteMessage("\n Error parsing dxf: " + ex.Message);

                return new TypedValue();
            }
        }

        public bool String2Ents(string str)
        {
            try
            {
                string[] ents = str.Split(new char[] { '!' });

                foreach (string ent in ents)
                {
                    string[] pairs = ent.Split(new char[] { '|' });

                    List<TypedValue> typedValues = new List<TypedValue>();

                    foreach (string pair in pairs)
                    {
                        string[] typedValueStr = pair.Split(new char[] { '*' });

                        typedValues.Add(
                            GenerateTypedValue(
                                typedValueStr[0],
                                typedValueStr[1]));
                    }

                    ResultBuffer rb = new ResultBuffer(typedValues.ToArray());

                    int res = Imports.acdbEntMake(rb.UnmanagedObject);
                }

                return true;
            }
            catch
            {
                return false;
            }
        }

        string entitiesStr = null;

        [CommandMethod("Ent2StringCmd")]
        public void Ent2StringCmd()
        {
            Document doc = Application.DocumentManager.MdiActiveDocument;
            Editor ed = doc.Editor;

            PromptSelectionOptions pso = new PromptSelectionOptions();

            pso.MessageForAdding = "\nSelect Entities:";

            PromptSelectionResult psr = ed.GetSelection(pso);

            if (psr.Status != PromptStatus.OK)
                return;

            entitiesStr = Ents2String(psr.Value.GetObjectIds());

            ed.WriteMessage("\n - Result: " + (entitiesStr != null ? entitiesStr : "*Error*"));
        }

        [CommandMethod("String2EntsCmd")]
        public void String2EntsCmd()
        {
            if (entitiesStr != null)
                String2Ents(entitiesStr); 
        }

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

                string ents = Ents2String(ids);

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
                    bool res = String2Ents(args.functionParams.args);

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
