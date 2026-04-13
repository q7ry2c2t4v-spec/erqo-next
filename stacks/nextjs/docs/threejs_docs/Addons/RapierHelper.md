# RapierHelper

> Source: https://threejs.org/docs/pages/RapierHelper.html
> Category: Addons

[EventDispatcher](EventDispatcher.html) → [Object3D](Object3D.html) → [Line](Line.html) → [LineSegments](LineSegments.html) → 

# RapierHelper

This class displays all Rapier Colliders in outline.

## Import

RapierHelper is an addon, and must be imported explicitly, see [Installation#Addons](https://threejs.org/manual/#en/installation).
    
    
    import { RapierHelper } from 'three/addons/helpers/RapierHelper.js';

## Constructor

### new RapierHelper( world : RAPIER.world )

Constructs a new Rapier debug helper.

**world** |  The Rapier world to visualize.  
---|---  
  
## Properties

### .world : RAPIER.world

The Rapier world to visualize.

## Methods

### .dispose()

Frees the GPU-related resources allocated by this instance. Call this method whenever this instance is no longer used in your app.

### .update()

Call this in the render loop to update the outlines.

## Source

[examples/jsm/helpers/RapierHelper.js](https://github.com/mrdoob/three.js/blob/master/examples/jsm/helpers/RapierHelper.js)
