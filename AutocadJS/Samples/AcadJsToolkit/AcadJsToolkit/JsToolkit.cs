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
using System.Text;
using System.Runtime.InteropServices;
using Autodesk.AutoCAD.DatabaseServices;
using Autodesk.AutoCAD.Geometry;
using Autodesk.AutoCAD.ApplicationServices;
using Autodesk.AutoCAD.EditorInput;

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
            EntryPoint = "acdbEntGetX")]
        public static extern System.IntPtr acdbEntGetX(ref ads_name ename, IntPtr rb);

        [DllImport("accore.dll",
            CharSet = CharSet.Unicode,
            CallingConvention = CallingConvention.Cdecl,
            EntryPoint = "acdbEntMake")]
        public static extern int acdbEntMake(System.IntPtr rb);

        public enum DataType
        {
            RTNONE = 5000, /* No result */
            RTREAL = 5001, /*Real number */
            RTPOINT = 5002, /* 2D point X and Y only */
            RTSHORT = 5003, /* Short integer */
            RTANG = 5004, /* Angle */
            RTSTR = 5005, /* String */
            RTENAME = 5006, /* Entity name */
            RTPICKS = 5007, /* Pick set */
            RTORINT = 5008, /* Orientation */
            RT3DPOINT = 5009, /* 3D point - X, Y, and Z */
            RTLONG = 5010, /* Long integer */
            RTVOID = 5014, /* Blank symbol */
            RTLB = 5016, /* list begin */
            RTLE = 5017, /* list end */
            RTDOTE = 5018, /* dotted pair */
            RTNIL = 5019, /* nil */
            RTDXF0 = 5020, /* DXF code 0 for ads_buildlist only */
            RTT = 5021, /* T atom */
            RTRESBUF = 5023, /* resbuf */
            RTMODELESS = 5027, /* interrupted by modeless dialog */
            RTNEG1 = -1,
            RTNEG4 = -4
        }
    }

    class JsToolkit
    {
        public static string Ent2String(ObjectId id)
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

        public static string Ents2String(ObjectId[] ids)
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

        static Imports.DataType dxfCodeToDataType(int dxfCode)
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

        static TypedValue GenerateTypedValue(string codeStr, string valueStr)
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
            catch (System.Exception ex)
            {
                Document doc = Application.DocumentManager.MdiActiveDocument;
                Editor ed = doc.Editor;

                ed.WriteMessage("\n Error parsing dxf: " + ex.Message);

                return new TypedValue();
            }
        }

        public static bool String2Ents(string str)
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
    }
}
