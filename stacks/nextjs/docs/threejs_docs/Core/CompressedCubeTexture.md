# CompressedCubeTexture

> Source: https://threejs.org/docs/pages/CompressedCubeTexture.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Texture](Texture.html) → [CompressedTexture](CompressedTexture.html) → 

# CompressedCubeTexture

Creates a cube texture based on data in compressed form.

These texture are usually loaded with [CompressedTextureLoader](CompressedTextureLoader.html).

## Constructor

### new CompressedCubeTexture( images : Array.<[CompressedTexture](CompressedTexture.html)>, format : number, type : number )

Constructs a new compressed texture.

**images** |  An array of compressed textures.  
---|---  
**format** |  The texture format. Default is `RGBAFormat`.  
**type** |  The texture type. Default is `UnsignedByteType`.  
  
## Properties

### .isCompressedCubeTexture : boolean (readonly) 

This flag can be used for type testing.

Default is `true`.

### .isCubeTexture : boolean (readonly) 

This flag can be used for type testing.

Default is `true`.

## Source

[src/textures/CompressedCubeTexture.js](https://github.com/mrdoob/three.js/blob/master/src/textures/CompressedCubeTexture.js)
