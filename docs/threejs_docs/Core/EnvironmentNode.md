# EnvironmentNode

> Source: https://threejs.org/docs/pages/EnvironmentNode.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Node](Node.html) → [LightingNode](LightingNode.html) → 

# EnvironmentNode

Represents a physical model for Image-based lighting (IBL). The environment is defined via environment maps in the equirectangular, cube map or cubeUV (PMREM) format. `EnvironmentNode` is intended for PBR materials like [MeshStandardNodeMaterial](MeshStandardNodeMaterial.html).

## Constructor

### new EnvironmentNode( envNode : [Node](Node.html) )

Constructs a new environment node.

**envNode** |  A node representing the environment. Default is `null`.  
---|---  
  
## Properties

### .envNode : [Node](Node.html)

A node representing the environment.

Default is `null`.

## Source

[src/nodes/lighting/EnvironmentNode.js](https://github.com/mrdoob/three.js/blob/master/src/nodes/lighting/EnvironmentNode.js)
