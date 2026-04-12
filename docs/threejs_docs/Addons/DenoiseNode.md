# DenoiseNode

> Source: https://threejs.org/docs/pages/DenoiseNode.html
> Category: Addons

[EventDispatcher](EventDispatcher.html) → [Node](Node.html) → [TempNode](TempNode.html) → 

# DenoiseNode

Post processing node for denoising data like raw screen-space ambient occlusion output. Denoise can noticeably improve the quality of ambient occlusion but also add quite some overhead to the post processing setup. It's best to make its usage optional (e.g. via graphic settings).

Reference: <https://openaccess.thecvf.com/content/WACV2021/papers/Khademi_Self-Supervised_Poisson-Gaussian_Denoising_WACV_2021_paper.pdf>.

## Import

DenoiseNode is an addon, and must be imported explicitly, see [Installation#Addons](https://threejs.org/manual/#en/installation).
    
    
    import { denoise } from 'three/addons/tsl/display/DenoiseNode.js';

## Constructor

### new DenoiseNode( textureNode : [TextureNode](TextureNode.html), depthNode : [Node](Node.html).<float>, normalNode : [Node](Node.html).<vec3>, camera : [Camera](Camera.html) )

Constructs a new denoise node.

**textureNode** |  The texture node that represents the input of the effect (e.g. AO).  
---|---  
**depthNode** |  A node that represents the scene's depth.  
**normalNode** |  A node that represents the scene's normals.  
**camera** |  The camera the scene is rendered with.  
  
## Properties

### .depthNode : [Node](Node.html).<float>

A node that represents the scene's depth.

### .depthPhi : [UniformNode](UniformNode.html).<float>

The depth Phi value.

### .index : [UniformNode](UniformNode.html).<float>

The index.

### .lumaPhi : [UniformNode](UniformNode.html).<float>

The luma Phi value.

### .noiseNode : [TextureNode](TextureNode.html)

The node represents the internal noise texture.

### .normalNode : [Node](Node.html).<vec3>

A node that represents the scene's normals. If no normals are passed to the constructor (because MRT is not available), normals can be automatically reconstructed from depth values in the shader.

### .normalPhi : [UniformNode](UniformNode.html).<float>

The normal Phi value.

### .radius : [UniformNode](UniformNode.html).<float>

The radius.

### .textureNode : [TextureNode](TextureNode.html)

The texture node that represents the input of the effect (e.g. AO).

### .updateBeforeType : string

The `updateBeforeType` is set to `NodeUpdateType.FRAME` since the node updates its internal uniforms once per frame in `updateBefore()`.

Default is `'frame'`.

**Overrides:** [TempNode#updateBeforeType](TempNode.html#updateBeforeType)

## Methods

### .setup( builder : [NodeBuilder](NodeBuilder.html) ) : ShaderCallNodeInternal

This method is used to setup the effect's TSL code.

**builder** |  The current node builder.  
---|---  
  
**Overrides:** [TempNode#setup](TempNode.html#setup)

### .updateBefore( frame : [NodeFrame](NodeFrame.html) )

This method is used to update internal uniforms once per frame.

**frame** |  The current node frame.  
---|---  
  
**Overrides:** [TempNode#updateBefore](TempNode.html#updateBefore)

## Source

[examples/jsm/tsl/display/DenoiseNode.js](https://github.com/mrdoob/three.js/blob/master/examples/jsm/tsl/display/DenoiseNode.js)
