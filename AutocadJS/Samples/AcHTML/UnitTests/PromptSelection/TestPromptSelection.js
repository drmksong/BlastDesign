function setPromptSelectionOptions(options) {
    
    // If the messages edit boxes are empty, we do not set the message and thus
    // let the acad default messages show
    if (document.getElementById('messageForAdding').value)
        options.messageForAdding = 
            document.getElementById('messageForAdding').value;

    if (document.getElementById('messageForRemoval').value)
        options.messageForRemoval = 
            document.getElementById('messageForRemoval').value;

    options.singlePickInSpace = 
        document.getElementById('singlePickInSpace').checked;
    
    options.allowDuplicates = 
        document.getElementById('allowDuplicates').checked;
    
    options.selectEverythingInAperture = 
        document.getElementById('selectEverythingInAperture').checked;
    
    options.singleOnly = document.getElementById('singleOnly').checked;
    
    options.rejectObjectsOnLockedLayers = 
        document.getElementById('rejectObjectsOnLockedLayers').checked;
    
    options.rejectObjectsFromNonCurrentSpace = 
        document.getElementById('rejectObjectsFromNonCurrentSpace').checked;
    
    options.selectEverythingInAperture = 
        document.getElementById('selectEverythingInAperture').checked;
    
    options.rejectPaperspaceViewport = 
        document.getElementById('rejectPaperspaceViewport').checked;

}

function onCompletePromptSelectionResult(jsonPromptResult) {

    document.getElementById('jsonResult').value = jsonPromptResult;

    var resObj = JSON.parse(jsonPromptResult);
    
    if (resObj) {
        document.getElementById('resultStatus').value = '';
        document.getElementById('resultValue').value = '';

        if (resObj.status == 5100) { // normal (point selected/entered)
            document.getElementById('resultStatus').value = 'normal';
            document.getElementById('resultValue').value = 
                JSON.stringify(resObj.value);
            
        } else if (resObj.status == -5005) { // keyword/arbitrary input
            document.getElementById('resultStatus').value = 'keyword/arbitrary';
            
        } else if (resObj.status == 5000) { // Enter/Space key (null input)
            document.getElementById('resultStatus').value = 'enter/space';
            
        } else if (resObj.status == -5002) { // Cancel
            document.getElementById('resultStatus').value = 'cancel';
            
        } else {
            document.getElementById('resultStatus').value = '???';
        }
    }
}

function onErrorPromptResult(jsonPromptResult) {

    document.getElementById('jsonResult').value = jsonPromptResult;

    var resObj = JSON.parse(jsonPromptResult);
    if (resObj) {
        document.getElementById('resultStatus').value = 'error';
        document.getElementById('resultValue').value = '';
    }
}

function promptForSelection() {
    if (document.getElementById('useInvalidOptions').checked == true) {
        Acad.Editor.getSelection("").then(
            onCompletePromptSelectionResult,
            onErrorPromptResult);
    } 
    else {
        
        var options = new Acad.PromptSelectionOptions();

        setPromptSelectionOptions(options);

        Acad.Editor.getSelection(options).then(
            onCompletePromptSelectionResult,
            onErrorPromptResult);
    }
}