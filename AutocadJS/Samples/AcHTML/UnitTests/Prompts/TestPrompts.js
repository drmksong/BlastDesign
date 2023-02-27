function randomCanvasX() {
    var canvas = document.getElementById("setContentsCanvas");

    return Math.floor((Math.random()*canvas.width)+1);
}

function randomCanvasY() {
    var canvas = document.getElementById("setContentsCanvas");

    return Math.floor((Math.random()*canvas.height)+1);
}

window.onload = function () {
    //
    // Give the canvas a random background color and draw
    // a random line path on it using random color so 
    // that the picture looks different every time we reload.
    //
    var canvas = document.getElementById("setContentsCanvas");
    var context = canvas.getContext("2d");

    context.fillStyle = "#" + Math.random().toString(16).slice(2, 8);
    context.fillRect(0, 0, canvas.width, canvas.height);

    context.lineWidth = 4;
    context.strokeStyle = "#" + Math.random().toString(16).slice(2, 8);

    context.beginPath();

    context.moveTo(randomCanvasX(), randomCanvasY());

    for (i = 0; i < 5; i++) {
        context.lineTo(randomCanvasX(), randomCanvasY());
    }

    context.stroke();
};

function onPromptTypeChanged() {

    document.getElementById('allowNone').disabled = true;
    document.getElementById('allowArbitraryInput').disabled = true;
    document.getElementById('useDashedLine').disabled = true;
    document.getElementById('limitsChecked').disabled = true;
    document.getElementById('useBasePoint').disabled = true;
    document.getElementById('allowNegative').disabled = true;
    document.getElementById('allowZero').disabled = true;

    document.getElementById('useDefaultValue').disabled = true;

    document.getElementById('lowerUpperLimitsChecked').disabled = true;
    document.getElementById('lowerLimit').value = "";
    document.getElementById('upperLimit').value = "";

    document.getElementById('useAngleBase').disabled = true;
    document.getElementById('allowSpaces').disabled = true;
    document.getElementById('only2d').disabled = true;


    document.getElementById('dialogCaption').value = '';
    document.getElementById('dialogName').value = '';
    document.getElementById('initialFileName').value = '';
    document.getElementById('initialDirectory').value = '';
    document.getElementById('filter').value = '';
    document.getElementById('filterIndex').value = 0;
    document.getElementById('preferCommandLine').disabled = true;
    document.getElementById('allowUrls').disabled = true;
    document.getElementById('showReadOnly').disabled = true;
    document.getElementById('searchPath').disabled = true;
    document.getElementById('transferRemoteFiles').disabled = true;

    var promptType = document.getElementById('promptType').value;
    if (promptType == 'PromptCorner') {
        document.getElementById('messageAndKeywords').value = 'Select corner point [Rectangle/Circle/Line]';
        document.getElementById('globalKeywords').value = 'Rectangle Circle Line';

        document.getElementById('allowNone').disabled = false;
        document.getElementById('allowArbitraryInput').disabled = false;
        document.getElementById('useDashedLine').disabled = false;
        document.getElementById('limitsChecked').disabled = false;

    } else if (promptType == 'PromptPoint') {
        document.getElementById('messageAndKeywords').value = 'Select point [Rectangle/Circle/Line]';
        document.getElementById('globalKeywords').value = 'Rectangle Circle Line';

        document.getElementById('allowNone').disabled = false;
        document.getElementById('allowArbitraryInput').disabled = false;
        document.getElementById('useDashedLine').disabled = false;
        document.getElementById('limitsChecked').disabled = false;
        document.getElementById('useBasePoint').disabled = false;

    } else if (promptType == 'PromptInteger') {
        document.getElementById('messageAndKeywords').value = 'Enter integer';
        document.getElementById('globalKeywords').value = '';

        document.getElementById('allowNone').disabled = false;
        document.getElementById('allowArbitraryInput').disabled = false;
        document.getElementById('allowNegative').disabled = false;
        document.getElementById('allowZero').disabled = false;

        document.getElementById('useDefaultValue').disabled = false;
        document.getElementById('defaultValue').value = 888;

        document.getElementById('lowerUpperLimitsChecked').disabled = false;
        document.getElementById('lowerLimit').value = -100;
        document.getElementById('upperLimit').value = 100;

    } else if (promptType == 'PromptDouble') {
        document.getElementById('messageAndKeywords').value = 'Enter double';
        document.getElementById('globalKeywords').value = '';

        document.getElementById('allowNone').disabled = false;
        document.getElementById('allowArbitraryInput').disabled = false;
        document.getElementById('allowNegative').disabled = false;
        document.getElementById('allowZero').disabled = false;

        document.getElementById('useDefaultValue').disabled = false;
        document.getElementById('defaultValue').value = 0.123;

    } else if (promptType == 'PromptDistance') {

        document.getElementById('messageAndKeywords').value = 'Enter distance';
        document.getElementById('globalKeywords').value = '';

        document.getElementById('allowNone').disabled = false;
        document.getElementById('allowArbitraryInput').disabled = false;
        document.getElementById('useDashedLine').disabled = false;
        document.getElementById('allowNegative').disabled = false;
        document.getElementById('allowZero').disabled = false;

        document.getElementById('useDefaultValue').disabled = false;
        document.getElementById('defaultValue').value = 25.4;

        document.getElementById('useBasePoint').disabled = false;

        document.getElementById('only2d').disabled = false;

    } else if (promptType == 'PromptAngle') {

        document.getElementById('messageAndKeywords').value = 'Enter angle';
        document.getElementById('globalKeywords').value = '';

        document.getElementById('allowNone').disabled = false;
        document.getElementById('allowArbitraryInput').disabled = false;
        document.getElementById('allowZero').disabled = false;
        document.getElementById('useDashedLine').disabled = false;

        document.getElementById('useDefaultValue').disabled = false;
        document.getElementById('defaultValue').value = Math.PI;

        document.getElementById('useBasePoint').disabled = false;
        document.getElementById('useAngleBase').disabled = false;
    } else if (promptType == 'PromptString') {

        document.getElementById('messageAndKeywords').value = 'Enter string';
        document.getElementById('globalKeywords').value = '';

        document.getElementById('useDefaultValue').disabled = false;
        document.getElementById('defaultValue').value = 'this is a default string';

        document.getElementById('allowSpaces').disabled = false;
    } else if (promptType == 'PromptKeyword') {
        document.getElementById('messageAndKeywords').value = 'Select keyword [Rectangle/Circle/Line]';
        document.getElementById('globalKeywords').value = 'Rectangle Circle Line';

        document.getElementById('allowNone').disabled = false;
        document.getElementById('allowArbitraryInput').disabled = false;
    } else if (promptType == 'PromptFileNameForOpen') {
        document.getElementById('message').value = 'Open File ';

        document.getElementById('preferCommandLine').disabled = false;
        document.getElementById('allowUrls').disabled = false;
        document.getElementById('showReadOnly').disabled = false;
        document.getElementById('searchPath').disabled = false;
        document.getElementById('transferRemoteFiles').disabled = false;
    } else if (promptType == 'PromptFileNameForSave') {
        document.getElementById('message').value = 'Open File ';

        document.getElementById('preferCommandLine').disabled = false;
        document.getElementById('allowUrls').disabled = false;
        document.getElementById('deriveInitialFilenameFromDrawingName').disabled = false;
        document.getElementById('displaySaveOptionsMenuItem').disabled = false;
        document.getElementById('forceOverwriteWarningForScriptsAndLisp').disabled = false;
    }
}

