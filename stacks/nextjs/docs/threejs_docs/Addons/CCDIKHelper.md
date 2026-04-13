# CCDIKHelper

> Source: https://threejs.org/docs/pages/CCDIKHelper.html
> Category: Addons

[EventDispatcher](EventDispatcher.html) → [Object3D](Object3D.html) → 

# CCDIKHelper

Helper for visualizing IK bones.

## Import

CCDIKHelper is an addon, and must be imported explicitly, see [Installation#Addons](https://threejs.org/manual/#en/installation).
    
    
    import { CCDIKHelper } from 'three/addons/animation/CCDIKSolver.js';

## Constructor

### new CCDIKHelper( mesh : [SkinnedMesh](SkinnedMesh.html), iks : Array.<[CCDIKSolver~IK](CCDIKSolver.html#~IK)>, sphereSize : number )

**mesh** |  The skinned mesh.  
---|---  
**iks** |  The IK objects. Default is `[]`.  
**sphereSize** |  The sphere size. Default is `0.25`.  
  
## Properties

### .effectorSphereMaterial : [MeshBasicMaterial](MeshBasicMaterial.html)

The material for the effector spheres.

### .iks : Array.<[CCDIKSolver~IK](CCDIKSolver.html#~IK)>

The IK objects.

### .lineMaterial : [LineBasicMaterial](LineBasicMaterial.html)

A global line material.

### .linkSphereMaterial : [MeshBasicMaterial](MeshBasicMaterial.html)

The material for the link spheres.

### .root : [SkinnedMesh](SkinnedMesh.html)

The skinned mesh this helper refers to.

### .sphereGeometry : [SphereGeometry](SphereGeometry.html)

The helpers sphere geometry.

### .targetSphereMaterial : [MeshBasicMaterial](MeshBasicMaterial.html)

The material for the target spheres.

## Methods

### .dispose()

Frees the GPU-related resources allocated by this instance. Call this method whenever this instance is no longer used in your app.

## Source

[examples/jsm/animation/CCDIKSolver.js](https://github.com/mrdoob/three.js/blob/master/examples/jsm/animation/CCDIKSolver.js)
