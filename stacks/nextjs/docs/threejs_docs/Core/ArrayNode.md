# ArrayNode

> Source: https://threejs.org/docs/pages/ArrayNode.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Node](Node.html) → [TempNode](TempNode.html) → 

# ArrayNode

ArrayNode represents a collection of nodes, typically created using the [array](TSL.html#array) function.

## Code Example
    
    
    const colors = array( [
    	vec3( 1, 0, 0 ),
    	vec3( 0, 1, 0 ),
    	vec3( 0, 0, 1 )
    ] );
    const redColor = tintColors.element( 0 );
    

## Constructor

### new ArrayNode( nodeType : string, count : number, values : Array.<[Node](Node.html)> )

Constructs a new array node.

**nodeType** |  The data type of the elements.  
---|---  
**count** |  Size of the array.  
**values** |  Array default values. Default is `null`.  
  
## Properties

### .count : number

Array size.

### .isArrayNode : boolean (readonly) 

This flag can be used for type testing.

Default is `true`.

### .values : Array.<[Node](Node.html)>

Array default values.

## Methods

### .generate( builder : [NodeBuilder](NodeBuilder.html) ) : string

This method builds the output node and returns the resulting array as a shader string.

**builder** |  The current node builder.  
---|---  
  
**Overrides:** [TempNode#generate](TempNode.html#generate)

**Returns:** The generated shader string.

### .getArrayCount( builder : [NodeBuilder](NodeBuilder.html) ) : number

Returns the number of elements in the node array.

**builder** |  The current node builder.  
---|---  
  
**Overrides:** [TempNode#getArrayCount](TempNode.html#getArrayCount)

**Returns:** The number of elements in the node array.

### .getElementType( builder : [NodeBuilder](NodeBuilder.html) ) : string

Returns the node's type.

**builder** |  The current node builder.  
---|---  
  
**Overrides:** [TempNode#getElementType](TempNode.html#getElementType)

**Returns:** The type of the node.

### .getMemberType( builder : [NodeBuilder](NodeBuilder.html), name : string ) : string

Returns the type of a member variable.

**builder** |  The current node builder.  
---|---  
**name** |  The name of the member variable.  
  
**Overrides:** [TempNode#getMemberType](TempNode.html#getMemberType)

**Returns:** The type of the member variable.

### .getNodeType( builder : [NodeBuilder](NodeBuilder.html) ) : string

Returns the node's type.

**builder** |  The current node builder.  
---|---  
  
**Overrides:** [TempNode#getNodeType](TempNode.html#getNodeType)

**Returns:** The type of the node.

## Source

[src/nodes/core/ArrayNode.js](https://github.com/mrdoob/three.js/blob/master/src/nodes/core/ArrayNode.js)
