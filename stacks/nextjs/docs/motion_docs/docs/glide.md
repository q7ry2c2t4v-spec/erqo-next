# glide

> Source: https://motion.dev/docs/glide

**Note:** This API is **deprecated**. You can use `type: "inertia"` with the new `[animate()](./animate)`[ function](./animate).

—-

`glide` can animate transforms using momentum physics. This is great for creating scroll momentum animations.

import { animate, glide } from "motion"

  

animate(

element,

{ x: 500 },

{ easing: glide() }

)

**Note:** `glide` is a simulation, so provided target keyframes and `duration` will be overridden.

## Velocity

`glide` will automatically pass velocity from any running animations into the next one, so interrupting an animation will feel natural.

This can be overridden by manually passing `velocity` to `glide`. `velocity` is measured as units per second.

animate(

"#carousel",

{ x: 100 },

{ easing: glide({ velocity: 1000 }) }

)

If you want to pass a different `velocity` per value (for instance for animating at the end of a pointer gesture) you can create value-specific options:

animate(

"#ball",

{ x: 0, y: 0 },

{

x: { easing: glide({ velocity: 200 }) },

y: { easing: spring({ velocity: 500 }) }

}

)

### Boundaries

By setting `min` and/or `max` you can set boundaries to the glide animation. If the animated value exceeds these boundaries, a [spring](./spring) animation will start to catch the value and animate it to the exceeded boundary.
    
    
    glide({ min: -100, max: 100 })

### Options

### `velocity`

**Default:** `0` or the value's current velocity

The velocity (in units per second) at which to start the glide animation.
    
    
    glide({ velocity: 1000 })

### `power`

**Default:** `0.8`

`power` influences how much of the initial `velocity` is factored into the animation, and thus how far the animation will glide.

Higher values will throw the animation further and feel lighter, whereas lower values will feel heavier.
    
    
    glide({ power: 1 })

### `decay`

**Default:** `0.325`

A time constant (in seconds) used to calculate velocity decay. Higher values lead to longer animations with more gradual deceleration and a lighter feel.
    
    
    glide({ decay: 0.5 })

### `restSpeed`

**Default:** `2`, or `0.05` for `scale`

A speed (in absolute units per second) below which the spring animation is considered finished.
    
    
    spring({ restSpeed: 1 })

### `restDistance`

**Default:** `0.5` or `0.01`for `scale`

A distance from the animation target, below which the spring animation is considered finished.
    
    
    spring({ restDistance: 0.1 })

### `changeTarget`

The glide animation automatically calculates a target to animate to. By setting `changeTarget`, you can take this calculated target and return a new one.

For instance, the function in the following example will snap the target to the next `100`:
    
    
    const roundTo = 100
    
    glide({
      changeTarget: (target) => Math.ceil(target / roundTo) * roundTo
    })

### `min`

A minimum boundary for the glide animation. If the animated value exceeds this boundary, a spring animation will take over to snap the value to `min`.
    
    
    glide({ min: -100 })

### `max`

A maximum boundary for the glide animation. If the animated value exceeds this boundary, a spring animation will take over to snap the value to `max`.
    
    
    glide({ max: 100 })

### `bounceStiffness`

**Default:** `100`

The attraction force of a spring used if the animation exceeds the boundaries defined by `min`/`max`. Higher values create faster, sharper movement.
    
    
    glide({ min: 100, bounceStiffness: 500 })

### `bounceDamping`

**Default:** `10`

The opposing force of a spring. Higher values reduce the bounciness of the spring.
    
    
    glide({ max: 100, bounceDamping: 30 })

## Limitations

There are currently some limitations with the `spring` easing.

### Duration

Springs with `damping: 0` can last an infinite amount of time, but the Web Animations API needs a finite `duration`. So springs currently max out at 10 seconds (which is more than long enough for the vast majority of UI animations).  
Increase `damping` relative to `stiffness` to decrease the duration of your animation.

### Timeline keyframes

`spring` is supported in `timeline` but independent transforms **must** be defined with start and end keyframes: `{ x: [0, 100] }`.

## No hardware acceleration

`spring` only works with independent transforms, which are not yet hardware accelerated in browsers.
