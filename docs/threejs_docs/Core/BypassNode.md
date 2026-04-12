# BypassNode

> Source: https://threejs.org/docs/pages/BypassNode.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Node](Node.html) → 

# BypassNode

The class generates the code of a given node but returns another node in the output. This can be used to call a method or node that does not return a value, i.e. type `void` on an input where returning a value is required. Example:

## Code Example
    
    
    material.colorNode = myColor.bypass( runVoidFn() )
    

## Constructor

### new BypassNode( outputNode : [Node](Node.html), callNode : [Node](Node.html) )

Constructs a new bypass node.

**outputNode** |  The output node.  
---|---  
**callNode** |  The call node.  
  
## Properties

### .callNode : [Node](Node.html)

The call node.

### .isBypassNode : boolean (readonly) 

This flag can be used for type testing.

Default is `true`.

### .outputNode : [Node](Node.html)

The output node.

## Source

[src/nodes/core/BypassNode.js](https://github.com/mrdoob/three.js/blob/master/src/nodes/core/BypassNode.js)
