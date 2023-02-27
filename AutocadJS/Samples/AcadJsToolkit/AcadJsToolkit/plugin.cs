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

// This line is not mandatory, but improves loading performances
[assembly: ExtensionApplication(typeof(AcadJsToolkit.MyPlugin))]
[assembly: CommandClass(typeof(AcadJsToolkit.MyPlugin))]

namespace AcadJsToolkit
{
    // This class is instantiated by AutoCAD once and kept alive for the 
    // duration of the session. If you don't do any one time initialization 
    // then you should remove this class.
    public class MyPlugin : IExtensionApplication
    {
        void Register()
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

        [CommandMethod("UnregisterAcadJsToolkit")]
        public void UnregisterMe()
        {
            //AutoCAD (or vertical) and Application keys
            Microsoft.Win32.RegistryKey acadKey =
                Microsoft.Win32.Registry.CurrentUser.OpenSubKey(
                    HostApplicationServices.Current.MachineRegistryProductRootKey);

            Microsoft.Win32.RegistryKey acadAppKey = acadKey.OpenSubKey("Applications", true);

            //get assembly name and delete
            string curAssemblyName = System.Reflection.Assembly.GetExecutingAssembly().GetName().Name;

            String[] subKeys = acadAppKey.GetSubKeyNames();

            foreach (String subKey in subKeys)
            {
                if (subKey.Equals(curAssemblyName))
                {
                    acadAppKey.DeleteSubKeyTree(curAssemblyName);
                    break;
                }
            }

            acadAppKey.Close();
        }

        void IExtensionApplication.Initialize()
        {
            // Add one time initialization here
            // One common scenario is to setup a callback function here that 
            // unmanaged code can call. 
            // To do this:
            // 1. Export a function from unmanaged code that takes a function
            //    pointer and stores the passed in value in a global variable.
            // 2. Call this exported function in this function passing delegate.
            // 3. When unmanaged code needs the services of this managed module
            //    you simply call acrxLoadApp() and by the time acrxLoadApp 
            //    returns  global function pointer is initialized to point to
            //    the C# delegate.
            // For more info see: 
            // http://msdn2.microsoft.com/en-US/library/5zwkzwf4(VS.80).aspx
            // http://msdn2.microsoft.com/en-us/library/44ey4b32(VS.80).aspx
            // http://msdn2.microsoft.com/en-US/library/7esfatk4.aspx
            // as well as some of the existing AutoCAD managed apps.

            // Initialize your plug-in application here
            Register();
        }

        void IExtensionApplication.Terminate()
        {
            // Do plug-in application clean up here
        }
    }
}
