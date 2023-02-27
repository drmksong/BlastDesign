
TransientType = {
    "Image": 0,
    "Rectangle": 1,
    "Circle": 2,
};

var transient_location = new Array();
var cur_cursor = ' ';
var encoded_image;

var pt0 = new Array();
var pt1 = new Array();
var pt2 = new Array();
var pt3 = new Array();

var colors = new Array();
colors['Red']       = "#ff0000";
colors['Yellow']    = "#ffff00";
colors['Green']     = "#00ff00";
colors['Cyan']      = "#00ffff";
colors['Blue']      = "#0000ff";
colors['Magenta']   = "#ff00ff";
colors['White']     = "#ffffff";
colors['Atomic Tangerine'] = "#ffa474";

var drawables = new Array();
var transientIds = new Array();

function transientMouseEventHandler(eventname, args) {

    var text = "";
    text += "id: " + args.id + "<br/>";
    text += "event: " + args.eventname + "<br/>";

    if ( args.eventname != "mouseleave" ) {
        text += "pos: ("    + args.mouse_xpos + ", " + args.mouse_ypos + ")<br/>";
        text += "shift: "   + args.mouse_shiftkey_state + ", ";
        text += "ctrl: "    + args.mouse_ctrlkey_state + "<br/>";
        text += "lbutton: " + args.mouse_lbutton_state + ", ";
        text += "mbutton: " + args.mouse_mbutton_state + ", ";
        text += "rbutton: " + args.mouse_rbutton_state + "<br/>";
        
        if ( args.eventname == "mousewheel" ) {
            text += "wheel delta: " + args.mouse_wheel_delta + "<br/>";
        }
    }
    document.getElementById('mouseevents').innerHTML = text;
    
    if ( args.eventname == "lbuttondown" ) {
        document.getElementById('SelectedID').value = args['transient'].getId();
       
        if (args.mouse_ctrlkey_state == true)  // Simple test test to swap image types.
        {
            if (document.getElementById('BubbleType').selectedIndex == 2)
                document.getElementById('BubbleType').selectedIndex = 3;
            else 
                document.getElementById('BubbleType').selectedIndex = 2;
            updateSelectedTransient();
        }
    }
}

function createDrawableImage() {
    // This method builds up an xml string that contains data to create an AcGiTransient that represents the sticky. 
    // It uses the position obtained from getTransientLocation() and the encoded image from createEncodedImage().

    // Note:  height and width of drawable and image must match; 
    var imgWidth = 28;
    var imgHeight = 28;

    var xOffset = -50;
    var yOffset = 125;
    var bubbleType = document.getElementById('BubbleType').selectedIndex; // 0 == small, 1 == extended
    if (bubbleType == 2 || bubbleType == 3) {
        imgWidth = 247;
        imgHeight = 84;
        xOffset = -50;
        yOffset = 100;
    }

    var cursorType = document.getElementById('Cursor').value;
    if (cursorType == 'None')
        cur_cursor = ' ';
    else
        cur_cursor = ' cursor="' + cursorType + '"';


   

    var ptUCS = Acad.Editor.CurrentViewport.ucsToWorld(new Acad.Point3d(transient_location[0],transient_location[1], transient_location[2]));

    transient_location[0] = ptUCS.x;
    transient_location[1] = ptUCS.y;
    transient_location[2] = ptUCS.z;

    var xAxis2 =  Acad.SystemVariableCollection.getSystemVariable('UCSXDIR'); 
    var yAxis2 =  Acad.SystemVariableCollection.getSystemVariable('UCSYDIR');
    

    var uDir = '" uDir="' +  xAxis2.value.x + ',' + xAxis2.value.y + ',' +  xAxis2.value.z + '" ';
    var vDir = ' vDir="'  +  yAxis2.value.x + ',' + yAxis2.value.y + ',' +  yAxis2.value.z + '" ';
  
    var drawable = '<?xml version="1.0" encoding="utf-8"?> \
      <!-- the event handler will receive the id--> \
      <drawable \
        xmlns="http://www.autodesk.com/AutoCAD/drawstream.xsd"\
        xmlns:t="http://www.autodesk.com/AutoCAD/transient.xsd"\
        t:onmouseover ="onmouseover"'
        +
        cur_cursor
        +
        '>\
          <graphics color="#ff0000" id="id1">\
            <scaleTransform type="World" extents="1,1,1">\
            <graphics>\
              <image srcHeight="'
               +
               imgHeight.toString()
               +
               '" srcWidth="'
               +
               imgWidth.toString()
               +
               '" xOffset="' + xOffset + '" yOffset="' + yOffset + uDir + vDir + 'position="'
               +
               transient_location.toString()
               +
               '">'
               +
               encoded_image
               +
            '</image>\
            </graphics>\
            </scaleTransform>\
          </graphics>\
      </drawable>        ';

    //alert (drawable);
    return drawable;
}


