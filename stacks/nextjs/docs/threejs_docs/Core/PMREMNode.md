# PMREMNode

> Source: https://threejs.org/docs/pages/PMREMNode.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Node](Node.html) → [TempNode](TempNode.html) → 

# PMREMNode

This node represents a PMREM which is a special type of preprocessed environment map intended for PBR materials.

## Code Example
    
    
    const material = new MeshStandardNodeMaterial();
    material.envNode = pmremTexture( envMap );
    

## Constructor

### new PMREMNode( value : [Texture](Texture.html), uvNode : [Node](Node.html).<vec2>, levelNode : [Node](Node.html).<float> )

Constructs a new function overloading node.

**value** |  The input texture.  
---|---  
**uvNode** |  The uv node. Default is `null`.  
**levelNode** |  The level node. Default is `null`.  
  
## Properties

### .levelNode : [Node](Node.html).<float>

The level node.

### .updateBeforeType : string

The `updateBeforeType` is set to `NodeUpdateType.RENDER`.

Default is `'render'`.

**Overrides:** [TempNode#updateBeforeType](TempNode.html#updateBeforeType)

### .uvNode : [Node](Node.html).<vec2>

The uv node.

### .value : [Texture](Texture.html)

The node's texture value.

## Methods

### .updateFromTexture( texture : [Texture](Texture.html) )

Uses the given PMREM texture to update internal values.

**texture** |  The PMREM texture.  
---|---  
  
## Source

[src/nodes/pmrem/PMREMNode.js](https://github.com/mrdoob/three.js/blob/master/src/nodes/pmrem/PMREMNode.js)
