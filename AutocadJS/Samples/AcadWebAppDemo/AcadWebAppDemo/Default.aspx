<%@ Page Title="Home Page" Language="C#" MasterPageFile="~/Site.master" AutoEventWireup="true"
    CodeBehind="Default.aspx.cs" Inherits="AcadWebAppDemo._Default" %>

<asp:Content ID="HeaderContent" runat="server" ContentPlaceHolderID="HeadContent">
</asp:Content>

<asp:Content ID="BodyContent" runat="server" ContentPlaceHolderID="MainContent">

    <script type="text/javascript" src="http://www.autocadws.com/jsapi/v1/Autodesk.AutoCAD.js"></script>
    <script type="text/javascript" src="Scripts\jquery-1.4.1.min.js"></script>
    <script type="text/javascript" src="Scripts\AcadWebAppDemo.js"></script>

    <script type="text/javascript">

        window.onload = OnWindowLoad;

        function OnWindowLoad() {

            GetEntities();
            GetViews();
        }

        function addToCombo(id, text) {

            var combo = document.getElementById(id);
            var option = document.createElement("option");

            option.text = text;
           
            try {
                combo.add(option, null);
            }
            catch (error) {
                combo.add(option); // IE only
            }
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        function SaveGroup() {

            var entname = document.getElementById("entname").value;

            var combo = document.getElementById("comboEntity");

            for (var i = 0; i < combo.length; i++) {
                if (combo.options[i].value == entname) {
                    alert("Group " + entname + " already exists...");
                    return;
                }
            }

            SaveEntityDb(entname);
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        function LoadGroup() {

            var combo = document.getElementById("comboEntity");

            var entname = combo.options[combo.selectedIndex].value;

            LoadEntityDb(entname);
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        function ClearGroups() {

            var combo = document.getElementById("comboEntity");

            combo.options.length = 0;

            ClearEntitiesDb();
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        function SaveView() {

            var viewname = document.getElementById("viewname").value;

            var combo = document.getElementById("comboView");

            for (var i=0; i<combo.length; i++){
                if(combo.options[i].value == viewname){
                    alert("View " + viewname + " already exists...");
                    return;
                }
            }

            var pos = Acad.Editor.CurrentViewport.position;

            var target = Acad.Editor.CurrentViewport.target;

            var up = Acad.Editor.CurrentViewport.upVector;

            var fieldHeight = Acad.Editor.CurrentViewport.fieldHeight;

            var fieldWidth = Acad.Editor.CurrentViewport.fieldWidth;

            var projection = Acad.Editor.CurrentViewport.projection;

            SaveViewDb(viewname, 
                pos.x, pos.y, pos.z,
                target.x, target.y, target.z,
                up.x, up.y, up.z,
                fieldHeight,
                fieldWidth,
                projection);

            addToCombo("comboView", viewname);
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        function LoadView() {

            var combo = document.getElementById("comboView");

            var viewName = combo.options[combo.selectedIndex].value;

            LoadViewDb(viewName);
        }

        /////////////////////////////////////////////////////////////////////////////
        // 
        //
        /////////////////////////////////////////////////////////////////////////////
        function ClearViews() {

            var combo = document.getElementById("comboView");

            combo.options.length = 0;

            ClearViewsDb();
        }

    </script>

    <h2>
        Welcome to Developer Days 2012!
    </h2>

    <div>
        <hr />
        Entity Demo:
        <br />

        <br />
        <input type='button' value='Clear Groups' onclick='ClearGroups()' style='width:100px'/>
        <br />

        <br />
        <input type='button' value='Save Group' onclick='SaveGroup()' style='width:100px'/>
        <input type='text' id='entname' value='Group Name' style='width:100px' onfocus="this.value=''" />
        <br />

        <br />
        <input type='button' value="Load Group" onclick='LoadGroup()' style='width:100px'/>        
        <select id='comboEntity' style='width:105px'>      
        </select>
        <br />

        <br />

        <hr />
        View Demo:
        <br />
     
        <br />
        <input type='button' value='Clear Views' onclick='ClearViews()' style='width:100px'/>
        <br />
     
        <br />
        <input type='button' onclick='SaveView()' value='Save View' style='width:100px'/>
        <input type='text' id='viewname' value='View Name' style='width:100px' onfocus="this.value=''" />
        <br />
     
        <br />
        <input type='button' value="Load View" onclick='LoadView()' style='width:100px'/>
        <select id='comboView' style='width:105px'>
        </select>
        <br />

        <br />
        <hr />
    </div>
</asp:Content>