function addImageTransient() {

    function onComplete(args) {

        var bubbleType = document.getElementById('BubbleType').selectedIndex; // 0 == small, 1 == extended
        var bubbleID = document.getElementById('BubbleID').value;
        var postedBy = document.getElementById('BubblePostedBy').value;
        var message = document.getElementById('BubbleMessage').value;

        var resObj = JSON.parse(args);
        if (resObj) {
            transient_location[0] = resObj.value.x;
            transient_location[1] =  resObj.value.y;
            transient_location[2] =  resObj.value.z;
            var drawingFeed = new Acad.DrawingFeedPrivate();
            encoded_image = drawingFeed.generateImage(bubbleType, bubbleID, postedBy, message);

            var drawable = createDrawableImage();


            var transient1 = new Acad.Transient();
            var id = transient1.getId();
            transientIds.push(id);

            // Save some of the transient data in a map of drawables using the id as a key value.
            // This enables us to reset things like the correct location point for updateTransient. 
            // The createDrawableImage()  method use the location point.
            var drawData = new Object();
            drawData.pt0 = transient_location.slice(0); // copy the array
            drawables[id] = new Object();
            drawables[id].drawData = drawData;
            drawables[id].type = TransientType.Image;


            transient1.addEventListener(transient1.eventname.lbuttondown, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.lbuttondblclk, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.lbuttonup, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mbuttondown, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mbuttondblclk, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mbuttonup, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.rbuttondown, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.rbuttondblclk, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.rbuttonup, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mouseleave, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mousemove, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mousewheel, transientMouseEventHandler);
            //transient1.addEventListener(transient1.eventname.mousehover, transientMouseEventHandler);
            
            Acad.Application.activedocument.transientManager.addTransient(transient1, drawable);

            var bubbleID = document.getElementById('BubbleID');
            bubbleID.value = parseInt(bubbleID.value) + 1;
        }
    }

    function onError(args) {
        alert('Unable to create transient: ' + args);
    }

    var optionsFirst = new Acad.PromptPointOptions('Specify image transient location:', new Acad.Point3d(0, 0, 0));
    Acad.Editor.getPoint(optionsFirst).then(onComplete,   onError);
}


