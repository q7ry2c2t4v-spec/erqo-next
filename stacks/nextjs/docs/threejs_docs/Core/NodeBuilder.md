# NodeBuilder

> Source: https://threejs.org/docs/pages/NodeBuilder.html
> Category: Core

# NodeBuilder

Base class for builders which generate a shader program based on a 3D object and its node material definition.

## Constructor

### new NodeBuilder( object : [Object3D](Object3D.html), renderer : [Renderer](Renderer.html), parser : [NodeParser](NodeParser.html) )

Constructs a new node builder.

**object** |  The 3D object.  
---|---  
**renderer** |  The current renderer.  
**parser** |  A reference to a node parser.  
  
## Properties

### .activeStacks : Array.<[StackNode](StackNode.html)>

The active stack nodes.

### .attributes : Array.<[NodeAttribute](NodeAttribute.html)>

This array holds the node attributes of this builder created via [AttributeNode](AttributeNode.html).

### .bindGroups : Array.<[BindGroup](BindGroup.html)>

Reference to the array of bind groups.

### .bindings : Object

This dictionary holds the bindings for each shader stage.

### .bindingsIndexes : Object

This dictionary maintains the binding indices per bind group.

### .bufferAttributes : Array.<[NodeAttribute](NodeAttribute.html)>

This array holds the node attributes of this builder created via [BufferAttributeNode](BufferAttributeNode.html).

### .buildStage : 'setup' | 'analyze' | 'generate'

The current build stage.

### .cache : [NodeCache](NodeCache.html)

The builder's cache.

### .camera : [Camera](Camera.html)

The camera the 3D object is rendered with.

Default is `null`.

### .chaining : Array.<[Node](Node.html)>

A chain of nodes. Used to check recursive calls in node-graph.

### .clippingContext : [ClippingContext](ClippingContext.html)

The current clipping context.

### .codes : Object.<string, Array.<[NodeCode](NodeCode.html)>>

This dictionary holds the (native) node codes of this builder. The codes are maintained in an array for each shader stage.

### .computeShader : string

The generated compute shader.

### .context : Object

The builder's context.

### .currentFunctionNode : [FunctionNode](FunctionNode.html)

Reference to the current function node.

Default is `null`.

### .currentNode : [Node](Node.html)

A reference the current node which is the last node in the chain of nodes.

### .declarations : Object

This dictionary holds the declarations for each shader stage.

### .environmentNode : [Node](Node.html)

A reference to the current environment node.

Default is `null`.

### .flow : Object

Current code flow. All code generated in this stack will be stored in `.flow`.

### .flowCode : Object.<string, string>

Nodes code from `.flowNodes`.

### .flowNodes : Object.<string, Array.<[Node](Node.html)>>

Nodes used in the primary flow of code generation.

### .fnCall : [Node](Node.html)

The current TSL function(Fn) call node.

Default is `null`.

### .fogNode : [Node](Node.html)

A reference to the current fog node.

Default is `null`.

### .fragmentShader : string

The generated fragment shader.

### .geometry : [BufferGeometry](BufferGeometry.html)

The geometry of the 3D object.

### .globalCache : [NodeCache](NodeCache.html)

