# UniformArrayElementNode

> Source: https://threejs.org/docs/pages/UniformArrayElementNode.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Node](Node.html) → [ArrayElementNode](ArrayElementNode.html) → 

# UniformArrayElementNode

Represents the element access on uniform array nodes.

## Constructor

### new UniformArrayElementNode( uniformArrayNode : [UniformArrayNode](UniformArrayNode.html), indexNode : [IndexNode](IndexNode.html) )

Constructs a new buffer node.

**uniformArrayNode** |  The uniform array node to access.  
---|---  
**indexNode** |  The index data that define the position of the accessed element in the array.  
  
## Properties

### .isArrayBufferElementNode : boolean (readonly) 

This flag can be used for type testing.

Default is `true`.

## Source

[src/nodes/accessors/UniformArrayNode.js](https://github.com/mrdoob/three.js/blob/master/src/nodes/accessors/UniformArrayNode.js)
