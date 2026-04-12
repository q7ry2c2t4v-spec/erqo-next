# MeshSSSNodeMaterial

> Source: https://threejs.org/docs/pages/MeshSSSNodeMaterial.html
> Category: Core

[EventDispatcher](EventDispatcher.html) → [Material](Material.html) → [NodeMaterial](NodeMaterial.html) → [MeshStandardNodeMaterial](MeshStandardNodeMaterial.html) → [MeshPhysicalNodeMaterial](MeshPhysicalNodeMaterial.html) → 

# MeshSSSNodeMaterial

This node material is an experimental extension of [MeshPhysicalNodeMaterial](MeshPhysicalNodeMaterial.html) that implements a Subsurface scattering (SSS) term.

## Constructor

### new MeshSSSNodeMaterial( parameters : Object )

Constructs a new mesh SSS node material.

**parameters** |  The configuration parameter.  
---|---  
  
## Properties

### .thicknessAmbientNode : [Node](Node.html).<float>

Represents the thickness ambient factor.

### .thicknessAttenuationNode : [Node](Node.html).<float>

Represents the thickness attenuation.

### .thicknessColorNode : [Node](Node.html).<vec3>

Represents the thickness color.

Default is `null`.

### .thicknessDistortionNode : [Node](Node.html).<float>

Represents the distortion factor.

### .thicknessPowerNode : [Node](Node.html).<float>

Represents the thickness power.

### .thicknessScaleNode : [Node](Node.html).<float>

Represents the thickness scale.

### .useSSS : boolean

Whether the lighting model should use SSS or not.

Default is `true`.

## Methods

### .setupLightingModel() : [SSSLightingModel](SSSLightingModel.html)

Setups the lighting model.

**Overrides:** [MeshPhysicalNodeMaterial#setupLightingModel](MeshPhysicalNodeMaterial.html#setupLightingModel)

**Returns:** The lighting model.

## Source

[src/materials/nodes/MeshSSSNodeMaterial.js](https://github.com/mrdoob/three.js/blob/master/src/materials/nodes/MeshSSSNodeMaterial.js)
