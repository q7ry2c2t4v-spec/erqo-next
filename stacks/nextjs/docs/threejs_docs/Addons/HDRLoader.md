# HDRLoader

> Source: https://threejs.org/docs/pages/HDRLoader.html
> Category: Addons

[Loader](Loader.html) → [DataTextureLoader](DataTextureLoader.html) → 

# HDRLoader

A loader for the RGBE HDR texture format.

## Code Example
    
    
    const loader = new HDRLoader();
    const envMap = await loader.loadAsync( 'textures/equirectangular/blouberg_sunrise_2_1k.hdr' );
    envMap.mapping = THREE.EquirectangularReflectionMapping;
    scene.environment = envMap;
    

## Import

HDRLoader is an addon, and must be imported explicitly, see [Installation#Addons](https://threejs.org/manual/#en/installation).
    
    
    import { HDRLoader } from 'three/addons/loaders/HDRLoader.js';

## Constructor

### new HDRLoader( manager : [LoadingManager](LoadingManager.html) )

Constructs a new RGBE/HDR loader.

**manager** |  The loading manager.  
---|---  
  
## Properties

### .type : [HalfFloatType](global.html#HalfFloatType) | [FloatType](global.html#FloatType)

The texture type.

Default is `HalfFloatType`.

## Methods

### .parse( buffer : ArrayBuffer ) : [DataTextureLoader~TexData](DataTextureLoader.html#~TexData)

Parses the given RGBE texture data.

**buffer** |  The raw texture data.  
---|---  
  
**Overrides:** [DataTextureLoader#parse](DataTextureLoader.html#parse)

**Returns:** An object representing the parsed texture data.

### .setDataType( value : [HalfFloatType](global.html#HalfFloatType) | [FloatType](global.html#FloatType) ) : [HDRLoader](HDRLoader.html)

Sets the texture type.

**value** |  The texture type to set.  
---|---  
  
**Returns:** A reference to this loader.

## Source

[examples/jsm/loaders/HDRLoader.js](https://github.com/mrdoob/three.js/blob/master/examples/jsm/loaders/HDRLoader.js)
