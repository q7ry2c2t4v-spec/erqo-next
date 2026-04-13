# Codegen

> Source: https://motion.dev/docs/studio-sdk-codegen

[Motion Studio SDK](./studio-sdk)'s code generation functions allow you to export editor state into code for CSS or Motion.

## Transition generation

Both CSS and Motion transition export functions support:

  * **Easing:** Generated from `ease` and `duration`.

  * **Spring (Time)** : Generated from `duration`/`visualDuration` and `bounce`

  * **Spring (Physical)** : Generated from `stiffness`, `mass`, and `damping`.

`ease` currently only supports bezier curve definitions, for instance `[0.3, 0.05, 0.45, 1]`. Support for easing functions is coming soon.

### `toCSSTransition`

Generates a partial CSS `transition` definition for a given `[TransitionState](./studio-sdk-state)`.

import { toCSSTransition } from "motion-studio"

  

const cssString = toCSSTransition(state)

// Output: "0.3s cubic-bezier(0.3, 0.05, 0.45, 1)"

This string can then be used as part of a bigger CSS `transition` definition:

`transition: opacity ${cssString}`

Springs will be returned as `linear()` easing curves.

### `toMotionTransition`

Generates a Motion `transition` as a string. This can then be copy/pasted or otherwise inserted into Motion code.

import { toMotionTransition } from "motion-studio"

  

const code = toMotionTransition(state)

/* Output:

{

type: "spring",

visualDuration: 0.3,

bounce: 0.2

}

*/
