# AtomicFunctionNode

> Source: https://threejs.org/docs/pages/AtomicFunctionNode.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Node](Node.html) → 

# AtomicFunctionNode

`AtomicFunctionNode` represents any function that can operate on atomic variable types within a shader. In an atomic function, any modification to an atomic variable will occur as an indivisible step with a defined order relative to other modifications. Accordingly, even if multiple atomic functions are modifying an atomic variable at once atomic operations will not interfere with each other.

This node can only be used with a WebGPU backend.

## Constructor

### new AtomicFunctionNode( method : string, pointerNode : [Node](Node.html), valueNode : [Node](Node.html) )

Constructs a new atomic function node.

**method** |  The signature of the atomic function to construct.  
---|---  
**pointerNode** |  An atomic variable or element of an atomic buffer.  
**valueNode** |  The value that mutates the atomic variable.  
  
## Properties

### .method : string

The signature of the atomic function to construct.

### .parents : boolean

Creates a list of the parents for this node for detecting if the node needs to return a value.

Default is `true`.

**Overrides:** [Node#parents](Node.html#parents)

### .pointerNode : [Node](Node.html)

An atomic variable or element of an atomic buffer.

### .valueNode : [Node](Node.html)

A value that modifies the atomic variable.

## Methods

### .getInputType( builder : [NodeBuilder](NodeBuilder.html) ) : string

Overwrites the default implementation to return the type of the pointer node.

**builder** |  The current node builder.  
---|---  
  
**Returns:** The input type.

### .getNodeType( builder : [NodeBuilder](NodeBuilder.html) ) : string

Overwritten since the node type is inferred from the input type.

**builder** |  The current node builder.  
---|---  
  
**Overrides:** [Node#getNodeType](Node.html#getNodeType)

**Returns:** The node type.

## Source

[src/nodes/gpgpu/AtomicFunctionNode.js](https://github.com/mrdoob/three.js/blob/master/src/nodes/gpgpu/AtomicFunctionNode.js)
