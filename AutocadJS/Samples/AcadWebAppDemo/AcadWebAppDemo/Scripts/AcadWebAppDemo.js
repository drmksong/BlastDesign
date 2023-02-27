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

/////////////////////////////////////////////////////////////////////////////
// 
//
/////////////////////////////////////////////////////////////////////////////
function ExecutePageMethod(page, fn, args, successFn, errorFn) {

    $.ajax({
        type: "POST",
        url: page + "/" + fn,
        contentType: "application/json; charset=utf-8",
        data: args,
        dataType: "json",
        success: successFn,
        error: errorFn
    });
}

/////////////////////////////////////////////////////////////////////////////
// 
//
/////////////////////////////////////////////////////////////////////////////
function OnFailure(result) {
    alert("Ajax call failed...");
    var resultObj = JSON.parse(result);
    if (resultObj) {

    }
}

/////////////////////////////////////////////////////////////////////////////
// 
//
/////////////////////////////////////////////////////////////////////////////
var currentName = "";

function SaveEntityDb(name) {

    try {

        currentName = name;

        var options = new Acad.PromptSelectionOptions();

        options.messageForAdding = "\nSelect Entities";

        options.singleOnly = false;
        options.singlePickInSpace = false;
        options.selectEverythingInAperture = false;
        options.rejectObjectsOnLockedLayers = false;
        options.allowDuplicates = false;

        Acad.Editor.getSelection(options).then(
            OnSelectSuccess,
            OnSelectError);
    }
    catch (e) {
        write(e.message);
    }
}

function OnSelectSuccess(result) {

    var resultObj = JSON.parse(result);

    if (resultObj) {

        if (resultObj.status == 5100) {

            execAsync(JSON.stringify({
                functionName: 'EntToString',
                invokeAsCommand: false,
                functionParams: { args: resultObj.value }
            }),
            OnParseSuccess,
            OnParseError);
        }
    }
}

function OnSelectError(result) {
    write("\nOnSelectError: " + result);
}

function CreateEntProps(
    name,
    data) {

    this.GroupName = name;
    this.DxfData = data;
}

function OnParseSuccess(result) {

    var resultObj = JSON.parse(result);

    var entProps = new CreateEntProps(
        currentName,
        resultObj.result);

    var jsonContent = JSON.stringify(entProps);

    var jsonMsg = "{\'entProps\':\'" + jsonContent + "\' }";

    ExecutePageMethod(
        "Default.aspx",
        "SaveEntities",
        jsonMsg,
        OnSaveSuccess,
        OnSaveError);
}

function OnParseError(result) {
    write("\nOnParseError: " + result);
}

function OnSaveSuccess(result) {

    var combo = document.getElementById("comboEntity");

    addToCombo("comboEntity", currentName);
}

function OnSaveError(result) {
    write("\nOnSaveError: " + result);
}

/////////////////////////////////////////////////////////////////////////////
// 
//
/////////////////////////////////////////////////////////////////////////////
function LoadEntityDb(groupName) {

    try {

        var jsonMsg = "{\'groupName\':\'" + groupName + "\' }";

        ExecutePageMethod(
            "Default.aspx",
            "LoadGroup",
            jsonMsg,
            OnLoadGroupSuccess,
            OnLoadGroupError);
    }
    catch (e) {

    }
}

function OnLoadGroupSuccess(result) {

    var entProps = jQuery.parseJSON(result.d);

    write('\nLoading Group: ' + entProps.GroupName);

    execAsync(JSON.stringify({
        functionName: 'StringToEnt',
        invokeAsCommand: true,
        functionParams: { args: entProps.DxfData }
    }),
            OnCreateGroupSuccess,
            OnCreateGroupError);
}

function OnLoadGroupError(result) {
    write("\nOnLoadGroupError: " + result);
}

function OnCreateGroupSuccess(result) {

}

function OnCreateGroupError(result) {
    write("\nOnCreateGroupError: " + result);
}

/////////////////////////////////////////////////////////////////////////////
// 
//
/////////////////////////////////////////////////////////////////////////////
function GetEntities() {

    try {

        ExecutePageMethod(
            "Default.aspx",
            "GetEntities",
            "",
            OnGetEntitiesSuccess,
            OnFailure);
    }
    catch (e) {

    }
}

