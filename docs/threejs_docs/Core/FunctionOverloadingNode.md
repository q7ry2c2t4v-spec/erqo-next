# FunctionOverloadingNode

> Source: https://threejs.org/docs/pages/FunctionOverloadingNode.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Node](Node.html) → 

# FunctionOverloadingNode

This class allows to define multiple overloaded versions of the same function. Depending on the parameters of the function call, the node picks the best-fit overloaded version.

## Constructor

### new FunctionOverloadingNode( functionNodes : Array.<function()>, …parametersNodes : [Node](Node.html) )

Constructs a new function overloading node.

**functionNodes** |  Array of `Fn` function definitions.  
---|---  
**parametersNodes** |  A list of parameter nodes.  
  
## Properties

### .functionNodes : Array.<function()>

Array of `Fn` function definitions.

### .global : boolean

This node is marked as global.

Default is `true`.

**Overrides:** [Node#global](Node.html#global)

### .parametersNodes : Array.<[Node](Node.html)>

A list of parameter nodes.

## Methods

### .getCandidateFn( builder : [NodeBuilder](NodeBuilder.html) ) : [FunctionNode](FunctionNode.html)

Returns the candidate function for the current parameters.

**builder** |  The current node builder.  
---|---  
  
**Returns:** The candidate function.

### .getNodeType( builder : [NodeBuilder](NodeBuilder.html) ) : string

This method is overwritten since the node type is inferred from the function's return type.

**builder** |  The current node builder.  
---|---  
  
**Overrides:** [Node#getNodeType](Node.html#getNodeType)

**Returns:** The node type.

### .setup( builder : [NodeBuilder](NodeBuilder.html) ) : [Node](Node.html)

Sets up the node for the current parameters.

**builder** |  The current node builder.  
---|---  
  
**Overrides:** [Node#setup](Node.html#setup)

**Returns:** The setup node.

## Source

[src/nodes/utils/FunctionOverloadingNode.js](https://github.com/mrdoob/three.js/blob/master/src/nodes/utils/FunctionOverloadingNode.js)