function createDrawablePolyline() {
    // This method builds up an xml string that contains data to create an AcGiTransient that represents the polyline. 

    var color = document.getElementById('ColorCB').value;
    var linetype = document.getElementById('LineTypeCB').value;
    var lineweight = document.getElementById('LineWeightCB').value;
    var filled = document.getElementById('Filled').checked;

   
    var cursorType = document.getElementById('Cursor').value;
    if (cursorType == 'None')
        cur_cursor = ' ';
    else
        cur_cursor = ' cursor="' + cursorType + '"';
    // Set the other rectangle corners based on the picked corners.
    pt1[0] = pt0[0];
    pt1[1] = pt2[1];
    pt1[2] = pt0[2];

    pt3[0] = pt2[0];
    pt3[1] = pt0[1];
    pt3[2] = pt0[2];

    var ptUCS = Acad.Editor.CurrentViewport.ucsToWorld(new Acad.Point3d(pt0[0],pt0[1], pt0[2]));
    pt0[0] = ptUCS.x;
    pt0[1] = ptUCS.y;
    pt0[2] = ptUCS.z;

    ptUCS = Acad.Editor.CurrentViewport.ucsToWorld(new Acad.Point3d(pt1[0],pt1[1], pt1[2]));
    pt1[0] = ptUCS.x;
    pt1[1] = ptUCS.y;
    pt1[2] = ptUCS.z;


    ptUCS = Acad.Editor.CurrentViewport.ucsToWorld(new Acad.Point3d(pt2[0],pt2[1], pt2[2]));
    pt2[0] = ptUCS.x;
    pt2[1] = ptUCS.y;
    pt2[2] = ptUCS.z;

    ptUCS = Acad.Editor.CurrentViewport.ucsToWorld(new Acad.Point3d(pt3[0],pt3[1], pt3[2]));
    pt3[0] = ptUCS.x;
    pt3[1] = ptUCS.y;
    pt3[2] = ptUCS.z;


    var drawable = '<?xml version="1.0" encoding="utf-8"?> \
      <!-- the event handler will receive the id--> \
      <drawable \
        xmlns="http://www.autodesk.com/AutoCAD/drawstream.xsd"\
        xmlns:t="http://www.autodesk.com/AutoCAD/transient.xsd"\
        t:onmouseover ="onmouseover"'
        +
        cur_cursor
        +
        '>\
          <graphics color="' + colors[color] + '" id="id1" lineweight="' + lineweight + '" linetype="' + linetype + '" filled="' + filled + '">\
            <polyline isClosed="true">\
              <vertices>\
                <vertex>' + pt0.toString() + '</vertex>\
                <vertex>' + pt1.toString() + '</vertex>\
                <vertex>' + pt2.toString() + '</vertex>\
                <vertex>' + pt3.toString() + '</vertex>\
              </vertices>\
            </polyline>\
          </graphics>\
      </drawable>        ';
    return drawable;
}

function addPolylineTransient() {

    function onCompleteFirst(args) {

        var resObj = JSON.parse(args);
        if (resObj) {
            pt0[0] = resObj.value.x;
            pt0[1] = resObj.value.y;
            pt0[2] = resObj.value.z;
            
            var optionsSecond = new Acad.PromptCornerOptions('Pick second corner point', new Acad.Point3d(resObj.value.x, resObj.value.y, resObj.value.z));
            Acad.Editor.getCorner(optionsSecond).then(onCompleteSecond, onError);
        }
    }

    function onCompleteSecond(args) {

        var resObj = JSON.parse(args);
        if (resObj) {
            pt2[0] = resObj.value.x;
            pt2[1] = resObj.value.y;
            pt2[2] = resObj.value.z;

            var drawable = createDrawablePolyline();
         
            var transient1 = new Acad.Transient();

            var id = transient1.getId();

            // Save some of the transient data in a map of drawables using the id as a key value.
            // This enables us to reset things like the correct corner points for updateTransient. 
            // The createDrawablePolyline()  method use the corner points.
            var drawData = new Object();
            drawData.pt0 = pt0.slice(0);  // copy the array
            drawData.pt2 = pt2.slice(0);
            drawables[id] = new Object();
            drawables[id].drawData = drawData;
            drawables[id].type = TransientType.Rectangle;
     
           
            transient1.addEventListener(transient1.eventname.lbuttondown, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.lbuttondblclk, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.lbuttonup, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mbuttondown, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mbuttondblclk, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mbuttonup, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.rbuttondown, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.rbuttondblclk, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.rbuttonup, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mouseleave, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mousemove, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mousewheel, transientMouseEventHandler);
            //transient1.addEventListener(transient1.eventname.mousehover, transientMouseEventHandler);

            Acad.Application.activedocument.transientManager.addTransient(transient1, drawable);
        }
    }

    function onError(args) {
        alert('Unable to create polyline transient: ' + args);
    }
   
    var optionsFirst = new Acad.PromptPointOptions('Pick first corner point', new Acad.Point3d(0, 0, 0));
    Acad.Editor.getPoint(optionsFirst).then(onCompleteFirst,
                                        onError);
}

