# Scroll animation

> Source: https://motion.dev/docs/vue-scroll-animations

There are two types of scroll animations:

  * **Scroll-triggered:** A normal animation is triggered when an element enters the viewport.

  * **Scroll-linked:** Values are linked directly to scroll progress.

Motion is capable of both types of animation.

## Scroll-triggered animations

Scroll-triggered animations are just normal animations that fire when an element enters or leaves the viewport.

Motion offers[ the ](./vue-motion-component#whileinview)`[whileInView](./vue-motion-component#whileinview)`[ prop](./vue-motion-component#whileinview) to set an animation target or variant when the element enters the view.

<motion.div

:initial="{ opacity: 0 }"

:whileInView="{ opacity: 1 }"

/>

### One-time animations

With [the ](./vue-motion-component#inviewoptions)`[inViewOptions](./vue-motion-component#inviewoptions)`[ ](./vue-motion-component#inviewoptions), it's possible to set `once: true` so once an element has entered the viewport, it won't animate back out.

<motion.div

initial="hidden"

whileInView="visible"

:inViewOptions="{ once: true }"

/>

### Changing scroll container

By default, the element will be considered within the viewport when it enters/leaves the **window**. This can be changed by providing the `ref` of another scrollable element.
    
    
    <script setup>
      import { ref } from "vue"
      const scrollRef = ref(null)
    </script>
    
    <template>
        <div ref="scrollRef" :style="{ overflow: 'scroll' }">
          <motion.div
            :initial="{ opacity: 0 }"
            :whileInView="{ opacity: 1 }"
            :inViewOptions="{ root: scrollRef }"
          />
        </div>
    </template>
    
    

For more configuration options, checkout [the ](./vue-motion-component#viewport-1)`[motion](./vue-motion-component#viewport-1)`[ component](./vue-motion-component#viewport-1) API reference.

### Setting state

It's also possible to set state when any element (not just a `motion` component) enters and leaves the viewport with the `[useInView](./vue-use-in-view)`[ hook](./vue-use-in-view).

## Scroll-linked animations

Scroll-linked animations are created using [motion values](./vue-motion-value) and the `[useScroll](./vue-use-scroll)`[ hook](./vue-use-scroll).

`useScroll` returns four motion values, two that store scroll offset in pixels (`scrollX` and `scrollY`) and two that store scroll progress as a value between `0` and `1`.

These motion values can be passed directly to specific styles. For instance, passing `scrollYProgress` to `scaleX` works great as a progress bar.
    
    
    <script>
    import { useScroll } from "motion-v"
    const { scrollYProgress } = useScroll();
    </script>
    
    <template>
      <motion.div :style="{ scaleX: scrollYProgress }" />  
    </template>
    
    

### Value smoothing

This value can be smoothed by passing it through `[useSpring](./vue-use-spring)`.
    
    
    <script setup>  
    const { scrollYProgress } = useScroll();
    const scaleX = useSpring(scrollYProgress, {
      stiffness: 100,
      damping: 30,
      restDelta: 0.001
    })
    </script>
    
    <template>
     <motion.div :style="{ scaleX }" />
    </template>

### Transform other values

With [the ](./vue-use-transform)`[useTransform](./vue-use-transform)`[ hook](./vue-use-transform), it's easy to use the progress motion values to mix between any value, like colors:
    
    
    <script setup>  
    const backgroundColor = useTransform(
      scrollYProgress,
      [0, 0.5, 1],
      ["#f00", "#0f0", "#00f"]
    )
    </script>
    
    <template>
      <motion.div :style="{ backgroundColor }" />
    </template>

### Examples

#### Track element scroll offset

#### Track element within viewport

#### Parallax

#### Scroll velocity and direction

Read the [full ](./vue-use-scroll)`[useScroll](./vue-use-scroll)`[ docs](./vue-use-scroll) to discover more about creating the above effects.
