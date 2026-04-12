# InteractiveGroup

> Source: https://threejs.org/docs/pages/InteractiveGroup.html
> Category: Addons

[EventDispatcher](EventDispatcher.html) → [Object3D](Object3D.html) → [Group](Group.html) → 

# InteractiveGroup

This class can be used to group 3D objects in an interactive group. The group itself can listen to Pointer, Mouse or XR controller events to detect selections of descendant 3D objects. If a 3D object is selected, the respective event is going to dispatched to it.

## Code Example
    
    
    const group = new InteractiveGroup();
    group.listenToPointerEvents( renderer, camera );
    group.listenToXRControllerEvents( controller1 );
    group.listenToXRControllerEvents( controller2 );
    scene.add( group );
    // now add objects that should be interactive
    group.add( mesh1, mesh2, mesh3 );
    

## Import

InteractiveGroup is an addon, and must be imported explicitly, see [Installation#Addons](https://threejs.org/manual/#en/installation).
    
    
    import { InteractiveGroup } from 'three/addons/interactive/InteractiveGroup.js';

## Constructor

### new InteractiveGroup()

## Properties

### .camera : [Camera](Camera.html)

The camera used for raycasting.

Default is `null`.

### .controllers : Array.<[Group](Group.html)>

An array of XR controllers.

### .element : HTMLElement

The internal raycaster.

Default is `null`.

### .raycaster : [Raycaster](Raycaster.html)

The internal raycaster.

## Methods

### .disconnect()

Disconnects this interactive group from the DOM and all XR controllers.

### .disconnectXrControllerEvents()

Disconnects this interactive group from all XR controllers.

### .disconnectionPointerEvents()

Disconnects this interactive group from all Pointer and Mouse Events.

### .listenToPointerEvents( renderer : [WebGPURenderer](WebGPURenderer.html) | [WebGLRenderer](WebGLRenderer.html), camera : [Camera](Camera.html) )

Calling this method makes sure the interactive group listens to Pointer and Mouse events. The target is the `domElement` of the given renderer. The camera is required for the internal raycasting so 3D objects can be detected based on the events.

**renderer** |  The renderer.  
---|---  
**camera** |  The camera.  
  
### .listenToXRControllerEvents( controller : [Group](Group.html) )

Calling this method makes sure the interactive group listens to events of the given XR controller.

**controller** |  The XR controller.  
---|---  
  
## Source

[examples/jsm/interactive/InteractiveGroup.js](https://github.com/mrdoob/three.js/blob/master/examples/jsm/interactive/InteractiveGroup.js)
