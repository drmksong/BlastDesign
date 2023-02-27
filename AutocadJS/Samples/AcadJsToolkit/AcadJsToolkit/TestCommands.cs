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
using Autodesk.AutoCAD.Runtime;
using Autodesk.AutoCAD.ApplicationServices;
using Autodesk.AutoCAD.EditorInput;
using Autodesk.AutoCAD.DatabaseServices;

[assembly: CommandClass(typeof(AcadJsToolkit.TestCommands))]

namespace AcadJsToolkit
{
    class TestCommands
    {
        [CommandMethod("acdbEntGet")]
        public void acdbEntGet()
        {
            Document doc = Application.DocumentManager.MdiActiveDocument;
            Editor ed = doc.Editor;

            PromptEntityResult per = ed.GetEntity("\nSelect an Entity: ");

            if (per.Status != PromptStatus.OK)
                return;

            Imports.ads_name name = new Imports.ads_name();

            // extract the id into an ename
            int result = Imports.acdbGetAdsName(ref name, per.ObjectId);

            // now I have the ename lets entget it into a result buffer
            ResultBuffer rb = new ResultBuffer();
            Autodesk.AutoCAD.Runtime.Interop.AttachUnmanagedObject(
                rb,
                Imports.acdbEntGet(ref name),
                true);

            // print out what we have
            ResultBufferEnumerator iter = rb.GetEnumerator();

            while (iter.MoveNext())
            {
                TypedValue TmpVal = (TypedValue)iter.Current;

                string strValue = (TmpVal.Value != null ? TmpVal.Value.ToString() : "*Nothing*");

                ed.WriteMessage("\n - Code: " + TmpVal.TypeCode.ToString() + "  = " + strValue);
            }
        }

        [CommandMethod("acdbEntGetX")]
        public void acdbEntGetX()
        {
            Document doc = Application.DocumentManager.MdiActiveDocument;
            Editor ed = doc.Editor;

            PromptEntityResult per = ed.GetEntity("\nSelect an Entity: ");

            if (per.Status != PromptStatus.OK)
                return;

            Imports.ads_name ename = new Imports.ads_name();

            int result = Imports.acdbGetAdsName(ref ename, per.ObjectId);

            ResultBuffer args = new ResultBuffer(new TypedValue(1001, "MyApp"));

            ResultBuffer rb = new ResultBuffer();
            Interop.AttachUnmanagedObject(
                rb,
                Imports.acdbEntGetX(ref ename, args.UnmanagedObject),
                true);

            ResultBufferEnumerator iter = rb.GetEnumerator();

            while (iter.MoveNext())
            {
                TypedValue TmpVal = (TypedValue)iter.Current;

                string strValue = (TmpVal.Value != null ? TmpVal.Value.ToString() : "*Nothing*");

                ed.WriteMessage("\n - Code: " + TmpVal.TypeCode.ToString() + "  = " + strValue);
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

            entitiesStr = JsToolkit.Ents2String(psr.Value.GetObjectIds());

            ed.WriteMessage("\n - Result: " + (entitiesStr != null ? entitiesStr : "*Error*"));
        }

        [CommandMethod("String2EntsCmd")]
        public void String2EntsCmd()
        {
            if (entitiesStr != null)
                JsToolkit.String2Ents(entitiesStr);
        }
    }
}
