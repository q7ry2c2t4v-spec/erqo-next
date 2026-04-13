# SelectionBox

> Source: https://threejs.org/docs/pages/SelectionBox.html
> Category: Addons

# SelectionBox

This class can be used to select 3D objects in a scene with a selection box. It is recommended to visualize the selected area with the help of [SelectionHelper](SelectionHelper.html).

## Code Example
    
    
    const selectionBox = new SelectionBox( camera, scene );
    const selectedObjects = selectionBox.select( startPoint, endPoint );
    

## Import

SelectionBox is an addon, and must be imported explicitly, see [Installation#Addons](https://threejs.org/manual/#en/installation).
    
    
    import { SelectionBox } from 'three/addons/interactive/SelectionBox.js';

## Constructor

### new SelectionBox( camera : [Camera](Camera.html), scene : [Scene](Scene.html), deep : number )

Constructs a new selection box.

**camera** |  The camera the scene is rendered with.  
---|---  
**scene** |  The scene.  
**deep** |  How deep the selection frustum of perspective cameras should extend. Default is `Number.MAX_VALUE`.  
  
## Properties

### .batches : Object

The selected batches of batched meshes.

### .camera : [Camera](Camera.html)

The camera the scene is rendered with.

### .collection : Array.<[Object3D](Object3D.html)>

The selected 3D objects.

### .deep : number

How deep the selection frustum of perspective cameras should extend.

Default is `Number.MAX_VALUE`.

### .endPoint : [Vector3](Vector3.html)

The end point of the selection.

### .instances : Object

The selected instance IDs of instanced meshes.

### .scene : [Scene](Scene.html)

The camera the scene is rendered with.

### .startPoint : [Vector3](Vector3.html)

The start point of the selection.

## Methods

### .select( startPoint : [Vector3](Vector3.html), endPoint : [Vector3](Vector3.html) ) : Array.<[Object3D](Object3D.html)>

This method selects 3D objects in the scene based on the given start and end point. If no parameters are provided, the method uses the start and end values of the respective members.

**startPoint** |  The start point.  
---|---  
**endPoint** |  The end point.  
  
**Returns:** The selected 3D objects.

## Source

[examples/jsm/interactive/SelectionBox.js](https://github.com/mrdoob/three.js/blob/master/examples/jsm/interactive/SelectionBox.js)
