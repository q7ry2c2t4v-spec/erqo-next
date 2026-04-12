# SpotLightNode

> Source: https://threejs.org/docs/pages/SpotLightNode.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Node](Node.html) → [LightingNode](LightingNode.html) → [AnalyticLightNode](AnalyticLightNode.html) → 

# SpotLightNode

Module for representing spot lights as nodes.

## Constructor

### new SpotLightNode( light : [SpotLight](SpotLight.html) )

Constructs a new spot light node.

**light** |  The spot light source. Default is `null`.  
---|---  
  
## Properties

### .colorNode : [UniformNode](UniformNode.html).<[Color](Color.html)>

Uniform node representing the light color.

**Overrides:** [AnalyticLightNode#colorNode](AnalyticLightNode.html#colorNode)

### .coneCosNode : [UniformNode](UniformNode.html).<float>

Uniform node representing the cone cosine.

### .cutoffDistanceNode : [UniformNode](UniformNode.html).<float>

Uniform node representing the cutoff distance.

### .decayExponentNode : [UniformNode](UniformNode.html).<float>

Uniform node representing the decay exponent.

### .penumbraCosNode : [UniformNode](UniformNode.html).<float>

Uniform node representing the penumbra cosine.

## Methods

### .getSpotAttenuation( builder : [NodeBuilder](NodeBuilder.html), angleCosine : [Node](Node.html).<float> ) : [Node](Node.html).<float>

Computes the spot attenuation for the given angle.

**builder** |  The node builder.  
---|---  
**angleCosine** |  The angle to compute the spot attenuation for.  
  
**Returns:** The spot attenuation.

### .update( frame : [NodeFrame](NodeFrame.html) )

Overwritten to updated spot light specific uniforms.

**frame** |  A reference to the current node frame.  
---|---  
  
**Overrides:** [AnalyticLightNode#update](AnalyticLightNode.html#update)

## Source

[src/nodes/lighting/SpotLightNode.js](https://github.com/mrdoob/three.js/blob/master/src/nodes/lighting/SpotLightNode.js)
