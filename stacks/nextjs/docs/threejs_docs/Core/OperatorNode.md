# OperatorNode

> Source: https://threejs.org/docs/pages/OperatorNode.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Node](Node.html) → [TempNode](TempNode.html) → 

# OperatorNode

This node represents basic mathematical and logical operations like addition, subtraction or comparisons (e.g. `equal()`).

## Constructor

### new OperatorNode( op : string, aNode : [Node](Node.html), bNode : [Node](Node.html), …params : [Node](Node.html) )

Constructs a new operator node.

**op** |  The operator.  
---|---  
**aNode** |  The first input.  
**bNode** |  The second input.  
**params** |  Additional input parameters.  
  
## Properties

### .aNode : [Node](Node.html)

The first input.

### .bNode : [Node](Node.html)

The second input.

### .isOperatorNode : boolean (readonly) 

This flag can be used for type testing.

Default is `true`.

### .op : string

The operator.

## Methods

### .getNodeType( builder : [NodeBuilder](NodeBuilder.html), output : string ) : string

This method is overwritten since the node type is inferred from the operator and the input node types.

**builder** |  The current node builder.  
---|---  
**output** |  The output type. Default is `null`.  
  
**Overrides:** [TempNode#getNodeType](TempNode.html#getNodeType)

**Returns:** The node type.

### .getOperatorMethod( builder : [NodeBuilder](NodeBuilder.html), output : string ) : string

Returns the operator method name.

**builder** |  The current node builder.  
---|---  
**output** |  The output type.  
  
**Returns:** The operator method name.

## Source

[src/nodes/math/OperatorNode.js](https://github.com/mrdoob/three.js/blob/master/src/nodes/math/OperatorNode.js)
