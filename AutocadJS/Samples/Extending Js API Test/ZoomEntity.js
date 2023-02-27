// Command to zoom to the extents of a selected entity

function zoomEntity() {
  try {
    
    // Set the options for our user prompt

    var peo = new Acad.PromptEntityOptions();
    peo.setMessageAndKeywords("\nSelect an entity", "");
    peo.allowObjectOnLockedLayer = true;

    // Ask the user to select an entity

    Acad.Editor.getEntity(peo).then(onComplete, onError);
  }
  catch(e) {
    write(e.message);
  }
}

function onComplete(jsonPromptResult) {
  try {
    
    // Parse the JSON string containing the prompt result

    var resultObj = JSON.parse(jsonPromptResult);
    if (resultObj && resultObj.status == 5100) {
      
      // If it was successful, get the selected entity...

      var entity = new Acad.DBEntity(resultObj.objectId);

      // ... and its extents

      var ext = entity.getExtents();

      // Zoom to the object's extents, choosing to animate the
      // view transition (if possible to do so)

      Acad.Editor.CurrentViewport.zoomExtents(
        ext.minPoint3d, ext.maxPoint3d, true
      );
    }
  }
  catch(e) {
    write(e.message);
  }
}

function onError(jsonPromptResult) {
  write("\nProblem encountered.");
}

// Add the command, we'll make it transparent

Acad.Editor.addCommand(
  "ZOOM_CMDS",
  "ZEN",
  "ZEN",
  Acad.CommandFlag.TRANSPARENT,
  zoomEntity
);

write("\nRegistered ZEN command.\n");