function OnGetEntitiesSuccess(result) {

    var ents = jQuery.parseJSON(result.d);

    for (var i = 0; i < ents.length; i++) {
        addToCombo("comboEntity", ents[i].GroupName);
    }
}

/////////////////////////////////////////////////////////////////////////////
// 
//
/////////////////////////////////////////////////////////////////////////////
function ClearEntitiesDb() {

    try {

        ExecutePageMethod(
            "Default.aspx",
            "ClearEntities",
            "",
            OnClearEntitiesSuccess,
            OnFailure);
    }
    catch (e) {

    }
}

function OnClearEntitiesSuccess(result) {

}

/////////////////////////////////////////////////////////////////////////////
// 
//
/////////////////////////////////////////////////////////////////////////////
function CreateView(
    name, 
    posx, posy, posz,
    targetx, targety, targetz,
    upx, upy, upz,
    fieldHeight, fieldWidth, projection) {

    this.Name = name;

    this.Position = new Array();

    this.Position[0] = posx;
    this.Position[1] = posy;
    this.Position[2] = posz;


    this.Target = new Array();

    this.Target[0] = targetx;
    this.Target[1] = targety;
    this.Target[2] = targetz;


    this.UpVector = new Array();

    this.UpVector[0] = upx;
    this.UpVector[1] = upy;
    this.UpVector[2] = upz;

    this.FieldHeight = fieldHeight;
    this.FieldWidth = fieldWidth;
    this.Projection = projection;
}

function SaveViewDb(
    viewName, 
    posx, posy, posz,
    targetx, targety, targetz,
    upx, upy, upz,
    fieldHeight, fieldWidth, projection) {

    try {

        var view = new CreateView( 
            viewName, 
            posx, posy, posz,
            targetx, targety, targetz,
            upx, upy, upz,
            fieldHeight, fieldWidth, projection);

        var jsonContent = JSON.stringify(view);

        var jsonMsg = "{\'viewProps\':\'" + jsonContent + "\' }";

        ExecutePageMethod(
            "Default.aspx",
            "SaveView",
            jsonMsg,
            OnSaveViewSuccess,
            OnFailure);
    }
    catch (e) {

    }
}

function OnSaveViewSuccess(result) {
    //alert("OnSaveViewSuccess: " + result.d);
}

/////////////////////////////////////////////////////////////////////////////
// 
//
/////////////////////////////////////////////////////////////////////////////
function LoadViewDb(viewName) {
    
    try {

        var jsonMsg = "{\'viewName\':\'" + viewName + "\' }";

        ExecutePageMethod(
            "Default.aspx",
            "LoadView",
            jsonMsg,
            OnLoadViewSuccess,
            OnFailure);
    }
    catch (e) {

    }
}

function OnLoadViewSuccess(result) {

    var view = jQuery.parseJSON(result.d);

    var pos = view.Position;

    var target = view.Target;

    var up = view.UpVector;

    var fieldHeight = view.FieldHeight;

    var fieldWidth = view.FieldWidth;

    var projection = view.Projection; 

    Acad.Editor.CurrentViewport.setView(
        new Acad.Point3d(pos[0], pos[1], pos[2]),
        new Acad.Point3d(target[0], target[1], target[2]),
        new Acad.Vector3d(up[0], up[1], up[2]),
        fieldWidth, fieldHeight,
        projection, 
        true);
}

/////////////////////////////////////////////////////////////////////////////
// 
//
/////////////////////////////////////////////////////////////////////////////
function GetViews() {

    try {

        ExecutePageMethod(
            "Default.aspx",
            "GetViews",
            "",
            OnGetViewsSuccess,
            OnFailure);
    }
    catch (e) {

    }
}

function OnGetViewsSuccess(result) {

    var views = jQuery.parseJSON(result.d);

    for (var i=0; i<views.length; i++){
        addToCombo("comboView", views[i].Name); 
    }
}

/////////////////////////////////////////////////////////////////////////////
// 
//
/////////////////////////////////////////////////////////////////////////////
function ClearViewsDb() {

    try {

        ExecutePageMethod(
            "Default.aspx",
            "ClearViews",
            "",
            OnClearViewsSuccess,
            OnFailure);
    }
    catch (e) {

    }
}

function OnClearViewsSuccess(result) {

    //alert("OnClearViewsSuccess: " + result.d);
}
