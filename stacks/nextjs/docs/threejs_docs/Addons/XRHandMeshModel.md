# XRHandMeshModel

> Source: https://threejs.org/docs/pages/XRHandMeshModel.html
> Category: Addons

# XRHandMeshModel

Represents one of the hand model types [XRHandModelFactory](XRHandModelFactory.html) might produce depending on the selected profile. `XRHandMeshModel` represents a hand with a custom asset.

## Import

XRHandMeshModel is an addon, and must be imported explicitly, see [Installation#Addons](https://threejs.org/manual/#en/installation).
    
    
    import { XRHandMeshModel } from 'three/addons/webxr/XRHandMeshModel.js';

## Constructor

### new XRHandMeshModel( handModel : [XRHandModel](XRHandModel.html), controller : [Group](Group.html), path : string, handedness : XRHandedness, loader : [Loader](Loader.html), onLoad : function )

Constructs a new XR hand mesh model.

**handModel** |  The hand model.  
---|---  
**controller** |  The WebXR controller.  
**path** |  The model path.  
**handedness** |  The handedness of the XR input source.  
**loader** |  The loader. If not provided, an instance of `GLTFLoader` will be used to load models. Default is `null`.  
**onLoad** |  A callback that is executed when a controller model has been loaded. Default is `null`.  
  
## Properties

### .bones : Array.<[Bone](Bone.html)>

An array of bones representing the bones of the hand skeleton.

### .controller : [Group](Group.html)

The WebXR controller.

### .handModel : [XRHandModel](XRHandModel.html)

The hand model.

## Methods

### .updateMesh()

Updates the mesh based on the tracked XR joints data.

## Source

[examples/jsm/webxr/XRHandMeshModel.js](https://github.com/mrdoob/three.js/blob/master/examples/jsm/webxr/XRHandMeshModel.js)
