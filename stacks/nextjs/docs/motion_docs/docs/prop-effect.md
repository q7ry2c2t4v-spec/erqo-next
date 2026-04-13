# propEffect

> Source: https://motion.dev/docs/prop-effect

`propEffect` applies the output of [motion values](./motion-value) to the properties of an object.

When these motion values update, the element will re-render once per frame during the [render step of the frameloop](./frame).

const pos = { x: 0, y: 0, z: 0 }

const x = motionValue(0)

  

propEffect(pos, { x })

  

// Set x on pos to 100

x.set(100)

  

// Animate x on pos to 200

animate(x, 200)

This can also be used for rendering Three.js props:

const cube = new THREE.Mesh(geometry, material)

const x = motionValue(0)

  

propEffect(cube.position, { x })

## Usage

Import `propEffect` from `"motion"`:

import { propEffect } from "motion"

`propEffect` accepts an a single object, plus a map of motion values:

const data = { opacity: 0, x: 100 }

const opacity = motionValue(0)

  

propEffect(data, { opacity })

When any of the motion values update, the element(s) will re-render on the next animation frame:

opacity.set(1)

Each motion value can be applied to any number of styles, and any number of elements.

Any motion value can be provided, including those defined by `[mapValue](./map-value)` and `[transformValue](./transform-value)`.

### Cancel

`propEffect` returns a cleanup function which, when called, will stop applying changes to the motion values to the element:
    
    
    const rotateX = motionValue(0)
    const cancel = propEffect(threeRotation, { x: rotateX })
    
    cancel()
