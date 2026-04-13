# springValue

> Source: https://motion.dev/docs/spring-value

`springValue` creates a new [motion value](./motion-value) that reacts to changes with a physics-based spring animation.

`springValue` either accepts a number:

const x = springValue(0)

const y = springValue("100%")

  

// These will go to their new target with a spring animation

x.set(100)

y.set("0%")

  

styleEffect("div", { x, y })

Or another motion value:

const pointerX = motionValue(0)

const x = springValue(pointerX)

  

document.addEventListener("pointerMove", (e) => {

// x will animate these changes with a spring animation

pointerX.set(e.clientX)

})

  

styleEffect("div", { x })

## Usage

`springValue` accepts either a number value or a motion value.

### Number

A number can be provided with or without a unit:
    
    
    import { springValue } from "motion"
    
    const scaleX = springValue(0)
    const rotate = springValue("1turn")

When we've provided a number, we can animate the returned motion value by calling its `.set()`
    
    
    scaleX.set(1)
    rotate.set("2turn")

### Motion value

Alternatively, we can attach a spring onto another motion value by passing it to `springValue`:
    
    
    const opacity = motionValue(1)
    const x = mapValue(opacity, [0, 1], [0, 100])
    const xWithSpring = springValue(x)

## Options

All of the normal Motion [spring options](https://motion.dev/docs/animate#spring) are supported via a second argument.
    
    
    springValue(0, { stiffness: 1000 })

Although `duration` and `visualDuration` are accepted, it's recommended to define springs using the physics-based options `stiffness`, `damping` and `mass`. This is because these options incorporate the velocity of the value for the smoothest and most reactive motion.
