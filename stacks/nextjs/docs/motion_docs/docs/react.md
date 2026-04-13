# Get started with Motion for React

> Source: https://motion.dev/docs/react

Presented by

[Clerk](https://clerk.com?utm_campaign=motion-react-start-guide)

**Motion for React** (previously Framer Motion) is a React animation library for building smooth, production-grade UI animations. You can start with simple prop-based animations before growing to layout, gesture and scroll animations.

Motion's hybrid engine runs animations natively in the browser using the Web Animations API and ScrollTimeline for 120fps performance. When you need capabilities those APIs can't provide (like spring physics, interruptible keyframes, or gesture tracking) it seamlessly falls back to JavaScript.

Motion is trusted by companies like [Framer](https://framer.com) and [Figma](https://figma.com) to power animations for their millions of users, and has over 30 million downloads per month on [npm](https://www.npmjs.com/package/framer-motion).

In this guide, we'll learn **why** and **when** you should use Motion, how to **install** it, and give you an overview of its main features.

## Why Motion for React?

React gives you the power to build dynamic user interfaces, but orchestrating complex, performant animations can be a challenge. Motion is a production-ready React animation library designed to solve this problem, making it simple to create everything from beautiful micro-interactions to complex, gesture-driven animations.

import { motion } from "motion/react"

function Component() {

return <motion.button animate={{ opacity: 1 }} />

}

### Key advantages

Here’s when it’s the right choice for your project.

  * **Built for React.** While other animation libraries like [GSAP](./gsap-vs-motion) are messy to integrate with React, Motion's declarative API is a natural fit. Animations can be linked directly to state and props.

  * **Hardware-acceleration.** Motion leverages the same high-performance browser animations as CSS, ensuring your UIs stay smooth and snappy. 120fps animations with a much simpler and more expressive API.

  * **Animate anything.** CSS has hard limits. Values you can't animate, keyframes you can't interrupt, staggers that must be hardcoded. Motion provides a single, consistent API that scales from simple to complex.

  * **App-like gestures.** Standard CSS `:hover` events are unreliable on touch devices. Motion provides robust, cross-device gesture recognisers for tap, drag, and hover that feel native and intuitive on any device.

  * **Production ready.** Built on TypeScript, surrounded by an extensive test suite, and fully tree-shakable so you only include what you import.

### When is CSS a better choice?

For simple, self-contained effects (like a color change on hover) a standard CSS transition is a lightweight solution. The strength of Motion is that it can do these simple kinds of animations but also scale to anything you can imagine. All with the same easy to write and maintain API.

## Install

Motion is available via [npm](https://www.npmjs.com/package/motion):
    
    
    npm install motion

Features can now be imported via `"motion/react"`:
    
    
    import { motion } from "motion/react"

Prefer to install via CDN, or looking for framework-specific instructions? Check out our [full installation guide](./react-installation).

## Create your first animation

The `<motion />` component is the foundation of Motion for React. Prefix any HTML or SVG tag with `motion.` to unlock animation props like `animate`, `whileHover`, and `exit`:
    
    
    <motion.ul animate={{ rotate: 360 }} />

When values in `animate` change, Motion automatically transitions between them. 

Physical properties like `x` and `scale` use spring physics by default; visual properties like `opacity` use tween easing. Override the animation type, duration, easing, or delay via [the ](./react-transitions)`[transition](./react-transitions)`[ prop](./react-transitions):
    
    
    <motion.div
      animate={{
        scale: 2,
        transition: { duration: 2 }
      }}
    />

[Learn more about React animation](./react-animation)

If you're the kind of developer who learns better by doing, check out our library of [Basics examples](https://motion.dev/examples#basics). Each comes complete with a live demo and copy/paste source code.

## Enter animation

When a component enters the page, it will automatically animate to the values defined in the `animate` prop.

You can provide values to animate from via the `initial` prop (otherwise these will be read from the DOM).
    
    
    <motion.button initial={{ scale: 0 }} animate={{ scale: 1 }} />

Or disable this initial animation entirely by setting `initial` to `false`.
    
    
    <motion.button initial={false} animate={{ scale: 1 }} />

## Hover & tap animation

`<motion />` extends React's event system with powerful [gesture animations](./react-gestures). It currently supports hover, tap, focus, and drag.
    
    
    <motion.button
      whileHover={{ scale: 1.1 }}
      whileTap={{ scale: 0.95 }}
      onHoverStart={() => console.log('hover started!')}
    />

Motion's gestures are designed to feel better than using CSS or JavaScript events alone. 

## Scroll animation

Motion supports both types of [scroll animations](./react-scroll-animations): **Scroll-triggered** and **scroll-linked**.

To trigger an animation on scroll, the `whileInView` prop defines a state to animate to/from when an element enters/leaves the viewport:
    
    
    <motion.div
      initial={{ backgroundColor: "rgb(0, 255, 0)", opacity: 0 }}
      whileInView={{ backgroundColor: "rgb(255, 0, 0)", opacity: 1 }}
    />

Whereas to link a value directly to scroll position, it's possible to use `MotionValue`s via `useScroll`.
    
    
    const { scrollYProgress } = useScroll()
    
    return <motion.div style={{ scaleX: scrollYProgress }} />

## Layout animation

Motion's [layout animation](./react-layout-animations) engine detects layout changes (size, position, reorder) and smoothly animates between states using transforms. Unlike basic "FLIP" implementations, it does so while correcting for scale-distortion. 

It's as easy as applying the `layout` prop.
    
    
    <motion.div layout />

Or to animate between completely different elements, a `layoutId`:
    
    
    <motion.div layoutId="underline" />

## Exit animations

By wrapping `motion` components with `<AnimatePresence>` we gain access to [exit animations](./react-animate-presence). This allows us to animate elements as they're removed from the DOM.
    
    
    <AnimatePresence>
      {show ? <motion.div key="box" exit={{ opacity: 0 }} /> : null}
    </AnimatePresence>

## SVG animations

Motion has full support for [SVG animations](./react-svg-animation), including support for animating `viewBox` and special values for simple path drawing effects.
    
    
    <motion.circle animate={{ pathLength: 1 }} />

## Development tools

Want an AI that knows every Motion API and can generate animations on demand? Or visual animation editing, directly in your code editor? [Motion Studio](../studio) provides all that and more. Enhance your workflow tools with an [AI-searchable examples database](./studio-ai-context), a [CSS and Motion transition editor](./studio-visual-controls), [performance audit skill](./animation-performance-audit), and more.

### Install Motion Studio 

One-click install for Cursor:

[Add Extension](cursor:extension/motion.motion-vscode-extension)

[Add MCP](https://cursor.com/en-US/install-mcp?name=motion&config=eyJjb21tYW5kIjoibnB4IC15IGh0dHBzOi8vYXBpLm1vdGlvbi5kZXYvcmVnaXN0cnkudGd6P3BhY2thZ2U9bW90aW9uLXN0dWRpby1tY3AmdmVyc2lvbj1sYXRlc3QifQ%3D%3D)

Motion Studio is also compatible with VS Code, Google Antigravity and more. [See full installation guide](./studio-install). 

#### Stay in the loop

Sign up for the Motion newsletter.

Subscribe

## Learn next

That covers the core building blocks. Here's where to go next based on what you want to build and your learning style.

The [React animation](./react-animation) guide will teach you more about the different types of animations you can build with this React animation library. 

Or, you can learn by doing, diving straight into our collection of [examples](https://motion.dev/examples?platform=react#basics). Each comes complete with full source code that you can copy-paste into your project.
