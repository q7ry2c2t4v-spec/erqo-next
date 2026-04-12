# SkyMesh

> Source: https://threejs.org/docs/pages/SkyMesh.html
> Category: Addons

[EventDispatcher](EventDispatcher.html) → [Object3D](Object3D.html) → [Mesh](Mesh.html) → 

# SkyMesh

Represents a skydome for scene backgrounds. Based on [A Practical Analytic Model for Daylight](https://www.researchgate.net/publication/220720443_A_Practical_Analytic_Model_for_Daylight) aka The Preetham Model, the de facto standard for analytical skydomes.

Note that this class can only be used with [WebGPURenderer](WebGPURenderer.html). When using [WebGLRenderer](WebGLRenderer.html), use [Sky](Sky.html).

More references:

  * <http://simonwallner.at/project/atmospheric-scattering/>
  * <http://blenderartists.org/forum/showthread.php?245954-preethams-sky-impementation-HDR>

## Code Example
    
    
    const sky = new SkyMesh();
    sky.scale.setScalar( 10000 );
    scene.add( sky );
    

## Import

SkyMesh is an addon, and must be imported explicitly, see [Installation#Addons](https://threejs.org/manual/#en/installation).
    
    
    import { SkyMesh } from 'three/addons/objects/SkyMesh.js';

## Constructor

### new SkyMesh()

Constructs a new skydome.

## Properties

### .cloudCoverage : [UniformNode](UniformNode.html).<float>

The cloud coverage uniform.

### .cloudDensity : [UniformNode](UniformNode.html).<float>

The cloud density uniform.

### .cloudElevation : [UniformNode](UniformNode.html).<float>

The cloud elevation uniform.

### .cloudScale : [UniformNode](UniformNode.html).<float>

The cloud scale uniform.

### .cloudSpeed : [UniformNode](UniformNode.html).<float>

The cloud speed uniform.

### .isSky : boolean (readonly) 

This flag can be used for type testing.

Default is `true`.

**Deprecated:** Use isSkyMesh instead.

### .isSkyMesh : boolean (readonly) 

This flag can be used for type testing.

Default is `true`.

### .mieCoefficient : [UniformNode](UniformNode.html).<float>

The mieCoefficient uniform.

### .mieDirectionalG : [UniformNode](UniformNode.html).<float>

The mieDirectionalG uniform.

### .rayleigh : [UniformNode](UniformNode.html).<float>

The rayleigh uniform.

### .sunPosition : [UniformNode](UniformNode.html).<vec3>

The sun position uniform.

### .turbidity : [UniformNode](UniformNode.html).<float>

The turbidity uniform.

### .upUniform : [UniformNode](UniformNode.html).<vec3>

The up position.

## Source

[examples/jsm/objects/SkyMesh.js](https://github.com/mrdoob/three.js/blob/master/examples/jsm/objects/SkyMesh.js)
