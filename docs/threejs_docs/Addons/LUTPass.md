# LUTPass

> Source: https://threejs.org/docs/pages/LUTPass.html
> Category: Addons

[Pass](Pass.html) → [ShaderPass](ShaderPass.html) → 

# LUTPass

Pass for color grading via lookup tables.

## Code Example
    
    
    const lutPass = new LUTPass( { lut: lut.texture3D } );
    composer.addPass( lutPass );
    

## Import

LUTPass is an addon, and must be imported explicitly, see [Installation#Addons](https://threejs.org/manual/#en/installation).
    
    
    import { LUTPass } from 'three/addons/postprocessing/LUTPass.js';

## Constructor

### new LUTPass( options : Object )

Constructs a LUT pass.

**options** |  The pass options. Default is `{}`.  
---|---  
  
## Properties

### .intensity : number

The intensity.

Default is `1`.

### .lut : [Data3DTexture](Data3DTexture.html)

The LUT as a 3D texture.

Default is `null`.

## Source

[examples/jsm/postprocessing/LUTPass.js](https://github.com/mrdoob/three.js/blob/master/examples/jsm/postprocessing/LUTPass.js)