Since the [NodeBuilder#cache](NodeBuilder.html#cache) might be temporarily overwritten by other caches, this member retains the reference to the builder's own cache.

Default is `this.cache`.

### .hashNodes : Object.<number, [Node](Node.html)>

A dictionary that assigns each node to a unique hash.

### .lightsNode : [LightsNode](LightsNode.html)

A reference to the current lights node.

Default is `null`.

### .material : [Material](Material.html)

The material of the 3D object.

### .nodes : Array.<[Node](Node.html)>

A list of all nodes the builder is processing for this 3D object.

### .object : [Object3D](Object3D.html)

The 3D object.

### .observer : [NodeMaterialObserver](NodeMaterialObserver.html)

A reference to a node material observer.

Default is `null`.

### .parser : [NodeParser](NodeParser.html)

A reference to a node parser.

### .renderer : [Renderer](Renderer.html)

The current renderer.

### .scene : [Scene](Scene.html)

The scene the 3D object belongs to.

Default is `null`.

### .sequentialNodes : Array.<[Node](Node.html)>

A list of all nodes the builder is processing in sequential order.

This is used to determine the update order of nodes, which is important for NodeUpdateType#UPDATE_BEFORE and NodeUpdateType#UPDATE_AFTER.

### .shaderStage : 'vertex' | 'fragment' | 'compute' | 'any'

The current shader stage.

### .stack : [StackNode](StackNode.html)

The current stack. This reflects the current process in the code block hierarchy, it is useful to know if the current process is inside a conditional for example.

### .stacks : Array.<[StackNode](StackNode.html)>

List of stack nodes. The current stack hierarchy is stored in an array.

### .structs : Object

This dictionary holds the output structs of the builder. The structs are maintained in an array for each shader stage.

### .subBuild

Returns the current sub-build layer.

### .subBuildFn : string

The current sub-build TSL function(Fn).

Default is `null`.

### .subBuildLayers : Array.<[SubBuildNode](SubBuildNode.html)>

The sub-build layers.

Default is `[]`.

### .tab : string

A tab value. Used for shader string generation.

Default is `'\t'`.

### .types : Object

This dictionary holds the types of the builder.

### .uniforms : Object

This dictionary holds the node uniforms of the builder. The uniforms are maintained in an array for each shader stage.

### .updateAfterNodes : Array.<[Node](Node.html)>

A list of all nodes which [Node#updateAfter](Node.html#updateAfter) method should be executed.

### .updateBeforeNodes : Array.<[Node](Node.html)>

A list of all nodes which [Node#updateBefore](Node.html#updateBefore) method should be executed.

### .updateNodes : Array.<[Node](Node.html)>

A list of all nodes which [Node#update](Node.html#update) method should be executed.

### .vars : Object.<string, (Array.<[NodeVar](NodeVar.html)>|number)>

This dictionary holds the node variables of this builder. The variables are maintained in an array for each shader stage. This dictionary is also used to count the number of variables according to their type (const, vars).

### .varyings : Array.<[NodeVarying](NodeVarying.html)>

This array holds the node varyings of this builder.

### .vertexShader : string

The generated vertex shader.

## Methods

### .addChain( node : [Node](Node.html) )

Adds the given node to the internal node chain. This is used to check recursive calls in node-graph.

**node** |  The node to add.  
---|---  
  
### .addContext( context : Object ) : Object

Adds context data to the builder's current context.

**context** |  The context to add.  
---|---  
  
**Returns:** The previous context.

### .addFlow( shaderStage : 'vertex' | 'fragment' | 'compute', node : [Node](Node.html) ) : [Node](Node.html)

Adds the Node to a target flow so that it can generate code in the 'generate' process.

**shaderStage** |  The shader stage.  
---|---  
**node** |  The node to add.  
  
**Returns:** The node.

### .addFlowCode( code : string ) : [NodeBuilder](NodeBuilder.html)

Adds a code to the current code flow.

**code** |  Shader code.  
---|---  
  
**Returns:** A reference to this node builder.

### .addFlowCodeHierarchy( node : [Node](Node.html), nodeBlock : [Node](Node.html) )

Adds a code flow based on the code-block hierarchy. This is used so that code-blocks like If,Else create their variables locally if the Node is only used inside one of these conditionals in the current shader stage.

**node** |  The node to add.  
---|---  
**nodeBlock** |  Node-based code-block. Usually 'ConditionalNode'.  
  
### .addFlowTab() : [NodeBuilder](NodeBuilder.html)

Add tab in the code that will be generated so that other snippets respect the current tabulation. Typically used in codes with If,Else.

**Returns:** A reference to this node builder.

### .addInclude( node : [Node](Node.html) ) : void

Includes a node in the current function node.

**node** |  The node to include.  
---|---  
  
### .addLineFlowCode( code : string, node : [Node](Node.html) ) : [NodeBuilder](NodeBuilder.html)

Add a inline-code to the current flow.

**code** |  The code to add.  
---|---  
**node** |  Optional Node, can help the system understand if the Node is part of a code-block. Default is `null`.  
  
**Returns:** A reference to this node builder.

### .addLineFlowCodeBlock( node : [Node](Node.html), code : string, nodeBlock : [Node](Node.html) )

Add a inline-code to the current flow code-block.

**node** |  The node to add.  
---|---  
**code** |  The code to add.  
**nodeBlock** |  Current ConditionalNode  
  
### .addNode( node : [Node](Node.html) )

Adds a node to this builder.

**node** |  The node to add.  
---|---  
  
### .addSequentialNode( node : [Node](Node.html) )

It is used to add Nodes that will be used as FRAME and RENDER events, and need to follow a certain sequence in the calls to work correctly. This function should be called after 'setup()' in the 'build()' process to ensure that the child nodes are processed first.

**node** |  The node to add.  
---|---  
  
### .addStack() : [StackNode](StackNode.html)

Adds a stack node to the internal stack.

**Returns:** The added stack node.

### .addSubBuild( subBuild : [SubBuildNode](SubBuildNode.html) )

Adds a sub-build layer to the node builder.

**subBuild** |  The sub-build layer to add.  
---|---  
  
### .build() : [NodeBuilder](NodeBuilder.html)

Central build method which controls the build for the given object.

**Returns:** A reference to this node builder.

### .buildCode() (abstract) 

Controls the code build of the shader stages.

### .buildFunctionCode( shaderNode : ShaderNodeInternal ) : string (abstract) 

Builds the given shader node.

**shaderNode** |  The shader node.  
---|---  
  
**Returns:** The function code.

### .buildFunctionNode( shaderNode : ShaderNodeInternal ) : [FunctionNode](FunctionNode.html)

Returns the native shader operator name for a given generic name. It is a similar type of method like [NodeBuilder#getMethod](NodeBuilder.html#getMethod).

**shaderNode** |  The shader node to build the function node with.  
---|---  
  
**Returns:** The build function node.

### .buildUpdateNodes()

Checks the update types of nodes

### .changeComponentType( type : string, newComponentType : string ) : string

For a given type this method changes the component type to the given value. E.g. `vec4` should be changed to the new component type `uint` which results in `uvec4`.

**type** |  The type.  
---|---  
**newComponentType** |  The new component type.  
  
**Returns:** The new type.

### .createCubeRenderTarget( size : number, options : Object ) : [CubeRenderTarget](CubeRenderTarget.html)

Factory method for creating an instance of [CubeRenderTarget](CubeRenderTarget.html) with the given dimensions and options.

**size** |  The size of the cube render target.  
---|---  
**options** |  The options of the cube render target.  
  
**Returns:** The cube render target.

### .createRenderTarget( width : number, height : number, options : Object ) : [RenderTarget](RenderTarget.html)

Factory method for creating an instance of [RenderTarget](RenderTarget.html) with the given dimensions and options.

**width** |  The width of the render target.  
---|---  
**height** |  The height of the render target.  
**options** |  The options of the render target.  
  
**Returns:** The render target.

### .flowBuildStage( node : [Node](Node.html), buildStage : string, output : [Node](Node.html) | string ) : [Node](Node.html) | string

Executes the node in a specific build stage.

This function can be used to arbitrarily execute the specified build stage outside of the standard build process. For instance, if a node's type depends on properties created by the 'setup' stage, then flowBuildStage(node, 'setup') can be used to execute the setup build stage and access its generated nodes before the standard build process begins.

**node** |  The node to execute.  
---|---  
**buildStage** |  The build stage to execute the node in.  
**output** |  Expected output type. For example 'vec3'. Default is `null`.  
  
**Returns:** The result of the node build.

### .flowChildNode( node : [Node](Node.html), output : string ) : Object

Generates a code flow based on a child Node.

**node** |  The node to execute.  
---|---  
**output** |  Expected output type. For example 'vec3'. Default is `null`.  
  
**Returns:** The code flow.

### .flowNode( node : [Node](Node.html) ) : Object

Executes the node flow based on a root node to generate the final shader code.

**node** |  The node to execute.  
---|---  
  
**Returns:** The code flow.

### .flowNodeFromShaderStage( shaderStage : 'vertex' | 'fragment' | 'compute' | 'any', node : [Node](Node.html), output : string, propertyName : string ) : Object | [Node](Node.html)

Executes a flow of code in a different stage.

Some nodes like `varying()` have the ability to compute code in vertex-stage and return the value in fragment-stage even if it is being executed in an input fragment.

**shaderStage** |  The shader stage.  
---|---  
**node** |  The node to execute.  
**output** |  Expected output type. For example 'vec3'. Default is `null`.  
**propertyName** |  The property name to assign the result. Default is `null`.  
  
**Returns:** The code flow or node.build() result.

### .flowShaderNode( shaderNode : ShaderNodeInternal ) : Object

Generates a code flow based on a TSL function: Fn().

**shaderNode** |  A function code will be generated based on the input.  
---|---  
  
### .flowStagesNode( node : [Node](Node.html), output : string ) : Object

Runs the node flow through all the steps of creation, 'setup', 'analyze', 'generate'.

**node** |  The node to execute.  
---|---  
**output** |  Expected output type. For example 'vec3'. Default is `null`.  
  
### .format( snippet : string, fromType : string, toType : string ) : string

Formats the given shader snippet from a given type into another one. E.g. this method might be used to convert a simple float string `"1.0"` into a `vec3` representation: `"vec3<f32>( 1.0 )"`.

**snippet** |  The shader snippet.  
---|---  
**fromType** |  The source type.  
**toType** |  The target type.  
  
**Returns:** The updated shader string.

### .generateArray( type : string, count : number, values : Array.<[Node](Node.html)> ) : string

Generates the array shader string for the given type and value.

**type** |  The type.  
---|---  
**count** |  The count.  
**values** |  The default values. Default is `null`.  
  
**Returns:** The generated value as a shader string.

### .generateArrayDeclaration( type : string, count : number ) : string

Generates the array declaration string.

**type** |  The type.  
---|---  
**count** |  The count.  
  
**Returns:** The generated value as a shader string.

### .generateConst( type : string, value : [any](global.html#any) ) : string

Generates the shader string for the given type and value.

**type** |  The type.  
---|---  
**value** |  The value. Default is `null`.  
  
**Returns:** The generated value as a shader string.

### .generateStruct( type : string, membersLayout : Array.<Object>, values : Array.<[Node](Node.html)> ) : string

Generates the struct shader string.

**type** |  The type.  
---|---  
**membersLayout** |  The count.  
**values** |  The default values. Default is `null`.  
  
**Returns:** The generated value as a shader string.

### .generateTexture( texture : [Texture](Texture.html), textureProperty : string, uvSnippet : string ) : string (abstract) 

Generates a texture sample shader string for the given texture data.

**texture** |  The texture.  
---|---  
**textureProperty** |  The texture property name.  
**uvSnippet** |  Snippet defining the texture coordinates.  
  
**Returns:** The generated shader string.

### .generateTextureLod( texture : [Texture](Texture.html), textureProperty : string, uvSnippet : string, depthSnippet : string, levelSnippet : string ) : string (abstract) 

Generates a texture LOD shader string for the given texture data.

**texture** |  The texture.  
---|---  
**textureProperty** |  The texture property name.  
**uvSnippet** |  Snippet defining the texture coordinates.  
**depthSnippet** |  Snippet defining the 0-based texture array index to sample.  
**levelSnippet** |  Snippet defining the mip level.  
  
**Returns:** The generated shader string.

### .getActiveStack() : [StackNode](StackNode.html)

Returns the active stack.

**Returns:** The active stack.

### .getAttribute( name : string, type : string ) : [NodeAttribute](NodeAttribute.html)

Returns a node attribute for the given name and type.

**name** |  The attribute's name.  
---|---  
**type** |  The attribute's type.  
  
**Returns:** The node attribute.

### .getAttributes( shaderStage : 'vertex' | 'fragment' | 'compute' | 'any' ) : string (abstract) 

Returns the attribute definitions as a shader string for the given shader stage.

**shaderStage** |  The shader stage.  
---|---  
  
**Returns:** The attribute code section.

### .getAttributesArray() : Array.<[NodeAttribute](NodeAttribute.html)>

Returns an array holding all node attributes of this node builder.

**Returns:** The node attributes of this builder.

### .getBaseStack() : [StackNode](StackNode.html)

Returns the base stack.

**Returns:** The base stack.

### .getBindGroupArray( groupName : string, shaderStage : 'vertex' | 'fragment' | 'compute' | 'any' ) : Array.<[NodeUniformsGroup](NodeUniformsGroup.html)>

Returns an array of node uniform groups for the given group name and shader stage.

**groupName** |  The group name.  
---|---  
**shaderStage** |  The shader stage.  
  
**Returns:** The array of node uniform groups.

### .getBindings() : Array.<[BindGroup](BindGroup.html)>

Returns a list bindings of all shader stages separated by groups.

**Returns:** The list of bindings.

### .getBufferAttributeFromNode( node : [BufferAttributeNode](BufferAttributeNode.html), type : string ) : [NodeAttribute](NodeAttribute.html)

Returns an instance of [NodeAttribute](NodeAttribute.html) for the given buffer attribute node.

**node** |  The buffer attribute node.  
---|---  
**type** |  The node type.  
  
**Returns:** The node attribute.

### .getBuildStage() : 'setup' | 'analyze' | 'generate'

Returns the current build stage.

**Returns:** The current build stage.

### .getCache() : [NodeCache](NodeCache.html)

Returns the builder's current cache.

**Returns:** The builder's current cache.

### .getCacheFromNode( node : [Node](Node.html), parent : boolean ) : [NodeCache](NodeCache.html)

Returns a cache for the given node.

**node** |  The node.  
---|---  
**parent** |  Whether this node refers to a shared parent cache or not. Default is `true`.  
  
**Returns:** The cache.

### .getClosestSubBuild( data : [Node](Node.html) | Set.<string> | Array.<string> ) : string

Returns the closest sub-build layer for the given data.

**data** |  The data to get the closest sub-build layer from.  
---|---  
  
**Returns:** The closest sub-build name or null if none found.

### .getCodeFromNode( node : [CodeNode](CodeNode.html), type : string, shaderStage : 'vertex' | 'fragment' | 'compute' | 'any' ) : [NodeCode](NodeCode.html)

Returns an instance of [NodeCode](NodeCode.html) for the given code node.

**node** |  The code node.  
---|---  
**type** |  The node type.  
**shaderStage** |  The shader stage. Default is `this.shaderStage`.  
  
**Returns:** The node code.

### .getCodes( shaderStage : 'vertex' | 'fragment' | 'compute' | 'any' ) : string

Returns the native code definitions as a shader string for the given shader stage.

**shaderStage** |  The shader stage.  
---|---  
  
**Returns:** The native code section.

### .getComponentType( type : string ) : string

Returns the component type for a given type.

**type** |  The type.  
---|---  
  
**Returns:** The component type.

### .getComponentTypeFromTexture( texture : [Texture](Texture.html) ) : string

Returns the component type of a given texture.

**texture** |  The texture.  
---|---  
  
**Returns:** The component type.

### .getContext() : Object

Returns the builder's current context.

**Returns:** The builder's current context.

### .getDataFromNode( node : [Node](Node.html), shaderStage : 'vertex' | 'fragment' | 'compute' | 'any', cache : [NodeCache](NodeCache.html) ) : Object

The builder maintains (cached) data for each node during the building process. This method can be used to get these data for a specific shader stage and cache.

**node** |  The node to get the data for.  
---|---  
**shaderStage** |  The shader stage. Default is `this.shaderStage`.  
**cache** |  An optional cache. Default is `null`.  
  
**Returns:** The node data.

### .getDrawIndex() : string (abstract) 

Returns the drawIndex input variable as a native shader string. Only relevant for WebGL and its `WEBGL_multi_draw` extension.

**Returns:** The drawIndex shader string.

### .getElementType( type : string ) : string

Returns the element type for a given type.

**type** |  The type.  
---|---  
  
**Returns:** The element type.

### .getFlowData( node : [Node](Node.html), shaderStage : 'vertex' | 'fragment' | 'compute' | 'any' ) : Object

Gets the current flow data based on a Node.

**node** |  Node that the flow was started.  
---|---  
**shaderStage** |  The shader stage.  
  
**Returns:** The flow data.

### .getFragCoord() : string (abstract) 

Returns the fragCoord input variable as a native shader string.

**Returns:** The fragCoord shader string.

### .getFrontFacing() : string (abstract) 

Returns the frontFacing input variable as a native shader string.

**Returns:** The frontFacing shader string.

### .getFunctionOperator( op : string ) : string (abstract) 

Returns the native shader operator name for a given generic name. It is a similar type of method like [NodeBuilder#getMethod](NodeBuilder.html#getMethod).

**op** |  The operator name to resolve.  
---|---  
  
**Returns:** The resolved operator name.

### .getHash() : string

Returns the hash of this node builder.

**Returns:** The hash.

### .getInstanceIndex() : string (abstract) 

Contextually returns either the vertex stage instance index builtin or the linearized index of an compute invocation within a grid of workgroups.

**Returns:** The instanceIndex shader string.

### .getIntegerType( type : string ) : string

Returns the integer type pendant for the given type.

**type** |  The type.  
---|---  
  
**Returns:** The integer type.

### .getMethod( method : string ) : string (abstract) 

Returns the native shader method name for a given generic name. E.g. the method name `textureDimensions` matches the WGSL name but must be resolved to `textureSize` in GLSL.

**method** |  The method name to resolve.  
---|---  
  
**Returns:** The resolved method name.

### .getNodeFromHash( hash : number ) : [Node](Node.html)

Returns a node for the given hash, see [NodeBuilder#setHashNode](NodeBuilder.html#setHashNode).

**hash** |  The hash of the node.  
---|---  
  
**Returns:** The found node.

### .getNodeProperties( node : [Node](Node.html), shaderStage : 'vertex' | 'fragment' | 'compute' | 'any' ) : Object

Returns the properties for the given node and shader stage.

Properties are typically used within a build stage to reference a node's child node or nodes manually assigned to the properties in a separate build stage. A typical usage pattern for defining nodes manually would be assigning dependency nodes to the current node's properties in the setup stage and building those properties in the generate stage.

**node** |  The node to get the properties for.  
---|---  
**shaderStage** |  The shader stage. Default is `'any'`.  
  
**Returns:** The node properties.

### .getNodeUniform( uniformNode : [NodeUniform](NodeUniform.html), type : string ) : [Uniform](Uniform.html)

Returns a uniform representation which is later used for UBO generation and rendering.

**uniformNode** |  The uniform node.  
---|---  
**type** |  The requested type.  
  
**Returns:** The uniform.

### .getOutputStructName() : string (abstract) 

Returns the output struct name which is required by [OutputStructNode](OutputStructNode.html).

**Returns:** The name of the output struct.

### .getOutputStructTypeFromNode( node : [OutputStructNode](OutputStructNode.html), membersLayout : Array.<Object> ) : StructType

Returns an instance of StructType for the given output struct node.

**node** |  The output struct node.  
---|---  
**membersLayout** |  The output struct types.  
  
**Returns:** The struct type attribute.

### .getPropertyName( node : [Node](Node.html), shaderStage : 'vertex' | 'fragment' | 'compute' | 'any' ) : string

Returns for the given node and shader stage the property name for the shader.

**node** |  The node.  
---|---  
**shaderStage** |  The shader stage.  
  
**Returns:** The property name.

### .getShaderStage() : 'vertex' | 'fragment' | 'compute' | 'any'

Returns the current shader stage.

**Returns:** The current shader stage.

### .getSharedContext() : Object

Gets a context used in shader construction that can be shared across different materials. This is necessary since the renderer cache can reuse shaders generated in one material and use them in another.

**Returns:** The builder's current context without material.

### .getSharedDataFromNode( node : [Node](Node.html) ) : Object

Returns shared data object for the given node.

**node** |  The node to get shared data from.  
---|---  
  
**Returns:** The shared data.

### .getSignature() : string

Returns a signature with the engine's current revision.

**Returns:** The signature.

### .getStructTypeFromNode( node : [OutputStructNode](OutputStructNode.html), membersLayout : Array.<Object>, name : string, shaderStage : 'vertex' | 'fragment' | 'compute' | 'any' ) : StructType

Returns an instance of StructType for the given output struct node.

**node** |  The output struct node.  
---|---  
**membersLayout** |  The output struct types.  
**name** |  The name of the struct. Default is `null`.  
**shaderStage** |  The shader stage. Default is `this.shaderStage`.  
  
**Returns:** The struct type attribute.

### .getStructTypeNode( name : string, shaderStage : 'vertex' | 'fragment' | 'compute' | 'any' ) : StructType

Returns an instance of StructType for the given struct name and shader stage or null if not found.

**name** |  The name of the struct.  
---|---  
**shaderStage** |  The shader stage. Default is `this.shaderStage`.  
  
**Returns:** The struct type or null if not found.

### .getSubBuildOutput( node : [Node](Node.html) ) : string

Returns the output node of a sub-build layer.

**node** |  The node to get the output from.  
---|---  
  
**Returns:** The output node name.

### .getSubBuildProperty( property : string, node : [Node](Node.html) ) : string

Returns the sub-build property name for the given property and node.

**property** |  The property name. Default is `''`.  
---|---  
**node** |  The node to get the sub-build from. Default is `null`.  
  
**Returns:** The sub-build property name.

### .getTernary( condSnippet : string, ifSnippet : string, elseSnippet : string ) : string (abstract) 

Returns the native snippet for a ternary operation. E.g. GLSL would output a ternary op as `cond ? x : y` whereas WGSL would output it as `select(y, x, cond)`

**condSnippet** |  The condition determining which expression gets resolved.  
---|---  
**ifSnippet** |  The expression to resolve to if the condition is true.  
**elseSnippet** |  The expression to resolve to if the condition is false.  
  
**Returns:** The resolved method name.

### .getType( type : string ) : string

It might be necessary to convert certain data types to different ones so this method can be used to hide the conversion.

**type** |  The type.  
---|---  
  
**Returns:** The updated type.

### .getTypeFromArray( array : TypedArray ) : string

Returns the type for a given typed array.

**array** |  The typed array.  
---|---  
  
**Returns:** The type.

### .getTypeFromAttribute( attribute : [BufferAttribute](BufferAttribute.html) ) : string

Returns the type for a given buffer attribute.

**attribute** |  The buffer attribute.  
---|---  
  
**Returns:** The type.

### .getTypeFromLength( length : number, componentType : string ) : string

Returns the data type for the given the length and component type.

**length** |  The length.  
---|---  
**componentType** |  The component type. Default is `'float'`.  
  
**Returns:** The type.

### .getTypeLength( type : string ) : number

Returns the length for the given data type.

**type** |  The data type.  
---|---  
  
**Returns:** The length.

### .getUniformBufferLimit() : number

Returns the maximum number of bytes available for uniform buffers.

**Returns:** The maximum number of bytes available for uniform buffers.

### .getUniformFromNode( node : [UniformNode](UniformNode.html), type : string, shaderStage : 'vertex' | 'fragment' | 'compute' | 'any', name : string ) : [NodeUniform](NodeUniform.html)

Returns an instance of [NodeUniform](NodeUniform.html) for the given uniform node.

**node** |  The uniform node.  
---|---  
**type** |  The uniform type.  
**shaderStage** |  The shader stage. Default is `this.shaderStage`.  
**name** |  The name of the uniform. Default is `null`.  
  
**Returns:** The node uniform.

### .getUniforms( shaderStage : 'vertex' | 'fragment' | 'compute' | 'any' ) : string (abstract) 

Returns the uniform definitions as a shader string for the given shader stage.

**shaderStage** |  The shader stage.  
---|---  
  
**Returns:** The uniform code section.

### .getVar( type : string, name : string, count : number ) : string

Returns a single variable definition as a shader string for the given variable type and name.

**type** |  The variable's type.  
---|---  
**name** |  The variable's name.  
**count** |  The array length. Default is `null`.  
  
**Returns:** The shader string.

### .getVarFromNode( node : [VarNode](VarNode.html), name : string, type : string, shaderStage : 'vertex' | 'fragment' | 'compute' | 'any', readOnly : boolean ) : [NodeVar](NodeVar.html)

Returns an instance of [NodeVar](NodeVar.html) for the given variable node.

**node** |  The variable node.  
---|---  
**name** |  The variable's name. Default is `null`.  
**type** |  The variable's type. Default is `node.getNodeType( this )`.  
**shaderStage** |  The shader stage. Default is `this.shaderStage`.  
**readOnly** |  Whether the variable is read-only or not. Default is `false`.  
  
**Returns:** The node variable.

### .getVars( shaderStage : 'vertex' | 'fragment' | 'compute' | 'any' ) : string

Returns the variable definitions as a shader string for the given shader stage.

**shaderStage** |  The shader stage.  
---|---  
  
**Returns:** The variable code section.

### .getVaryingFromNode( node : [VaryingNode](VaryingNode.html) | [PropertyNode](PropertyNode.html), name : string, type : string, interpolationType : string, interpolationSampling : string ) : [NodeVar](NodeVar.html)

Returns an instance of [NodeVarying](NodeVarying.html) for the given varying node.

**node** |  The varying node.  
---|---  
**name** |  The varying's name. Default is `null`.  
**type** |  The varying's type. Default is `node.getNodeType( this )`.  
**interpolationType** |  The interpolation type of the varying. Default is `null`.  
**interpolationSampling** |  The interpolation sampling type of the varying. Default is `null`.  
  
**Returns:** The node varying.

### .getVaryings( shaderStage : 'vertex' | 'fragment' | 'compute' | 'any' ) : string (abstract) 

Returns the varying definitions as a shader string for the given shader stage.

**shaderStage** |  The shader stage.  
---|---  
  
**Returns:** The varying code section.

### .getVectorFromMatrix( type : string ) : string

Returns the vector type for a given matrix type.

**type** |  The matrix type.  
---|---  
  
**Returns:** The vector type.

### .getVectorType( type : string ) : string

Returns the vector type for a given type.

**type** |  The type.  
---|---  
  
**Returns:** The vector type.

### .getVertexIndex() : string (abstract) 

Returns the vertexIndex input variable as a native shader string.

**Returns:** The instanceIndex shader string.

### .hasGeometryAttribute( name : string ) : boolean

Whether the given attribute name is defined in the geometry or not.

**name** |  The attribute name.  
---|---  
  
**Returns:** Whether the given attribute name is defined in the geometry.

### .includes( node : [Node](Node.html) ) : boolean

Whether the given node is included in the internal array of nodes or not.

**node** |  The node to test.  
---|---  
  
**Returns:** Whether the given node is included in the internal array of nodes or not.

### .increaseUsage( node : [Node](Node.html) ) : number

Calling this method increases the usage count for the given node by one.

**node** |  The node to increase the usage count for.  
---|---  
  
**Returns:** The updated usage count.

### .isAvailable( name : string ) : boolean (abstract) 

Whether the requested feature is available or not.

**name** |  The requested feature.  
---|---  
  
**Returns:** Whether the requested feature is supported or not.

### .isDeterministic( node : [Node](Node.html) ) : boolean

Returns whether a Node or its flow is deterministic, useful for use in `const`.

**node** |  The varying node.  
---|---  
  
**Returns:** Returns true if deterministic.

### .isFilteredTexture( texture : [Texture](Texture.html) ) : boolean

Whether the given texture is filtered or not.

**texture** |  The texture to check.  
---|---  
  
**Returns:** Whether the given texture is filtered or not.

### .isFlatShading() : boolean

Whether the material is using flat shading or not.

**Returns:** Whether the material is using flat shading or not.

### .isFlipY() : boolean (abstract) 

Whether to flip texture data along its vertical axis or not. WebGL needs this method evaluate to `true`, WebGPU to `false`.

**Returns:** Whether to flip texture data along its vertical axis or not.

### .isInteger( type : string ) : boolean

Returns the type is an integer type.

**type** |  The type.  
---|---  
  
**Returns:** Whether the type is an integer type or not.

### .isMatrix( type : string ) : boolean

Whether the given type is a matrix type or not.

**type** |  The type to check.  
---|---  
  
**Returns:** Whether the given type is a matrix type or not.

### .isOpaque() : boolean

Whether the material is opaque or not.

**Returns:** Whether the material is opaque or not.

### .isReference( type : string ) : boolean

Whether the given type is a reference type or not.

**type** |  The type to check.  
---|---  
  
**Returns:** Whether the given type is a reference type or not.

### .isVector( type : string ) : boolean

Whether the given type is a vector type or not.

**type** |  The type to check.  
---|---  
  
**Returns:** Whether the given type is a vector type or not.

### .needsPreviousData() : boolean

Returns `true` if data from the previous frame are required. Relevant when computing motion vectors with [VelocityNode](VelocityNode.html).

**Returns:** Whether data from the previous frame are required or not.

### .needsToWorkingColorSpace( texture : [Texture](Texture.html) ) : boolean (abstract) 

Checks if the given texture requires a manual conversion to the working color space.

**texture** |  The texture to check.  
---|---  
  
**Returns:** Whether the given texture requires a conversion to working color space or not.

### .registerDeclaration( node : Object )

Registers a node declaration in the current shader stage.

**node** |  The node to be registered.  
---|---  
  
### .removeActiveStack( stack : [StackNode](StackNode.html) )

Removes the active stack from the internal stack.

**stack** |  The stack node to remove.  
---|---  
  
### .removeChain( node : [Node](Node.html) )

Removes the given node from the internal node chain.

**node** |  The node to remove.  
---|---  
  
### .removeFlowTab() : [NodeBuilder](NodeBuilder.html)

Removes a tab.

**Returns:** A reference to this node builder.

### .removeStack() : [StackNode](StackNode.html)

Removes the last stack node from the internal stack.

**Returns:** The removed stack node.

### .removeSubBuild() : [SubBuildNode](SubBuildNode.html)

Removes the last sub-build layer from the node builder.

**Returns:** The removed sub-build layer.

### .setActiveStack( stack : [StackNode](StackNode.html) )

Adds an active stack to the internal stack.

**stack** |  The stack node to add.  
---|---  
  
### .setBuildStage( buildStage : 'setup' | 'analyze' | 'generate' )

Sets the current build stage.

**buildStage** |  The build stage to set.  
---|---  
  
### .setCache( cache : [NodeCache](NodeCache.html) )

Sets builder's cache.

**cache** |  The cache to set.  
---|---  
  
### .setContext( context : Object )

Sets builder's context.

**context** |  The context to set.  
---|---  
  
### .setHashNode( node : [Node](Node.html), hash : number )

The builder maintains each node in a hash-based dictionary. This method sets the given node (value) with the given hash (key) into this dictionary.

**node** |  The node to add.  
---|---  
**hash** |  The hash of the node.  
  
### .setShaderStage( shaderStage : 'vertex' | 'fragment' | 'compute' | 'any' )

Sets the current shader stage.

**shaderStage** |  The shader stage to set.  
---|---  
  
### .sortBindingGroups()

Sorts the bind groups and updates [NodeBuilder#bindingsIndexes](NodeBuilder.html#bindingsIndexes).

## Source

[src/nodes/core/NodeBuilder.js](https://github.com/mrdoob/three.js/blob/master/src/nodes/core/NodeBuilder.js)
