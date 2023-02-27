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
using Autodesk.AutoCAD.DatabaseServices;
using Autodesk.AutoCAD.EditorInput;
using Autodesk.AutoCAD.Geometry;
using Autodesk.AutoCAD.Colors;
using Autodesk.AutoCAD.DatabaseServices.Filters;
using Autodesk.AutoCAD.Windows.ToolPalette;
using System.Windows.Forms;
using Autodesk.AutoCAD.Windows;

[assembly: CommandClass(typeof(AcHTML.AcHTMLCmd))]
[assembly: ExtensionApplication(typeof(AcHTML.AcHTMLCmd))]

namespace AcHTML
{
    public class AcHTMLCmd: IExtensionApplication
    {
        public void RegisterMe()
        {
            //AutoCAD (or vertical) and Application keys
            Microsoft.Win32.RegistryKey acadKey =
                Microsoft.Win32.Registry.CurrentUser.OpenSubKey(
                    HostApplicationServices.Current.MachineRegistryProductRootKey);

            Microsoft.Win32.RegistryKey acadAppKey = acadKey.OpenSubKey("Applications", true);

            string curAssemblyName = System.Reflection.Assembly.GetExecutingAssembly().GetName().Name;
            string curAssemblyPath = System.Reflection.Assembly.GetExecutingAssembly().Location;
            string curAssemblyFullName = System.Reflection.Assembly.GetExecutingAssembly().GetName().FullName;

            //already registered?
            String[] subKeyNames = acadAppKey.GetSubKeyNames();

            foreach (String subKeyName in subKeyNames)
            {
                if (subKeyName.Equals(curAssemblyName))
                {
                    Microsoft.Win32.RegistryKey subkey = acadAppKey.OpenSubKey(subKeyName, true);
                    subkey.SetValue("LOADER", curAssemblyPath, Microsoft.Win32.RegistryValueKind.String);
                    subkey.Close();
                    acadAppKey.Close();
                    return;
                }
            }

            //create the addin key
            Microsoft.Win32.RegistryKey acadAppAddInKey = acadAppKey.CreateSubKey(curAssemblyName);

            acadAppAddInKey.SetValue("DESCRIPTION", curAssemblyFullName, Microsoft.Win32.RegistryValueKind.String);
            acadAppAddInKey.SetValue("LOADCTRLS", 14, Microsoft.Win32.RegistryValueKind.DWord);
            acadAppAddInKey.SetValue("LOADER", curAssemblyPath, Microsoft.Win32.RegistryValueKind.String);
            acadAppAddInKey.SetValue("MANAGED", 1, Microsoft.Win32.RegistryValueKind.DWord);

            acadAppKey.Close();
        }

        public void Initialize()
        {
            RegisterMe();
        }

        public void Terminate()
        {
        }

        private string SelectFile(string title, string filter, string dir)
        {
            System.Windows.Forms.OpenFileDialog ofd =
                new System.Windows.Forms.OpenFileDialog();

            ofd.Filter = filter;
            ofd.Title = title;
            ofd.InitialDirectory = dir;
            
            if (ofd.ShowDialog() != DialogResult.OK)
                return string.Empty;

            return ofd.FileName;
        }

        static Autodesk.AutoCAD.Windows.PaletteSet _ps = null;

        [CommandMethod("AdnJsDemo")]
        public void AdnJsDemo()
        {
            string dir = System.Environment.GetFolderPath(
                System.Environment.SpecialFolder.Desktop);

            if (System.IO.Directory.Exists(@"C:\AcHTML\UnitTests\"))
                dir = @"C:\AcHTML\UnitTests\";

            string filename = SelectFile(
                "Select Html File to load...", 
                "Html Files (*.html)|*.html",
                dir);

            if (filename == string.Empty)
                return;

            if (_ps == null)
            {
                _ps = new Autodesk.AutoCAD.Windows.PaletteSet(
                    "JavaScript Demo",
                    new Guid("730CF323-7D71-40A1-990E-F7CF81A84340"));
            }

            String url = "file:///" + filename;

            try
            {
                String tabName = "";
                Uri uri = new Uri(url);

                if (uri.IsFile)
                {
                    String[] segments = uri.Segments;

                    if (segments.Length > 0)
                    {
                        tabName = segments[segments.Length - 1];

                        String[] fileSplit = tabName.Split('.');

                        if (fileSplit.Length > 0)
                            tabName = fileSplit[0];
                    }
                }
                else
                {
                    tabName = uri.Host;
                }

                if(_ps.Count !=0) 
                {
                    _ps[0].PaletteSet.Remove(0);
                }

                // The PaletteSet.Add method takes as input an Uri
                // that can point either to a local html page or any online url
                Palette p = _ps.Add(tabName, uri);

                _ps.Visible = true;
            }
            catch (UriFormatException ex)  
            {
                // This exception will catch an empty our null Uri
                System.Windows.Forms.MessageBox.Show(ex.Message);
            }
        }
    }
}
