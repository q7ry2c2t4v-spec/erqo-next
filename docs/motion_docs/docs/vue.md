# Get started with Motion for Vue

> Source: https://motion.dev/docs/vue

Motion for Vue is a simple yet limitless animation library. It's the only animation library with a **hybrid engine** , capable of hardware accelerated animations.

In this guide, we'll learn how to install Motion Vue and take a whirlwind tour of its main features.

## Why Motion for Vue?

Vue gives you the power to build dynamic user interfaces, but orchestrating complex, performant animations can be a challenge. Motion is a production-ready library designed to solve this, making it simple to create everything from beautiful micro-interactions to complex, gesture-driven animations.

<motion.button :animate="{ opacity: 1 }" />

### Key advantages

Here's when it's the right choice for your project.

  * Build for Vue. While other animation libraries are messy to integrate, Motion's declarative API feels like a natural extension of Vue. Animations can be linked directly to state and props.

  * **Hardware-acceleration.** Motion leverages the same high-performance browser animations as pure CSS, ensuring your UIs stay smooth and snappy. You get the power of 120fps animations with a much simpler and more expressive API.

  * **Animate anything.** CSS has hard limits. There's values you can't animate, keyframes you can't interrupt, staggers that must be hardcoded. Motion provides a single, consistent API that handles everything from simple transitions to advanced scroll, layout, and gesture-driven effects.

  * **App-like gestures.** Standard CSS `:hover` events are unreliable on touch devices. Motion provides robust, cross-device gesture recognisers for press, drag, and hover, making it easy to build interactions that feel native and intuitive on any device.

### When is CSS a better choice?

For simple, self-contained effects (like a color change on hover) a standard CSS transition is a lightweight solution. The strength of Motion is that it can do these simple kinds of animations but also scale to anything you can imagine. All with the same easy to write and maintain API.

## Install

Motion for Vue is available via npm:
    
    
    npm install motion-v

### Nuxt modules

Motion Vue offers Nuxt modules support.

In `nuxt.config.ts`, simply add `motion-v/nuxt` into the modules, and it will auto-imports all the components for you.
    
    
    export default defineNuxtConfig({
      modules: ['motion-v/nuxt'],
    })

### `unplugin-vue-components`

Motion for Vue also supports [unplugin-vue-components](https://github.com/antfu/unplugin-vue-components) to auto-import all components from `motion-v`:
    
    
    import Components from 'unplugin-vue-components/vite'
    import MotionResolver from 'motion-v/resolver'
    
    export default defineConfig({
      plugins: [
        vue(),
        Components({
          dts: true,
          resolvers: [
            MotionResolver()
          ],
        }),
      ],
    })

> **Note:** Auto-import currently doesn't support [the <motion /> component](./vue-motion-component) so you'll need to import it manually.

**Note:** Motion for Vue contains APIs specifically tailored for Vue, but every feature from [vanilla Motion ](./quick-start)is also compatible and available for advanced use-cases.

## Usage

The core of Motion for Vue is [the ](./vue-motion-component)`[<motion />](./vue-motion-component)`[ component](./vue-motion-component). It's a normal DOM element, supercharged with animation capabilities.
    
    
    <template>
      <motion.div />
    </template>

Animating a `motion` component is as straightforward as setting values via the `animate` prop:
    
    
    <motion.ul :animate="{ rotate: 360 }" />

When values in `animate` change, the component will animate. Motion has great-feeling defaults, but animations can of course be configured via [the ](./vue-transitions)`[transition](./vue-transitions)`[ prop](./vue-transitions).
    
    
    <motion.div
      :animate="{
        scale: 2,
        transition: { duration: 2 }
      }"
    />

### Enter animation

When a component enters the page, it will automatically animate from the rendered value, but you can provide different values via the `initial` prop.
    
    
    <motion.button :initial="{ scale: 0 }" :animate="{ scale: 1 }" />

Or disable this initial animation entirely by setting `initial` to `false`.
    
    
    <motion.button :initial="false" :animate="{ scale: 1 }" />

### Gestures

`<motion />` extends Vue's event system with powerful gesture recognises. It currently supports hover, press, focus, and drag gestures.
    
    
    <motion.button
      :whileHover="{ scale: 1.1 }"
      :whilePress="{ scale: 0.95 }"
      @hoverStart="() => console.log('hover started!')"
    />

Motion's gestures are designed to feel better than using CSS alone. For instance, hover events are correctly not triggered by touch screen taps. [Learn more about gestures](./vue-gestures).

### Scroll animations

Motion supports both types of scroll animations, **scroll-triggered** and **scroll-linked**.

To trigger an animation on scroll, the `whileInView` prop defines a state to animate to/from when an element enters/leaves the viewport:
    
    
    <motion.div
      :initial="{ backgroundColor: 'rgb(0, 255, 0)', opacity: 0 }"
      :whileInView="{ backgroundColor: 'rgb(255, 0, 0)', opacity: 1 }"
    />

Whereas to link a value directly to scroll position, it's possible to use `MotionValue`s via `[useScroll](./vue-use-scroll)`.
    
    
    <script setup >
      const { scrollYProgress } = useScroll()
    </script>
    
    <template>
      <motion.div :style="{ scaleX: scrollYProgress }" />
    </template>

[Learn more](./vue-scroll-animations) about Motion's scroll animations.

### Layout animations

Motion has an industry-leading layout animation engine that supports animating between changes in layout, using only transforms, between the same or different elements, with full scale correction.

It's as easy as applying the `layout` prop.
    
    
    <motion.div layout />

Or to animate between different elements, a `layoutId`:
    
    
    <motion.div layoutId="underline" />

[Learn more](./vue-layout-animations) about layout animations.

### Exit animations

By wrapping `motion` components with `<AnimatePresence>` we gain access to the `exit` prop. 
    
    
    <AnimatePresence>
      <motion.div v-if="show" key="box" :exit="{ opacity: 0 }" />
    </AnimatePresence>

[Learn more](./vue-animate-presence) about `AnimatePresence`.

## Development tools

[Motion Studio](../studio) provides visual editing and AI tools to enhance your animation development workflow, like inline bezier editing, CSS spring generation and more.

### Install Motion Studio 

One-click install for Cursor:

[Add Extension](cursor:extension/motion.motion-vscode-extension)

[Add MCP](https://cursor.com/en-US/install-mcp?name=motion&config=eyJjb21tYW5kIjoibnB4IC15IGh0dHBzOi8vYXBpLm1vdGlvbi5kZXYvcmVnaXN0cnkudGd6P3BhY2thZ2U9bW90aW9uLXN0dWRpby1tY3AmdmVyc2lvbj1sYXRlc3QifQ%3D%3D)

Motion Studio is also compatible with VS Code, Google Antigravity and more. [See full installation guide](./studio-install). 

##   

## Learn next

That's a very quick overview of Motion for Vue's basic features. But there's a lot more to learn! 

Next, we recommend diving further into the [the ](./vue-motion-component)`[<motion />](./vue-motion-component)`[ component](./vue-motion-component) to learn more about its powerful features, like variants.

Or, you can dive straight in to our [examples](https://motion.dev/examples?platform=vue), where each example comes complete with full source code that you can copy/paste into your project.