function setPromptOptions(options) {
    var messageAndKeywords = '\n' + document.getElementById('messageAndKeywords').value;
    var globalKeywords = document.getElementById('globalKeywords').value;

    options.setMessageAndKeywords(messageAndKeywords, globalKeywords);
}

function setPromptCornerOptions(options) {
    setPromptOptions(options);

    options.allowNone = document.getElementById('allowNone').checked;
    options.allowArbitraryInput = document.getElementById('allowArbitraryInput').checked;
    options.useDashedLine = document.getElementById('useDashedLine').checked;
    options.limitsChecked = document.getElementById('limitsChecked').checked;

    var basePointX = Number(document.getElementById('basePointX').value);
    var basePointY = Number(document.getElementById('basePointY').value);
    var basePointZ = Number(document.getElementById('basePointZ').value);

    options.basePoint = new Acad.Point3d(basePointX, basePointY, basePointZ);
}

function setPromptNumericalOptions(options) {
    setPromptOptions(options);

    options.allowNone = document.getElementById('allowNone').checked;
    options.allowArbitraryInput = document.getElementById('allowArbitraryInput').checked;
    options.allowNegative = document.getElementById('allowNegative').checked;
    options.allowZero = document.getElementById('allowZero').checked;
    options.useDefaultValue = document.getElementById('useDefaultValue').checked;
}