function createDrawableCircle() {
    // This method builds up an xml string that contains data to create an AcGiTransient that represents the circle. 

    var color = document.getElementById('ColorCB').value;
    var linetype = document.getElementById('LineTypeCB').value;
    var lineweight = document.getElementById('LineWeightCB').value;
    var filled = document.getElementById('Filled').checked;

    var cursorType = document.getElementById('Cursor').value;
    if (cursorType == 'None')
        cur_cursor = ' ';
    else
        cur_cursor = ' cursor="' + cursorType + '"';

    var radius = Math.sqrt(Math.pow(pt2[0] - pt0[0], 2) + Math.pow(pt2[1] - pt0[1], 2));

    var drawable = '<?xml version="1.0" encoding="utf-8"?> \
      <!-- the event handler will receive the id--> \
      <drawable \
        xmlns="http://www.autodesk.com/AutoCAD/drawstream.xsd"\
        xmlns:t="http://www.autodesk.com/AutoCAD/transient.xsd"\
         t:onmouseover ="onmouseover"'
        +
        cur_cursor
        +
        '>\
          <graphics color="' + colors[color] + '" id="id1" lineweight="' + lineweight + '" linetype="' + linetype + '" filled="' + filled + '">\
               <circle center ="' + pt0.toString() + '" radius ="' + radius.toString() + '"/>\
          </graphics>\
      </drawable>        ';
    return drawable;
}

function addCircleTransient() {

    function onCompleteFirst(args) {

        var resObj = JSON.parse(args);
        if (resObj) {
            pt0[0] = resObj.value.x;
            pt0[1] = resObj.value.y;
            pt0[2] = resObj.value.z;

            var optionsSecond = new Acad.PromptPointOptions('Pick point on circle');
            optionsSecond.useBasePoint = true;
            optionsSecond.basePoint = new Acad.Point3d(resObj.value.x, resObj.value.y, resObj.value.z);
            Acad.Editor.getPoint(optionsSecond).then(onCompleteSecond, onError);
        }
    }

    function onCompleteSecond(args) {

        var resObj = JSON.parse(args);
        if (resObj) {
            pt2[0] = resObj.value.x;
            pt2[1] = resObj.value.y;
            pt2[2] = resObj.value.z;

            var drawable = createDrawableCircle();

            var transient1 = new Acad.Transient();

            var id = transient1.getId();
            transientIds.push(id);

            // Save some of the transient data in a map of drawables using the id as a key value.
            // This enables us to reset things like the correct corner points for updateTransient. 
            // The createDrawablePolyline()  method use the corner points.
            var drawData = new Object();
            drawData.pt0 = pt0.slice(0);  // copy the array
            drawData.pt2 = pt2.slice(0);
            drawables[id] = new Object();
            drawables[id].drawData = drawData;
            drawables[id].type = TransientType.Circle;


            transient1.addEventListener(transient1.eventname.lbuttondown, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.lbuttondblclk, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.lbuttonup, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mbuttondown, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mbuttondblclk, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mbuttonup, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.rbuttondown, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.rbuttondblclk, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.rbuttonup, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mouseleave, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mousemove, transientMouseEventHandler);
            transient1.addEventListener(transient1.eventname.mousewheel, transientMouseEventHandler);
            //transient1.addEventListener(transient1.eventname.mousehover, transientMouseEventHandler);

            Acad.Application.activedocument.transientManager.addTransient(transient1, drawable);
        }
    }

    function onError(args) {
        alert('Unable to create circle transient: ' + args);
    }

    var optionsFirst = new Acad.PromptPointOptions('Pick center point', new Acad.Point3d(0, 0, 0));
    Acad.Editor.getPoint(optionsFirst).then(onCompleteFirst,
                                        onError);
}


