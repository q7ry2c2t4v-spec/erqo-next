# Sky

> Source: https://threejs.org/docs/pages/Sky.html
> Category: Addons

[EventDispatcher](EventDispatcher.html) → [Object3D](Object3D.html) → [Mesh](Mesh.html) → 

# Sky

Represents a skydome for scene backgrounds. Based on [A Practical Analytic Model for Daylight](https://www.researchgate.net/publication/220720443_A_Practical_Analytic_Model_for_Daylight) aka The Preetham Model, the de facto standard for analytical skydomes.

Note that this class can only be used with [WebGLRenderer](WebGLRenderer.html). When using [WebGPURenderer](WebGPURenderer.html), use [SkyMesh](SkyMesh.html).

More references:

  * <http://simonwallner.at/project/atmospheric-scattering/>
  * <http://blenderartists.org/forum/showthread.php?245954-preethams-sky-impementation-HDR>

## Code Example
    
    
    const sky = new Sky();
    sky.scale.setScalar( 10000 );
    scene.add( sky );
    

## Import

Sky is an addon, and must be imported explicitly, see [Installation#Addons](https://threejs.org/manual/#en/installation).
    
    
    import { Sky } from 'three/addons/objects/Sky.js';

## Constructor

### new Sky()

Constructs a new skydome.

## Properties

### .isSky : boolean (readonly) 

This flag can be used for type testing.

Default is `true`.

## Source

[examples/jsm/objects/Sky.js](https://github.com/mrdoob/three.js/blob/master/examples/jsm/objects/Sky.js)