function setPromptIntegerOptions(options) {
    setPromptNumericalOptions(options);

    options.lowerLimit = Number(document.getElementById('lowerLimit').value);
    options.upperLimit = Number(document.getElementById('upperLimit').value);

    if (options.useDefaultValue) {
        options.defaultValue = Number(document.getElementById('defaultValue').value);
    }
}

function setPromptDoubleOptions(options) {
    setPromptNumericalOptions(options);

    if (options.useDefaultValue) {
        options.defaultValue = Number(document.getElementById('defaultValue').value);
    }
}

function setPromptDistanceOptions(options) {
    setPromptNumericalOptions(options);

    options.useDashedLine = document.getElementById('useDashedLine').checked;
    options.only2d = document.getElementById('only2d').checked;

    if (options.useDefaultValue) {
        options.defaultValue = Number(document.getElementById('defaultValue').value);
    }

    options.useBasePoint = document.getElementById('useBasePoint').checked;

    if (options.useBasePoint) {
        var basePointX = Number(document.getElementById('basePointX').value);
        var basePointY = Number(document.getElementById('basePointY').value);
        var basePointZ = Number(document.getElementById('basePointZ').value);

        options.basePoint = new Acad.Point3d(basePointX, basePointY, basePointZ);
    }
}

function setPromptAngleOptions(options) {
    setPromptOptions(options);

    options.allowNone = document.getElementById('allowNone').checked;
    options.allowArbitraryInput = document.getElementById('allowArbitraryInput').checked;
    options.allowZero = document.getElementById('allowZero').checked;
    options.useDashedLine = document.getElementById('useDashedLine').checked;
    options.useDefaultValue = document.getElementById('useDefaultValue').checked;

    if (options.useDefaultValue) {
        options.defaultValue = Number(document.getElementById('defaultValue').value);
    }

    options.useBasePoint = document.getElementById('useBasePoint').checked;

    if (options.useBasePoint) {
        var basePointX = Number(document.getElementById('basePointX').value);
        var basePointY = Number(document.getElementById('basePointY').value);
        var basePointZ = Number(document.getElementById('basePointZ').value);

        options.basePoint = new Acad.Point3d(basePointX, basePointY, basePointZ);
    }

    options.useAngleBase = document.getElementById('useAngleBase').checked;
}

function setPromptStringOptions(options) {
    setPromptOptions(options);

    options.useDefaultValue = document.getElementById('useDefaultValue').checked;

    if (options.useDefaultValue) {
        options.defaultValue = document.getElementById('defaultValue').value;
    }

    options.allowSpaces = document.getElementById('allowSpaces').checked;
}

function setPromptOpenFileOptions(options) {
    options.message = document.getElementById('message').value;
    if(document.getElementById('dialogCaption').value)
        options.dialogCaption = document.getElementById('dialogCaption').value;
    if(document.getElementById('dialogName').value)
        options.dialogName = document.getElementById('dialogName').value;
    if(document.getElementById('initialFileName').value)
        options.initialFileName = document.getElementById('initialFileName').value;
    if(document.getElementById('initialDirectory').value)
        options.initialDirectory = document.getElementById('initialDirectory').value;
    if(document.getElementById('filter').value)
        options.filter = document.getElementById('filter').value;
    options.filterIndex = document.getElementById('filterIndex').value;
    options.preferCommandLine = document.getElementById('preferCommandLine').checked;
    options.allowUrls = document.getElementById('allowUrls').checked;
	options.showReadOnly = document.getElementById('showReadOnly').checked;
    options.searchPath = document.getElementById('searchPath').checked;
    options.transferRemoteFiles = document.getElementById('transferRemoteFiles').checked;
}

