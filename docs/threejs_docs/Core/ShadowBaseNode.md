# ShadowBaseNode

> Source: https://threejs.org/docs/pages/ShadowBaseNode.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Node](Node.html) → 

# ShadowBaseNode

Base class for all shadow nodes.

Shadow nodes encapsulate shadow related logic and are always coupled to lighting nodes. Lighting nodes might share the same shadow node type or use specific ones depending on their requirements.

## Constructor

### new ShadowBaseNode( light : [Light](Light.html) )

Constructs a new shadow base node.

**light** |  The shadow casting light.  
---|---  
  
## Properties

### .isShadowBaseNode : boolean (readonly) 

This flag can be used for type testing.

Default is `true`.

### .light : [Light](Light.html)

The shadow casting light.

### .updateBeforeType : string

Overwritten since shadows are updated by default per render.

Default is `'render'`.

**Overrides:** [Node#updateBeforeType](Node.html#updateBeforeType)

## Methods

### .setupShadowPosition( object : [NodeBuilder](NodeBuilder.html) )

Setups the shadow position node which is by default the predefined TSL node object `shadowPositionWorld`.

**object** |  A configuration object that must at least hold a material reference.  
---|---  
  
## Source

[src/nodes/lighting/ShadowBaseNode.js](https://github.com/mrdoob/three.js/blob/master/src/nodes/lighting/ShadowBaseNode.js)
