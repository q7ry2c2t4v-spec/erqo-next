# svgEffect

> Source: https://motion.dev/docs/svg-effect

`svgEffect` applies the output of [motion values](./motion-value) to styles and attributes of one or more elements.

When these motion values update, the element will re-render once per frame during the [render step of the frameloop](./frame).

const cx = motionValue(100)

  

svgEffect("circle", { cx })

In addition to regular styles, `svgEffect` also supports simple `0`-`1` progress values for drawing-style animations.

These values can be used with any SVG element that supports `stroke`, for instance `<rect>`, `<path>` etc.

By default, `svgEffect` applies valid styles via `.style`. In cases where there's also a valid attribute equivalent with the same name, these can be set with the `attr` prefix:

const width = motionValue(400)

  

svgEffect("rect", { attrWidth: width })

## Usage

Import `svgEffect` from `"motion"`:
    
    
    import { svgEffect } from "motion"

`svgEffect` accepts an element, list of elements, or CSS selector, plus a map of motion values:
    
    
    const stroke = motionValue("#00f")
    const strokeWidth = motionValue(5)
    
    svgEffect("circle", { strokeWidth, stroke })

When any of the motion values update, the element(s) will re-render on the next animation frame:
    
    
    stroke.set("#f00")
    animate(strokeWidth, 1)

Each motion value can be applied to any number of styles/attributes, and any number of elements.
    
    
    const progress = motionValue(0)
    
    svgEffect("#progress", {
      pathLength: progress,
      pathOffset: progress
    })

Any motion value can be provided, including those defined by `[mapValue](./map-value)` and `[transformValue](./transform-value)`.

### Draw animations

`svgEffect` makes it simple to make "draw"-style animations using the following special values: 

  * `pathLength` controls the line length.

  * `pathSpacing` controls the spacing between line segments.

  * `pathOffset` controls the position of the line along the path.

Each can be set as a progress value between `0`-`1`. 
    
    
    const pathLength = motionValue(0.5)
    
    svgEffect("circle", { pathLength }) // 0.5 = half path length

Draw animations are supported on the following elements:

  * `<circle>`

  * `<ellipse>`

  * `<line>`

  * `<path>`

  * `<polygon>`

  * `<polyline>`

  * `<rect>`

#### Infinite looping

By leaving `pathSpacing` unset, it will be dynamically calculated to allow for infinite looping animations.
    
    
    const pathLength = motionValue(0.5)
    const pathOffset = motionValue(0)
    
    svgEffect("path", { pathLength, pathOffset })
    
    animate(pathOffset, [0, 1], { repeat: Infinity })

### CSS-style transform origin

By default, SVG transform origins are calculated relative to the `viewBox`, which is usually unintuitive and unlike CSS transform origins, which are calculated relative to the element.

`svgEffect` will automatically apply the `transform-box: fill-box` style when a `transform` is detected. This will make the transform origin calculated relative to the element, as in CSS.

This can be overridden by manually setting `transformBox`:
    
    
    svgEffect("path", { transformBox: motionValue("view-box") })

### Cancel

`svgEffect` returns a cleanup function which, when called, will stop applying changes to the motion values to the element:
    
    
    const width = motionValue("0px")
    const cancel = svgEffect("#progress", { width })
    
    cancel()