function setPromptSaveFileOptions(options) {
    options.message = document.getElementById('message').value;
    if (document.getElementById('dialogCaption').value)
        options.dialogCaption = document.getElementById('dialogCaption').value;
    if (document.getElementById('dialogName').value)
        options.dialogName = document.getElementById('dialogName').value;
    if (document.getElementById('initialFileName').value)
        options.initialFileName = document.getElementById('initialFileName').value;
    if (document.getElementById('initialDirectory').value)
        options.initialDirectory = document.getElementById('initialDirectory').value;
    if (document.getElementById('filter').value)
        options.filter = document.getElementById('filter').value;
    options.filterIndex = document.getElementById('filterIndex').value;
    options.preferCommandLine = document.getElementById('preferCommandLine').checked;
    options.allowUrls = document.getElementById('allowUrls').checked;
    options.deriveInitialFilenameFromDrawingName = document.getElementById('deriveInitialFilenameFromDrawingName').checked;
    options.displaySaveOptionsMenuItem = document.getElementById('displaySaveOptionsMenuItem').checked;
    options.forceOverwriteWarningForScriptsAndLisp = document.getElementById('forceOverwriteWarningForScriptsAndLisp').checked;
}

function setPromptKeywordOptions(options) {
    setPromptOptions(options);

    options.allowNone = document.getElementById('allowNone').checked;
    options.allowArbitraryInput = document.getElementById('allowArbitraryInput').checked;
}

function onCompletePromptStringResult(jsonPromptResult) {

    document.getElementById('jsonResult').value = jsonPromptResult;

    var resObj = JSON.parse(jsonPromptResult);
    if (resObj) {
        document.getElementById('resultStatus').value = '';
        document.getElementById('stringResult').value = '';
        document.getElementById('resultValue').value = '';

        if (resObj.status == 5100) { // normal (string entered)
            document.getElementById('resultStatus').value = 'normal';
            document.getElementById('stringResult').value = resObj.stringResult;
        } else if (resObj.status == -5005) { // keyword/arbitrary input
            document.getElementById('resultStatus').value = 'keyword/arbitrary';
            document.getElementById('stringResult').value = resObj.stringResult;
        } else if (resObj.status == 5000) { // Enter/Space key (null input)
            document.getElementById('resultStatus').value = 'enter/space';
        } else if (resObj.status == -5002) { // Cancel
            document.getElementById('resultStatus').value = 'cancel';
        } else {
            document.getElementById('resultStatus').value = '???';
        }
    }
}


function onCompletePromptPointResult(jsonPromptResult) {

    document.getElementById('jsonResult').value = jsonPromptResult;

    var resObj = JSON.parse(jsonPromptResult);
    if (resObj) {
        document.getElementById('resultStatus').value = '';
        document.getElementById('stringResult').value = '';
        document.getElementById('resultValue').value = '';

        if (resObj.status == 5100) { // normal (point selected/entered)
            document.getElementById('resultStatus').value = 'normal';
            document.getElementById('resultValue').value = resObj.value.x + "," + resObj.value.y + "," + resObj.value.z;
        } else if (resObj.status == -5005) { // keyword/arbitrary input
            document.getElementById('resultStatus').value = 'keyword/arbitrary';
            document.getElementById('stringResult').value = resObj.stringResult;
        } else if (resObj.status == 5000) { // Enter/Space key (null input)
            document.getElementById('resultStatus').value = 'enter/space';
        } else if (resObj.status == -5002) { // Cancel
            document.getElementById('resultStatus').value = 'cancel';
        } else {
            document.getElementById('resultStatus').value = '???';
        }
    }
}

