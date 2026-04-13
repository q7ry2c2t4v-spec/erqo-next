# FXAAPass

> Source: https://threejs.org/docs/pages/FXAAPass.html
> Category: Addons

[Pass](Pass.html) → [ShaderPass](ShaderPass.html) → 

# FXAAPass

A pass for applying FXAA.

## Code Example
    
    
    const fxaaPass = new FXAAPass();
    composer.addPass( fxaaPass );
    

## Import

FXAAPass is an addon, and must be imported explicitly, see [Installation#Addons](https://threejs.org/manual/#en/installation).
    
    
    import { FXAAPass } from 'three/addons/postprocessing/FXAAPass.js';

## Constructor

### new FXAAPass()

Constructs a new FXAA pass.

## Methods

### .setSize( width : number, height : number )

Sets the size of the pass.

**width** |  The width to set.  
---|---  
**height** |  The height to set.  
  
**Overrides:** [ShaderPass#setSize](ShaderPass.html#setSize)

## Source

[examples/jsm/postprocessing/FXAAPass.js](https://github.com/mrdoob/three.js/blob/master/examples/jsm/postprocessing/FXAAPass.js)
