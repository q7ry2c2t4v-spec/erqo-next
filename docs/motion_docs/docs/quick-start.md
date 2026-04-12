# Get started with Motion

> Source: https://motion.dev/docs/quick-start

Motion is an animation library that's easy to start and fun to master.

Its unique hybrid engine combines the performance of the browser with the limitless potential of a JavaScript engine. This means you can animate anything, like:

  * **HTML/CSS**

  * **SVG** (like path drawing animations) 

  * **WebGL**(3D graphics)

The best part? It's also tiny, with a mini HTML/SVG version of the `animate()` function that's just 2.3kb!

By the end of this quick guide, you'll have installed Motion and made your first animation.

## Install

You can install Motion in two ways: 

  1. A package manager like npm or Yarn (**most popular)**

  2. HTML `script` tag

### Package manager

Motion can be installed via the `"motion"` package.

npm install motion

Then imported in your JavaScript:

import { animate, scroll } from "motion"

### `script` tag 

It's possible to import Motion directly using a `script` tag. This is perfect if you're working with a basic HTML page, or using a no-code tool like Webflow.

Import using the modern `import` syntax:
    
    
    <script type="module">
      import { animate, scroll } from "https://cdn.jsdelivr.net/npm/motion@latest/+esm"
    </script>

Or you can add `Motion` as a global variable using the legacy include:
    
    
    <script src="https://cdn.jsdelivr.net/npm/motion@latest/dist/motion.js"></script>
    <script>
      const { animate, scroll } = Motion
    </script>

It's best practise to replace "latest" in these URLs with a specific version, like `11.11.13`. You can find the latest version in the site footer.

### Create an animation

The "Hello world!" of any animation library is a simple transform animation. 

Let's start by importing the `[animate](./animate)`[ function](./animate).
    
    
    import { animate } from "motion"

`animate` can animate one or more elements. You can either use a [CSS selector](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll#obtaining_a_list_of_matches) (like `".my-class"`) or provide the elements directly:
    
    
    // CSS selector
    animate(".box", { rotate: 360 })
    
    // Elements
    const boxes = document.querySelectorAll(".box")
    
    animate(boxes, { rotate: 360 })

You can see here we're setting `rotate` to `360`. This will rotate the element 360 degrees:

## What can be animated?

Motion lets you animate anything:

  * **CSS properties** (like `opacity`, `transform` and `filter`)

  * **SVG attributes and paths**

  * **Independent transforms** (`x`, `rotateY` etc)

  * **JavaScript objects** (containing strings/colors/numbers)

With Motion, you don't have to worry about achieving the best performance available. When a value can be hardware accelerated, like `opacity`, `filter` or `transform`, it will be.

`animate` isn't limited to HTML. It can animate single values or any kind of object. For example, the rotation of a Three.js object:
    
    
    animate(
      cube.rotation,
      { y: rad(360), z: rad(360) },
      { duration: 10, repeat: Infinity, ease: "linear" }
    )

## Customising animations

Motion comes with smart defaults, so your animations should look and feel great out of the box. But you can further tweak options like:

  * **Duration** (how long the animation lasts)

  * **Delay**(how long it waits before starting)

  * **Easing** (how it speeds up and slows down)

  * **Repeat** (how it repeats, how many times, etc)

    
    
    animate(
      element,
      { scale: [0.4, 1] },
      { ease: "circInOut", duration: 1.2 }
    );

Motion also has amazing [spring animations](./spring) for natural, kinetic animations:
    
    
    animate(
      element,
      { rotate: 90 },
      { type: "spring", stiffness: 300 }
    );

## Stagger animations

When animating multiple elements, it can feel more natural or lively to offset the animations of each. This is called **staggering**.

Motion provides a `stagger` function that can be used to dynamically set `delay`:
    
    
    import { animate, stagger } from "motion"
    
    animate(
      "li",
      { y: 0, opacity: 1 },
      { delay: stagger(0.1) }
    )

## Development tools

[Motion Studio](../studio) provides visual editing and AI tools to enhance your animation development workflow, like inline bezier editing, CSS spring generation and more.

### Install Motion Studio 

One-click install for Cursor:

[Add Extension](cursor:extension/motion.motion-vscode-extension)

[Add MCP](https://cursor.com/en-US/install-mcp?name=motion&config=eyJjb21tYW5kIjoibnB4IC15IGh0dHBzOi8vYXBpLm1vdGlvbi5kZXYvcmVnaXN0cnkudGd6P3BhY2thZ2U9bW90aW9uLXN0dWRpby1tY3AmdmVyc2lvbj1sYXRlc3QifQ%3D%3D)

Motion Studio is also compatible with VS Code, Google Antigravity and more. [See full installation guide](./studio-install). 

### What's next?

You've just learned the basics of Motion and created a simple animation. But there's so much more to discover, like:

  * [**Keyframes and sequences**](./animate): Create more complex animations

  * [**Controls**](./animate): Pause, resume or change animations

  * [**Scroll-linked animations**](./scroll)**:** Link values to scroll position

  * [**Scroll-triggered animations**](./inview): Trigger animations when elements enter the viewport

Or you can dive straight into our [examples](https://motion.dev/examples?platform=js), which include copy & paste source code to add straight to your project.
