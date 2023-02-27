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
using Autodesk.AutoCAD.Geometry;
using Autodesk.AutoCAD.ApplicationServices;
using Autodesk.AutoCAD.EditorInput;
using Autodesk.AutoCAD.DatabaseServices;

[assembly: CommandClass(typeof(DotNetJsTest.DotNetCallBacks))]

namespace DotNetJsTest
{
    // Simple tests for JavaScript extensibility API in .Net
    // Philippe Leefsma, 2013
    public class DotNetCallBacks
    {
        [JavaScriptCallback("TestDotNetRead")]
        public string TestDotNetRead(string jsonArgs)
        {
            Document doc = Application.DocumentManager.MdiActiveDocument;
            Database db = doc.Database;
            Editor ed = doc.Editor;

            using (Transaction tx = doc.TransactionManager.StartTransaction())
            {
                BlockTableRecord btr = tx.GetObject(db.CurrentSpaceId, OpenMode.ForRead) 
                    as BlockTableRecord;

                foreach (ObjectId id in btr)
                {
                    ed.WriteMessage("\nEntity: " + id.ObjectClass.Name);
                }

                tx.Commit();
            }
               
            return "{\"retCode\":0, \"result\":\"OK\"}";
        }

        [JavaScriptCallback("TestDotNetWrite")]
        public string TestDotNetWrite(string jsonArgs)
        {
            Document doc = Application.DocumentManager.MdiActiveDocument;
            Database db = doc.Database;
            Editor ed = doc.Editor;

            //Lock required for a write access to db from Js invoked callback
            using (DocumentLock lk = doc.LockDocument())
            {
                using (Transaction tx = doc.TransactionManager.StartTransaction())
                {
                    BlockTableRecord btr = tx.GetObject(db.CurrentSpaceId, OpenMode.ForWrite)
                        as BlockTableRecord;

                    Circle circle = new Circle(new Point3d(10, 10, 0), Vector3d.ZAxis, 5.0);

                    btr.AppendEntity(circle);
                    tx.AddNewlyCreatedDBObject(circle, true);

                    tx.Commit();
                }
            }

            return "{\"retCode\":0, \"result\":\"OK\"}";
        }

        //Webloads a local JavaScript script (.js)
        [CommandMethod("NetWebLoad")]
        public void NetWebLoad()
        {
            string dir = System.Environment.GetFolderPath(
                System.Environment.SpecialFolder.Desktop);

            string filename = SelectFile(
                "Select script to load...", 
                "JavaScript Files (*.js)|*.js",
                dir);

            if (filename == string.Empty)
                return;

            Autodesk.AutoCAD.ApplicationServices.Core.Application.LoadJSScript(
                new Uri("file:///" + filename));
        }

        private string SelectFile(string title, string filter, string dir)
        {
            System.Windows.Forms.OpenFileDialog ofd =
                new System.Windows.Forms.OpenFileDialog();

            ofd.Filter = filter;
            ofd.Title = title;
            ofd.InitialDirectory = dir;

            if (ofd.ShowDialog() != System.Windows.Forms.DialogResult.OK)
                return string.Empty;

            return ofd.FileName;
        }
    }
}


