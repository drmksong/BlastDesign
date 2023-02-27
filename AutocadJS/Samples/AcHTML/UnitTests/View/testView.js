

function testCaptureView() {
    try {        
    
        var layoutSnapshot = document.getElementById('layerSnapshot').checked == 1 ? true : false;
        var obj = Acad.Editor.captureView(layoutSnapshot);
        
        document.getElementById('capturedRestoreViewId').value = obj;
        
    }catch(e){
        alert(': error test_Editor_captureView failed with error ' + e.message);
    }
}

function testRestoreView() {
    try{
    
        var id = document.getElementById('capturedRestoreViewId').value;
        Acad.Editor.restoreView(id);  
          
    }catch(e){
        alert(': error test_Editor_restoreView failed with error ' + e.message);
    }
}


function clearView(){
        document.getElementById('p.x').value = '';
        document.getElementById('p.y').value = '';
        document.getElementById('p.z').value = '';
        document.getElementById('t.x').value = '';
        document.getElementById('t.y').value = '';
        document.getElementById('t.z').value = '';
        document.getElementById('u.x').value = '';
        document.getElementById('u.y').value = '';
        document.getElementById('u.z').value = '';
        document.getElementById('fh').value = '';
        document.getElementById('fw').value = '';
        document.getElementById('proj').value = '';
}

function getView(){

        var obj = Acad.Editor.CurrentViewport.getViewProperties();
        
        document.getElementById('p.x').value = obj.position.x;
        document.getElementById('p.y').value = obj.position.y;
        document.getElementById('p.z').value = obj.position.z;
        
        document.getElementById('t.x').value = obj.target.x;
        document.getElementById('t.y').value = obj.target.y;
        document.getElementById('t.z').value = obj.target.z;
        
        document.getElementById('u.x').value = obj.upVector.x;
        document.getElementById('u.y').value = obj.upVector.y;
        document.getElementById('u.z').value = obj.upVector.z;
        
        document.getElementById('fh').value = obj.fieldHeight;
        document.getElementById('fw').value = obj.fieldWidth;
        
        document.getElementById('proj').value = obj.projection;
}

function setView(){   
 
    var animate = document.getElementById('animate').checked==1 ? true: false;
    
    Acad.Editor.CurrentViewport.setView(
        new Acad.Point3d(document.getElementById('p.x').value, document.getElementById('p.y').value, document.getElementById('p.z').value),
        new Acad.Point3d(document.getElementById('t.x').value, document.getElementById('t.y').value, document.getElementById('t.z').value), 
        new Acad.Vector3d(document.getElementById('u.x').value, document.getElementById('u.y').value, document.getElementById('u.z').value), 
        document.getElementById('fw').value,
        document.getElementById('fh').value,
        document.getElementById('proj').value,
        animate);
}

