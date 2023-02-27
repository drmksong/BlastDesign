//
///////////////////////////////////////////////////////////////////////////////
//
//                 (C) Copyright 2012 by Autodesk, Inc.
//
// The information contained herein is confidential, proprietary to Autodesk,
// Inc., and considered a trade secret as defined in section 499C of the
// penal code of the State of California.  Use of this information by anyone
// other than authorized employees of Autodesk, Inc. is granted only under a
// written non-disclosure agreement, expressly prescribing the scope and
// manner of such use.
//
///////////////////////////////////////////////////////////////////////////////
/**
* For Internal Use
* Create AutoCAD namespace
*
*/
var Autodesk = Autodesk || {
};
Autodesk["AutoCAD"] = {
};
var Acad = Autodesk.AutoCAD;
/**
* This enum wraps the Acad::PromptStatus ObjectARX class.
*
*/
Acad.PromptStatus = {
    "None": 5000,
    "OK": 5100,
    "Modeless": 5027,
    "Error": -5001,
    "Cancel": -5002,
    "Rejected": -5003,
    "Failed": -5004,
    "Keyword": -5005,
    "Direct": -5999
};
/**
* This JSAPI enum wraps resbuf type. This enumeration provides values that
* describe the value data type of a system variable.
*
*/
Acad.ResultValueType = {
    "RTNONE": 5000,
    "RTREAL": // No result
    5001,
    "RTPOINT": // Real number
    5002,
    "RTSHORT": // 2D point X and Y only
    5003,
    "RTANG": // Short integer
    5004,
    "RTSTR": // Angle
    5005,
    "RTORINT": // String
    5008,
    "RT3DPOINT": // Orientation
    5009,
    "RTLONG": // 3D point - X, Y, and Z
    5010
};
// Long integer
/**
* This enum lists the drag status for jigging.
*
*/
Acad.DragStatus = {
    "kModeless": -17,
    "kNoChange": -6,
    "kCancel": -4,
    "kOther": -3,
    "kNull": -1,
    "kNormal": 0,
    "kKW1": 1,
    "kKW2": 2,
    "kKW3": 3,
    "kKW4": 4,
    "kKW5": 5,
    "kKW6": 6,
    "kKW7": 7,
    "kKW8": 8,
    "kKW9": 9
};
/**
* This enum lists the cursor types that may be used while dragging.
*
*/
Acad.DragCursor = {
    "Normal": 0,
    "None": 1,
    "Selection": 2
};
/**
* This enum wraps the AcEdJig::CursorType ObjectARX enum. It gives the type of cursor that are available.
*
*/
Acad.CursorType = {
    "kNoSpecialCursor": -1,
    "kCrosshair": // No Special Cursor Specified
    0,
    "kRectCursor": // Full Screen Cross Hair.
    1,
    "kRubberBand": // Rectangular cursor.
    2,
    "kNotRotated": // Rubber band line.
    3,
    "kTargetBox": // NotRotated Type.
    4,
    "kRotatedCrosshair": // Target Box Type.
    5,
    "kInvisible": // Rotated Crosshair w/ rubber band.
    7,
    "kEntitySelect": // Invisible cursor.
    8,
    "kParallelogram": // Entity selection target cursor.
    9,
    "kEntitySelectNoPersp": // Parallelogram cursor.
    10,
    "kPkfirstOrGrips": // Pickbox, suppressed in persp.
    11
};
// Auto-select cursor.
/**
* This enum lists the transient cursor types that are available. They are the operating system cursors.
*
*/
Acad.TransientCursorType = {
    "kNone": "None",
    "kArrow": "Arrow",
    "kIbeam": "Ibeam",
    "kWait": "Wait",
    "kCross": "Cross",
    "kUpArrow": "UpArrow",
    "kSizeNWSE": "SizeNWSE",
    "kSizeNESW": "SizeNESW",
    "kSizeWE": "SizeWE",
    "kSizeNS": "SizeNS",
    "kSizeAll": "SizeAll",
    "kNo": "No",
    "kHand": "Hand",
    "kAppStarting": "AppStarting",
    "kHelp": "Help"
};
/**
* This enum wraps the AcEdJig::UserInputControls ObjectARX class.
* Returns the bitwise OR'd value of all user input control settings in effect at the present time for this particular jig.
*
*/
Acad.UserInputControls = {
    "kGovernedByOrthoMode": 1,
    "kNullResponseAccepted": 2,
    "kDontEchoCancelForCtrlC": 4,
    "kDontUpdateLastPoint": 8,
    "kNoDwgLimitsChecking": 16,
    "kNoZeroResponseAccepted": 32,
    "kNoNegativeResponseAccepted": 64,
    "kAccept3dCoordinates": 128,
    "kAcceptMouseUpAsPoint": 256,
    "kAnyBlankTerminatesInput": 512,
    "kInitialBlankTerminatesInput": 1024,
    "kAcceptOtherInputString": 2048,
    "kGovernedByUCSDetect": 4096,
    "kNoZDirectionOrtho": 8192,
    "kImpliedFaceForUCSChange": 16384,
    "kUseBasePointElevation": 32768,
    "kDisableDirectDistanceInput": 65536
};
/**
* This enum lists the return result from Task Dialog
*
*/
Acad.TaskDialogResult = {
    "kRetOk": 1,
    "kRetCancel": 2,
    "kRetAbort": 3,
    "kRetRetry": 4,
    "kRetIgnore": 5,
    "kRetYes": 6,
    "kRetNo": 7,
    "kRetClose": 8,
    "kRetHelp": 9,
    "kRetTryAgain": 10,
    "kRetContinue": 11,
    "kRetTimeout": 32000
};
/**
* This enum lists the button that can be set for Task Dialog
*
*/
Acad.TaskDialogButton = {
    "kButtonOk": 1,
    "kButtonYes": // selected control return value kRetOk
    2,
    "kButtonNo": // selected control return value kRetYes
    4,
    "kButtonCancel": // selected control return value kRetNo
    8,
    "kButtonRetry": // selected control return value kRetCancel
    16,
    "kButtonClose": // selected control return value kRetRetry
    32
};
// selected control return value kRetClose
/**
* This enum lists the flag associated with AutoCAD command.
*
*/
Acad.CommandFlag = {
    "MODAL": 0,
    "TRANSPARENT": 1,
    "USEPICKSET": 2,
    "REDRAW": 4,
    "NOPERSPECTIVE": 8,
    "NOMULTIPLE": // NOT allowed in perspective views
    16,
    "NOTILEMODE": 32,
    "NOPAPERSPACE": // NOT allowed with TILEMODE == 1
    64,
    "NOOEM": // NOT allowed in Paperspace
    256,
    "UNDEFINED": 512,
    "INPROGRESS": 1024,
    "DEFUN": 2048,
    "LISPASCMD": 4096,
    "NONEWSTACK": // For Internal use only
    65536,
    "NOINTERNALLOCK": // For internal use only
    131072,
    "DOCREADLOCK": 524288,
    "DOCEXCLUSIVELOCK": // not set = DOCWRITELOCK
    1048576,
    "SESSION": // not set = DOCSHAREDLOCK
    2097152,
    "INTERRUPTIBLE": // Run cmd handler in the session fiber
    4194304,
    "NOHISTORY": // Supports OPM display of command properties
    8388608,
    "NO_UNDO_MARKER": // Command does not become default
    16777216,
    "NOBEDIT": // No Undo or Repeat presence.
    33554432,
    "NOACTIONRECORDING": // blocked during a bedit session
    67108864,
    "ACTIONMACRO": // Disallow Action Recording
    134217728,
    "RELAXASSOC": // Action Macro command
    268435456,
    "CORE": // Allow relaxed network evaluation during drag operation
    536870912,
    "NOINFERCONSTRAINT": // For internal use only
    1073741824,
    "TEMPSHOWDYNDIM": // Disallow Inferring constraints
    2147483648
};
// Temporarily show dynamic dimensions for selected entities during this command
/**
* For Internal use
*
*/
Acad.Int32MinValue = (-32768);
Acad.Int32MaxValue = 32767;
/**
* For Internal use
*
*/
Acad.extend = function (subClass, baseClass) {
    function inheritance() {
    }
    inheritance.prototype = baseClass.prototype;
    subClass.prototype = new inheritance();
};
/**
* This JSAPI enum wraps the AcGiMapper::Projection ObjectARX enum.
* This enumeration provides values that describe the mapping projection of the mapper.
*
*/
Acad.Enum_Projection = {
    "Parallel": 0,
    "Perspective": 1
};
/**
* This function tests whether the number passed is a valid float
* @param n of type float
* @returns boolean
*/
Acad.isNumber = function (n) {
    return !isNaN(parseFloat(n)) && isFinite(n) && typeof (n) !== 'string';
};
/**
* This function tests whether the number passed is a Integer
* @param value is a number
* @returns boolean
*/
Acad.isInteger = function (value) {
    return !isNaN(parseInt(value)) && (parseFloat(value) == parseInt(value));
};
/**
* This is ErrorStatus defined for Shaping Layer.
*
*/
Acad.ErrorStatus = {
    "eJsOk": 0
};
/*
* Creates a container object which holds Viewport related properties
* @param position of type Acad.Position3d
* @param target of type Acad.Position3d
* @param upVector of type Acad.Vector3d
* @param fieldWidth of type double
* @param fieldHeight of type double
* @param projection of type Acad.Enum_Projection
* @return a container object of type Acad.ViewProperties
*
*/
Acad.ViewProperties = function (position, target, upVector, fieldWidth, fieldHeight, projection) {
    if(!Acad.isNumber(fieldWidth)) {
        throw TypeError('fieldWidth should be a double value');
    }
    if(!Acad.isNumber(fieldHeight)) {
        throw TypeError('fieldHeight should be a double value');
    }
    if(!(position instanceof Acad.Point3d)) {
        throw TypeError('position should be of type Acad.Point3d');
    }
    if(!(target instanceof Acad.Point3d)) {
        throw TypeError('target should be of type Acad.Point3d');
    }
    if(!(upVector instanceof Acad.Vector3d)) {
        throw TypeError('upVector should be of type Acad.Vector3d');
    }
    if(!(projection === Acad.Enum_Projection.Parallel || projection === Acad.Enum_Projection.Perspective)) {
        throw TypeError('projection should be  Acad.Enum_Projection.Parallel or Acad.Enum_Projection.Perspective ');
    }
    this.position = position;
    this.target = target;
    this.upVector = upVector;
    this.fieldWidth = fieldWidth;
    this.fieldHeight = fieldHeight;
    this.projection = projection;
};
/*
* This is also used as a base class, designed to achieve Promise Pattern
*
*/
Acad.Promise = function () {
    /*
    * This is the function used to register callback
    * @param success Function pointer call at the time of success/cancel.
    * @param error Function pointer call at the time of error.
    * @throws TypeError
    *
    */
    this.then = function (success, error) {
        if(typeof (success) == 'function') {
            this.success = success;
        } else {
            throw TypeError('success function pointer should be of type function');
        }
        if(typeof (error) == 'function') {
            this.error = error;
        } else {
            throw TypeError('error function pointer should be of type function');
        }
    };
};
//
///////////////////////////////////////////////////////////////////////////////
//
//                 (C) Copyright 2012 by Autodesk, Inc.
//
// The information contained herein is confidential, proprietary to Autodesk,
// Inc., and considered a trade secret as defined in section 499C of the
// penal code of the State of California.  Use of this information by anyone
// other than authorized employees of Autodesk, Inc. is granted only under a
// written non-disclosure agreement, expressly prescribing the scope and
// manner of such use.
//
///////////////////////////////////////////////////////////////////////////////
/**
* This class can be used to log messages to a file.
* The log file is named AcJs.log and is created in C:\Users\...\AppData\Local\Autodesk\AcCloudConnect
* Logging is turned off by default, and will need to be explicitly enabled.
*/
Acad.Logger = new function () {
    var logEnabled = false;
    var jsonStr = exec(JSON.stringify({
        functionName: 'Ac_Log_isLoggingEnabled',
        invokeAsCommand: false,
        functionParams: undefined
    }));
    var jsonObj = JSON.parse(jsonStr);
    if(jsonObj.retCode == Acad.ErrorStatus.eJsOk) {
        if(jsonObj.logenabled) {
            logEnabled = true;
        }
    }
    function oncomplete() {
    }
    function onerror() {
    }
    this.isLogEnabled = function () {
        var jsonStr = exec(JSON.stringify({
            functionName: 'Ac_Log_isLoggingEnabled',
            invokeAsCommand: false,
            functionParams: undefined
        }));
        var jsonObj = JSON.parse(jsonStr);
        if(jsonObj.retCode == Acad.ErrorStatus.eJsOk) {
            if(jsonObj.logenabled) {
                logEnabled = true;
            }
        }
    };
    this.logFatal = function (value) {
        if(!logEnabled) {
            return;
        }
        execAsync(JSON.stringify({
            functionName: 'Ac_Log_logFatal',
            invokeAsCommand: false,
            functionParams: {
                msg: value
            }
        }), oncomplete, onerror);
    };
    this.logError = function (value) {
        if(!logEnabled) {
            return;
        }
        execAsync(JSON.stringify({
            functionName: 'Ac_Log_logError',
            invokeAsCommand: false,
            functionParams: {
                msg: value
            }
        }), oncomplete, onerror);
    };
    this.logWarn = function (value) {
        if(!logEnabled) {
            return;
        }
        execAsync(JSON.stringify({
            functionName: 'Ac_Log_logWarn',
            invokeAsCommand: false,
            functionParams: {
                msg: value
            }
        }), oncomplete, onerror);
    };
    this.logInfo = function (value) {
        if(!logEnabled) {
            return;
        }
        execAsync(JSON.stringify({
            functionName: 'Ac_Log_logInfo',
            invokeAsCommand: false,
            functionParams: {
                msg: value
            }
        }), oncomplete, onerror);
    };
    this.logDebug = function (value) {
        if(!logEnabled) {
            return;
        }
        execAsync(JSON.stringify({
            functionName: 'Ac_Log_logDebug',
            invokeAsCommand: false,
            functionParams: {
                msg: value
            }
        }), oncomplete, onerror);
    };
    this.logTrace = function (value) {
        if(!logEnabled) {
            return;
        }
        execAsync(JSON.stringify({
            functionName: 'Ac_Log_logTrace',
            invokeAsCommand: false,
            functionParams: {
                msg: value
            }
        }), oncomplete, onerror);
    };
    this.setLogLevel = function (value) {
        if(!logEnabled) {
            return;
        }
        execAsync(JSON.stringify({
            functionName: 'Ac_Log_setLogLevel',
            invokeAsCommand: false,
            functionParams: {
                logLevel: Number(value)
            }
        }), oncomplete, onerror);
    };
    this.getLogLevel = function (value) {
        if(!logEnabled) {
            return 0;
        }
        var jsonStr = exec(JSON.stringify({
            functionName: 'Ac_Log_getLogLevel',
            invokeAsCommand: false,
            functionParams: undefined
        }));
        var jsonObj = JSON.parse(jsonStr);
        if(jsonObj.retCode == Acad.ErrorStatus.eJsOk) {
            return jsonObj.loglevel;
        } else {
            return 0;
        }
    };
}();
//
///////////////////////////////////////////////////////////////////////////////
//
//                 (C) Copyright 2012 by Autodesk, Inc.
//
// The information contained herein is confidential, proprietary to Autodesk,
// Inc., and considered a trade secret as defined in section 499C of the
// penal code of the State of California.  Use of this information by anyone
// other than authorized employees of Autodesk, Inc. is granted only under a
// written non-disclosure agreement, expressly prescribing the scope and
// manner of such use.
//
///////////////////////////////////////////////////////////////////////////////
/**
* @class Acad.TransientManager
* This is the controller object that is used to create and manage the
* transients.
*/
Acad.TransientManager = function () {
    var transients = [];
    var transientid = 1;
    registerCallback('Ac_transientManager_event', transientManager_event);
    /**
    * This function is for internal use.
    *
    */
    function transientManager_event(args) {
        var obj = JSON.parse(args);
        if(!obj) {
            return;
        }
        var id = obj.id;
        var eventname = obj.eventname;
        var index = getIndex(id);
        if(index == -1) {
            return;
        }
        var transient = transients[index];
        obj.transient = transient;
        transient.dispatchEvent(eventname, obj);
    }
    /**
    * The addTransient function is used to add an Acad.Transient object to the AutoCAD transient manager.
    * The XML data represents an AcGiDrawable object defined by the transient.xsd schema.
    * @param transient is of type Acad.Transient.
    * @param xmlData is of type string.
    * @param onComplete is a function type called on successful completion of this method.
    * @param onError is a function type called if an error occurs.
    *
    */
    this.addTransient = function (transient, xmlData, onComplete, onError) {
        if(getIndex(transient.getId()) != -1) {
            return;
        }
        var completefn = onComplete || complete;
        var errorfn = onError || error;
        transients.push(transient);
        execAsync(JSON.stringify({
            functionName: 'Ac_TransientManager_addtransient',
            invokeAsCommand: false,
            functionParams: {
                id: transient.getId(),
                data: xmlData
            }
        }), completefn, errorfn);
    };
    /**
    * The updateTransient function is used to update an Acad.Transient object in the AutoCAD transient manager.
    * The XML data represents an AcGiDrawable object defined by the transient.xsd schema.
    * @param transientId is of type int.
    * @param xmlData is of type string.
    * @param onComplete is a function type called on successful completion of this method.
    * @param onError is a function type called if an error occurs.
    *
    */
    this.updateTransient = function (transientId, xmlData, onComplete, onError) {
        var completefn = onComplete || complete;
        var errorfn = onError || error;
        execAsync(JSON.stringify({
            functionName: 'Ac_TransientManager_updatetransient',
            invokeAsCommand: false,
            functionParams: {
                id: transientId,
                data: xmlData
            }
        }), completefn, errorfn);
    };
    /**
    * The eraseTransient function is used erase the the Acad.Transient object from the AutoCAD transient manager.
    * @param transientId is of type int.
    * @param onComplete is a function type called on successful completion of this method.
    * @param onError is a function type called if an error occurs.
    *
    */
    this.eraseTransient = function (transientId, onComplete, onError) {
        var completefn = onComplete || complete;
        var errorfn = onError || error;
        execAsync(JSON.stringify({
            functionName: 'Ac_TransientManager_erasetransient',
            invokeAsCommand: false,
            functionParams: {
                id: transientId
            }
        }), completefn, errorfn);
    };
    /**
    * The eraseTransients function is used erase Acad.Transient objects from the AutoCAD transient manager.
    * @param transientIds is of type Array int.
    * @param onComplete is a function type called on successful completion of this method.
    * @param onError is a function type called if an error occurs.
    *
    */
    this.eraseTransients = function (transientIds, onComplete, onError) {
        var completefn = onComplete || complete;
        var errorfn = onError || error;
        execAsync(JSON.stringify({
            functionName: 'Ac_TransientManager_erasetransients',
            invokeAsCommand: false,
            functionParams: {
                ids: transientIds
            }
        }), completefn, errorfn);
    };
    /**
    * The showTransients function is used show or hide the Acad.Transient objects in
    * the AutoCAD transient manager.
    * @param transientIds is of type Array int.
    * @param bShow is of type bool.
    * @param onComplete is a function type called on successful completion of this method.
    * @param onError is a function type called if an error occurs.
    *
    */
    this.showTransients = function (transientIds, bShow, onComplete, onError) {
        var completefn = onComplete || complete;
        var errorfn = onError || error;
        execAsync(JSON.stringify({
            functionName: 'Ac_TransientManager_showtransients',
            invokeAsCommand: false,
            functionParams: {
                ids: transientIds,
                show: bShow
            }
        }), completefn, errorfn);
    };
    /**
    * The getCursor function is used to get the current cursor assigned to the Acad.Transient object.
    * It is returned in the cursor property of the object in the onComplete method.
    * This is the optional 'cursor' attribute in the transient XML schema.
    * @param transientId is of type int.
    * @param onComplete is a function type called on successful completion of this method.
    * @param onError is a function type called if an error occurs.
    *
    */
    this.getCursor = function (transientId, onComplete, onError) {
        var completefn = onComplete || complete;
        var errorfn = onError || error;
        execAsync(JSON.stringify({
            functionName: 'Ac_TransientManager_getcursor',
            invokeAsCommand: false,
            functionParams: {
                id: transientId
            }
        }), completefn, errorfn);
    };
    /**
    * This function is a private API for internal use.
    *
    */
    this.generateImage = function (imgtype, imgId, imgPostedBy, imgMessage) {
        var jsonStr = exec(JSON.stringify({
            functionName: 'Ac_Transientmanager_generateimage',
            invokeAsCommand: false,
            functionParams: {
                type: imgtype,
                id: imgId,
                postedby: imgPostedBy,
                message: imgMessage
            }
        }));
        return jsonStr;
    };
    /**
    * This function is for internal use.
    * generate id from stub layer
    *
    */
    this.getNewId = function () {
        var jsonResponse = exec(JSON.stringify({
            functionName: 'Ac_TransientManager_getNewId',
            invokeAsCommand: false
        }));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
        return parseInt(jsonObj.id);
    };
    /**
    * This function is for internal use.
    *
    */
    function getIndex(id) {
        for(var i = 0, len = transients.length; i < len; i++) {
            if(transients[i].getId() === id) {
                return i;
            }
        }
        return -1;
    }
    function complete() {
    }
    function error() {
    }
};
/**
* @class Acad.TransientManager
* This is the controller object that is used to create and manage the
* transients.
*/
Acad.Transient = function () {
    var id = Acad.Application.activedocument.transientManager.getNewId();
    var eventobject = new Acad.EventObject();
    this.eventname = {
        "mousemove": "mousemove",
        "mouseleave": "mouseleave",
        "lbuttondown": "lbuttondown",
        "lbuttonup": "lbuttonup",
        "lbuttondblclk": "lbuttondblclk",
        "rbuttondown": "rbuttondown",
        "rbuttonup": "rbuttonup",
        "rbuttondblclk": "rbuttondblclk",
        "mbuttondown": "mbuttondown",
        "mbuttonup": "mbuttonup",
        "mbuttondblclk": "mbuttondblclk",
        "mousewheel": "mousewheel"
    };
    //"mousehover"    : "mousehover",
    /**
    * This function is used to add a callback.
    * @param eventname is the event for which fn would be called.
    * @param fn is a callback function, which is called when an event occurs.
    *
    */
    this.addEventListener = function (eventname, fn) {
        eventobject.addEventListener(eventname, fn);
    };
    /**
    * This function is used to remove a callback.
    * @param eventname is the event for which fn would be called.
    * @param fn is a callback function, which would not be called further for the given eventname.
    *
    */
    this.removeEventListener = function (eventname, fn) {
        eventobject.removeEventListener(eventname, fn);
    };
    /**
    * The getId function is used get the assigned transient id.
    * @return int.
    *
    */
    this.getId = function () {
        return id;
    };
    /**
    * This function is for internal use.
    *
    */
    this.dispatchEvent = function (eventname, args) {
        eventobject.dispatchEvent(eventname, args);
    };
};
//
///////////////////////////////////////////////////////////////////////////////
//
//                 (C) Copyright 2012 by Autodesk, Inc.
//
// The information contained herein is confidential, proprietary to Autodesk,
// Inc., and considered a trade secret as defined in section 499C of the
// penal code of the State of California.  Use of this information by anyone
// other than authorized employees of Autodesk, Inc. is granted only under a
// written non-disclosure agreement, expressly prescribing the scope and
// manner of such use.
//
///////////////////////////////////////////////////////////////////////////////
/**
* @class Acad.OSet,
* The object contains a collection of object identifiers.
* Its similar to ads_name, and valid only while you are working on a drawing
* with AutoCAD, and they are invalid when exiting from AutoCAD or switching to
* another drawing.
*/
Acad.OSet = function () {
    var dbObjects = [];
    function getIndex(id) {
        for(var i = 0, len = dbObjects.length; i < len; i++) {
            // Allow type coercion for now since the id can be number or string.
            if(dbObjects[i] == id) {
                return i;
            }
        }
        return -1;
    }
    /**
    * The method will add the input object id to the collection.
    * @param Input object id.
    */
    this.add = function (id) {
        if(!id) {
            return;
        }
        if(typeof id === "string" || typeof id === "number") {
            dbObjects.push(id);
        } else {
            if(id instanceof Array) {
                dbObjects = dbObjects.concat(id);
            } else {
                if(id instanceof Acad.OSet) {
                    for(var i = 0, len = id.getCount(); i < len; i++) {
                        dbObjects.push(id.getId(i));
                    }
                }
            }
        }
    };
    /**
    * The method will remove the input object id from the collection.
    * @param Input id.
    */
    this.remove = function (id) {
        var index = getIndex(id);
        if(index !== -1) {
            dbObjects.splice(index, 1);
        }
    };
    /**
    * The method will remove all the ids from the collection.
    */
    this.clear = function () {
        dbObjects = [];
    };
    /**
    * The method will return the number of items in the collection.
    * @return Returns the number of items in the collection.
    */
    this.getCount = function () {
        return dbObjects.length;
    };
    /**
    * The method will return the id given the index of the item in the collection.
    * @param Input index, it should be more than or equal to 0 and less than the number of items in the collection.
    * @return Returns the id at the given index.
    */
    this.getId = function (index) {
        return dbObjects[index];
    };
    /**
    * The method will return the index of the input id, in the collection.
    * @param Input id.
    * @return Returns the index of the input id if it is present, otherwise returns -1.
    */
    this.indexOf = function (id) {
        return getIndex(id);
    };
    /**
    * The method can be used to test if the id is present in the collection.
    * @param Input id.
    * @return Returns true if the id is present in the collection, otherwise returns false.
    */
    this.contains = function (id) {
        return getIndex(id) != -1;
    };
    /**
    * The method will return all the ids in the collection.
    * @return Returns an array that contains all the ids in the collection.
    */
    this.getAllIds = function () {
        var ids = [];
        ids = ids.concat(dbObjects);
        return ids;
    };
};
/**
* @class Acad.DBEntity,
* The object represents a database resident entity
* Its similar to AcDbEntity, and valid only while you are working on a drawing
* with AutoCAD, and is invalid when exiting from AutoCAD or switching to
* another drawing.
* @param id is the object identifier
*/
Acad.DBEntity = function (id) {
    if(!id) {
        throw TypeError(" id is mandatory for new DBEntity");
    }
    var entityId = id;
    /**
    * Returns the object identifier. Read only property.
    * @return id which is of string type
    */
    Object.defineProperty(this, "id", {
        get: function () {
            return entityId;
        },
        set: function (val) {
            throw Error(" You are not allowed to set this property");
        }
    });
    /**
    * Returns the object geometric extents defined by min and max points.
    * @return object of type Acad.Bounds3d
    */
    this.getExtents = function () {
        var args = {
        };
        args.functionName = "Ac_DBEntity_getExtents";
        args.invokeAsCommand = false;
        args.functionParams = new function () {
            this.id = entityId;
        }();
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
        var minPt3d = new Acad.Point3d(jsonObj.minPoint3d.x, jsonObj.minPoint3d.y, jsonObj.minPoint3d.z);
        var maxPt3d = new Acad.Point3d(jsonObj.maxPoint3d.x, jsonObj.maxPoint3d.y, jsonObj.maxPoint3d.z);
        return new Acad.Bounds3d(minPt3d, maxPt3d);
    };
};
/**
* @class Acad.TaskDialog,
* The object represents a task dialog
*/
Acad.TaskDialog = new function () {
    /**
    * Show a custom task dialog.
    * @param strWindowTitle is the string for dialog title.
    * @param strMainInstruction is the string for main instruction in the dialog.
    * @param strContentText is the string for content text in the dialog.
    * @param nCommonButtons is the integer flag which specifies buttons displayed in the dialog.
    * It can be bitwise OR values of enum Acad.TaskDialogButton, such as Acad.TaskDialogButton.kButtonOk | Acad.TaskDialogButton.kButtonCancel.
    * @returns the promise object, the then argument can be used. Success callback will return result in enum Acad.TaskDialogResult.
    */
    this.showTaskDialog = function (strWindowTitle, strMainInstruction, strContentText, nCommonButtons) {
        if(typeof (strWindowTitle) !== 'string') {
            throw TypeError('strWindowTitle should be of type string');
        }
        if(typeof (strMainInstruction) !== 'string') {
            throw TypeError('strMainInstruction should be of type string');
        }
        if(typeof (strContentText) !== 'string') {
            throw TypeError('strContentText should be of type string');
        }
        if(!(Acad.isInteger(nCommonButtons))) {
            throw TypeError('nCommonButtons should be of type integer');
        }
        var result = new Acad.Promise();
        execAsync(JSON.stringify({
            functionName: 'Ac_TaskDialog_showTaskDialog',
            invokeAsCommand: false,
            functionParams: {
                windowTitle: strWindowTitle,
                mainInstruction: strMainInstruction,
                contentText: strContentText,
                commonButtons: nCommonButtons
            }
        }), function (jsonResponse) {
            if(typeof (result.success) == 'function') {
                var jsonObj = JSON.parse(jsonResponse);
                result.success(jsonObj.dialogResult);
            }
        }, function (jsonResponse) {
            if(typeof (result.error) == 'function') {
                var jsonObj = JSON.parse(jsonResponse);
                var errValue;
                if(jsonObj) {
                    errValue = jsonObj.retCode;
                }
                result.error(errValue);
            }
        });
        return result;
    };
    /**
    * Show a task dialog with confirmation message to delete.
    * @param strTitle is the string for dialog title: "<strTitle> - Delete <strTitle>".
    * @param strMessage is the string for message in the dialog: "Are you sure you want to delete <strMessage> ?"
    * @returns the promise object, the then argument can be used. Success callback will return result in enum Acad.TaskDialogResult.
    */
    this.showDeleteConfirmationTaskDialog = function (strTitle, strMessage) {
        if(typeof (strTitle) !== 'string') {
            throw TypeError('strTitle should be of type string');
        }
        if(typeof (strMessage) !== 'string') {
            throw TypeError('strMessage should be of type string');
        }
        var result = new Acad.Promise();
        execAsync(JSON.stringify({
            functionName: 'Ac_TaskDialog_showDeleteConfirmationTaskDialog',
            invokeAsCommand: false,
            functionParams: {
                dialogTitle: strTitle,
                dialogMessage: strMessage
            }
        }), function (jsonResponse) {
            if(typeof (result.success) == 'function') {
                var jsonObj = JSON.parse(jsonResponse);
                result.success(jsonObj.dialogResult);
            }
        }, function (jsonResponse) {
            if(typeof (result.error) == 'function') {
                var jsonObj = JSON.parse(jsonResponse);
                var errValue;
                if(jsonObj) {
                    errValue = jsonObj.retCode;
                }
                result.error(errValue);
            }
        });
        return result;
    };
}();
/**
* For Internal Use
*
*/
Acad.EventObject = function () {
    this.listeners = {
    };
};
Acad.EventObject.prototype = {
    constructor: Acad.EventObject,
    addEventListener: function (eventname, listener) {
        if(typeof this.listeners[eventname] == "undefined") {
            this.listeners[eventname] = [];
        }
        this.listeners[eventname].push(listener);
    },
    removeEventListener: function (eventname, listener) {
        if(this.listeners[eventname] instanceof Array) {
            var listeners = this.listeners[eventname];
            for(var i = 0, len = listeners.length; i < len; i++) {
                if(listeners[i] === listener) {
                    break;
                }
            }
            listeners.splice(i, 1);
        }
    },
    dispatchEvent: function (eventname, args) {
        if(this.listeners[eventname] instanceof Array) {
            var listeners = this.listeners[eventname];
            for(var i = 0, len = listeners.length; i < len; i++) {
                listeners[i](eventname, args);
            }
        }
    },
    count: function (eventname) {
        if(this.listeners[eventname] instanceof Array) {
            var listeners = this.listeners[eventname];
            return listeners.length;
        }
        return 0;
    }
};
/**
* @class Acad.Application, its a singleton. The class
* provides services for accessing the active document object.
*/
Acad.Application = (function () {
    var documents = [
        new DocumentImp()
    ];
    function DocumentImp() {
        var dbobjects = {
        };
        this.eventname = {
            "modified": "modified",
            "erased": "erased"
        };
        registerCallback('Ac_activedocument_databaseobject_event', activedocument_databaseobject_event);
        /**
        * This returns a transient manager object.
        */
        this.transientManager = new Acad.TransientManager();
        /**
        * This function is for internal use.
        *
        */
        function activedocument_databaseobject_event(args) {
            var obj = JSON.parse(args);
            if(!obj) {
                return;
            }
            var id = obj.id;
            var eventname = obj.eventname;
            var eventobj = dbobjects[id];
            if(eventobj) {
                eventobj.dispatchEvent(eventname, obj);
            }
        }
        /**
        * This function is for internal use.
        *
        */
        function oncomplete() {
        }
        /**
        * This function is for internal use.
        *
        */
        function onerror() {
        }
        /**
        * The method can be used to subscribe to object event notifications
        * for an object.
        * @param oset is the object to be observed.
        * @param Input event for receiving notification. It can be one of the values in Acad.Application.activedocument.eventname.
        * @param Input event handler, the event handler will called when the respective event occurs.
        * @throws Error
        */
        this.startObserving = function (oset, eventname, fn) {
            if(!fn) {
                throw Error("startObserving(): Invalid listener");
            }
            if(!eventname || (eventname != this.eventname.modified && eventname != this.eventname.erased)) {
                throw Error("startObserving(): Invalid eventname");
            }
            if(!oset) {
                throw Error("startObserving(): Invalid oset");
            }
            if(!(oset instanceof Acad.OSet)) {
                throw new TypeError("startObserving(): oset should be of type Acad.OSet");
            }
            var osetCount = oset.getCount();
            if(osetCount <= 0) {
                throw Error("startObserving(): Empty oset");
            }
            var objId;
            for(var i = 0, len = oset.getCount(); i < len; i++) {
                objId = oset.getId(i);
                var eventobject = dbobjects[objId];
                if(!eventobject) {
                    eventobject = new Acad.EventObject();
                    // Augument the object with a new property
                    eventobject.objId = objId;
                    dbobjects[objId] = eventobject;
                }
                eventobject.addEventListener(eventname, fn);
            }
            execAsync(JSON.stringify({
                functionName: 'Ac_Application_activedocument_addobjectreactor',
                invokeAsCommand: false,
                functionParams: {
                    ids: oset.getAllIds()
                }
            }), oncomplete, onerror);
        };
        /**
        * The method can be used to unsubscribe from receiving object event
        * notifications for the respective object.
        * @param oset is the object from which to stop receiving notifications.
        * @param Input event to stop receiving notifications.
        * @param Input event handler that was passed to startObserving method.
        * @throws Error
        */
        this.stopObserving = function (oset, eventname, fn) {
            if(!fn) {
                throw Error("stopObserving(): Invalid listener");
            }
            if(!eventname || (eventname != this.eventname.modified && eventname != this.eventname.erased)) {
                throw Error("stopObserving(): Invalid eventname");
            }
            if(!oset) {
                throw Error("stopObserving(): Invalid oset");
            }
            if(!(oset instanceof Acad.OSet)) {
                throw new TypeError("stopObserving(): oset should be of type Acad.OSet");
            }
            var osetCount = oset.getCount();
            if(osetCount <= 0) {
                throw Error("stopObserving(): Empty oset");
            }
            var ids = [];
            for(var i = 0; i < osetCount; i++) {
                var objId = oset.getId(i);
                var eventobject = dbobjects[objId];
                if(eventobject) {
                    eventobject.removeEventListener(eventname, fn);
                    if(eventobject.count(this.eventname.modified) <= 0 && eventobject.count(this.eventname.erased) <= 0) {
                        ids.push(objId);
                        dbobjects[objId] = undefined;
                    }
                }
            }
            if(ids.length <= 0) {
                return;
            }
            execAsync(JSON.stringify({
                functionName: 'Ac_Application_activedocument_removeobjectreactor',
                invokeAsCommand: false,
                functionParams: {
                    ids: ids
                }
            }), oncomplete, onerror);
        };
        /**
        * This function can be used to get the array of handles from the OSet.
        * @param Input oset that contains the object ids.
        * @returns the promise object, the then argument can be used.
        */
        this.getHandle = function (oset) {
            if(!oset) {
                throw Error("getHandle(): Invalid oset");
            }
            if(!(oset instanceof Acad.OSet)) {
                throw new TypeError("getHandle(): oset should be of type Acad.OSet");
            }
            var osetCount = oset.getCount();
            if(osetCount <= 0) {
                throw Error("getHandle(): Empty oset");
            }
            var result = new Acad.Promise();
            execAsync(JSON.stringify({
                functionName: 'Ac_Application_activedocument_gethandle',
                invokeAsCommand: false,
                functionParams: {
                    ids: oset.getAllIds()
                }
            }), function (jsonResponse) {
                if(typeof (result.success) == 'function') {
                    var obj = JSON.parse(jsonResponse);
                    var retvalue;
                    if(obj) {
                        retvalue = obj.value;
                    }
                    result.success(retvalue);
                }
            }, function (jsonResponse) {
                if(typeof (result.error) == 'function') {
                    var jsonObj = JSON.parse(jsonResponse);
                    var errValue;
                    if(jsonObj) {
                        errValue = jsonObj.retCode;
                    }
                    result.error(errValue);
                }
            });
            return result;
        };
        /**
        * This function can be used to get the array of object ids from the handles.
        * @param Input array containing the handles.
        * @returns the promise object, the then argument can be used.
        */
        this.getObjectSet = function (handles) {
            if(!handles) {
                throw Error("getObjectSet(): Invalid handles");
            }
            if(!(handles instanceof Array)) {
                throw Error("getObjectSet(): Invalid handles");
            }
            if(handles.length <= 0) {
                throw Error("getObjectSet(): empty handles");
            }
            var result = new Acad.Promise();
            execAsync(JSON.stringify({
                functionName: 'Ac_Application_activedocument_getobjectset',
                invokeAsCommand: false,
                functionParams: {
                    ids: handles
                }
            }), function (jsonResponse) {
                if(typeof (result.success) == 'function') {
                    var obj = JSON.parse(jsonResponse);
                    var retvalue;
                    if(obj) {
                        retvalue = obj.value;
                    }
                    result.success(retvalue);
                }
            }, function (jsonResponse) {
                if(typeof (result.error) == 'function') {
                    var jsonObj = JSON.parse(jsonResponse);
                    var errValue;
                    if(jsonObj) {
                        errValue = jsonObj.retCode;
                    }
                    result.error(errValue);
                }
            });
            return result;
        };
        /**
        * The function can be used to launch the login dialog.
        * @returns the promise object, the then argument can be used.
        */
        this.loginA360 = function () {
            var result = new Acad.Promise();
            execAsync(JSON.stringify({
                functionName: 'Ac_Application_activedocument_logina360',
                invokeAsCommand: false,
                functionParams: undefined
            }), function (jsonResponse) {
                if(typeof (result.success) == 'function') {
                    result.success();
                }
            }, function (jsonResponse) {
                if(typeof (result.error) == 'function') {
                    var jsonObj = JSON.parse(jsonResponse);
                    var errValue;
                    if(jsonObj) {
                        errValue = jsonObj.retCode;
                    }
                    result.error(errValue);
                }
            });
            return result;
        };
        /**
        * The function can be used to share the drawing.
        * @returns the promise object, the then argument can be used.
        */
        this.shareDrawing = function () {
            var result = new Acad.Promise();
            execAsync(JSON.stringify({
                functionName: 'Ac_Application_activedocument_sharedrawing',
                invokeAsCommand: false,
                functionParams: undefined
            }), function (jsonResponse) {
                if(typeof (result.success) == 'function') {
                    result.success();
                }
            }, function (jsonResponse) {
                if(typeof (result.error) == 'function') {
                    var jsonObj = JSON.parse(jsonResponse);
                    var errValue;
                    if(jsonObj) {
                        errValue = jsonObj.retCode;
                    }
                    result.error(errValue);
                }
            });
            return result;
        };
        /**
        * The function can be used to share the drawing.
        * @returns the promise object, the then argument can be used.
        */
        this.getContacts = function () {
            var result = new Acad.Promise();
            execAsync(JSON.stringify({
                functionName: 'Ac_Application_activedocument_getcontacts',
                invokeAsCommand: false,
                functionParams: undefined
            }), function (jsonResponse) {
                if(typeof (result.success) == 'function') {
                    var obj = JSON.parse(jsonResponse);
                    var contacts;
                    if(obj) {
                        contacts = obj.contacts;
                    }
                    result.success(contacts);
                }
            }, function (jsonResponse) {
                if(typeof (result.error) == 'function') {
                    var jsonObj = JSON.parse(jsonResponse);
                    var errValue;
                    if(jsonObj) {
                        errValue = jsonObj.retCode;
                    }
                    result.error(errValue);
                }
            });
            return result;
        };
        /**
        * The function can be used to save and sync a file to A360.
        * @returns the promise object, the then argument can be used.
        */
        this.saveSync = function () {
            var result = new Acad.Promise();
            execAsync(JSON.stringify({
                functionName: 'Ac_Application_activedocument_savesync',
                invokeAsCommand: false,
                functionParams: undefined
            }), function (jsonResponse) {
                if(typeof (result.success) == 'function') {
                    result.success();
                }
            }, function (jsonResponse) {
                if(typeof (result.error) == 'function') {
                    var jsonObj = JSON.parse(jsonResponse);
                    var errValue;
                    if(jsonObj) {
                        errValue = jsonObj.retCode;
                    }
                    result.error(errValue);
                }
            });
            return result;
        };
        /**
        * This function can be used to verify if the user is the owner of the
        * of the file that is on the cloud.
        * @returns the promise object, the then argument can be used.
        * The success method will be called with the boolean argument
        * indicating if the user is the owner.
        */
        this.isCloudFileOwner = function () {
            var result = new Acad.Promise();
            execAsync(JSON.stringify({
                functionName: 'Ac_Application_activedocument_iscloudfileowner',
                invokeAsCommand: false,
                functionParams: undefined
            }), function (jsonResponse) {
                if(typeof (result.success) == 'function') {
                    var obj = JSON.parse(jsonResponse);
                    var value;
                    if(obj) {
                        value = obj.value;
                    }
                    result.success(value);
                }
            }, function (jsonResponse) {
                if(typeof (result.error) == 'function') {
                    var jsonObj = JSON.parse(jsonResponse);
                    var errValue;
                    if(jsonObj) {
                        errValue = jsonObj.retCode;
                    }
                    result.error(errValue);
                }
            });
            return result;
        };
        /**
        * The method can be used to launch a modal dialog with
        * the specified url
        * @param value is the url to be rendered.
        *
        */
        this.showModalDialog = function (value) {
            execAsync(JSON.stringify({
                functionName: 'Ac_Application_activedocument_showmodaldialog',
                invokeAsCommand: false,
                functionParams: {
                    url: value
                }
            }), oncomplete, onerror);
        };
        /**
        * The method can be used to set the commit state of the modal dialog.
        * It is analogous to the OK or Cancel return value of a dialog.
        * Calling this method dismisses the HTML dialog.
        * @param value is the bool value of the commit state
        *
        */
        this.modalDialogCommit = function (value) {
            execAsync(JSON.stringify({
                functionName: 'Ac_Application_activedocument_modaldialogcommit',
                invokeAsCommand: false,
                functionParams: {
                    commit: value
                }
            }), oncomplete, onerror);
        };
        /**
        * The method can be used to launch a palette with
        * the specified url
        * @param strPaletteName is the palette name .
        * @param uriOfHtmlPage is the url to be rendered.
        *
        */
        this.addPalette = function (strPaletteName, uriOfHtmlPage) {
            if(typeof (strPaletteName) !== 'string') {
                throw TypeError('strPaletteName should be of type string');
            }
            if(typeof (uriOfHtmlPage) !== 'string') {
                throw TypeError('uriOfHtmlPage should be of type string');
            }
            execAsync(JSON.stringify({
                functionName: 'Ac_Application_activedocument_addPalette',
                invokeAsCommand: false,
                functionParams: {
                    paletteName: strPaletteName,
                    url: uriOfHtmlPage
                }
            }), oncomplete, onerror);
        };
        /**
        * The method can be used to capture an image of the current document.
        * The image is returned as a base64 encoded bitmap.
        * @param values are the width and height of the final image.
        * @returns the promise object, the then argument can be used.
        *
        */
        this.capturePreview = function (w, h) {
            var result = new Acad.Promise();
            execAsync(JSON.stringify({
                functionName: 'Ac_Application_activedocument_capturepreview',
                invokeAsCommand: false,
                functionParams: {
                    width: w,
                    height: h
                }
            }), function (retvalue) {
                if(typeof (result.success) == 'function') {
                    var obj = JSON.parse(retvalue);
                    var encodedbmp;
                    if(obj) {
                        encodedbmp = obj.encodedbitmap;
                    }
                    result.success(encodedbmp);
                }
            }, function (jsonResponse) {
                if(typeof (result.error) == 'function') {
                    var jsonObj = JSON.parse(jsonResponse);
                    var errValue;
                    if(jsonObj) {
                        errValue = jsonObj.retCode;
                    }
                    result.error(errValue);
                }
            });
            return result;
        };
        /**
        * This function can be used to highlight the list of entities represented by the given OSet.
        * @param Input oset that contains the object ids.
        */
        this.highlight = function (oset) {
            if(!oset) {
                throw Error("highlight(): Invalid oset");
            }
            if(!(oset instanceof Acad.OSet)) {
                throw new TypeError("highlight(): oset should be of type Acad.OSet");
            }
            var osetCount = oset.getCount();
            if(osetCount <= 0) {
                throw Error("highlight(): Empty oset");
            }
            var jsonStr = exec(JSON.stringify({
                functionName: 'Ac_Application_activedocument_highlight',
                invokeAsCommand: true,
                functionParams: {
                    ids: oset.getAllIds()
                }
            }));
            var jsonObj = JSON.parse(jsonStr);
            if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
                throw Error(jsonObj.retErrorString);
            }
        };
        /**
        * This function can be used to unhighlight the list of entities represented by the given OSet.
        * @param Input oset that contains the object ids.
        */
        this.unhighlight = function (oset) {
            if(!oset) {
                throw Error("unhighlight(): Invalid oset");
            }
            if(!(oset instanceof Acad.OSet)) {
                throw new TypeError("unhighlight(): oset should be of type Acad.OSet");
            }
            var osetCount = oset.getCount();
            if(osetCount <= 0) {
                throw Error("unhighlight(): Empty oset");
            }
            var jsonStr = exec(JSON.stringify({
                functionName: 'Ac_Application_activedocument_unhighlight',
                invokeAsCommand: true,
                functionParams: {
                    ids: oset.getAllIds()
                }
            }));
            var jsonObj = JSON.parse(jsonStr);
            if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
                throw Error(jsonObj.retErrorString);
            }
        };
    }
    ; ;
    return {
        activedocument: /**
        * This returns the current document object.
        */
        documents[0]
    };
})();
//
///////////////////////////////////////////////////////////////////////////////
//
//                 (C) Copyright 2012 by Autodesk, Inc.
//
// The information contained herein is confidential, proprietary to Autodesk,
// Inc., and considered a trade secret as defined in section 499C of the
// penal code of the State of California.  Use of this information by anyone
// other than authorized employees of Autodesk, Inc. is granted only under a
// written non-disclosure agreement, expressly prescribing the scope and
// manner of such use.
//
///////////////////////////////////////////////////////////////////////////////
Acad.Editor = new function () {
    /**
    * The getInteger function is used to get the integer from user.
    * @param opts is of type PromptIntegerOptions
    * @return PromptIntegerResult.
    * @throws TypeError
    *
    */
    this.getInteger = function (options) {
        if(!(options instanceof Acad.PromptIntegerOptions)) {
            throw TypeError("Input parameter should be PromptIntegerOptions type.");
        }
        var args = {
            'functionName': 'Ac_Editor_getInteger',
            'invokeAsCommand': true
        };
        args.functionParams = options;
        return Acad.promptExecAsync(args);
    };
    /**
    * The getDouble function is used to get the double from user.
    * @param options is of type PromptDoubleOptions
    * @return PromptDoubleResult.
    * @throws TypeError
    *
    */
    this.getDouble = function (options) {
        if(!(options instanceof Acad.PromptDoubleOptions)) {
            throw TypeError("Input parameter should be PromptDoubleOptions type.");
        }
        var args = {
            'functionName': 'Ac_Editor_getDouble',
            'invokeAsCommand': true
        };
        args.functionParams = options;
        return Acad.promptExecAsync(args);
    };
    /**
    * The getDistance function is used to get user input for a linear distance.
    * @param options is of type PromptDistanceOptions.
    * @return PromptDoubleResult.
    * @throws TypeError
    *
    */
    this.getDistance = function (options) {
        if(!(options instanceof Acad.PromptDistanceOptions)) {
            throw TypeError("Input parameter should be PromptDistanceOptions type.");
        }
        var args = {
            'functionName': 'Ac_Editor_getDistance',
            'invokeAsCommand': true
        };
        args.functionParams = options;
        return Acad.promptExecAsync(args);
    };
    /**
    * The getAngle function is used to get user input for an angle, taking into account the current value of the ANGBASE system variable.
    * @param options is of type PromptAngleOptions.
    * @return PromptDoubleResult.
    * @throws TypeError
    *
    */
    this.getAngle = function (options) {
        if(!(options instanceof Acad.PromptAngleOptions)) {
            throw TypeError("Input parameter should be PromptAngleOptions type.");
        }
        var args = {
            'functionName': 'Ac_Editor_getAngle',
            'invokeAsCommand': true
        };
        args.functionParams = options;
        return Acad.promptExecAsync(args);
    };
    /**
    * Gets user input for a keyword.
    * Wraps the acedGetKword() ObjectARX function.
    * The AutoCAD user can enter the keyword from the keyboard. The list of keywords that GetKeywords() accepts is set by a prior call to GetInteger().
    * If the user enters a string not specified in the call to GetInteger(), AutoCAD displays an error message and tries again (and redisplays prompt, if one was specified).
    * If the user types only [Return], GetKeywords() returns an empty string ("") unless the call to GetInteger() also disallowed null input.
    * @param options is of type PromptKeywordOptions
    * @return PromptResult.
    * @throws TypeError
    *
    */
    this.getKeywords = function (options) {
        if(!(options instanceof Acad.PromptKeywordOptions)) {
            throw TypeError("Input parameter should be PromptKeywordOptions type.");
        }
        var args = {
            'functionName': 'Ac_Editor_getKeywords',
            'invokeAsCommand': true
        };
        args.functionParams = options;
        return Acad.promptExecAsync(args);
    };
    /**
    * The getPoint function is used to get user input for a point.
    * @param opts is of type PromptPointOptions.
    * @return PromptPointResult.
    * @throws TypeError
    *
    */
    this.getPoint = function (options) {
        if(!(options instanceof Acad.PromptPointOptions)) {
            throw TypeError("Input parameter should be PromptPointOptions type.");
        }
        var args = {
            'functionName': 'Ac_Editor_getPoint',
            'invokeAsCommand': true
        };
        args.functionParams = options;
        return Acad.promptExecAsync(args);
    };
    /**
    * The getCorner function is used to Gets user input for the corner of a rectangle.
    * @param opts is of type PromptCornerOptions.
    * @return PromptPointResult.
    * @throws TypeError
    *
    */
    this.getCorner = function (options) {
        if(!(options instanceof Acad.PromptCornerOptions)) {
            throw TypeError("Input parameter should be PromptCornerOptions type.");
        }
        var args = {
            'functionName': 'Ac_Editor_getCorner',
            'invokeAsCommand': true
        };
        args.functionParams = options;
        return Acad.promptExecAsync(args);
    };
    /**
    * The getString function is used to Gets user input for string.
    * @param opts is of type PromptStringOptions.
    * @return PromptStringResult.
    * @throws TypeError
    *
    */
    this.getString = function (options) {
        if(!(options instanceof Acad.PromptStringOptions)) {
            throw TypeError("Input parameter should be PromptStringOptions type.");
        }
        var args = {
            'functionName': 'Ac_Editor_getString',
            'invokeAsCommand': true
        };
        args.functionParams = options;
        return Acad.promptExecAsync(args);
    };
    /**
    * The getSelection function returns the selection set obtained.
    * @param opts is of type PromptSelectionOptions.
    * @return PromptSelectionResult.
    * @throws TypeError
    *
    */
    this.getSelection = function (options) {
        if(!(options instanceof Acad.PromptSelectionOptions)) {
            throw TypeError("Input parameter should be PromptSelectionOptions type.");
        }
        var args = {
            'functionName': 'Ac_Editor_getSelection',
            'invokeAsCommand': true
        };
        args.functionParams = options;
        return Acad.promptExecAsync(args);
    };
    /**
    * Prompts the user to select an entity by specifying a point.
    * Pauses for user input and returns both an entity name and the point that is used to select the entity.
    * GetEntity() does not return the names of nongraphical objects.
    * @param opts is of type PromptEntityOptions.
    * @return PromptEntityResult.
    * @throws TypeError
    *
    */
    this.getEntity = function (options) {
        if(!(options instanceof Acad.PromptEntityOptions)) {
            throw TypeError("Input parameter should be PromptEntityOptions type.");
        }
        var args = {
            'functionName': 'Ac_Editor_getEntity',
            'invokeAsCommand': true
        };
        args.functionParams = options;
        return Acad.promptExecAsync(args);
    };
    /**
    * Gets the name of an entity selected by the user and the point used to select the entity.
    * @param opts is of type PromptNestedEntityOptions.
    * @return PromptNestedEntityResult.
    * @throws TypeError
    *
    */
    this.getNestedEntity = function (options) {
        if(!(options instanceof Acad.PromptNestedEntityOptions)) {
            throw TypeError("Input parameter should be PromptNestedEntityOptions type.");
        }
        var args = {
            'functionName': 'Ac_Editor_getNestedEntity',
            'invokeAsCommand': true
        };
        args.functionParams = options;
        return Acad.promptExecAsync(args);
    };
    /**
    * This method returns false if the host busy processing other commands else returns true.
    * @return boolean.
    * @throws TypeError
    *
    */
    this.isQuiescent = function () {
        var args = {
        };
        args.functionName = "Ac_Editor_isQuiescent";
        args.invokeAsCommand = false;
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
        return jsonObj.state === 1 ? true : false;
    };
    /**
    * This method cancels the last command
    * @throws Error
    *
    */
    this.cancelCommand = function () {
        var args = {
        };
        args.functionName = "Ac_Editor_cancelCommand";
        args.invokeAsCommand = false;
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
    };
    /**
    * This method accpets variable number of string arguments which is the commands passed to Native environment and it waits for the commnd operation to complete.
    * @param AutoCAD commands as string arguments
    * @throws TypeError
    *
    */
    this.executeCommand = function () {
        var count = arguments.length;
        if(count < 1) {
            throw Error('Acad.Editor.executeCommand should be called with atleast one parameter');
        }
        var temp = new Array();
        for(var i = 0; i < count; i++) {
            if(typeof (arguments[i]) !== 'string') {
                throw TypeError('Arguments to Acad.Editor.executeCommand should be of type string');
            }
            temp.push(arguments[i]);
        }
        var args = {
        };
        args.functionName = "Ac_Editor_executeCommand";
        args.invokeAsCommand = false;
        args.functionParams = temp;
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
    };
    /**
    * This method registers an AutoCAD command.
    * @param groupName is a string that specifies the command group name to add the command to.
    * @param globalName is a string that specifies the global and untranslated name of the command to add.
    * @param localName is a string that specifies the local and translated name of the command to add.
    * @param flags is an integer that specifies the flag associated with the command.
    * The flags should be either Acad.CommandFlag.TRANSPARENT or Acad.CommandFlag.MODAL,
    * and can be logically ORd with other flags in Acad.CommandFlag.
    * @param jsFunc will be executed when this command is invoked.
    * @throws TypeError
    *
    */
    this.addCommand = function (groupName, globalName, localName, flags, jsFunc) {
        if(typeof (groupName) !== 'string') {
            throw TypeError('groupName should be of type string');
        }
        if(typeof (globalName) !== 'string') {
            throw TypeError('globalName should be of type string');
        }
        if(typeof (localName) !== 'string') {
            throw TypeError('localName should be of type string');
        }
        if(!(Acad.isInteger(flags))) {
            throw TypeError('flags should be of type integer');
        }
        if(typeof (jsFunc) !== 'function') {
            throw TypeError("jsFunc should be of type function");
        }
        var args = {
        };
        args.functionName = "Ac_Editor_addCommand";
        args.invokeAsCommand = true;
        args.functionParams = {
            'groupName': groupName,
            'globalName': globalName,
            'localName': localName,
            'flags': flags
        };
        //syncronously execute the adding of the command, this registers
        //the command with Autocad. autocad will fire a synchronous event,
        //identified by globalName when the command is typed
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
        //now register a callback with the globalName so that js gets called when the command
        //is invoked
        registerCallback(globalName, jsFunc);
    };
    /**
    * This method accpets variable number of string arguments which is the commands passed to Native environment and it doesnot waits for the commnd operation to complete.It follows promise pattern
    * to receive success and callbacks from native in async fashion
    * @param AutoCAD commands as string arguments
    * @throws TypeError
    *
    */
    this.executeCommandAsync = function () {
        var count = arguments.length;
        if(count < 1) {
            throw Error('Acad.Editor.executeCommandAsync should be called with atleast one parameter');
        }
        var temp = new Array();
        for(var i = 0; i < count; i++) {
            if(typeof (arguments[i]) !== 'string') {
                throw TypeError('Arguments to Acad.Editor.executeCommandAsync should be of type string');
            }
            temp.push(arguments[i]);
        }
        var args = {
        };
        args.functionName = "Ac_Editor_executeCommandAsync";
        args.invokeAsCommand = false;
        args.functionParams = temp;
        return Acad.promptExecAsync(args);
    };
    /**
    * Drag a transient entity during jigging.
    * @param jig is of type Acad.DrawJig.
    * @throws TypeError
    * @return dragStatus of type Acad.DragStatus in success function callback
    *
    */
    this.drag = function (jig) {
        if(!(jig instanceof Acad.DrawJig)) {
            throw TypeError("jig should be of type DrawJig.");
        }
        var options = jig.jigOptions;
        var acquireMode = 0;
        if(options instanceof Acad.JigPromptPointOptions) {
            acquireMode = 1;
        } else {
            if(options instanceof Acad.JigPromptDistanceOptions) {
                acquireMode = 2;
            } else {
                if(options instanceof Acad.JigPromptAngleOptions) {
                    acquireMode = 3;
                } else {
                    if(options instanceof Acad.JigPromptStringOptions) {
                        acquireMode = 4;
                    }
                }
            }
        }
        var args = {
        };
        args.functionName = "Ac_Editor_Drag";
        args.invokeAsCommand = true;
        args.functionParams = {
            'acquireMode': acquireMode,
            'jigOptions': options
        };
        return Acad.promptExecAsync(args);
    };
}();
/**
* This function is for internal use
*
*/
Acad.promptExecAsync = function (param) {
    var promptResult = new Acad.PromptResults();
    execAsync(JSON.stringify(param), function (result) {
        if(typeof (promptResult.success) == 'function') {
            promptResult.success(result);
        }
    }, function (result) {
        if(typeof (promptResult.error) == 'function') {
            promptResult.error(result);
        }
    });
    return promptResult;
};
Acad.Editor.CurrentViewport = new function () {
    /**
    * This method sets the camera parameters needed to define the transformation from world space to
    * normalized device coordinates. All values are specified in the world space coordinate system.
    * Ensure that the camera position and target are distinct. As well, the specified upVector cannot be parallel
    * to the eye vector (computed as the vector from the target to the position). fieldWidth and fieldHeight
    * help define the transformation from view space to normalized device coordinates
    * setView is not supported in Paper Space.
    * @param position of type Acad.Point3d
    * @param target of type Acad.Point3d
    * @param upVector of type Acad.Vector3d
    * @param fieldWidth of type float
    * @param fieldHeight of type float
    * @param projection (Parallel or Perspective )
    * @param animate is boolean
    *
    */
    this.setView = function (position, target, upVector, fieldWidth, fieldHeight, projection, animate) {
        if(!Acad.isNumber(fieldWidth) || !(parseFloat(fieldWidth) > 0)) {
            throw TypeError('fieldWidth should be a double value and greater than 0');
        }
        if(!Acad.isNumber(fieldHeight) || !(parseFloat(fieldHeight) > 0)) {
            throw TypeError('fieldHeight should be a double value and greater than 0');
        }
        if(!(position && target && upVector)) {
            throw Error('position/target/upVector are mandatory.');
        }
        if(!(position instanceof Acad.Point3d)) {
            throw TypeError('position should be of type Acad.Point3d');
        }
        if(!(target instanceof Acad.Point3d)) {
            throw TypeError('target should be of type Acad.Point3d');
        }
        if(!(upVector instanceof Acad.Vector3d)) {
            throw TypeError('upVector should be of type Acad.Vector3d');
        }
        if(animate && (typeof (animate) !== 'boolean')) {
            throw TypeError('animate flag should be boolean');
        }
        if(projection && (projection !== Acad.Enum_Projection.Parallel && projection !== Acad.Enum_Projection.Perspective)) {
            throw TypeError('projection should be  Acad.Enum_Projection.Parallel or Acad.Enum_Projection.Perspective ');
        }
        var args = {
        };
        args.functionName = "Ac_Editor_CurrentViewport_setView";
        args.invokeAsCommand = true;
        args.functionParams = new function () {
            this.position = position;
            this.target = target;
            this.upVector = upVector;
            this.fieldWidth = fieldWidth;
            this.fieldHeight = fieldHeight;
            this.projection = projection || Acad.Enum_Projection.Parallel// default is Acad.Enum_Projection.Parallel
            ;
            this.animate = animate || false// default is false
            ;
        }();
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
    };
    /**
    * Translates the camera target and position by the specified camera space dolly vector. All other camera parameters
    * are left unaffected. The basis of camera space is as follows: positive Y is along the up vector,
    * positive Z is along the eye vector from the camera position to the camera target, and X is the cross product of those two vectors.
    *
    * @param Input camera space dolly vector of type Acad.Vector3d
    * @param animate is boolean
    *
    */
    this.dolly = function (dollyVector, animate) {
        if(!(dollyVector)) {
            throw Error('dollyVector is mandatory.');
        }
        if(!(dollyVector instanceof Acad.Vector3d)) {
            throw TypeError('dollyVector should be of type Acad.Vector3d');
        }
        if(animate && (typeof (animate) !== 'boolean')) {
            throw TypeError('animate flag should be boolean');
        }
        var args = {
        };
        args.functionName = "Ac_Editor_CurrentViewport_dolly";
        args.invokeAsCommand = true;
        args.functionParams = new function () {
            this.dollyVector = dollyVector;
            this.animate = animate || false// default is false
            ;
        }();
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
    };
    /**
    * Rotates the camera�s up vector about the eye vector by the specified amount in radians. Positive angles correspond to a clockwise rotation when viewed from the camera position to the camera target
    * roll is not supported in Paper Space.
    * @param rollAngle of type double
    * @param animate is boolean
    *
    */
    this.roll = function (rollAngle, animate) {
        if(!Acad.isNumber(rollAngle)) {
            throw TypeError('rollAngle should be a double value');
        }
        if(animate && (typeof (animate) !== 'boolean')) {
            throw TypeError('animate flag should be boolean');
        }
        var args = {
        };
        args.functionName = "Ac_Editor_CurrentViewport_roll";
        args.invokeAsCommand = true;
        args.functionParams = new function () {
            this.rollAngle = rollAngle;
            this.animate = animate || false// default is false
            ;
        }();
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
    };
    /**
    * Orbits the camera. During orbit, the camera target and distance from position to target remain fixed; the camera position moves along the surface of a sphere described by these constraints.
    * The angleX and angleY parameters are in radians and correspond to angles traversed on this sphere along the cross product of the up vector and the eye vector (X) and along the up vector (Y).
    * The angleX component of the orbit is performed before the angleY component
    * orbit is not supported in Paper Space.
    * @param angleX of type double
    * @param angleY of type double
    * @param animate is boolean
    *
    */
    this.orbit = function (angleX, angleY, animate) {
        if(!(Acad.isNumber(angleX) && Acad.isNumber(angleY))) {
            throw TypeError('angleX/angleY should be a double value');
        }
        if(animate && (typeof (animate) !== 'boolean')) {
            throw TypeError('animate flag should be boolean');
        }
        var args = {
        };
        args.functionName = "Ac_Editor_CurrentViewport_orbit";
        args.invokeAsCommand = true;
        args.functionParams = new function () {
            this.angleX = angleX;
            this.angleY = angleY;
            this.animate = animate || false// default is false
            ;
        }();
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
    };
    /**
    * Pans the camera. During pan, the camera position and distance from position to target remain fixed; the camera target moves along the surface of a
    * sphere described by these constraints. The angleX and angleY parameters are in radians and correspond to angles traversed on this sphere along the cross product
    * of the up vector and the eye vector (angleX) and along the up vector (angleY). The angleX component of the pan is performed before the angleY component.
    * pan is not supported in Paper Space.
    * @param angleX of type double
    * @param angleY of type double
    * @param animate is boolean
    *
    */
    this.pan = function (angleX, angleY, animate) {
        if(!(Acad.isNumber(angleX) && Acad.isNumber(angleY))) {
            throw TypeError('angleX/angleY should be a double value');
        }
        if(animate && (typeof (animate) !== 'boolean')) {
            throw TypeError('animate flag should be boolean');
        }
        var args = {
        };
        args.functionName = "Ac_Editor_CurrentViewport_pan";
        args.invokeAsCommand = true;
        args.functionParams = new function () {
            this.angleX = angleX;
            this.angleY = angleY;
            this.animate = animate || false// default is false
            ;
        }();
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
    };
    /**
    * Modifies the current view such that the input bounding box defined by the two extents points is completely within the view.
    * @param minPoint should represent the corner of the box that is defined by the three smallest component values of type Acad.Point3d.
    * @param maxPoint should represent the corner of the box that is defined by the three largest component values of type Acad.Point3d.
    * @param animate is boolean
    */
    this.zoomExtents = function (minPoint, maxPoint, animate) {
        if(!(minPoint && maxPoint)) {
            throw Error('minPoint/maxPoint are mandatory.');
        }
        if(!(minPoint instanceof Acad.Point3d)) {
            throw TypeError('minPoint should be of type Acad.Point3d');
        }
        if(!(maxPoint instanceof Acad.Point3d)) {
            throw TypeError('maxPoint should be of type Acad.Point3d');
        }
        if(!(maxPoint.x >= minPoint.x && maxPoint.y >= minPoint.y && maxPoint.z >= minPoint.z)) {
            throw TypeError('maxPoint should be greater than or equal to minPoint');
        }
        if(animate && (typeof (animate) !== 'boolean')) {
            throw TypeError('animate flag should be boolean');
        }
        var args = {
        };
        args.functionName = "Ac_Editor_CurrentViewport_zoomExtents";
        args.invokeAsCommand = true;
        args.functionParams = new function () {
            this.minPoint = minPoint;
            this.maxPoint = maxPoint;
            this.animate = animate || false// default is false
            ;
        }();
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
    };
    /**
    * Changes the viewing field (the focal length) of the camera to give the effect of dynamically moving in or out of a scene.
    * The camera position and target are not changed. The specified factor must be positive
    * @param zoomFactor is of type double
    * @param animate is boolean
    */
    this.zoom = function (zoomFactor, animate) {
        if(!Acad.isNumber(zoomFactor) || !(parseFloat(zoomFactor) > 0)) {
            throw TypeError('zoomFactor should be a double value and greater than 0');
        }
        if(animate && (typeof (animate) !== 'boolean')) {
            throw TypeError('animate flag should be boolean');
        }
        var args = {
        };
        args.functionName = "Ac_Editor_CurrentViewport_zoom";
        args.invokeAsCommand = true;
        args.functionParams = new function () {
            this.zoomFactor = zoomFactor;
            this.animate = animate || false// default is false
            ;
        }();
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
    };
    /**
    * Modifies the current view such that the new window displays the region defined by the input screen coordinates.
    * The aspect ratio is automatically maintained.
    * @param lowerLeft Input screen coordinate of the lower-left point of the new zoom window of type Acad.Point2d
    * @param upperRight Input screen coordinate of the upper-right point of the new zoom window of type Acad.Point2d
    * @param animate is boolean
    */
    this.zoomWindow = function (lowerLeft, upperRight, animate) {
        if(!(lowerLeft && upperRight)) {
            throw Error('lowerLeft/upperRight are mandatory.');
        }
        if(!(lowerLeft instanceof Acad.Point2d)) {
            throw TypeError('lowerLeft should be of type Acad.Point2d');
        }
        if(!(upperRight instanceof Acad.Point2d)) {
            throw TypeError('upperRight should be of type Acad.Point2d');
        }
        if(!(Acad.isInteger(lowerLeft.x) && Acad.isInteger(lowerLeft.y) && Acad.isInteger(upperRight.x) && Acad.isInteger(upperRight.y))) {
            throw TypeError('lowerLeft/upperRight screen coordinates should be integer');
        }
        if(animate && (typeof (animate) !== 'boolean')) {
            throw TypeError('animate flag should be boolean');
        }
        var args = {
        };
        args.functionName = "Ac_Editor_CurrentViewport_zoomWindow";
        args.invokeAsCommand = true;
        args.functionParams = new function () {
            this.lowerLeft = lowerLeft;
            this.upperRight = upperRight;
            this.animate = animate || false// default is false
            ;
        }();
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
    };
    /*
    * Returns the 2D point pt on the screen
    * @param Input point to grab of type Acad.Point3d
    * @return 2D point pt on the screen of type Acad.Point2d
    */
    this.pointToScreen = function (inputPoint) {
        if(!(inputPoint)) {
            throw Error('inputPoint is mandatory.');
        }
        if(!(inputPoint instanceof Acad.Point3d)) {
            throw TypeError('inputPoint should be of type Acad.Point3d');
        }
        var args = {
        };
        args.functionName = "Ac_Editor_CurrentViewport_pointToScreen";
        args.functionParams = new function () {
            this.inputPoint = inputPoint;
        }();
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
        return new Acad.Point2d(jsonObj.screenPoint.x, jsonObj.screenPoint.y);
    };
    /*
    * Returns the 3D point pt on the World Coordinate System
    * @param Input point is the screen point of type Acad.Point2d
    * @return 3D point on the World Coordinate System of type Acad.Point3d
    */
    this.pointToWorld = function (inputPoint) {
        if(!(inputPoint)) {
            throw Error('inputPoint is mandatory.');
        }
        if(!(inputPoint instanceof Acad.Point2d)) {
            throw TypeError('inputPoint should be of type Acad.Point2d');
        }
        var args = {
        };
        args.functionName = "Ac_Editor_CurrentViewport_pointToWorld";
        args.functionParams = new function () {
            this.inputPoint = inputPoint;
        }();
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
        return new Acad.Point3d(jsonObj.worldPoint.x, jsonObj.worldPoint.y, jsonObj.worldPoint.z);
    };
    /*
    * Converts a UCS point to UCS
    * @param Input point is the UCS point of type Acad.Point3d
    * @return a WCS point of type Acad.Point3d
    */
    this.ucsToWorld = function (inputPoint) {
        if(!(inputPoint)) {
            throw Error('inputPoint is mandatory.');
        }
        if(!(inputPoint instanceof Acad.Point3d)) {
            throw TypeError('inputPoint should be of type Acad.Point3d');
        }
        var args = {
        };
        args.functionName = "Ac_Editor_CurrentViewport_ucsToWorld";
        args.functionParams = new function () {
            this.inputPoint = inputPoint;
        }();
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
        return new Acad.Point3d(jsonObj.worldPoint.x, jsonObj.worldPoint.y, jsonObj.worldPoint.z);
    };
    /*
    * Converts a WCS point to UCS
    * @param Input point is the WCS point of type Acad.Point3d
    * @return a UCS point of type Acad.Point3d
    */
    this.worldToUCS = function (inputPoint) {
        if(!(inputPoint)) {
            throw Error('inputPoint is mandatory.');
        }
        if(!(inputPoint instanceof Acad.Point3d)) {
            throw TypeError('inputPoint should be of type Acad.Point3d');
        }
        var args = {
        };
        args.functionName = "Ac_Editor_CurrentViewport_worldToUCS";
        args.functionParams = new function () {
            this.inputPoint = inputPoint;
        }();
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
        return new Acad.Point3d(jsonObj.ucsPoint.x, jsonObj.ucsPoint.y, jsonObj.ucsPoint.z);
    };
    /*
    * This method retrieves the extents of the viewport in normalized device coordinates.
    * @return Acad.Rectangle2d object which has lowerLeft and upperRight as Acad.Point2d objects
    */
    this.getViewport = function () {
        var args = {
        };
        args.functionName = "Ac_Editor_CurrentViewport_getViewport";
        var jsonResponse = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonResponse);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
        return new Acad.Rectangle2d(new Acad.Point2d(jsonObj.lowerLeft.x, jsonObj.lowerLeft.y), new Acad.Point2d(jsonObj.upperRight.x, jsonObj.upperRight.y));
    };
    /**
    * The Methods which returns the position, target , upVector, fieldWidth and fieldHeight of current viewport.
    * @return fieldHeight of type float
    */
    this.getViewProperties = function () {
        var args = {
        };
        args.functionName = "Ac_Editor_CurrentViewport_getViewProperties";
        var jsonStr = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonStr);
        if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
            throw Error(jsonObj.retErrorString);
        }
        var position = new Acad.Point3d(jsonObj.position.x, jsonObj.position.y, jsonObj.position.z);
        var target = new Acad.Point3d(jsonObj.target.x, jsonObj.target.y, jsonObj.target.z);
        var upVector = new Acad.Vector3d(jsonObj.upVector.x, jsonObj.upVector.y, jsonObj.upVector.z);
        var fieldWidth = parseFloat(jsonObj.fieldWidth);
        var fieldHeight = parseFloat(jsonObj.fieldHeight);
        var projection = parseInt(jsonObj.projection);
        return new Acad.ViewProperties(position, target, upVector, fieldWidth, fieldHeight, projection);
    };
    /**
    * Returns the camera position. Make sure not to use Position when the view is in the interactive state.
    * @return position of type Acad.Point3d
    */
    Object.defineProperty(this, "position", {
        get: function () {
            var args = {
            };
            args.functionName = "Ac_Editor_CurrentViewport_position";
            var jsonStr = exec(JSON.stringify(args));
            var jsonObj = JSON.parse(jsonStr);
            if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
                throw Error(jsonObj.retErrorString);
            }
            return new Acad.Point3d(jsonObj.position.x, jsonObj.position.y, jsonObj.position.z);
        },
        set: function (val) {
            throw Error(" You are not allowed to set this property");
        }
    });
    /**
    * Returns the camera target. Make sure not to use Target when the view is in the interactive state.
    * @return target of type Acad.Point3d
    */
    Object.defineProperty(this, "target", {
        get: function () {
            var args = {
            };
            args.functionName = "Ac_Editor_CurrentViewport_target";
            var jsonStr = exec(JSON.stringify(args));
            var jsonObj = JSON.parse(jsonStr);
            if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
                throw Error(jsonObj.retErrorString);
            }
            return new Acad.Point3d(jsonObj.target.x, jsonObj.target.y, jsonObj.target.z);
        },
        set: function (val) {
            throw Error(" You are not allowed to set this property");
        }
    });
    /**
    * Returns the camera up vector. Make sure not to use UpVector when the view is in the interactive state.
    * @return upVector of type Acad.Vector3d
    */
    Object.defineProperty(this, "upVector", {
        get: function () {
            var args = {
            };
            args.functionName = "Ac_Editor_CurrentViewport_upVector";
            var jsonStr = exec(JSON.stringify(args));
            var jsonObj = JSON.parse(jsonStr);
            if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
                throw Error(jsonObj.retErrorString);
            }
            return new Acad.Vector3d(jsonObj.upVector.x, jsonObj.upVector.y, jsonObj.upVector.z);
        },
        set: function (val) {
            throw Error(" You are not allowed to set this property");
        }
    });
    /**
    * Returns the camera field width. Make sure that FieldWidth is not used when the view is in the interactive state.
    * @return fieldWidth of type float
    */
    Object.defineProperty(this, "fieldWidth", {
        get: function () {
            var args = {
            };
            args.functionName = "Ac_Editor_CurrentViewport_fieldWidth";
            var jsonStr = exec(JSON.stringify(args));
            var jsonObj = JSON.parse(jsonStr);
            if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
                throw Error(jsonObj.retErrorString);
            }
            return parseFloat(jsonObj.fieldWidth);
        },
        set: function (val) {
            throw Error(" You are not allowed to set this property");
        }
    });
    /**
    * Returns the camera field Height. Make sure that FieldHeight is not used when the view is in the interactive state.
    * @return fieldHeight of type float
    */
    Object.defineProperty(this, "fieldHeight", {
        get: function () {
            var args = {
            };
            args.functionName = "Ac_Editor_CurrentViewport_fieldHeight";
            var jsonStr = exec(JSON.stringify(args));
            var jsonObj = JSON.parse(jsonStr);
            if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
                throw Error(jsonObj.retErrorString);
            }
            return parseFloat(jsonObj.fieldHeight);
        },
        set: function (val) {
            throw Error(" You are not allowed to set this property");
        }
    });
    /**
    * Returns the projection. Make sure that projection is not used when the view is in the interactive state.
    * @return projection of type Acad.Enum_Projection
    */
    Object.defineProperty(this, "projection", {
        get: function () {
            var args = {
            };
            args.functionName = "Ac_Editor_CurrentViewport_projection";
            var jsonStr = exec(JSON.stringify(args));
            var jsonObj = JSON.parse(jsonStr);
            if(jsonObj.retCode !== Acad.ErrorStatus.eJsOk) {
                throw Error(jsonObj.retErrorString);
            }
            return parseInt(jsonObj.projection);
        },
        set: function (val) {
            throw Error(" You are not allowed to set this property");
        }
    });
}();
//
///////////////////////////////////////////////////////////////////////////////
//
//                 (C) Copyright 2012 by Autodesk, Inc.
//
// The information contained herein is confidential, proprietary to Autodesk,
// Inc., and considered a trade secret as defined in section 499C of the
// penal code of the State of California.  Use of this information by anyone
// other than authorized employees of Autodesk, Inc. is granted only under a
// written non-disclosure agreement, expressly prescribing the scope and
// manner of such use.
//
///////////////////////////////////////////////////////////////////////////////
/**
* This class wraps AcGePoint2d ObjectARX class. It represents a point in 2-dimensional space. It can be viewed as a structure consisting of two doubles.
* @param coordinates x, y.
* @throws TypeError
*
*/
Acad.Point2d = function (x, y) {
    /**
    * Returns the X coordinate axis.
    * @Type Number
    */
    if(typeof x == 'number') {
        this.x = x;
    } else {
        throw TypeError("x is not number");
    }
    /**
    * Returns the Y coordinate axis.
    * @Type Number
    */
    if(typeof y == 'number') {
        this.y = y;
    } else {
        throw TypeError("y is not number");
    }
};
/**
* This class wraps AcGePoint3d ObjectARX class. It represents a point in 3D space. It can be viewed as a structure consisting of three doubles.
* @param coordinates x, y, and z.
* @throws TypeError
*
*/
Acad.Point3d = function (x, y, z) {
    /**
    * Returns the X coordinate axis.
    * @Type Number
    */
    if(typeof x == 'number') {
        this.x = x;
    } else {
        throw TypeError("x is not number");
    }
    /**
    * Returns the Y coordinate axis.
    * @Type Number
    */
    if(typeof y == 'number') {
        this.y = y;
    } else {
        throw TypeError("y is not number");
    }
    /**
    * Returns the Z coordinate axis.
    * @Type Number
    */
    if(typeof z == 'number') {
        this.z = z;
    } else {
        throw TypeError("z is not number");
    }
};
/**
* This class wraps the AcGeVector2d ObjectARX class.
* Vector2d represents a vector in 2D space. It can be viewed as a structure consisting of two doubles.
* @param coordinates x, y.
* @throws TypeError
*
*/
Acad.Vector2d = function (x, y) {
    /**
    * Returns the X property value.
    * @Type Number
    */
    if(typeof x == 'number') {
        this.x = x;
    } else {
        throw TypeError("x is not number");
    }
    /**
    * Returns the Y property value.
    * @Type Number
    */
    if(typeof y == 'number') {
        this.y = y;
    } else {
        throw TypeError("y is not number");
    }
};
/**
* This class wraps the AcGeVector3d ObjectARX class.
* Vector3d represents a vector in 3D space. It can be viewed as a structure consisting of 3 doubles.
* @param coordinates x, y, and z correspondingly.
* @throws TypeError
*
*/
Acad.Vector3d = function (x, y, z) {
    /**
    * Returns the X property value.
    * @Type Number
    */
    if(typeof x == 'number') {
        this.x = x;
    } else {
        throw TypeError("x is not number");
    }
    /**
    * Returns the Y property value.
    * @Type Number
    */
    if(typeof y == 'number') {
        this.y = y;
    } else {
        throw TypeError("y is not number");
    }
    /**
    * Returns the Z property value.
    * @Type Number
    */
    if(typeof z == 'number') {
        this.z = z;
    } else {
        throw TypeError("z is not number");
    }
};
/**
* This class wraps the lowerLeft and upperRight Point2d objects.
* @param lowerLeft point of type Acad.Point2d
* @param upperRight point of type Acad.Point2d
* @throws TypeError
*
*/
Acad.Rectangle2d = function (lowerLeft, upperRight) {
    /**
    * lowerLeft point of Rectangle
    * @Type Acad.Point2d
    */
    if(lowerLeft instanceof Acad.Point2d) {
        this.lowerLeft = lowerLeft;
    } else {
        throw TypeError("lowerLeft should be of Acad.Point2d type.");
    }
    /**
    * upperRight point of Rectangle
    * @Type Acad.Point2d
    */
    if(upperRight instanceof Acad.Point2d) {
        this.upperRight = upperRight;
    } else {
        throw TypeError("upperRight should be of Acad.Point2d type.");
    }
};
/**
* @class Acad.Bounds3d,
* The object represents the 3d geometric extents of an entity
* Its similar to AcDbExtents, with minimum and maximum points
* @param minPt3d is the minimum point of the extents
* @param maxPt3d is the maximum point of the extents
* @throws TypeError
*
*/
Acad.Bounds3d = function (minPt3d, maxPt3d) {
    /**
    * minPoint3d is the minimum point of the extents.
    * @Type Acad.Point3d
    */
    if(minPt3d instanceof Acad.Point3d) {
        this.minPoint3d = minPt3d;
    } else {
        throw TypeError("minPt3d should be of Acad.Point3d type.");
    }
    /**
    * maxPoint3d is the maximum point of the extents.
    * @Type Acad.Point3d
    */
    if(maxPt3d instanceof Acad.Point3d) {
        this.maxPoint3d = maxPt3d;
    } else {
        throw TypeError("maxPt3d should be of Acad.Point3d type.");
    }
};
/**
* This class wraps the AcGeMatrix3d ObjectARX class.
* Class Matrix3d represents an affine transformation of 3D space, including translation.
*
*/
Acad.Matrix3d = function () {
    var matrix = new Array(4);
    for(var i = 0; i < matrix.length; i++) {
        matrix[i] = new Array(4);
    }
    return matrix;
};
//
///////////////////////////////////////////////////////////////////////////////
//
//                 (C) Copyright 2012 by Autodesk, Inc.
//
// The information contained herein is confidential, proprietary to Autodesk,
// Inc., and considered a trade secret as defined in section 499C of the
// penal code of the State of California.  Use of this information by anyone
// other than authorized employees of Autodesk, Inc. is granted only under a
// written non-disclosure agreement, expressly prescribing the scope and
// manner of such use.
//
///////////////////////////////////////////////////////////////////////////////
/**
* This is the base class for types that represent optional parameters for prompts.
* @param messageAndKeywords is the prompt message along with Keywords
*
*/
Acad.PromptOptions = function (messageAndKeywords) {
    this.messageAndKeywords = messageAndKeywords;
    this.globalKeywords = undefined;
    /**
    * Gets or sets the the AppendKeywordsToMessage property value.
    * @Type Boolean
    */
    this.appendKeywordsToMessage = true;
};
Acad.PromptOptions.prototype = {
    setMessageAndKeywords: /**
    * This method sets the prompt message to the first part of the messageAndKeywords string and sets the display keywords to the latter part of the same string.
    * The display keywords portion of messageAndKeywords must be surrounded by an opening square bracket ("[") at the beginning and a closing square bracket
    * ("]") at the end. The keywords in this list must be delimited by a forward slash character ("/").
    * Each display keyword specified in messageAndKeywords must also be matched by a keyword in the same position in the globalKeywords string.
    * Keywords in globalKeywords must be delimited by a single space.
    * @param messageAndKeywords is the prompt message along with Keywords
    * @param globalKeywords
    * @throws Error
    *
    */
    function (messageAndKeywords, globalKeywords) {
        if(!messageAndKeywords) {
            throw new Error('messageAndKeywords must be non-empty string');
        }
        if(globalKeywords) {
            var startKeywords = messageAndKeywords.lastIndexOf("[");
            var endKeywords = messageAndKeywords.lastIndexOf("]");
            if(startKeywords >= 0 && endKeywords > startKeywords + 1) {
                var displayKeywordsText = messageAndKeywords.substr(startKeywords + 1, (endKeywords - startKeywords - 1)).trim();
                if(displayKeywordsText) {
                    if(displayKeywordsText.split('/').length != globalKeywords.split(' ').length) {
                        throw new Error('Number of global and local keywords is not equal.');
                    }
                } else {
                    throw new Error('Keyword list is empty.');
                }
            } else {
                throw new Error('Keyword list is empty.');
            }
        } else {
            var start = messageAndKeywords.lastIndexOf('[');
            var end = messageAndKeywords.lastIndexOf(']');
            if(start >= 0 && end > start + 1) {
                throw new Error('Global keywords are missing');
            }
        }
        this.messageAndKeywords = messageAndKeywords;
        this.globalKeywords = globalKeywords;
    }
};
/**
* This is the base class for command prompt options used in various types of data acquisition.
* @param messageAndKeywords is the prompt message along with Keywords.
*
*/
Acad.PromptEditorOptions = function (messageAndKeywords) {
    Acad.PromptOptions.call(this, messageAndKeywords);
    var allowNone = true;
    var allowArbitraryInput = false;
    var allowNegative = true;
    var allowZero = true;
    var useDashedLine = false;
    var limitsChecked = true;
    var only2d = false;
    Object.defineProperty(this, "allowNone", {
        get: function () {
            return allowNone;
        },
        set: function (x) {
            allowNone = x;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(this, "allowArbitraryInput", {
        get: function () {
            return allowArbitraryInput;
        },
        set: function (x) {
            allowArbitraryInput = x;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(this, "allowNegative", {
        get: function () {
            return allowNegative;
        },
        set: function (x) {
            allowNegative = x;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(this, "allowZero", {
        get: function () {
            return allowZero;
        },
        set: function (x) {
            allowZero = x;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(this, "useDashedLine", {
        get: function () {
            return useDashedLine;
        },
        set: function (x) {
            useDashedLine = x;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(this, "limitsChecked", {
        get: function () {
            return limitsChecked;
        },
        set: function (x) {
            limitsChecked = x;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(this, "only2d", {
        get: function () {
            return only2d;
        },
        set: function (x) {
            only2d = x;
        },
        enumerable: false,
        configurable: true
    });
};
Acad.extend(Acad.PromptEditorOptions, Acad.PromptOptions);
/**
* This is the base class for types that represent optional parameters for numerical prompts.
* @param messageAndKeywords is the prompt message along with Keywords.
*
*/
Acad.PromptNumericalOptions = function (messageAndKeywords) {
    Acad.PromptEditorOptions.call(this, messageAndKeywords);
    var useDefaultValue = false;
    /**
    * Gets or sets whether the prompt should use the default value when the user presses ENTER without any other input.
    * The property allowing client code to set the default value is declared by derived classes.
    * @Type Boolean
    *
    */
    Object.defineProperty(this, "useDefaultValue", {
        get: function () {
            return useDefaultValue;
        },
        set: function (x) {
            useDefaultValue = x;
        },
        enumerable: true,
        configurable: true
    });
    /**
    * Gets or sets whether the prompt accepts ENTER as sole input.
    * True if ENTER on its own is allowed, false otherwise.
    * @Type Boolean
    */
    Object.defineProperty(this, "allowNone", {
        enumerable: true
    });
    /**
    * Gets or sets whether the prompts accepts arbitrary input.
    * @Type Boolean
    */
    Object.defineProperty(this, "allowArbitraryInput", {
        enumerable: true
    });
    /**
    * Gets or sets whether the prompt accepts negative valued input.
    * True if negative valued input is accepted, false otherwise.
    * @Type Boolean
    */
    Object.defineProperty(this, "allowNegative", {
        enumerable: true
    });
    /**
    * Gets or sets whether the prompt accepts zero valued input.
    * True if zero valued input is accepted, false otherwise.
    * @Type Boolean
    */
    Object.defineProperty(this, "allowZero", {
        enumerable: true
    });
};
Acad.extend(Acad.PromptNumericalOptions, Acad.PromptEditorOptions);
/**
* This class represents optional parameters for a prompt for an integer.
* @param messageAndKeywords is the prompt message along with Keywords.
* @param lowerLimit is lower limit of input.
* @param upperLimit is upper limit of input.
* @throws TypeError
*
*/
Acad.PromptIntegerOptions = function (messageAndKeywords, lowerLimit, upperLimit) {
    Acad.PromptNumericalOptions.call(this, messageAndKeywords);
    /**
    * Returns the lower limit integer value..
    * @Type Number
    */
    this.lowerLimit = lowerLimit || Acad.Int32MinValue;
    /**
    * Returns the upper limit integer value.
    * @Type Number
    */
    this.upperLimit = upperLimit || Acad.Int32MaxValue;
    var defaultValue;
    /**
    * The default value to be used when the user presses ENTER without any other input.
    * @Type Integer
    */
    Object.defineProperty(this, "defaultValue", {
        get: function () {
            return defaultValue;
        },
        set: function (x) {
            if(Acad.isInteger(x)) {
                defaultValue = x;
            } else {
                throw new TypeError('Default value should be of Integer Type');
            }
        },
        enumerable: true,
        configurable: true
    });
};
Acad.extend(Acad.PromptIntegerOptions, Acad.PromptNumericalOptions);
/**
* This class represents optional parameters for a prompt for a double.
* @param messageAndKeywords is the prompt message along with Keywords
* @throws TypeError
*
*/
Acad.PromptDoubleOptions = function (messageAndKeywords) {
    Acad.PromptNumericalOptions.call(this, messageAndKeywords);
    var defaultValue;
    /**
    * The default value to be used when the user presses ENTER without any other input.
    * @Type Number
    */
    Object.defineProperty(this, "defaultValue", {
        get: function () {
            return defaultValue;
        },
        set: function (x) {
            if(Acad.isNumber(x)) {
                defaultValue = x;
            } else {
                throw new TypeError('Default value should be Number.');
            }
        },
        enumerable: true,
        configurable: true
    });
};
Acad.extend(Acad.PromptDoubleOptions, Acad.PromptNumericalOptions);
/**
* This class represents optional parameters for prompt for distance.
* @param messageAndKeywords is the prompt message along with Keywords.
* @throws TypeError
*
*/
Acad.PromptDistanceOptions = function (messageAndKeywords) {
    Acad.PromptNumericalOptions.call(this, messageAndKeywords);
    /**
    * Gets or sets whether the base point is to be used.
    * @Type Boolean
    */
    this.useBasePoint = false;
    var basePoint;
    /**
    * Gets or sets the base point to be used by the prompt.
    * @Type Point3d
    */
    Object.defineProperty(this, "basePoint", {
        get: function () {
            return basePoint;
        },
        set: function (x) {
            if(x instanceof Acad.Point3d) {
                basePoint = x;
            } else {
                throw new TypeError('Point should be of Point3d type.');
            }
        },
        enumerable: true,
        configurable: true
    });
    var defaultValue;
    /**
    * The default value to be used when the user presses ENTER without any other input.
    * @Type Number
    */
    Object.defineProperty(this, "defaultValue", {
        get: function () {
            return defaultValue;
        },
        set: function (x) {
            if(Acad.isNumber(x)) {
                defaultValue = x;
            } else {
                throw new TypeError('Default value should be Number.');
            }
        },
        enumerable: true,
        configurable: true
    });
    /**
    * Gets or sets whether a dashed "rubber band" line is to be drawn between the base point and
    * the cursor's current location while prompting.
    * @Type Boolean
    */
    Object.defineProperty(this, "useDashedLine", {
        enumerable: true
    });
    /**
    * Gets or sets whether the distance returned should be measured as a 2D projection to the UCS.
    * @Type Boolean
    */
    Object.defineProperty(this, "only2d", {
        enumerable: true
    });
};
Acad.extend(Acad.PromptDistanceOptions, Acad.PromptNumericalOptions);
/**
* This class represents optional parameters for a corner prompt.
* @param messageAndKeywords is the prompt message along with Keywords.
* @param basePoint is input base point
* @throws TypeError
*
*/
Acad.PromptCornerOptions = function (messageAndKeywords, basePoint) {
    Acad.PromptEditorOptions.call(this, messageAndKeywords);
    /**
    * Gets or sets the base point to be used by the prompt.
    * @Type Point3d
    */
    if(basePoint != undefined) {
        if(basePoint instanceof Acad.Point3d) {
            this.basePoint = basePoint;
        } else {
            throw new TypeError('Point should be of Point3d type.');
        }
    } else {
        this.basePoint = undefined;
    }
    /**
    * Gets or sets whether the prompt accepts ENTER as sole input.
    * @Type Boolean
    */
    Object.defineProperty(this, "allowNone", {
        enumerable: true
    });
    /**
    * Gets or sets whether the prompts accepts arbitrary input.
    * @Type Boolean
    */
    Object.defineProperty(this, "allowArbitraryInput", {
        enumerable: true
    });
    /**
    * Gets or sets whether a dashed "rubber band" line is to be drawn between the base point and
    * the cursor's current location while prompting.
    * @Type Boolean
    */
    Object.defineProperty(this, "useDashedLine", {
        enumerable: true
    });
    /**
    * Gets or sets whether limits checks are carried out on the input value.
    * @Type Boolean
    */
    Object.defineProperty(this, "limitsChecked", {
        enumerable: true
    });
};
Acad.extend(Acad.PromptCornerOptions, Acad.PromptEditorOptions);
/**
* This class represents optional parameters for a prompt for point.
* @param messageAndKeywords is the prompt message along with Keywords.
*
*/
Acad.PromptPointOptions = function (messageAndKeywords) {
    Acad.PromptCornerOptions.call(this, messageAndKeywords, new Acad.Point3d(0, 0, 0));
    /**
    * Gets or sets whether the base point is to be used.
    * True if the BasePoint value is to be used, false otherwise.
    * @Type Boolean
    */
    this.useBasePoint = false;
};
Acad.extend(Acad.PromptPointOptions, Acad.PromptCornerOptions);
/**
* This class represents optional parameters for a prompt for string.
* @param messageAndKeywords is the prompt message along with Keywords.
* @throws TypeError
*
*/
Acad.PromptStringOptions = function (messageAndKeywords) {
    Acad.PromptEditorOptions.call(this, messageAndKeywords);
    /**
    * Gets or sets whether the prompt should allow spaces.
    * @Type Boolean
    */
    this.allowSpaces = false;
    /**
    * Gets or sets whether the prompt should use the default value when
    * the user presses ENTER without any other input. The property allowing
    * client code to set the default value is declared by derived classes.
    * @Type Boolean
    *
    */
    this.useDefaultValue = false;
    var defaultValue;
    /**
    * The default value to be used when the user presses ENTER without any other input.
    * @Type String
    */
    Object.defineProperty(this, "defaultValue", {
        get: function () {
            return defaultValue;
        },
        set: function (x) {
            if(typeof (x) == 'string') {
                defaultValue = x;
            } else {
                throw new TypeError('Default value should be String.');
            }
        },
        enumerable: true,
        configurable: true
    });
};
Acad.extend(Acad.PromptStringOptions, Acad.PromptEditorOptions);
/**
* This class represents optional parameters for a prompt for an angle.
* @param messageAndKeywords is the prompt message along with Keywords
* @throws TypeError
*
*/
Acad.PromptAngleOptions = function (messageAndKeywords) {
    Acad.PromptEditorOptions.call(this, messageAndKeywords);
    /**
    * Returns a Boolean indicating whether the base point is to be used or not.
    * @Type Boolean
    */
    this.useBasePoint = false;
    /**
    * Gets or sets whether the base angle value is used.
    * @Type Boolean
    */
    this.useAngleBase = false;
    /**
    * Gets or sets whether the prompt should use the default value when the user presses ENTER without any other input.
    * The property allowing client code to set the default value is declared by derived classes.
    * @Type Boolean
    */
    this.useDefaultValue = false;
    var basePoint;
    /**
    * Gets or sets the base point to be used by the prompt.
    * @Type Point3d
    */
    Object.defineProperty(this, "basePoint", {
        get: function () {
            return basePoint;
        },
        set: function (point) {
            if(point instanceof Acad.Point3d) {
                basePoint = point;
            } else {
                throw new TypeError('Point should be of Point3d type.');
            }
        },
        enumerable: true,
        configurable: true
    });
    var defaultValue;
    /**
    * The default value to be used when the user presses ENTER without any other input.
    * @Type Number
    */
    Object.defineProperty(this, "defaultValue", {
        get: function () {
            return defaultValue;
        },
        set: function (x) {
            if(Acad.isNumber(x)) {
                defaultValue = x;
            } else {
                throw new TypeError('Default value should be Number.');
            }
        },
        enumerable: true,
        configurable: true
    });
    /**
    * Gets or sets whether the prompt accepts ENTER as sole input.
    * True if ENTER on its own is allowed, false otherwise.
    * @Type Boolean
    */
    Object.defineProperty(this, "allowNone", {
        enumerable: true
    });
    /**
    * Gets or sets whether the prompts accepts arbitrary input.
    * True if arbitrary input is accepted, false otherwise.
    * @Type Boolean
    */
    Object.defineProperty(this, "allowArbitraryInput", {
        enumerable: true
    });
    /**
    * Gets or sets whether the prompt accepts zero valued input.
    * True if zero valued input is accepted, false otherwise.
    * @Type Boolean
    */
    Object.defineProperty(this, "allowZero", {
        enumerable: true
    });
    /**
    * Gets or sets whether a dashed "rubber band" line is to be drawn between the base point and
    * the cursor's current location while prompting.
    * @Type Boolean
    */
    Object.defineProperty(this, "useDashedLine", {
        enumerable: true
    });
};
Acad.extend(Acad.PromptAngleOptions, Acad.PromptEditorOptions);
/**
* This class represents optional parameters for a prompt for a keyword.
* @param messageAndKeywords is the prompt message along with Keywords
*
*/
Acad.PromptKeywordOptions = function (messageAndKeywords) {
    Acad.PromptEditorOptions.call(this, messageAndKeywords);
    /**
    * Gets or sets whether the prompts accepts arbitrary input.
    * Returns true if arbitrary inputs are accepted.
    * @Type Boolean
    */
    Object.defineProperty(this, "allowNone", {
        enumerable: true
    });
    /**
    * Gets or sets whether the prompt accepts ENTER as sole input.
    * True if ENTER on its own is allowed, false otherwise.
    * @Type Boolean
    */
    Object.defineProperty(this, "allowArbitraryInput", {
        enumerable: true
    });
};
Acad.extend(Acad.PromptKeywordOptions, Acad.PromptEditorOptions);
/**
* This class represents optional parameters for a prompt for an entity.
* @param messageAndKeywords is the prompt message along with Keywords.
*
*/
Acad.PromptEntityOptions = function (messageAndKeywords) {
    Acad.PromptEditorOptions.call(this, messageAndKeywords);
    var rejectMessage = undefined;
    /**
    * Gets or sets message as the prompt that is posted if the type of a
    * picked entity is not allowed for this selection.
    * @Type String
    */
    Object.defineProperty(this, "rejectMessage", {
        get: function () {
            return rejectMessage;
        },
        set: function (x) {
            if(typeof (x) == 'string') {
                rejectMessage = x;
            } else {
                throw Error('Please provide reject message of string type.');
            }
        },
        enumerable: true,
        configurable: true
    });
    var allowedClasses = undefined;
    /**
    * Gets internal list of classes allowed for the selection.
    * @Type Array
    * @Read-Only
    */
    Object.defineProperty(this, "allowedClasses", {
        get: function () {
            return allowedClasses;
        },
        set: function (x) {
            throw Error('Please use addAllowedClass() function to modify it.');
        },
        enumerable: true,
        configurable: true
    });
    /**
    * Gets or sets whether the prompt allows selection of entities on locked layer.
    * @Type Boolean
    *
    */
    this.allowObjectOnLockedLayer = false;
    /**
    * Gets or sets whether the prompt accepts ENTER as sole input.
    * @Type Boolean
    *
    */
    Object.defineProperty(this, "allowNone", {
        enumerable: true
    });
    /**
    * This method adds type to the internal list of classes allowed for the selection. If exactMatch is true, then only objects of the exact class type are allowed.
    * Otherwise, objects of the specified type and of any derived types are allowed. If type is already in the class list, the value of exactMatch is applied to the existing class entry.
    * @param className name of allowed class
    * @param exactMatch boolean for exact type
    * @throws Error
    *
    */
    this.addAllowedClass = function (className, exactMatch) {
        if(rejectMessage == undefined) {
            throw Error('Use SetRejectMessage first.');
        }
        if(typeof (exactMatch) != 'boolean') {
            throw Error('Type of exactMatch should be boolean.');
        }
        if(allowedClasses == undefined) {
            allowedClasses = [];
        }
        // First check that already exist
        for(var index in allowedClasses) {
            var obj = allowedClasses[index];
            if(obj.hasOwnProperty('className') && obj['className'] == className) {
                obj['exactMatch'] = exactMatch;
                return;
            }
        }
        // Add the allowed classes
        var allowed = {
        };
        allowed['className'] = className;
        allowed['exactMatch'] = exactMatch;
        allowedClasses.push(allowed);
    };
    /**
    * This method removes the class indicated by type from the internal list of classes allowed for this selection.
    * @param className name of class
    *
    */
    this.removeAllowedClass = function (className) {
        if(className) {
            for(var index in allowedClasses) {
                var obj = allowedClasses[index];
                if(obj.hasOwnProperty('className') && obj['className'] == className) {
                    allowedClasses.splice(index, 1);
                    return;
                }
            }
        }
    };
};
Acad.extend(Acad.PromptEntityOptions, Acad.PromptEditorOptions);
/**
* This class represents optional parameters for a prompt for a nested entity.
* @param messageAndKeywords is the prompt message along with Keywords
* @param nonInteractivePickPoint is the Point3d
* @param useNonInteractivePickPoint is boolean
* @throws TypeError
*
*/
Acad.PromptNestedEntityOptions = function (messageAndKeywords) {
    Acad.PromptEditorOptions.call(this, messageAndKeywords);
    /**
    * Gets or sets whether the prompt should attempt a non-interactive pick.
    * @Type Boolean
    */
    this.useNonInteractivePickPoint = false;
    var nonInteractivePickPoint;
    /**
    * Gets or sets the value for a non-interactive pick point.
    * @Type Point3d
    */
    Object.defineProperty(this, "nonInteractivePickPoint", {
        get: function () {
            return nonInteractivePickPoint;
        },
        set: function (point) {
            if(point instanceof Acad.Point3d) {
                nonInteractivePickPoint = point;
            } else {
                throw new TypeError('nonInteractivePickPoint should be of Point3d type.');
            }
        },
        enumerable: true,
        configurable: true
    });
    /**
    * Gets or sets whether the prompt accepts ENTER as sole input.
    * True if ENTER on its own is allowed, false otherwise.
    * @Type Boolean
    */
    Object.defineProperty(this, "allowNone", {
        enumerable: true
    });
};
Acad.extend(Acad.PromptNestedEntityOptions, Acad.PromptEditorOptions);
/**
* This is the base class for jig prompt options.
* @param messageAndKeywords is the prompt message along with Keywords.
* @throw TypeError
*
*/
Acad.JigPromptOptions = function (messageAndKeywords) {
    Acad.PromptOptions.call(this, messageAndKeywords);
    var specialCursorType = 0;
    /**
    * Gets or sets the cursor to be associated with the prompt.
    * @Type Acad.CursorType
    */
    Object.defineProperty(this, "specialCursorType", {
        get: function () {
            return specialCursorType;
        },
        set: function (x) {
            var col = Acad.CursorType;// enum
            
            var isValid = false;
            for(var name in col) {
                if(col[name] === x) {
                    specialCursorType = x;
                    isValid = true;
                    break;
                }
            }
            if(!isValid) {
                throw new TypeError('Type of specialCursorType should be Acad.CursorType.');
            }
        },
        enumerable: true,
        configurable: true
    });
    var userInputControls = 0;
    /**
    * Sets or gets the bitwise OR'd value of all user input control.
    * The settings in effect at the present time for this particular jig.
    * @Type Acad.UserInputControls
    */
    Object.defineProperty(this, "userInputControls", {
        get: function () {
            return userInputControls;
        },
        set: function (x) {
            if(Acad.isInteger(x)) {
                userInputControls = x;
            } else {
                throw new TypeError('Type of userInputControls should be Acad.UserInputControls.');
            }
        },
        enumerable: true,
        configurable: true
    });
    var useDefaultValue = 0;
    /**
    * Gets or sets whether the prompt should use the default value when
    * the user presses ENTER without any other input. The property allowing
    * client code to set the default value is declared by derived classes.
    * @Type Boolean
    *
    */
    Object.defineProperty(this, "useDefaultValue", {
        get: function () {
            return useDefaultValue;
        },
        set: function (x) {
            if(typeof (x) == 'boolean') {
                useDefaultValue = x;
            } else {
                throw new TypeError('Type of useDefaultValue should be boolean.');
            }
        },
        enumerable: true,
        configurable: true
    });
};
Acad.extend(Acad.JigPromptOptions, Acad.PromptOptions);
/**
* This is the base class for jig prompt options used in various types of data acquisition.
* @param messageAndKeywords is the prompt message along with Keywords.
* @throws TypeError
*/
Acad.JigPromptGeometryOptions = function (messageAndKeywords) {
    Acad.JigPromptOptions.call(this, messageAndKeywords);
    var basePoint = new Acad.Point3d(0, 0, 0);
    /**
    * Gets or sets the base point to be used by the prompt.
    * @Type Point3d
    */
    Object.defineProperty(this, "basePoint", {
        get: function () {
            return basePoint;
        },
        set: function (x) {
            if(x instanceof Acad.Point3d) {
                basePoint = x;
            } else {
                throw new TypeError('Point should be of Point3d type.');
            }
        },
        enumerable: true,
        configurable: true
    });
    var useBasePoint = false;
    /**
    * Gets or sets whether the base point is to be used or not.
    * @Type Boolean
    */
    Object.defineProperty(this, "useBasePoint", {
        get: function () {
            return useBasePoint;
        },
        set: function (x) {
            if(typeof (x) == 'boolean') {
                useBasePoint = x;
            } else {
                throw Error('Type of useBasePoint should be boolean.');
            }
        },
        enumerable: true,
        configurable: true
    });
};
Acad.extend(Acad.JigPromptGeometryOptions, Acad.JigPromptOptions);
/**
* This class represents optional parameters for prompt for distance during jigging.
* @param messageAndKeywords is the prompt message along with Keywords.
* @throws TypeError
*
*/
Acad.JigPromptDistanceOptions = function (messageAndKeywords) {
    Acad.JigPromptGeometryOptions.call(this, messageAndKeywords);
    var defaultValue = 0;
    /**
    * Gets or sets default jig prompt distance options value.
    * @Type Number
    */
    Object.defineProperty(this, "defaultValue", {
        get: function () {
            return defaultValue;
        },
        set: function (x) {
            if(Acad.isNumber(x)) {
                defaultValue = x;
            } else {
                throw new TypeError('Default value should be Number.');
            }
        },
        enumerable: true,
        configurable: true
    });
};
Acad.extend(Acad.JigPromptDistanceOptions, Acad.JigPromptGeometryOptions);
/**
* This class represents optional parameters for prompt for angle during jigging.
* @param messageAndKeywords is the prompt message along with Keywords.
* @throws TypeError
*/
Acad.JigPromptAngleOptions = function (messageAndKeywords) {
    Acad.JigPromptGeometryOptions.call(this, messageAndKeywords);
    var defaultValue = 0;
    /**
    * Returns the default jig prompt angle options value.
    * @Type Number
    */
    Object.defineProperty(this, 'defaultValue', {
        get: function () {
            return defaultValue;
        },
        set: function (x) {
            if(Acad.isNumber(x)) {
                defaultValue = x;
            } else {
                throw new TypeError('Default value should be Number.');
            }
        },
        enumerable: true,
        configurable: true
    });
    var useBasePoint = true;
    /**
    * Gets whether the base point is to be used or not.
    * useBasePoint is always true as there must be a base point when prompt for angle during jigging.
    * @Read-Only
    * @Type Boolean
    */
    Object.defineProperty(this, "useBasePoint", {
        get: function () {
            return useBasePoint;
        },
        set: function () {
            throw Error("useBasePoint is read-only property");
        },
        enumerable: true,
        configurable: true
    });
};
Acad.extend(Acad.JigPromptAngleOptions, Acad.JigPromptGeometryOptions);
/**
* This class represents optional parameters for prompt for point during jigging.
* @param messageAndKeywords is the prompt message along with Keywords.
* @throws TypeError
*/
Acad.JigPromptPointOptions = function (messageAndKeywords) {
    Acad.JigPromptGeometryOptions.call(this, messageAndKeywords);
    var defaultValue = new Acad.Point3d(0, 0, 0);
    /**
    *  Returns the default value to be used for point option prompt.
    * @Type Acad.Point3d
    */
    Object.defineProperty(this, 'defaultValue', {
        get: function () {
            return defaultValue;
        },
        set: function (x) {
            if(x instanceof Acad.Point3d) {
                defaultValue = x;
            } else {
                throw new TypeError('Point should be of Point3d type.');
            }
        },
        enumerable: true,
        configurable: true
    });
};
Acad.extend(Acad.JigPromptPointOptions, Acad.JigPromptGeometryOptions);
/**
* This class represents optional parameters for prompt for string during jigging.
* @param messageAndKeywords is the prompt message along with Keywords.
* @throws TypeError
*/
Acad.JigPromptStringOptions = function (messageAndKeywords) {
    Acad.JigPromptOptions.call(this, messageAndKeywords);
    var defaultValue;
    /**
    * Returns the default value to be used for string option prompt.
    * @Type String
    */
    Object.defineProperty(this, 'defaultValue', {
        get: function () {
            return defaultValue;
        },
        set: function (x) {
            if(typeof (x) == 'string') {
                defaultValue = x;
            } else {
                throw new TypeError('Default value should be String.');
            }
        },
        enumerable: true,
        configurable: true
    });
};
Acad.extend(Acad.JigPromptStringOptions, Acad.JigPromptOptions);
//
///////////////////////////////////////////////////////////////////////////////
//
//                 (C) Copyright 2012 by Autodesk, Inc.
//
// The information contained herein is confidential, proprietary to Autodesk,
// Inc., and considered a trade secret as defined in section 499C of the
// penal code of the State of California.  Use of this information by anyone
// other than authorized employees of Autodesk, Inc. is granted only under a
// written non-disclosure agreement, expressly prescribing the scope and
// manner of such use.
//
///////////////////////////////////////////////////////////////////////////////
/**
* This is the base class for classes that hold the result of a prompt operation.
* @param retCode The status result of the prompt operation.
* @param stringResult The optional string result of the prompt operation.
* This value is set when Status is PromptStatus.Keyword or a prompt that returns a string as its primary result.
*
*/
Acad.PromptResults = function (retCode, stringResult) {
    Acad.Promise.call(this);
    /**
    * Gets the status result of the prompt operation.
    * @Read-Only
    * @Type Acad.PromptStatus
    */
    this.status = retCode;
    /**
    * Gets the optional string result of the prompt operation.
    * This value is set when status is RTKWORD or a prompt that returns a string as its primary result.
    * @Read-Only
    * @Type String
    */
    this.stringResult = stringResult;
};
Acad.extend(Acad.PromptResults, Acad.Promise);
/**
* This class holds the result of a prompt that returns an integer as its primary result.
* @param retCode The status result of the prompt operation.
* @param stringResult The optional string result of the prompt operation.
* @param value The integer that the user entered.
*
*/
Acad.PromptIntegerResult = function (retCode, stringResult, value) {
    Acad.PromptResults.call(this, retCode, stringResult);
    /**
    * Gets the integer that the user entered.
    * @Read-Only
    * @Type Integer
    */
    if(retCode == Acad.PromptStatus.OK) {
        this.value = value;
    }
};
Acad.extend(Acad.PromptIntegerResult, Acad.PromptResults);
/**
* This class holds the result of a prompt that returns a double as its primary result.
* @param retCode The status result of the prompt operation.
* @param stringResult The optional string result of the prompt operation.
* @param value The double that the user entered.
*
*/
Acad.PromptDoubleResult = function (retCode, stringResult, value) {
    Acad.PromptResults.call(this, retCode, stringResult);
    /**
    * Gets the double that the user entered.
    * @Read-Only
    * @Type Number
    */
    if(retCode == Acad.PromptStatus.OK) {
        this.value = value;
    }
};
Acad.extend(Acad.PromptDoubleResult, Acad.PromptResults);
/**
* This class holds the result of a prompt that returns a point as its primary result.
* @param retCode The status result of the prompt operation.
* @param stringResult The optional string result of the prompt operation.
* @param point The point that the user entered.
* @throws TypeError
*
*/
Acad.PromptPointResult = function (retCode, stringResult, point) {
    Acad.PromptResults.call(this, retCode, stringResult);
    /**
    * Gets the point that the user entered.
    * @Read-Only
    * @Type Acad.Point3d
    */
    if(retCode == Acad.PromptStatus.OK) {
        if(point instanceof Acad.Point3d) {
            this.value = point;
        } else {
            throw new TypeError("Point should be of Point3d type.");
        }
    }
};
Acad.extend(Acad.PromptPointResult, Acad.PromptResults);
/**
* This class holds the result of a prompt that returns an entity as its primary result.
* @param retCode The status result of the prompt operation.
* @param stringResult The optional string result of the prompt operation.
* @param objectId The entity that the user picked.
* @param point The point that was used to pick the entity.
* @throws TypeError
*
*/
Acad.PromptEntityResult = function (retCode, stringResult, objectId, point) {
    Acad.PromptResults.call(this, retCode, stringResult);
    /**
    * Gets the object id of entity that the user picked.
    * @Read-Only
    * @Type Integer
    */
    this.objectId = objectId;
    /**
    * Gets the point that was used to pick the entity.
    * @Read-Only
    * @Type Acad.Point3d
    */
    if(point instanceof Acad.Point3d) {
        this.pickedPoint = point;
    } else {
        throw new TypeError("Point should be of Point3d type.");
    }
};
Acad.extend(Acad.PromptEntityResult, Acad.PromptResults);
/**
* This class holds the result of a prompt that returns a nested entity as its primary result.
* @param retCode The status result of the prompt operation.
* @param stringResult the optional string result of the prompt operation.
* @param objectId The entity that the user picked.
* @param point The point that was used to pick the entity.
* @param xform The transformation matrix that is applied to the picked object by its containers.
* @param objectIds Collection of nested enities object Ids.
* @throws TypeError
*
*/
Acad.PromptNestedEntityResult = function (retCode, stringResult, objectId, point, xform, objectIds) {
    Acad.PromptEntityResult.call(this, retCode, stringResult, objectId, point);
    /**
    * Gets the transformation matrix that is applied to the picked object by its containers.
    * @Read-Only
    * @Type Acad.Matrix3d
    */
    if(xform instanceof Acad.Matrix3d) {
        this.matrix = xform;
    } else {
        throw new TypeError("matrix should be of Matrix3d type.");
    }
    /**
    * Gets an array of containers in which this entity is nested.
    * Returns an array of object IDs representing the containers of this nested entity.
    * @Read-Only
    * @Type Array
    */
    if(objectIds instanceof Array) {
        this.containers = objectIds;
    } else {
        throw new TypeError("objectIds should be of Array type.");
    }
};
Acad.extend(Acad.PromptNestedEntityResult, Acad.PromptEntityResult);
//
///////////////////////////////////////////////////////////////////////////////
//
//                 (C) Copyright 2012 by Autodesk, Inc.
//
// The information contained herein is confidential, proprietary to Autodesk,
// Inc., and considered a trade secret as defined in section 499C of the
// penal code of the State of California.  Use of this information by anyone
// other than authorized employees of Autodesk, Inc. is granted only under a
// written non-disclosure agreement, expressly prescribing the scope and
// manner of such use.
//
///////////////////////////////////////////////////////////////////////////////
/**
* This class provides optional parameters to a selection set prompt.
*
*/
Acad.PromptSelectionOptions = function () {
    this.allowDuplicates = false;
    this.messageAdding = undefined;
    this.messageRemoval = undefined;
    this.singlePickInSpace = false;
    this.selectEverythingInAperture = false;
    this.singleOnly = false;
    this.rejectObjectsOnLockedLayers = false;
    this.rejectObjectsFromNonCurrentSpace = false;
    this.rejectPaperspaceViewport = false;
};
/*
* This is the base class for a selected object.
*
*/
Acad.SelectedObject = function () {
    /*
    * Gets the object ID of this selected object.
    *
    */
    this.objectId = undefined;
    /*
    * Gets a value that describes what part of the object was selected.
    *
    */
    this.gsMarker = undefined;
};
/**
* This class represents the result of a prompt for a selection of objects.
* @param status is the status result of the prompt operation.
* @param objectIds is the array of SelectedObject.
* @throws TypeError
*
*/
Acad.PromptSelectionResult = function (status, objectIds) {
    Acad.PromptResults.call(this, status);
    if(objectIds instanceof Array) {
        this.value = objectIds;
    } else {
        // Array of SelectedObject
        throw new TypeError("objectIds should be of Array type.");
    }
};
Acad.extend(Acad.PromptSelectionResult, Acad.PromptResults);
//
///////////////////////////////////////////////////////////////////////////////
//
//                 (C) Copyright 2012 by Autodesk, Inc.
//
// The information contained herein is confidential, proprietary to Autodesk,
// Inc., and considered a trade secret as defined in section 499C of the
// penal code of the State of California.  Use of this information by anyone
// other than authorized employees of Autodesk, Inc. is granted only under a
// written non-disclosure agreement, expressly prescribing the scope and
// manner of such use.
//
///////////////////////////////////////////////////////////////////////////////
/**
* This class represents base jig class
* @param updateCallback is of type function and is the callback for update during jigging.
* @param options is of type Acad.JigPromptPointOptions, Acad.JigPromptDistanceOptions, Acad.JigPromptAngleOptions or Acad.JigPromptStringOptions.
*
*/
Acad.Jig = function (updateCallback, options) {
    if(typeof (updateCallback) != 'function') {
        throw TypeError("updateCallback should be function type.");
    }
    var acquireMode = 0;
    if(options instanceof Acad.JigPromptPointOptions) {
        acquireMode = 1;
    } else {
        if(options instanceof Acad.JigPromptDistanceOptions) {
            acquireMode = 2;
        } else {
            if(options instanceof Acad.JigPromptAngleOptions) {
                acquireMode = 3;
            } else {
                if(options instanceof Acad.JigPromptStringOptions) {
                    acquireMode = 4;
                }
            }
        }
    }
    if(acquireMode == 0) {
        throw TypeError("options should be of type Acad.JigPromptPointOptions, Acad.JigPromptDistanceOptions, Acad.JigPromptAngleOptions or Acad.JigPromptStringOptions.");
    }
    var onUpdate = updateCallback;
    /**
    * onUpdate is of type function and is the callback for update during jigging.
    * @Read-Only
    * @Type Boolean
    */
    Object.defineProperty(this, "onUpdate", {
        get: function () {
            return onUpdate;
        },
        set: function () {
            throw Error("onUpdate is read-only property");
        }
    });
    var jigOptions = options;
    /**
    * jigPromptOptions is of type Acad.JigPromptPointOptions, Acad.JigPromptDistanceOptions, Acad.JigPromptAngleOptions or Acad.JigPromptStringOptions.
    * @Read-Only
    * @Type Boolean
    */
    Object.defineProperty(this, "jigOptions", {
        get: function () {
            return jigOptions;
        },
        set: function () {
            throw Error("jigOptions is read-only property");
        }
    });
    if(acquireMode == 1) {
        registerCallback('Ac_Jig_Callback_update_acquirePoint', this.onUpdate);
    } else {
        if(acquireMode == 2) {
            registerCallback('Ac_Jig_Callback_update_acquireDistance', this.onUpdate);
        } else {
            if(acquireMode == 3) {
                registerCallback('Ac_Jig_Callback_update_acquireAngle', this.onUpdate);
            } else {
                if(acquireMode == 4) {
                    registerCallback('Ac_Jig_Callback_update_acquireString', this.onUpdate);
                }
            }
        }
    }
};
/**
* This class represents jig class for drawing transient jigging
* @param updateCallback is of type function and is the callback for update of transient during jigging.
* @param options is of type Acad.JigPromptPointOptions, Acad.JigPromptDistanceOptions, Acad.JigPromptAngleOptions or Acad.JigPromptStringOptions.
*
*/
Acad.DrawJig = function (updateCallback, options) {
    Acad.Jig.call(this, updateCallback, options);
    function complete() {
    }
    function error() {
    }
    /**
    * Add or update transient entity during jigging.
    * @param xmlData is of type string and is the XML for the drawable transient.
    * @param onComplete is a function type called on successful completion of this method.
    * @param onError is a function type called if an error occurs.
    *
    */
    this.update = function (xmlData, onComplete, onError) {
        if(typeof (xmlData) !== 'string') {
            throw TypeError('xmlData should be of type string');
        }
        ; ;
        if(typeof (onComplete) != 'function') {
            throw TypeError("onComplete should be function type.");
        }
        ; ;
        if(typeof (onError) != 'function') {
            throw TypeError("onError should be function type.");
        }
        ; ;
        var args = {
        };
        args.functionName = 'Ac_DrawJig_update';
        args.invokeAsCommand = false;
        args.functionParams = {
            'data': xmlData
        };
        var completefn = onComplete || complete;
        var errorfn = onError || error;
        execAsync(JSON.stringify(args), completefn, errorfn);
    };
};
Acad.extend(Acad.DrawJig, Acad.Jig);
//
///////////////////////////////////////////////////////////////////////////////
//
//                 (C) Copyright 2012 by Autodesk, Inc.
//
// The information contained herein is confidential, proprietary to Autodesk,
// Inc., and considered a trade secret as defined in section 499C of the
// penal code of the State of California.  Use of this information by anyone
// other than authorized employees of Autodesk, Inc. is granted only under a
// written non-disclosure agreement, expressly prescribing the scope and
// manner of such use.
//
///////////////////////////////////////////////////////////////////////////////
/**
* This class represents system variable collection
*
*/
Acad.SystemVariableCollection = new function () {
    var systemVariables = {
    };
    /**
    * This function returns the system variable
    * @param name is name of system variable.
    *
    */
    this.getSystemVariable = function (name) {
        if(name == undefined) {
            throw Error("Please provide name of System Variable.");
        }
        // Search system variable locally
        if(systemVariables.hasOwnProperty(name)) {
            return systemVariables[name];
        }
        var args = {
            'functionName': 'Ac_SystemVariableCollection_getSystemVariable',
            'invokeAsCommand': false
        };
        args.functionParams = {
            'name': name
        };
        var jsonStr = exec(JSON.stringify(args));
        var jsonObj = JSON.parse(jsonStr);
        if(jsonObj.retCode == Acad.ErrorStatus.eJsOk) {
            var sysVar = new SystemVariable(jsonObj.name, jsonObj.valueType, jsonObj.value, jsonObj.isActive, jsonObj.minimum, jsonObj.maximum);
            systemVariables[name] = sysVar;
            return sysVar;
        } else {
            throw Error(jsonObj.retErrorString);
        }
    };
    /**
    * This class represent system variable
    * @param sName is the name of system variable.
    * @param type is type of resource buffer.
    * @param sValue is the value of system variable .
    * @param active indicates whether the system varibale is active or not.
    * @param min is minimum value of system variable.
    * @param max is maximum value of system variable.
    *
    */
    function SystemVariable(sName, type, sValue, active, min, max) {
        var name = sName;
        var valueType = type;
        var value = sValue;
        var isActive = active;
        var minimum = min;
        var maximum = max;
        var eventObject = new Acad.EventObject();
        var isReactorAdded = false;
        /**
        * This property is used to get system variable name.
        * @Type String
        * @Read-Only
        * @throws Error
        *
        */
        Object.defineProperty(this, "name", {
            get: function () {
                return name;
            },
            set: function () {
                throw Error("name is read-only property");
            }
        });
        /**
        * This property is used to get system variable value type.
        * @Type Acad.ResultValueType
        * @Read-Only
        * @throws Error
        *
        */
        Object.defineProperty(this, "valueType", {
            get: function () {
                return valueType;
            },
            set: function () {
                throw Error("valueType is read-only property");
            }
        });
        /**
        * This property is used to get system variable minimum value.
        * @Type Number
        * @Read-Only
        * @throws Error
        *
        */
        Object.defineProperty(this, "minimum", {
            get: function () {
                return minimum;
            },
            set: function () {
                throw Error("minimum is read-only property");
            }
        });
        /**
        * This property is used to get system variable maximum value.
        * @Type Number
        * @Read-Only
        * @throws Error
        *
        */
        Object.defineProperty(this, "maximum", {
            get: function () {
                return maximum;
            },
            set: function () {
                throw Error("maximum is read-only property");
            }
        });
        /**
        * This property is used to get system variable status.
        * @Type Boolean
        * @Read-Only
        * @throws Error
        *
        */
        Object.defineProperty(this, "isActive", {
            get: function () {
                var args = {
                    'functionName': 'Ac_SystemVariable_isActive',
                    'invokeAsCommand': false
                };
                args.functionParams = {
                    'name': name
                };
                var jsonStr = exec(JSON.stringify(args));
                var jsonObj = JSON.parse(jsonStr);
                if(jsonObj.retCode == Acad.ErrorStatus.eJsOk) {
                    return jsonObj.isActive;
                } else {
                    throw Error(jsonObj.retErrorString);
                }
            },
            set: function () {
                throw Error("isActive is read-only property");
            }
        });
        /**
        * This property is used to get/set system variable value.
        * @Type Acad.ResultValueType
        * @throws Error
        * @throws TypeError
        *
        */
        Object.defineProperty(this, "value", {
            get: function () {
                var args = {
                    'functionName': 'Ac_SystemVariable_getValue',
                    'invokeAsCommand': false
                };
                args.functionParams = {
                    'name': name
                };
                var jsonStr = exec(JSON.stringify(args));
                var jsonObj = JSON.parse(jsonStr);
                if(jsonObj.retCode == Acad.ErrorStatus.eJsOk) {
                    switch(valueType) {
                        case Acad.ResultValueType.RTPOINT: {
                            value = new Acad.Point2d(jsonObj.value.x, jsonObj.value.y);
                            break;

                        }
                        case Acad.ResultValueType.RT3DPOINT: {
                            value = new Acad.Point3d(jsonObj.value.x, jsonObj.value.y, jsonObj.value.z);
                            break;

                        }
                        default: {
                            value = jsonObj.value;
                            break;

                        }
                    }
                    return value;
                } else {
                    throw Error(jsonObj.retErrorString);
                }
            },
            set: function (sValue) {
                // Check for value type
                switch(valueType) {
                    case Acad.ResultValueType.RTSHORT:
                    case Acad.ResultValueType.RTLONG: {
                        if(!(Acad.isInteger(sValue))) {
                            throw TypeError("value is not Integer type.");
                        }
                        break;

                    }
                    case Acad.ResultValueType.RTREAL:
                    case Acad.ResultValueType.RTANG: {
                        if(typeof sValue != 'number') {
                            throw TypeError("value is not number.");
                        }
                        break;

                    }
                    case Acad.ResultValueType.RTSTR: {
                        if(typeof sValue != 'string') {
                            throw TypeError("value is not string.");
                        }
                        break;

                    }
                    case Acad.ResultValueType.RTPOINT: {
                        if(!(sValue instanceof Acad.Point2d)) {
                            throw TypeError("Point should be of Point2d type.");
                        }
                        break;

                    }
                    case Acad.ResultValueType.RT3DPOINT: {
                        if(!(sValue instanceof Acad.Point3d)) {
                            throw TypeError("Point should be of Point3d type.");
                        }
                        break;

                    }
                    default: {
                        break;

                    }
                }
                var args = {
                    'functionName': 'Ac_SystemVariable_setValue',
                    'invokeAsCommand': false
                };
                args.functionParams = {
                    'name': name,
                    'valueResBuf': {
                        'valueType': valueType,
                        'value': sValue
                    }
                };
                var jsonStr = exec(JSON.stringify(args));
                var jsonObj = JSON.parse(jsonStr);
                if(jsonObj.retCode == Acad.ErrorStatus.eJsOk) {
                    value = sValue;
                } else {
                    throw Error(jsonObj.retErrorString);
                }
            }
        });
        /**
        * This function is used to set system variable value using command.
        * @remarks This is asynchronous function call. It will not return error if the value is not set successfully.
        * @remarks You should check if the value is set successfully in the listener callback function.
        * @param sValue is value of system variable.
        * @throws Error
        * @throws TypeError
        */
        this.postValue = function (sValue) {
            // Check for value type
            switch(valueType) {
                case Acad.ResultValueType.RTSHORT:
                case Acad.ResultValueType.RTLONG: {
                    if(!(Acad.isInteger(sValue))) {
                        throw TypeError("value is not Integer type.");
                    }
                    break;

                }
                case Acad.ResultValueType.RTREAL:
                case Acad.ResultValueType.RTANG: {
                    if(typeof sValue != 'number') {
                        throw TypeError("value is not number.");
                    }
                    break;

                }
                case Acad.ResultValueType.RTSTR: {
                    if(typeof sValue != 'string') {
                        throw TypeError("value is not string");
                    }
                    break;

                }
                case Acad.ResultValueType.RTPOINT: {
                    if(!(sValue instanceof Acad.Point2d)) {
                        throw TypeError("Point should be of Point2d type.");
                    }
                    break;

                }
                case Acad.ResultValueType.RT3DPOINT: {
                    if(!(sValue instanceof Acad.Point3d)) {
                        throw TypeError("Point should be of Point3d type.");
                    }
                    break;

                }
                default: {
                    break;

                }
            }
            var args = {
                'functionName': 'Ac_SystemVariable_postValue',
                'invokeAsCommand': false
            };
            args.functionParams = {
                'name': name,
                'valueResBuf': {
                    'valueType': valueType,
                    'value': sValue
                }
            };
            var jsonStr = exec(JSON.stringify(args));
            var jsonObj = JSON.parse(jsonStr);
            if(jsonObj.retCode == Acad.ErrorStatus.eJsOk) {
                value = sValue;
            } else {
                throw Error(jsonObj.retErrorString);
            }
        };
        this.eventname = {
            "valueChanged": "valueChanged",
            "activated": "activated"
        };
        /**
        * This function is used to add callback.
        * @param eventname is event for which callback would be called, possible value are "valueChanged" and "activated".
        * @param callback is a callback function, which is called when an event occurs.
        * @throws TypeError
        * @throws Error
        *
        */
        this.addEventListener = function (eventname, callback) {
            if(eventname != this.eventname.valueChanged && eventname != this.eventname.activated) {
                throw Error("Event name is not correct.");
            }
            // Register callback
            if(typeof callback == 'function') {
                if(eventObject.count(eventname) == 0 && isReactorAdded == false) {
                    registerCallback('Ac_SystemVariable_Callback_' + name, systemVariableCallback);
                    addReactor();
                }
                eventObject.addEventListener(eventname, callback);
            } else {
                throw TypeError("Callback should be function type.");
            }
        };
        /**
        * This function is used to remove callback.
        * @param eventname is event for which callback would be removed, possible value are "valueChanged" and "activated".
        * @param callback is a callback function, which would not be called further for given eventname.
        * @throws TypeError
        * @throws Error
        *
        */
        this.removeEventListener = function (eventname, callback) {
            if(eventname != this.eventname.valueChanged && eventname != this.eventname.activated) {
                throw Error("Event name is not correct.");
            }
            // Unregister callback
            if(typeof callback == 'function') {
                if(eventObject.count(eventname) > 0) {
                    eventObject.removeEventListener(eventname, callback);
                }
                // listeners is zero, so remove reactor
                if(eventObject.count(eventname) == 0 && isReactorAdded == true) {
                    removeReactor();
                }
            } else {
                throw TypeError("Callback should be function type.");
            }
        };
        /**
        * This function is for internal use.
        *
        */
        function systemVariableCallback(jsonStr) {
            var jsonObj = JSON.parse(jsonStr);
            eventObject.dispatchEvent(jsonObj.eventname, jsonObj.name);
        }
        /**
        * This function is for internal use.
        *
        */
        function addReactor() {
            var args = {
                'functionName': 'Ac_SystemVariable_addReactor',
                'invokeAsCommand': false
            };
            args.functionParams = {
                'name': name
            };
            var jsonStr = exec(JSON.stringify(args));
            var jsonObj = JSON.parse(jsonStr);
            if(jsonObj.retCode == Acad.ErrorStatus.eJsOk) {
                isReactorAdded = true;
            } else {
                throw Error(jsonObj.retErrorString);
            }
        }
        /**
        * This function is for internal use.
        *
        */
        function removeReactor() {
            var args = {
                'functionName': 'Ac_SystemVariable_removeReactor',
                'invokeAsCommand': false
            };
            args.functionParams = {
                'name': name
            };
            var jsonStr = exec(JSON.stringify(args));
            var jsonObj = JSON.parse(jsonStr);
            if(jsonObj.retCode == Acad.ErrorStatus.eJsOk) {
                isReactorAdded = false;
            } else {
                throw Error(jsonObj.retErrorString);
            }
        }
    }
}();
