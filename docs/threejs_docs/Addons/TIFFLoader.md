# TIFFLoader

> Source: https://threejs.org/docs/pages/TIFFLoader.html
> Category: Addons

[Loader](Loader.html) → [DataTextureLoader](DataTextureLoader.html) → 

# TIFFLoader

A loader for the TIFF texture format.

## Code Example
    
    
    const loader = new TIFFLoader();
    const texture = await loader.loadAsync( 'textures/tiff/crate_lzw.tif' );
    texture.colorSpace = THREE.SRGBColorSpace;
    

## Import

TIFFLoader is an addon, and must be imported explicitly, see [Installation#Addons](https://threejs.org/manual/#en/installation).
    
    
    import { TIFFLoader } from 'three/addons/loaders/TIFFLoader.js';

## Constructor

### new TIFFLoader( manager : [LoadingManager](LoadingManager.html) )

Constructs a new TIFF loader.

**manager** |  The loading manager.  
---|---  
  
## Methods

### .parse( buffer : ArrayBuffer ) : [DataTextureLoader~TexData](DataTextureLoader.html#~TexData)

Parses the given TIFF texture data.

**buffer** |  The raw texture data.  
---|---  
  
**Overrides:** [DataTextureLoader#parse](DataTextureLoader.html#parse)

**Returns:** An object representing the parsed texture data.

## Source

[examples/jsm/loaders/TIFFLoader.js](https://github.com/mrdoob/three.js/blob/master/examples/jsm/loaders/TIFFLoader.js)