function roll(){
    var angle = document.getElementById('rollAngle').value;
    var animateF = document.getElementById('animate').checked==1 ? true: false;
    try
    {
        getView();
        var p1 = parseFloat(document.getElementById('p.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('p.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('p.z').value).toFixed(6);
        var t1 = parseFloat(document.getElementById('t.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('t.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('t.z').value).toFixed(6);
        var u1 = parseFloat(document.getElementById('u.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('u.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('u.z').value).toFixed(6);
        var h1 = parseFloat(document.getElementById('fh').value).toFixed(6);
        var w1 = parseFloat(document.getElementById('fw').value).toFixed(6);
        Acad.Editor.CurrentViewport.roll(parseFloat(angle),animateF);
        getView();
        var p2 = parseFloat(document.getElementById('p.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('p.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('p.z').value).toFixed(6);
        var t2 = parseFloat(document.getElementById('t.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('t.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('t.z').value).toFixed(6);
        var u2 = parseFloat(document.getElementById('u.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('u.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('u.z').value).toFixed(6);
        var h2 = parseFloat(document.getElementById('fh').value).toFixed(6);
        var w2 = parseFloat(document.getElementById('fw').value).toFixed(6);
        if(p1!=p2) alert('Position changed after roll before roll=('+p1+') after roll= ('+p2+')');
        if(t1!=t2) alert('Target changed after roll before roll=('+t1+') after roll= ('+t2+')');
        if(u1!=u2) alert('Upvector changed after roll before roll=('+u1+') after roll= ('+u2+')');
        if(h1!=h2) alert('height changed after roll before roll=('+h1+') after roll= ('+h2+')');
        if(w1!=w2) alert('width changed after roll before roll=('+w1+') after roll= ('+w2+')');
    }catch(e){
        alert(e.message);
    }
}


function orbit(){
    var angleX = document.getElementById('angleXOrbit').value;
    var angleY = document.getElementById('angleYOrbit').value;
    var animateF = document.getElementById('animate').checked==1 ? true: false;
    try
    {
        getView();
        var p1 = parseFloat(document.getElementById('p.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('p.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('p.z').value).toFixed(6);
        var t1 = parseFloat(document.getElementById('t.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('t.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('t.z').value).toFixed(6);
        var u1 = parseFloat(document.getElementById('u.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('u.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('u.z').value).toFixed(6);
        var h1 = parseFloat(document.getElementById('fh').value).toFixed(6);
        var w1 = parseFloat(document.getElementById('fw').value).toFixed(6);
        Acad.Editor.CurrentViewport.orbit(parseFloat(angleX),parseFloat(angleY),animateF);
        getView();
        var p2 = parseFloat(document.getElementById('p.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('p.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('p.z').value).toFixed(6);
        var t2 = parseFloat(document.getElementById('t.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('t.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('t.z').value).toFixed(6);
        var u2 = parseFloat(document.getElementById('u.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('u.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('u.z').value).toFixed(6);
        var h2 = parseFloat(document.getElementById('fh').value).toFixed(6);
        var w2 = parseFloat(document.getElementById('fw').value).toFixed(6);
        if(p1!=p2) alert('Position changed after orbit before roll=('+p1+') after orbit= ('+p2+')');
        if(t1!=t2) alert('Target changed after orbit before roll=('+t1+') after orbit= ('+t2+')');
        if(u1!=u2) alert('Upvector changed after orbit before roll=('+u1+') after orbit= ('+u2+')');
        if(h1!=h2) alert('height changed after orbit before roll=('+h1+') after orbit= ('+h2+')');
        if(w1!=w2) alert('width changed after orbit before roll=('+w1+') after orbit= ('+w2+')');
    }catch(e){
        alert(e.message);
    }
}

function pan(){
    var angleX = document.getElementById('angleXPan').value;
    var angleY = document.getElementById('angleYPan').value;
    var animateF = document.getElementById('animate').checked==1 ? true: false;
    try
    {
        getView();
        var p1 = parseFloat(document.getElementById('p.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('p.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('p.z').value).toFixed(6);
        var t1 = parseFloat(document.getElementById('t.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('t.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('t.z').value).toFixed(6);
        var u1 = parseFloat(document.getElementById('u.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('u.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('u.z').value).toFixed(6);
        var h1 = parseFloat(document.getElementById('fh').value).toFixed(6);
        var w1 = parseFloat(document.getElementById('fw').value).toFixed(6);
        Acad.Editor.CurrentViewport.pan(parseFloat(angleX),parseFloat(angleY),animateF);
        getView();
        var p2 = parseFloat(document.getElementById('p.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('p.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('p.z').value).toFixed(6);
        var t2 = parseFloat(document.getElementById('t.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('t.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('t.z').value).toFixed(6);
        var u2 = parseFloat(document.getElementById('u.x').value).toFixed(6) + ","+ parseFloat(document.getElementById('u.y').value).toFixed(6) + ","+ parseFloat(document.getElementById('u.z').value).toFixed(6);
        var h2 = parseFloat(document.getElementById('fh').value).toFixed(6);
        var w2 = parseFloat(document.getElementById('fw').value).toFixed(6);
        if(p1!=p2) alert('Position changed after pan before pan=('+p1+') after pan= ('+p2+')');
        if(t1!=t2) alert('Target changed after pan before pan=('+t1+') after pan= ('+t2+')');
        if(u1!=u2) alert('Upvector changed after pan before pan=('+u1+') after pan= ('+u2+')');
        if(h1!=h2) alert('height changed after pan before pan=('+h1+') after pan= ('+h2+')');
        if(w1!=w2) alert('width changed after pan before pan=('+w1+') after pan= ('+w2+')');
    }catch(e){
        alert(e.message);
    }
}


function zoomExtents() {
    try{
    var animateF = document.getElementById('animate').checked==1 ? true: false;
    getView();
    alert('Zoom Simple');
    Acad.Editor.CurrentViewport.zoomExtents(new Acad.Point3d(0,0,0),new Acad.Point3d(4.3,4.1,0), animateF);
    getView();
    alert('Zoom Large');
    Acad.Editor.CurrentViewport.zoomExtents(new Acad.Point3d(1200,400,0), new Acad.Point3d(1500,600,500),animateF);
    getView();
    alert('Zoom small min Large');
    Acad.Editor.CurrentViewport.zoomExtents(new Acad.Point3d(0.5,3,0),new Acad.Point3d(1200,4001,0), animateF);
    getView();
    alert('Zoom small boundary');
    Acad.Editor.CurrentViewport.zoomExtents(new Acad.Point3d(0.5,3,0),new Acad.Point3d(0.5,3.1,0.2), animateF);
    getView();
    alert('Zoom same boundary');
    Acad.Editor.CurrentViewport.zoomExtents(new Acad.Point3d(10,10,10),new Acad.Point3d(10,10,10), animateF);
    getView();
    }catch(e){
        alert('zoomExtents failed with error '+e.message);
    }
}

function zoom() {
    var animateF = document.getElementById('animate').checked==1 ? true: false;
    try{
        getView();
        alert('Zoom factor > 1');
        Acad.Editor.CurrentViewport.zoom(2, animateF);
        getView();
        alert('Zoom factor < 1');
        Acad.Editor.CurrentViewport.zoom(0.5, animateF);
        getView();
        alert('Zoom factor = 1000');
        Acad.Editor.CurrentViewport.zoom(100000, animateF);
        getView();
        alert('Zoom factor = 0');
        Acad.Editor.CurrentViewport.zoom(0.002, animateF);
        
    }catch(e){
        alert('zoom failed with error '+e.message);
    }
}

var pt1;
var pt2;

function zoomWindow(){   
    var animateF = document.getElementById('animate').checked==1 ? true: false;
    //var pt1, pt2;
    var options = new Acad.PromptPointOptions('Select point 1');
    Acad.Editor.getPoint(options).then(onCompletePromptPointResult,onErrorPromptPointResult);
    //Acad.Editor.CurrentViewport.zoomWindow(new Acad.Point2d(0,0), new Acad.Point2d(100,100), animateF);

}


function onErrorPromptPointResult(jsonPromptResult) {
    alert('error');
}
function onCompletePromptPointResult(jsonPromptResult) {
    var resObj = JSON.parse(jsonPromptResult);
    pt1 = resObj.value;
    var options = new Acad.PromptPointOptions('Select point 2');
    Acad.Editor.getPoint(options).then(onCompletePromptPointResult1,onErrorPromptPointResult);
}

function onCompletePromptPointResult1(jsonPromptResult) {
    var animateF = document.getElementById('animate').checked==1 ? true: false;
    var resObj = JSON.parse(jsonPromptResult);
    pt2 = resObj.value;
    
    pt1 = Acad.Editor.CurrentViewport.pointToScreen(new Acad.Point3d(pt1.x,pt1.y,pt1.z));    
    pt2 = Acad.Editor.CurrentViewport.pointToScreen(new Acad.Point3d(pt2.x,pt2.y,pt2.z));

    var pt3 = Acad.Editor.CurrentViewport.getViewport();

    try{
        getView();
        Acad.Editor.CurrentViewport.zoomWindow(new Acad.Point2d(pt1.x,(pt3.upperRight.y-pt3.lowerLeft.y-pt1.y)), new Acad.Point2d(pt2.x,(pt3.upperRight.y-pt3.lowerLeft.y-pt2.y)), animateF);
        getView();
    }catch(e){
        alert('zoomeindow failed with error '+e.message);
    }
}

function pointToScreen() {
    var options = new Acad.PromptPointOptions('Select a point');
    Acad.Editor.getPoint(options).then(onCompletePromptPointResult2,onErrorPromptPointResult);
}

function pointToWorld(){
	try{
		var x = document.getElementById('pixelX').value;
		var y = document.getElementById('pixelY').value;
		var obj = Acad.Editor.CurrentViewport.pointToWorld(new Acad.Point2d(parseInt(x),parseInt(y)));
	    document.getElementById('worldX').value = obj.x;
		document.getElementById('worldY').value = obj.y;
		document.getElementById('worldZ').value = obj.z;
	}catch(e){
        alert('pointToWorld failed with error '+e.message);
    }
}

function getViewport() {

    var obj = Acad.Editor.CurrentViewport.getViewport();
    
    document.getElementById('viewportmin').value = obj.lowerLeft.x +','+ obj.lowerLeft.y;
    document.getElementById('viewportmax').value = obj.upperRight.x +','+ obj.upperRight.y;
    
}


function onCompletePromptPointResult2(jsonPromptResult) {
    var resObj = JSON.parse(jsonPromptResult);
    var pt2 = resObj.value;
    var obj = Acad.Editor.CurrentViewport.pointToScreen(new Acad.Point3d(pt2.x,pt2.y,pt2.z));
    document.getElementById('pixelX').value = obj.x;
    document.getElementById('pixelY').value = obj.y;
}



