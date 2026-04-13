# Motion Directive

> Source: https://motion.dev/docs/vue-directive

The `v-motion` directive provides a declarative way to add Motion animations to any HTML or SVG element without using wrapper components. It offers most of the powerful animation capabilities of the `[<motion/>](./vue-motion-component)` component with a more traditional Vue directive syntax.

## Install

### Global registration (Vue)

import { createApp } from 'vue'

import { MotionPlugin } from 'motion-v'

  

const app = createApp(App)

app.use(MotionPlugin)

### Global registration (Nuxt)

// nuxt.config.ts

export default defineNuxtConfig({

modules: ['motion-v/nuxt'],

motionV: {

directives: true,

},

})

### Local registration

<script setup>

import { vMotion } from 'motion-v'

</script>

## Syntax

### Basic animation

<div v-motion :initial="{ opacity: 0 }" :animate="{ opacity: 1 }">

Hello Motion

</div>

`v-motion` supports two syntax styles. You can also mix them: Element props take priority over the binding value.

### Binding value

Pass all options as a single object:
    
    
    <div
      v-motion="{
        initial: { opacity: 0, x: -30 },
        animate: { opacity: 1, x: 0 },
        transition: { duration: 0.6 },
      }"
    >
      Slide In
    </div>

### Props

Use `v-motion` as a marker and pass motion options as individual props:
    
    
    <div
      v-motion
      :initial="{ opacity: 0, y: 30 }"
      :animate="{ opacity: 1, y: 0 }"
      :transition="{ duration: 0.6 }"
    >
      Fade In
    </div>

### Mixed

When both are used, element props override binding value keys:
    
    
    <!-- initial will be { opacity: 0.2 }, not { opacity: 0.5 } -->
    <div
      v-motion="{ initial: { opacity: 0.5 }, transition: { duration: 0.5 } }"
      :initial="{ opacity: 0.2 }"
    >
      Props Win
    </div>

## Usage

`v-motion` supports the same animation props as the `[<motion>](./vue-motion-component)` component — `initial`, `animate`, `exit`, `transition`, gesture props (`whileHover`, `whilePress`, `whileFocus`, `whileInView`, `whileDrag`), and reactive bindings.

For detailed usage of these features, see the [Animation](./vue-animation).

## Exit animation

Use `exit` with `[<AnimatePresence>](./vue-animate-presence)` to animate elements out when they are removed with `v-if`.
    
    
    <script setup>
    import { ref } from 'vue'
    import { AnimatePresence } from 'motion-v'
    
    const isVisible = ref(true)
    </script>
    
    <template>
      <button @click="isVisible = !isVisible">
        Toggle
      </button>
    
      <AnimatePresence>
        <div
          v-if="isVisible"
          v-motion
          :initial="{ opacity: 0, scale: 0.5, rotate: -10 }"
          :animate="{ opacity: 1, scale: 1, rotate: 0 }"
          :exit="{ opacity: 0, scale: 0.5, rotate: 10 }"
          :transition="{ type: 'spring', duration: 0.5 }"
        >
          Toggle me
        </div>
      </AnimatePresence>
    </template>

## Presets

`MotionPlugin` accepts a `presets` option to register custom preset directives. Each preset is automatically registered as a `v-{name}` global directive:

### `MotionPlugin`
    
    
    app.use(MotionPlugin, {
      presets: {
        'fade-in': {
          initial: { opacity: 0 },
          animate: { opacity: 1 },
          transition: { duration: 0.5 },
        },
        'slide-up': {
          initial: { opacity: 0, y: 40 },
          animate: { opacity: 1, y: 0 },
          transition: { duration: 0.5 },
        },
        'scale-in': {
          initial: { opacity: 0, scale: 0.5 },
          animate: { opacity: 1, scale: 1 },
          transition: { type: 'spring', stiffness: 300, damping: 20 },
        },
      },
    })

### Nuxt Module

In `nuxt.config.ts`:
    
    
    export default defineNuxtConfig({
      modules: ['motion-v/nuxt'],
      motionV: {
        directives: true, // globally register v-motion
        presets: {
          'fade-in': {
            initial: { opacity: 0 },
            animate: { opacity: 1 },
          },
        },
      },
    })

Then use anywhere without imports:
    
    
    <template>
      <div v-fade-in>
        Fade
      </div>
      
      <div v-slide-up>
        Slide
      </div>
      
      <div v-scale-in>
        Scale
      </div>
    </template>
