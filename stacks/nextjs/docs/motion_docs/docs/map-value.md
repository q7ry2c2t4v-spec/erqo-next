# mapValue

> Source: https://motion.dev/docs/map-value

`mapValue` creates a new read-only [motion value](./motion-value) that maps the output of a numerical motion value to a range of numbers, colors or complex strings.

const x = motionValue(100)

  

// Fade out outside the 0-100 range

const opacity = mapValue(x, [-100, 0, 100, 200], [0, 1, 1, 0])

  

// Shift color when fading out

const backgroundColor = mapValue(opacity, [0, 1], ["#f00", "#00f"])

## Usage

Import `mapValue` from `"motion"`:

import { mapValue } from "motion"

`mapValue` accepts a **numerical** motion value, an input range, and an output range:

const x = motionValue(0)

const opacity = mapValue(x, [-100, 0, 100, 200], [0, 1, 1, 0])

  * Both ranges **must always be the same length**.

  * The **input range** must always be a linear series of numbers, either counting up or counting down.

  * The **output range** can be a non-linear series of numbers, colors, or complex strings.

When mapping to complex strings, the format of each string must be the same in each keyframe, with the same number of numbers and colors, all in the same order:
    
    
    const boxShadow = mapValue(
      progress,
      [0, 1],
      ["0px 0px 0px rgba(0, 0, 0, 0)", "10px 10px 5px rgba(0, 0, 0, 0.3)"]
    )

### Unclamped ranges

By default, `mapValue` clamps the output value to the ranges provided:
    
    
    const progress = motionValue(3)
    const double = mapValue(progress, [0, 1], [0, 2])
    
    double.get() // progress clamped to 1, outputs 2

By passing the `{ clamp: false }` option, we can unclamp this interpolation:
    
    
    const progress = motionValue(3)
    const double = mapValue(progress, [0, 1], [0, 2], { clamp: false })
    
    double.get() // 6
