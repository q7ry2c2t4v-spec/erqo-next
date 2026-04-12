# Cursor

> Source: https://motion.dev/docs/cursor

Checking Motion+ status…

Cursor

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

`Cursor` is a powerful React component for building creative and interactive cursor effects. Effortlessly replace the default browser cursor, create engaging follow-cursor animations, or add magnetic snapping to UI elements.

Built on Motion's [layout animations](./react-layout-animations), `Cursor` is performant and full customisable with variants, CSS and custom React components.

<Cursor />

`Cursor` is exclusive to [Motion+](../plus) members. Motion+ is a one-time payment, lifetime membership that unlocks exclusive components, premium examples and access to a private Discord community.

## Features

  * **Two modes:** Easily switch between replacing the default cursor or creating a "follow" cursor effect.

  * **State-aware:** Automatically adapts its appearance when hovering over links, buttons, or selectable text, and when pressed.

  * **Magnetic:** Make the cursor snap to interactive elements on hover for a tactile feel.

  * **Customisable:** Use CSS, Motion variants, and custom React components to create any cursor you can imagine.

  * **Accessible:** Can be disabled for users who prefer reduced motion.

## Install

First, add the `motion-plus` package to your project using your [private token](https://plus.motion.dev). You need to be a [Motion+ member](../plus) to generate a private token.
    
    
    npm install "https://api.motion.dev/registry.tgz?package=motion-plus&version=2.0.2&token=YOUR_AUTH_TOKEN"

## Usage

The `Cursor` component is used for both custom cursor and follow cursor effects:
    
    
    import { Cursor } from "motion-plus/react"

When `Cursor` is rendered, a default custom cursor will render on the page, hiding the browser's default cursor.
    
    
    <Cursor />

You can remove the cursor and restore the browser cursor at any time by removing the component.
    
    
    {isCursorVisible ? <Cursor /> : null}

### Styling

By default, the cursor is a neutral grey color. It's possible to change the cursor's styles using CSS.
    
    
    <Cursor className="my-cursor" style={{ backgroundColor: "red" }} />

####
