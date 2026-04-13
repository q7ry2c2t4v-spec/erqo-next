# attrEffect

> Source: https://motion.dev/docs/attr-effect

`attrEffect` applies the output of [motion values](./motion-value) to the attributes of one or more elements.

When these motion values update, the element will re-render once per frame during the [render step of the frameloop](./frame).

const width = motionValue(100)

  

attrEffect("rect", { width })

`attrEffect` will automatically handle casing for `aria` and `data` attributes, converting camel case to kebab case.

const value = motionValue("#fff")

  

attrEffect(counter, {

ariaValuenow: value,

dataValue: value

})

  

// <div aria-valuenow="#fff" data-value="#fff">

It will also dynamically set attributes via their JavaScript setter, if available, for improved type-safety and performance.

## Usage

Import `attrEffect` from `"motion"`:

import { attrEffect } from "motion"

`attrEffect` accepts an element, list of elements, or CSS selector, plus a map of motion values:

const progress = motionValue(0.5)

  

attrEffect("#progress", { "data-progress": progress })

When any of the motion values update, the element(s) will re-render on the next animation frame:

progress.set(1)

animate(progress, 1)

Each motion value can be applied to any number of attributes, on any number of elements.

Any motion value can be provided, including those defined by `[mapValue](./map-value)` and `[transformValue](./transform-value)`.

### Cancel

`attrEffect` returns a cleanup function which, when called, will stop applying changes to the motion values to the element:
    
    
    const cx = motionValue(0)
    const cy = motionValue(0)
    const cancel = attrEffect("circle", { cx, cy })
    
    cancel()
