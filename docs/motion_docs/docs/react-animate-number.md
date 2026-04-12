# AnimateNumber

> Source: https://motion.dev/docs/react-animate-number

Checking Motion+ status…

AnimateNumber

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

`AnimateNumber` is a lightweight (2.5kb) React component for creating beautiful number animations with Motion. It's perfect for counters, dynamic pricing, countdowns, and more. 

<AnimateNumber>{count}</AnimateNumber>

Built on top of Motion's powerful layout animations, `AnimateNumber` allows you to leverage all of Motion's existing transition settings, like `spring` and `tween`, to create fluid and engaging effects.

`AnimateNumber` is exclusive to [Motion+](../plus) members. Motion+ is a one-time payment, lifetime membership that unlocks exclusive components, premium examples and access to a private Discord community.

## Features

  * **Built on Motion:** Leverages Motion's robust animation engine, allowing you to use familiar `transition` props like `spring`, `duration`, and `ease`.

  * **Lightweight:** Adds only 2.5kb on top of Motion.

  * **Advanced formatting:** Uses the built-in `Intl.NumberFormat` for powerful, locale-aware number formatting (e.g., currency, compact notation).

  * **Customisable:** Provides distinct CSS classes for each part of the number (prefix, integer, fraction, suffix) for full styling control.

## Install

First, add the `motion-plus` package to your project using your [private token](https://plus.motion.dev). You need to be a [Motion+ member](../plus) to generate a private token.
    
    
    npm install "https://api.motion.dev/registry.tgz?package=motion-plus&version=2.10.0&token=YOUR_AUTH_TOKEN"

## Usage

`AnimateNumber` accepts a single child, a number.
    
    
    <AnimateNumber>300</AnimateNumber>

When this number changes, it'll animate to its latest value.
    
    
    import { AnimateNumber } from "motion-plus/react"
    
    function Counter() {
      const [count, setCount] = useState(0)
    
      return (
        <>
          <button onClick={() => setCount(count + 1)}>Increment</button>
          <AnimateNumber>{count}</AnimateNumber>
        </>
      )
    }

### Customise animation

The `transition` prop accepts Motion for React's [transition options](./react-transitions).
    
    
    <AnimateNumber transition={{ type: "spring" }}>

`transition` accepts value-specific transition settings, so it's possible to set specific transitions for `layout`, `y` and `opacity`:
    
    
    <AnimateNumber transition={{
      layout: { duration: 0.3 },
      opacity: { ease: "linear" },
      y: { type: "spring", visualDuration: 0.4, bounce: 0.2 }
    }}>