function updateSelectedTransient() {

    function onComplete(args) {

    }
    function onError(args) {
        alert('Unable to update transient: ' + args);
    }

    var id = parseInt(document.getElementById('SelectedID').value);

    if (typeof (drawables[id]) === "undefined") {
        alert('Invalid transient ID: ' + id);
        return;
    }
   
    if (drawables[id].type == TransientType.Rectangle) {
        // reset the correct points for createDrawablePolyline(). 
        pt0 = drawables[id].drawData.pt0.slice(0);
        pt2 = drawables[id].drawData.pt2.slice(0);
        var drawable = createDrawablePolyline();
        Acad.Application.activedocument.transientManager.updateTransient(id, drawable, onComplete, onError);
    }
    else if (drawables[id].type == TransientType.Image) {
        var bubbleType = document.getElementById('BubbleType').selectedIndex; // 0 == small, 1 == extended
        var bubbleID = document.getElementById('BubbleID').value;
        var postedBy = document.getElementById('BubblePostedBy').value;
        var message = document.getElementById('BubbleMessage').value;
        var drawingFeed = new Acad.DrawingFeedPrivate();
        transient_location = drawables[id].drawData.pt0.slice(0);

        encoded_image = drawingFeed.generateImage(bubbleType, bubbleID, postedBy, message);

        var drawable = createDrawableImage();
        Acad.Application.activedocument.transientManager.updateTransient(id, drawable, onComplete, onError);
    }
    else if (drawables[id].type == TransientType.Circle) {
        // reset the correct points for createDrawableCircle(). 
        pt0 = drawables[id].drawData.pt0.slice(0);
        pt2 = drawables[id].drawData.pt2.slice(0);
        var drawable = createDrawableCircle();
        Acad.Application.activedocument.transientManager.updateTransient(id, drawable, onComplete, onError);
    }
}

function hideTransients() {

    function onComplete(args) {

        
    }
    function onError(args) {
        alert('Invalid transient Id(s) found: ' + args);
    }

    Acad.Application.activedocument.transientManager.showTransients(transientIds, false, onComplete, onError);
}

function showTransients() {

    function onComplete(args) {
    }
    function onError(args) {
        alert('Invalid transient Id(s) found: ' + args);
    }

    Acad.Application.activedocument.transientManager.showTransients(transientIds, true, onComplete, onError);
}

function eraseSelectedTransient() {

    var id = parseInt(document.getElementById('SelectedID').value);

    function onComplete(args) {
        document.getElementById('SelectedID').value = '<none>';
        
        // delete transient from array
        for (var i=0;i<transientIds.length;i++){
            if(id == transientIds[i])
                transientIds.splice(i,1);
        }
    }
    function onError(args) {
        alert('Unable to delete transient: ' + args);
    }

    Acad.Application.activedocument.transientManager.eraseTransient(id, onComplete, onError); 
}

function eraseTransients() {
    function onComplete(args) {
        // delete all transients from array
        for (var i=0;i<transientIds.length;i++)
            transientIds.splice(0,1);
    }
    function onError(args) {
        alert('Unable to delete transients: ' + args);
    }

    Acad.Application.activedocument.transientManager.eraseTransients(transientIds, onComplete, onError);
}

function getCursor() {

    function onComplete(args) {
        var resObj = JSON.parse(args);
        if (resObj) {
            alert('Transient cursor: ' + resObj.cursor)
        }
       
    }
    function onError(args) {
        alert('Unable to get cursor: ' + args);
    }

    var id = parseInt(document.getElementById('SelectedID').value);

    Acad.Application.activedocument.transientManager.getCursor(id, onComplete, onError);    
}