# EasingCurve

> Source: https://motion.dev/docs/studio-sdk-easing-curve

`EasingCurve` is a React component that renders a cubic bezier easing curve or easing function as an SVG path. It supports axis lines and customisable styling.

## Usage

### Import

[Once installed](./studio-sdk), import `EasingCurve` from `"motion-studio"`.

import { EasingCurve } from "motion-studio"

### Draw curve

Given a `curve` definition, `EasingCurve` renders a `<path />` (and if `axisWidth` is defined, a `<polyline />` component), that you can render as part of an SVG.

function Component() {

return (

<svg viewBox="0 0 100 100">

<EasingCurve

curve={[0.17, 0.67, 0.83, 0.67]}

width={100}

height={100}

/>

</svg>

)

}

## Props

### `curve`

**Required.** Either an array of valid bezier curve points:

<EasingCurve curve={[0.17, 0.67, 0.83, 0.67]} />

Or as an easing function:
    
    
    import { circIn } from "motion"
    
    <EasingCurve curve={circIn} />

### Layout

`EasingCurve` supports `width`, `height`, `top` and `left` props, defined as pixels, for sizing and positioning the curve.
    
    
    <EasingCurve
      curve={curve}
      width={100}
      height={100}
      top={20}
    />

While it is possible to set `width` and `height` to different values, it is recommended that they are set to the same value as a square aspect ratio is easier to visually understand. In the future these might be replaced with a single `size` prop.

### Line styling

The drawn curve line can be styled using the `color` and `pathWidth` props.
    
    
    <EasingCurve curve={curve} color="#fff" pathWidth={2} />

### Axis styling

The axis lines aren't drawn by default. By setting `axisWidth` and `axisColor` these lines will be drawn with the provided values.
    
    
    <EasingCurve curve={curve} axisWidth={3} axisColor="#333" />

### Transition

To enable transitions between different easing curves, provide a `[transition](./react-transitions)` prop.
    
    
    <EasingCurve curve={curve} transition={{ duration: 0.3 }} />

This is useful for animating between preset curves, but can feel unresponsive if directly editing a curve.
