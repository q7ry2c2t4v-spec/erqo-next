# scrambleText

> Source: https://motion.dev/docs/scramble-text

Checking Motion+ status…

scrambleText

is exclusive to Motion+

290+ examples & 40+ tutorials

Premium APIs

Motion Studio editing tools

`alpha`

Discord community

Early access

Lifetime updates

[Get Motion+ for instant access](../plus)

One-time payment, lifetime updates

Already joined?

[Login](https://plus.motion.dev/login?redirect=)

`scrambleText` is a 1kb function that provides scramble text animations for vanilla JavaScript. It works with DOM elements or `[MotionValues](./motion-value)`.

import { scrambleText } from "motion-plus"

  

scrambleText("#title", { duration: 1 })

`scrambleText` is exclusive to [Motion+](../plus) members. Motion+ is a one-time payment, lifetime membership that unlocks exclusive components, premium examples and access to a private Discord community.

## Features

  * **Stagger:** Use Motion's `[stagger](./stagger)` function for both `delay` and `duration` to create letter-by-letter reveal effects.

  * **Playback control:** Returns playback controls to pause, play, hard stop or finish your animations.

  * **Customisable characters:** Use the default alphanumeric set, or provide custom characters (including emoji).

## Install

First, add the `motion-plus` package to your project using your [private token](https://plus.motion.dev). You need to be a [Motion+ member](../plus) to generate a private token.
    
    
    npm install "https://api.motion.dev/registry.tgz?package=motion-plus&version=2.6.1&token=YOUR_AUTH_TOKEN"

## Usage

Pass an element or CSS selector to scramble its text content:
    
    
    import { scrambleText } from "motion-plus-dom"
    
    // With selector
    scrambleText("#title", { duration: 1 })
    
    // With element reference
    const element = document.querySelector(".text")
    scrambleText(element, { duration: 1 })

### With `MotionValue`

Alternatively, you can pass a `MotionValue<string>` to `scrambleText`. It will animate back to the value as read when the animation starts.
    
    
    import { scrambleText } from "motion-plus-dom"
    import { motionValue } from "motion"
    
    const text = motionValue("Hello world!")
    
    // Subscribe to changes
    text.on("change", (latest) => {
      document.querySelector("#title").textContent = latest
    })
    
    scrambleText(text, { duration: 1 })

### Stagger

Use Motion's `[stagger()](./stagger)` function to reveal characters one by one:
    
    
    import { scrambleText } from "motion-plus-dom"
    import { stagger } from "motion"
    
    // Start scrambling at the same time, reveal with stagger
    scrambleText(element, {
      duration: stagger(0.05, { startDelay: 1 })
    })

#### Delay stagger

Stagger when each character starts scrambling:
    
    
    // Chars start scrambling one-by-one, all reveal after 1s
    scrambleText(element, {
      delay: stagger(0.1),
      duration: 1
    })

#### Direction

Use stagger's `from` option to control reveal direction:
    
    
    scrambleText(element, {
      delay: stagger(0.05, { from: "center" }),
      duration: 0.5
    })

### Infinite scramble

Set `duration` to `Infinity` for continuous scrambling until stopped:
    
    
    hover(element, () => {
      const controls = scrambleText(element, { duration: Infinity })
    
      return () => {
        controls.finish() // Reveal while preserving stagger
        // or controls.stop() for immediate reveal
      }
    })

### Custom characters
    
    
    // Binary effect
    scrambleText(element, { chars: "01", duration: 1 })
    
    // Symbols
    scrambleText(element, {
      chars: "!@#$%^&*()_+-=[]{}|;:,.<>?/~`░▒▓█▀▄■□▪▫●○◆◇◈◊※†‡"
    })
    
    // Emoji (use array for multi-byte characters)
    scrambleText(element, {
      chars: ["😀", "😃", "😄", "😁", "😆", "😅"]
    })

Character presets:
    
    
    const symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`░▒▓█▀▄■□▪▫●○◆◇◈◊※†‡"
    const blocks = "█▓▒░"
    const binary = "01"
    const hex = "0123456789ABCDEF"
    const katakana = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
    const dots = "⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏"
