# Group

> Source: https://threejs.org/docs/pages/Group.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Object3D](Object3D.html) → 

# Group

This is almost identical to an [Object3D](Object3D.html). Its purpose is to make working with groups of objects syntactically clearer.

## Code Example
    
    
    // Create a group and add the two cubes.
    // These cubes can now be rotated / scaled etc as a group.
    const group = new THREE.Group();
    group.add( meshA );
    group.add( meshB );
    scene.add( group );
    

## Constructor

### new Group()

## Properties

### .isGroup : boolean (readonly) 

This flag can be used for type testing.

Default is `true`.

## Source

[src/objects/Group.js](https://github.com/mrdoob/three.js/blob/master/src/objects/Group.js)
