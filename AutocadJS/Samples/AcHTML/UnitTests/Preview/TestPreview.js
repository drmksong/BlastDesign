
function onCapturePreviewComplete(encodedimage) {

    var container = document.getElementById('imageContainer');
    var img = document.createElement('img');

    var src = "data:image/bmp;base64," + encodedimage;

    img.setAttribute('src', src);

    container.appendChild(img);
    var br = document.createElement('hr');
    container.appendChild(br);
}

function onCapturePreviewError(args) {
    alert('Unable to create preview: '  + args);
}

function capturePreview() {
    try{
        
        var width = parseInt(document.getElementById('Width').value);
        var height = parseInt(document.getElementById('Height').value);

        Acad.Application.activedocument.capturePreview(width, height).then(
            onCapturePreviewComplete, 
            onCapturePreviewError);
            
    } catch (err) {
        alert(err.message);
    }
}