function onCompletePromptValueResult(jsonPromptResult) {

    document.getElementById('jsonResult').value = jsonPromptResult;

    var resObj = JSON.parse(jsonPromptResult);
    if (resObj) {
        document.getElementById('resultStatus').value = '';
        document.getElementById('stringResult').value = '';
        document.getElementById('resultValue').value = '';

        if (resObj.status == 5100) { // normal (point selected/entered)
            document.getElementById('resultStatus').value = 'normal';
            document.getElementById('resultValue').value = resObj.value;
        } else if (resObj.status == -5005) { // keyword/arbitrary input
            document.getElementById('resultStatus').value = 'keyword/arbitrary';
            document.getElementById('stringResult').value = resObj.stringResult;
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
        document.getElementById('stringResult').value = '';
        document.getElementById('resultValue').value = '';
    }
}

function promptForCorner() {
 
    var options = new Acad.PromptCornerOptions(
        'Select corner: ', 
        new Acad.Point3d(0, 0, 0));

    setPromptCornerOptions(options);

    Acad.Editor.getCorner(options).then(
        onCompletePromptPointResult,
        onErrorPromptResult);
}

function promptForPoint() {

    var options = new Acad.PromptPointOptions(
        'Select Point: ', 
        new Acad.Point3d(0, 0, 0));

    setPromptCornerOptions(options);

    options.useBasePoint = document.getElementById('useBasePoint').checked;

    Acad.Editor.getPoint(options).then(
        onCompletePromptPointResult,
        onErrorPromptResult);
}

function promptForInteger() {

    var options = new Acad.PromptIntegerOptions('Input Integer: ');

    setPromptIntegerOptions(options);

    Acad.Editor.getInteger(options).then(
        onCompletePromptValueResult,
        onErrorPromptResult);
}

function promptForDouble() {

    var options = new Acad.PromptDoubleOptions('Input Double: ');

    setPromptDoubleOptions(options);

    Acad.Editor.getDouble(options).then(
        onCompletePromptValueResult,
        onErrorPromptResult);
}

function promptForDistance() {

    var options = new Acad.PromptDistanceOptions('Input Distance: ');

    setPromptDistanceOptions(options);

    Acad.Editor.getDistance(options).then(
        onCompletePromptValueResult,
        onErrorPromptResult);
}

function promptFileNameForOpen() {

    var options = new Acad.PromptOpenFileOptions('Input Filename: ');

    setPromptOpenFileOptions(options);

    Acad.DrawingFeedPrivate.getFileNameForOpen(options).then(
        onCompletePromptStringResult,
        onErrorPromptResult);
}

function promptFileNameForSave() {

    var options = new Acad.PromptSaveFileOptions('Input Filename: ');

    setPromptSaveFileOptions(options);      

    Acad.DrawingFeedPrivate.getFileNameForSave(options).then(
        onCompletePromptStringResult,
        onErrorPromptResult);
}

function promptForAngle() {
        
    var options = new Acad.PromptAngleOptions('Select Angle: ');

    setPromptAngleOptions(options);

    Acad.Editor.getAngle(options).then(
        onCompletePromptValueResult,
       onErrorPromptResult);
}

function promptForString() {

    var options = new Acad.PromptStringOptions('Input String: ');

    setPromptStringOptions(options);

    Acad.Editor.getString(options).then(
        onCompletePromptStringResult,
        onErrorPromptResult);
}

function promptForKeyword() {

    var options = new Acad.PromptKeywordOptions('Input Keyword: ');

    setPromptKeywordOptions(options);

    Acad.Editor.getKeywords(options).then(
        onCompletePromptStringResult,
        onErrorPromptResult);
}

// read off the currently selected prompt type in the combo list box
// and invoke the appropriate promptForXXX()
function promptForUserInput() {
    try{
        var promptType = document.getElementById('promptType').value;

        if (promptType == 'PromptCorner') {
            promptForCorner();
        } else if (promptType == 'PromptPoint') {
            promptForPoint();
        } else if (promptType == 'PromptInteger') {
            promptForInteger();
        } else if (promptType == 'PromptDouble') {
            promptForDouble();
        } else if (promptType == 'PromptDistance') {
            promptForDistance();
        } else if (promptType == 'PromptAngle') {
            promptForAngle();
        } else if (promptType == 'PromptString') {
            promptForString();
        } else if (promptType == 'PromptKeyword') {
            promptForKeyword();
        } else if (promptType == 'PromptFileNameForOpen') {
            promptFileNameForOpen();
        } else if (promptType == 'PromptFileNameForSave') {
            promptFileNameForSave();
        }
    }catch(error){
        alert(error);
    }
}

function getContents() {
    try {
        var guid = document.getElementById('guid').value;
        var file = new Acad.DrawingFeedPrivate.SecureFile(guid);

        var encodeData = file.getContents();

        var img = document.getElementById("getContentsImage");
       
        var src = "data:image/bmp;base64," + encodeData;

        img.setAttribute('src', src);

    } catch (error) {
        alert(error);
    }
}

function setContents() {
    try {
        var canvas = document.getElementById("setContentsCanvas");
        
        var dataURL = canvas.toDataURL(canvas); // 'data:image/png:base64,...base64 data...'

        var base64str = dataURL.replace(/^data:image\/(png|jpg);base64,/, "");

        var guid = document.getElementById('guid').value;
        var file = new Acad.DrawingFeedPrivate.SecureFile(guid);

        file.setContents(base64str);

    } catch (error) {
        alert(error);
    }
}

function releaseGUID() {
    try {
        var guid = document.getElementById('guid').value;
        var file = new Acad.DrawingFeedPrivate.SecureFile(guid);

        file.release(guid);

    } catch (error) {
        alert(error);
    }
}