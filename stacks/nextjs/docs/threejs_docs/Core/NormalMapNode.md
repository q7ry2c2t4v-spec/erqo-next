# NormalMapNode

> Source: https://threejs.org/docs/pages/NormalMapNode.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Node](Node.html) → [TempNode](TempNode.html) → 

# NormalMapNode

This class can be used for applying normals maps to materials.

## Code Example
    
    
    material.normalNode = normalMap( texture( normalTex ) );
    

## Constructor

### new NormalMapNode( node : [Node](Node.html).<vec3>, scaleNode : [Node](Node.html).<vec2> )

Constructs a new normal map node.

**node** |  Represents the normal map data.  
---|---  
**scaleNode** |  Controls the intensity of the effect. Default is `null`.  
  
## Properties

### .node : [Node](Node.html).<vec3>

Represents the normal map data.

### .normalMapType : [TangentSpaceNormalMap](global.html#TangentSpaceNormalMap) | [ObjectSpaceNormalMap](global.html#ObjectSpaceNormalMap)

The normal map type.

Default is `TangentSpaceNormalMap`.

### .scaleNode : [Node](Node.html).<vec2>

Controls the intensity of the effect.

Default is `null`.

### .unpackNormalMode : string

Controls how to unpack the sampled normal map values.

Default is `NoNormalPacking`.

## Source

[src/nodes/display/NormalMapNode.js](https://github.com/mrdoob/three.js/blob/master/src/nodes/display/NormalMapNode.js)
