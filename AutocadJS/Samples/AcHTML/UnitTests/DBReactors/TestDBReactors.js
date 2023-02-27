
var observedEntities = new Acad.OSet();

function onObjectModified(eventname, args) {
    var TextLog = document.getElementById('TextLog');
    TextLog.value = TextLog.value + "Object Modified: " + args.id +'\n';
}

function onObjectErased(eventname, args) {
    var TextLog = document.getElementById('TextLog');
    TextLog.value = TextLog.value + "Object Erased: " + args.id +'\n';
}

function onComplete(jsonPromptResult) {
   
    var resultObj = JSON.parse(jsonPromptResult);

    if (resultObj) {
    
        // res ok 
        if (resultObj.status == 5100) {

            var TextIds = document.getElementById('TextIds');
            TextIds.value = TextIds.value + resultObj.objectId +'\n';
           
            //var entity = new Acad.DBEntity(resultObj.objectId);
            
            observedEntities.add(resultObj.objectId);

            Acad.Application.activedocument.startObserving(
                observedEntities, 
                Acad.Application.activedocument.eventname.modified, 
                onObjectModified);

             Acad.Application.activedocument.startObserving(
                observedEntities, 
                Acad.Application.activedocument.eventname.erased, 
                onObjectErased);
        } 
        
        //Keyword
        else if (resultObj.status == -5005) { 
        } 
        
        // Enter/Space key (null input)
        else if (resultObj.status == 5000) { 
        } 
        
        // Cancel
        else if (resultObj.status == -5002) {           
        } 
        
        //Other...
        else {
        }
    }
}

function onError(jsonPromptResult) {   
    write("Error: " + jsonPromptResult);
    
    var resultObj = JSON.parse(jsonPromptResult);
    if (resultObj) {
    }
}

function SelectEntity() {
    try {
        var peo = new Acad.PromptEntityOptions();
        peo.setMessageAndKeywords("\nSelect an Entity", "");
        peo.rejectMessage = "\nInvalid selection...";

        //peo.addAllowedClass("AcDbLine", true);
        peo.singlePickInSpace = true;
        peo.allowObjectOnLockedLayer = true;

        Acad.Editor.getEntity(peo).then(
            onComplete, 
            onError);		    
    }
    catch(e) {
        write(e.message);
    }
}

function StopObserving() {

    var TextIds = document.getElementById('TextIds');
    TextIds.value = "";

    var TextLog = document.getElementById('TextLog');
    TextLog.value = "";

    Acad.Application.activedocument.stopObserving(
        observedEntities, 
        Acad.Application.activedocument.eventname.modified, 
        onObjectModified);

    Acad.Application.activedocument.stopObserving(
        observedEntities, 
        Acad.Application.activedocument.eventname.erased, 
        onObjectErased);
        
    observedEntities = new Acad.OSet();
}