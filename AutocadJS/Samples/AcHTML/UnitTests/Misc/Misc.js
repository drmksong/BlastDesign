

///////////////////////////////////////////////////////////////////////////////
//
//
///////////////////////////////////////////////////////////////////////////////
function ShowModalDialog() {

    var value = document.getElementById('modal_dlg_url').value; 

    Acad.Application.activedocument.showModalDialog(value);
}

function ShowTaskDialog()
{
    print('Running unitest for Acad.TaskDialog.showTaskDialog ');

    try{
        var nCommonButtons = Acad.TaskDialogButton.kButtonOk | 
            Acad.TaskDialogButton.kButtonCancel;
        
        var nDefaultButton = Acad.TaskDialogButton.kButtonOk;

        Acad.TaskDialog.showTaskDialog(
            "Window Title", "Main Instruction", 
            "Content Text", 
            nCommonButtons, 
            nDefaultButton).then(
                function(dialogResult)
                {
                    if (dialogResult == Acad.TaskDialogResult.kRetOk) {
                        write("\nDialog Result: OK");
                    }
                    else if (dialogResult == Acad.TaskDialogResult.kRetCancel) {
                        write("\nDialog Result: Cancel");
                    }
                },
                function(retCode)
                {
                    write("\nError ShowTaskDialog (ret code: " + retCode + ")");
                });
    }
    catch(e)
    {
        write("\nError ShowTaskDialog: "  + e.message);
    }
};

///////////////////////////////////////////////////////////////////////////////
//
//
///////////////////////////////////////////////////////////////////////////////
function DefineJsCommand() {

    document.getElementById('defJsCommandBtn').disabled = true;

    Acad.Editor.addCommand(
        "JS_CMDS",
        "JSCOMMAND",
        "JSCOMMAND",
        Acad.CommandFlag.TRANSPARENT,
        jsCmd
    );
        
    write('\nCommand JsCommand defined...');
}

function jsCmd() {
  write('\nYou just invoked a JavaScript command!');
}

///////////////////////////////////////////////////////////////////////////////
//
//
///////////////////////////////////////////////////////////////////////////////
function onLoginSuccess() {
    write('\nLogin 360 Success');
}

function onLoginFailure() {
    write('\nLogin 360 Failure');
}

function loginA360() {
    Acad.Application.activedocument.loginA360().then(
        onLoginSuccess, 
        onLoginFailure);
}

function onShareSuccess() {
    write('\nShare Success');
}

function onShareFailure() {
    write('\nShare Failure');
}

function shareDrawing() {
    Acad.Application.activedocument.shareDrawing().then(
        onShareSuccess, 
        onShareFailure);
}

function onSaveSyncSuccess() {
    write('\nSaveSync Success');
}

function onSaveSyncFailure() {
    write('\nSaveSync Failure');
}

function saveSync() {
    Acad.Application.activedocument.saveSync().then(
        onSaveSyncSuccess, 
        onSaveSyncFailure);
}

function onIsCloudFileOwnerSuccess(owner) {
    if (owner) {
        write('\nThe user is owner of the cloud file');
    }
    else {
        write('\nThe user is not the owner of the cloud file');
    }
}

function onIsCloudFileOwnerFailure() {
    write('\nIsCloudFileOwner Failure');
}

function isCloudFileOwner() {
    Acad.Application.activedocument.isCloudFileOwner().then(
        onIsCloudFileOwnerSuccess, 
        onIsCloudFileOwnerFailure);
}

function onGetContactsSuccess(contacts) {
    
    var contact;
    
    if (contacts) {
        for (var i = 0, len = contacts.length; i < len; i++) {
            contact = contacts[i];
            if (!contact) {
                continue;
            }

            var text = 'FirstName: ' + contact.firstname + 
                       ', LastName: ' + contact.lastname;
            write('\n' + text);
        }
    }
}

function onGetContactsFailure() {
    write('\nGetContacts Failure');
}

function getContacts() {
    Acad.Application.activedocument.getContacts().then(
        onGetContactsSuccess, 
        onGetContactsFailure);
}

///////////////////////////////////////////////////////////////////////////////
//
//
///////////////////////////////////////////////////////////////////////////////

// Acad.Application.activedocument.unhighlight(o); 
         
var ids = new Acad.OSet();

function onHighlightComplete(jsonPromptResult) {
   
    var resultObj = JSON.parse(jsonPromptResult);
    
    if (resultObj) {
    
        // normal 
        if (resultObj.status == 5100) { 
            
            var id = JSON.stringify(resultObj.objectId);
            
            ids.add(id);

            Acad.Application.activedocument.highlight(ids);  
        } 
    }
}

function onHighlightError(jsonPromptResult) {
    
    var resultObj = JSON.parse(jsonPromptResult);
    
    if (resultObj) {
        
    }
}

function HighlightTest() {

    try
    {
        var peo = new Acad.PromptEntityOptions();

        peo.setMessageAndKeywords("\nSelect an Entity", "");
        peo.singlePickInSpace = true;
        peo.allowObjectOnLockedLayer = true;

        Acad.Editor.getEntity(peo).then(
            onHighlightComplete, 
            onHighlightError);
    }
    catch(e) {
            write(e.message);
    }
}

///////////////////////////////////////////////////////////////////////////////
//
//
///////////////////////////////////////////////////////////////////////////////
function executeCommand() {
  
    Acad.Editor.executeCommand(
        "_LINE", "0,0", "9.5,7", "-2.5,7", "7.25,0", "3.63,11.2", "_C");
}

function executeCommandAsync()
{
    try
    {
        Acad.Editor.executeCommandAsync("LINE", "1,1,0", "5,5,0").then(
        
            function(promptResult)
            {
                if (promptResult.status ==  Acad.PromptStatus.OK)
                {
                    write("\nExecuteCommandAsync() : " + 
                        JSON.stringify(promptResult) + "\n");
                }
            },
            function(promptResult)
            {
                write("\n: error executeCommandAsync() " + 
                    JSON.stringify(promptResult));
            }); 
    }
    catch (e)
    {
        print("\nError executeCommandAsync() " + e.message);
    }
};

