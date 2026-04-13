# SDK State

> Source: https://motion.dev/docs/studio-sdk-state

The [Motion Studio SDK](./studio-sdk) provides some basic state models for handling animation editing.

## `TransitionState`

Transitions represent Motion's animation options. 

`TransitionState` is always created with both `easing` and `spring` values, with `type` determining which is currently active, to allow for easy switching between transition type without dropping state.

import { TransitionState } from "motion-studio"

  

const state = new TransitionState()

The format is as following:

type TransitionType = "easing" | "spring"

  

interface EasingConfig {

duration: number

ease: BezierDefinition

}

  

interface SpringConfig {

duration: number

bounce: number

stiffness: number

damping: number

mass: number

type: "time" | "physics"

isVisualDuration: boolean

}

  

interface TransitionState {

type: TransitionType

easing: EasingConfig

spring: SpringConfig

}

## URL serialisation

These utilities allow you to serialise the `TransitionState` into a URL query parameter, and back out of a URL, enabling shareable configuration links.

### `toShareQueryString`

Serialises a `TransitionState` object into a URL query string.
    
    
    import { toShareQueryString } from "motion-studio"
    
    const queryString = toShareQueryString(state)
    // Output: "transition=%7B%22type%22%3A%22spring%22...%7D"

### `fromShareURL`

Parses a new `TransitionState` out of a full URL string. Returns `null` if the `transition` parameter is missing or invalid.
    
    
    import { fromShareURL } from "motion-studio"
    
    const state = fromShareURL(window.location.href)
