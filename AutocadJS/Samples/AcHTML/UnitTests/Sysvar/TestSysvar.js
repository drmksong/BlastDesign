
function sysvarValueChanged(eventname, sysvarname) {
    document.getElementById('onValueChanged').value = eventname + ' ' + sysvarname;
}

function sysvarActivatedChanged(eventname, sysvarname) {
    document.getElementById('onActivatedChanged').value = eventname + ' ' + sysvarname;
}

function displayResult(sysvar) {
    
    document.getElementById('SystemVariable_name').value = sysvar.name;
    document.getElementById('SystemVariable_valueType').value = sysvar.valueType;

    if (sysvar.valueType == Acad.ResultValueType.RT3DPOINT) {
        document.getElementById('SystemVariable_value').value = 'x: ' + sysvar.value.x + 'y: ' + sysvar.value.y + 'z: ' + sysvar.value.z;
    }
    else if (sysvar.valueType == Acad.ResultValueType.RTPOINT) {
        document.getElementById('SystemVariable_value').value = 'x: ' + sysvar.value.x + 'y: ' + sysvar.value.y;
    }
    else {
        document.getElementById('SystemVariable_value').value = sysvar.value;
    }

    document.getElementById('SystemVariable_isActive').value = sysvar.isActive;
    document.getElementById('SystemVariable_minmum').value = sysvar.minimum;
    document.getElementById('SystemVariable_maximum').value = sysvar.maximum;
}


function getSysvar(options) {
    var sysvarname = document.getElementById('sysvarname').value;
  
    var sysvar = Acad.SystemVariableCollection.getSystemVariable(sysvarname);

    displayResult(sysvar);

    return sysvar;
}

function postSysvarValue(options) {
    
    var sysvar = getSysvar(options);

    if (sysvar.valueType == Acad.ResultValueType.RT3DPOINT) {
            var pt3dX = Number(document.getElementById('sysvar_newvalue_x').value);
            var pt3dY = Number(document.getElementById('sysvar_newvalue_y').value);
            var pt3dZ = Number(document.getElementById('sysvar_newvalue_z').value);
            var pt3d = new Acad.Point3d(pt3dX, pt3dY, pt3dZ);
            sysvar.postValue(pt3d);
    }	
    else if (sysvar.valueType == Acad.ResultValueType.RTPOINT) {
            var ptX = Number(document.getElementById('sysvar_newvalue_x').value);
            var ptY = Number(document.getElementById('sysvar_newvalue_y').value);
            var pt = new Acad.Point2d(ptX, ptY);
            sysvar.postValue(pt);
    }
    else if (sysvar.valueType == Acad.ResultValueType.RTSTR) {
            var strVal = document.getElementById('sysvar_newvalue').value;
            sysvar.postValue(strVal);
    }
    else {
            var numVal = Number(document.getElementById('sysvar_newvalue').value);
            sysvar.postValue(numVal);
    }

    displayResult(sysvar);	
}

function setSysvarValue(options) {
    
    var sysvar = getSysvar(options);

    if (sysvar.valueType == Acad.ResultValueType.RT3DPOINT) {
            var pt3dX = Number(document.getElementById('sysvar_newvalue_x').value);
            var pt3dY = Number(document.getElementById('sysvar_newvalue_y').value);
            var pt3dZ = Number(document.getElementById('sysvar_newvalue_z').value);
            var pt3d = new Acad.Point3d(pt3dX, pt3dY, pt3dZ);
            sysvar.value = pt3d;
    }
    else if (sysvar.valueType == Acad.ResultValueType.RTPOINT) {
            var ptX = Number(document.getElementById('sysvar_newvalue_x').value);
            var ptY = Number(document.getElementById('sysvar_newvalue_y').value);
            var pt = new Acad.Point2d(ptX, ptY);
            sysvar.value = pt;
    }
    else if (sysvar.valueType == Acad.ResultValueType.RTSTR) {
            var strVal = document.getElementById('sysvar_newvalue').value;
            sysvar.value = strVal;
    }
    else {
            var numVal = Number(document.getElementById('sysvar_newvalue').value);
            sysvar.value = numVal;
    }

    displayResult(sysvar);	
}

function addListener(options) {
    
    var sysvar = getSysvar(options);

    // add listener for valueChanged
    sysvar.addEventListener(sysvar.eventname.valueChanged, sysvarValueChanged);

    // add listener for activated
    sysvar.addEventListener(sysvar.eventname.activated, sysvarActivatedChanged);
}

function removeListener(options) {
    
    var sysvar = getSysvar(options);

    // remove listeners for valueChanged
    sysvar.removeEventListener(sysvar.eventname.valueChanged, sysvarValueChanged);

    document.getElementById('onValueChanged').value = 'empty';

    // remove listeners for activated
    sysvar.removeEventListener(sysvar.eventname.activated, sysvarActivatedChanged);

    document.getElementById('onActivatedChanged').value = 'empty';
}

