# FunctionCallNode

> Source: https://threejs.org/docs/pages/FunctionCallNode.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Node](Node.html) → [TempNode](TempNode.html) → 

# FunctionCallNode

This module represents the call of a [FunctionNode](FunctionNode.html). Developers are usually not confronted with this module since they use the predefined TSL syntax `wgslFn` and `glslFn` which encapsulate this logic.

## Constructor

### new FunctionCallNode( functionNode : [FunctionNode](FunctionNode.html), parameters : Object.<string, [Node](Node.html)> )

Constructs a new function call node.

**functionNode** |  The function node. Default is `null`.  
---|---  
**parameters** |  The parameters for the function call. Default is `{}`.  
  
## Properties

### .functionNode : [FunctionNode](FunctionNode.html)

The function node.

Default is `null`.

### .parameters : Object.<string, [Node](Node.html)>

The parameters of the function call.

Default is `{}`.

## Methods

### .getMemberType( builder : [NodeBuilder](NodeBuilder.html), name : string ) : string

Returns the function node of this function call node.

**builder** |  The current node builder.  
---|---  
**name** |  The name of the member.  
  
**Overrides:** [TempNode#getMemberType](TempNode.html#getMemberType)

**Returns:** The type of the member.

### .getNodeType( builder : [NodeBuilder](NodeBuilder.html) ) : string

Returns the type of this function call node.

**builder** |  The current node builder.  
---|---  
  
**Overrides:** [TempNode#getNodeType](TempNode.html#getNodeType)

**Returns:** The type of this node.

### .getParameters() : Object.<string, [Node](Node.html)>

Returns the parameters of the function call node.

**Returns:** The parameters of this node.

### .setParameters( parameters : Object.<string, [Node](Node.html)> ) : [FunctionCallNode](FunctionCallNode.html)

Sets the parameters of the function call node.

**parameters** |  The parameters to set.  
---|---  
  
**Returns:** A reference to this node.

## Source

[src/nodes/code/FunctionCallNode.js](https://github.com/mrdoob/three.js/blob/master/src/nodes/code/FunctionCallNode.js)
