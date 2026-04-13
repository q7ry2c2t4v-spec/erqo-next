# OctreeHelper

> Source: https://threejs.org/docs/pages/OctreeHelper.html
> Category: Addons

[EventDispatcher](EventDispatcher.html) → [Object3D](Object3D.html) → [Line](Line.html) → [LineSegments](LineSegments.html) → 

# OctreeHelper

A helper for visualizing an Octree.

## Code Example
    
    
    const helper = new OctreeHelper( octree );
    scene.add( helper );
    

## Import

OctreeHelper is an addon, and must be imported explicitly, see [Installation#Addons](https://threejs.org/manual/#en/installation).
    
    
    import { OctreeHelper } from 'three/addons/helpers/OctreeHelper.js';

## Constructor

### new OctreeHelper( octree : [Octree](Octree.html), color : number | [Color](Color.html) | string )

Constructs a new Octree helper.

**octree** |  The octree to visualize.  
---|---  
**color** |  The helper's color. Default is `0xffff00`.  
  
## Properties

### .color : number | [Color](Color.html) | string

The helper's color.

### .octree : [Octree](Octree.html)

The octree to visualize.

## Methods

### .dispose()

Frees the GPU-related resources allocated by this instance. Call this method whenever this instance is no longer used in your app.

### .update()

Updates the helper. This method must be called whenever the Octree's structure is changed.

## Source

[examples/jsm/helpers/OctreeHelper.js](https://github.com/mrdoob/three.js/blob/master/examples/jsm/helpers/OctreeHelper.js)
