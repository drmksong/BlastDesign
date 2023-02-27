using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.Services;
using System.Web.Script.Services;
using Amazon.SimpleDB;
using Amazon.SimpleDB.Model;
using Amazon;
using System.Web.Script.Serialization;
using System.IO;
using System.Text;
using System.Runtime.Serialization.Json;
using System.Runtime.Serialization;

namespace AcadWebAppDemo
{
    public partial class _Default : System.Web.UI.Page
    {
        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        protected void Page_Load(object sender, EventArgs e)
        {
            AcadWebViewService.OnPageLoad(sender, e);
            AcadWebEntityService.OnPageLoad(sender, e);
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        [WebMethod]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static bool SaveView(string viewProps)
        {
            try
            {
                return AcadWebViewService.SaveView(viewProps); 
            }
            catch (Exception ex)
            {
                return false;
            }
        }

        [WebMethod]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static bool SaveEntities(string entProps)
        {
            try
            {
                return AcadWebEntityService.SaveEntities(entProps);
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
        [WebMethod]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static string LoadView(string viewName)
        {
            try
            {
                return AcadWebViewService.LoadView(viewName);
            }
            catch(Exception ex)
            {
                return string.Empty;
            }
        }

        [WebMethod]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static string LoadGroup(string groupName)
        {
            try
            {
                return AcadWebEntityService.LoadGroup(groupName);
            }
            catch (Exception ex)
            {
                return string.Empty;
            }
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        [WebMethod]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static string GetViews()
        {
            try
            {
                return AcadWebViewService.GetViews();
            }
            catch (Exception ex)
            {
                return string.Empty;
            }
        }

        [WebMethod]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static string GetEntities()
        {
            try
            {
                return AcadWebEntityService.GetEntities();
            }
            catch (Exception ex)
            {
                return string.Empty;
            }
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        [WebMethod]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static bool ClearViews()
        {
            try
            {
                return AcadWebViewService.ClearViews();
            }
            catch (Exception ex)
            {
                return false;
            }
        }

        [WebMethod]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public static bool ClearEntities()
        {
            try
            {
                return AcadWebEntityService.ClearEntities();
            }
            catch (Exception ex)
            {
                return false;
            }
        }
    }
}
