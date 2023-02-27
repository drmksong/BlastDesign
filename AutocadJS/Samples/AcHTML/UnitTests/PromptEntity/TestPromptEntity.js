function setPromptEntityOptions(options) {
    
    var messageAndKeywords = 
        '\n' + document.getElementById('messageAndKeywords').value;
    
    var globalKeywords = document.getElementById('globalKeywords').value;
    
    options.setMessageAndKeywords(messageAndKeywords, globalKeywords);
     
    if (document.getElementById('rejectMessage').value)

        options.SetRejectMessage(
            document.getElementById('rejectMessage').value;

    if (document.getElementById('addAllowedClass').value) {
        
        options.addAllowedClass(
            document.getElementById('addAllowedClass').value, 
            document.getElementById('exactMatch').checked);
    }
    
    if (document.getElementById('removeAllowedClass').value) {
        
        options.removeAllowedClass(
            document.getElementById('removeAllowedClass').value);
    }
	
    options.singlePickInSpace = 
        document.getElementById('allowNone').checked;
    
    options.allowObjectOnLockedLayer = 
        document.getElementById('allowObjectOnLockedLayer').checked;  
}

function onComplete(jsonPromptResult) {
    
    document.getElementById('jsonResult').value = jsonPromptResult;
 
    var resultObj = JSON.parse(jsonPromptResult);
    
    if (resultObj) {
    
        document.getElementById('resultStatus').value = '';
        document.getElementById('resultValue').value = '';

        if (resultObj.status == 5100) { // normal (point selected/entered)
            
            document.getElementById('resultStatus').value = 'normal';
            document.getElementById('resultValue').value = 
                JSON.stringify(resultObj.value);
        
        } else if (resultObj.status == -5005) { // keyword/arbitrary input
            
            document.getElementById('resultStatus').value = 'keyword/arbitrary';
            
        } else if (resultObj.status == 5000) { // Enter/Space key (null input)
            
            document.getElementById('resultStatus').value = 'enter/space';
            
        } else if (resultObj.status == -5002) { // Cancel
            
            document.getElementById('resultStatus').value = 'cancel';
            
        } else {
            
            document.getElementById('resultStatus').value = '???';
        }
    }
}

function onError(jsonPromptResult) {
    
    document.getElementById('jsonResult').value = jsonPromptResult;
    
    var resultObj = JSON.parse(jsonPromptResult);
    
    if (resultObj) {
        document.getElementById('resultStatus').value = 'Error!!!';
        document.getElementById('resultValue').value = '';
    }
}

function resetResultField()
{
    document.getElementById('jsonResult').value = '';
    document.getElementById('resultStatus').value = '';
    document.getElementById('resultValue').value = '';
}

function promptForEntity() {
    
    resetResultField();

    try{
            
        var options = new Acad.PromptEntityOptions();

        setPromptEntityOptions(options);

        Acad.Editor.getEntity(options).then(
            onComplete, 
            onError);
    }
    catch(e) {
        document.getElementById('resultStatus').value = e.message;
        alert(e.message);
    }
}