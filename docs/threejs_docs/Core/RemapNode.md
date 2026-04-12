# RemapNode

> Source: https://threejs.org/docs/pages/RemapNode.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Node](Node.html) → 

# RemapNode

This node allows to remap a node value from one range into another. E.g a value of `0.4` in the range `[ 0.3, 0.5 ]` should be remapped into the normalized range `[ 0, 1 ]`. `RemapNode` takes care of that and converts the original value of `0.4` to `0.5`.

## Constructor

### new RemapNode( node : [Node](Node.html), inLowNode : [Node](Node.html), inHighNode : [Node](Node.html), outLowNode : [Node](Node.html), outHighNode : [Node](Node.html) )

Constructs a new remap node.

**node** |  The node that should be remapped.  
---|---  
**inLowNode** |  The source or current lower bound of the range.  
**inHighNode** |  The source or current upper bound of the range.  
**outLowNode** |  The target lower bound of the range. Default is `float(0)`.  
**outHighNode** |  The target upper bound of the range. Default is `float(1)`.  
  
## Properties

### .doClamp : boolean

Whether the node value should be clamped before remapping it to the target range.

Default is `true`.

### .inHighNode : [Node](Node.html)

The source or current upper bound of the range.

### .inLowNode : [Node](Node.html)

The source or current lower bound of the range.

### .node : [Node](Node.html)

The node that should be remapped.

### .outHighNode : [Node](Node.html)

The target upper bound of the range.

Default is `float(1)`.

### .outLowNode : [Node](Node.html)

The target lower bound of the range.

Default is `float(0)`.

## Source

[src/nodes/utils/RemapNode.js](https://github.com/mrdoob/three.js/blob/master/src/nodes/utils/RemapNode.js)
