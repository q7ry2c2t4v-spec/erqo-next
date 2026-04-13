# KTXLoader

> Source: https://threejs.org/docs/pages/KTXLoader.html
> Category: Addons

[Loader](Loader.html) → [CompressedTextureLoader](CompressedTextureLoader.html) → 

# KTXLoader

A loader for the KTX texture compression format.

References:

  * [The KTX File Format and Tools](https://www.khronos.org/opengles/sdk/tools/KTX/)
  * [Babylon.JS khronosTextureContainer.ts](https://github.com/BabylonJS/Babylon.js/blob/master/src/Misc/khronosTextureContainer.ts)

## Code Example
    
    
    const loader = new KTXLoader();
    const map = loader.load( 'textures/compressed/lensflare_ASTC8x8.ktx' )
    map.colorSpace = THREE.SRGBColorSpace; // only for color textures
    

## Import

KTXLoader is an addon, and must be imported explicitly, see [Installation#Addons](https://threejs.org/manual/#en/installation).
    
    
    import { KTXLoader } from 'three/addons/loaders/KTXLoader.js';

## Constructor

### new KTXLoader( manager : [LoadingManager](LoadingManager.html) )

Constructs a new KTX loader.

**manager** |  The loading manager.  
---|---  
  
## Methods

### .parse( buffer : ArrayBuffer, loadMipmaps : boolean ) : [CompressedTextureLoader~TexData](CompressedTextureLoader.html#~TexData)

Parses the given KTX texture data.

**buffer** |  The raw texture data.  
---|---  
**loadMipmaps** |  Whether to load mipmaps or not.  
  
**Overrides:** [CompressedTextureLoader#parse](CompressedTextureLoader.html#parse)

**Returns:** An object representing the parsed texture data.

## Source

[examples/jsm/loaders/KTXLoader.js](https://github.com/mrdoob/three.js/blob/master/examples/jsm/loaders/KTXLoader.js)
