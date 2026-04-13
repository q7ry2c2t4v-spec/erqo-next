# Carousel

> Source: https://motion.dev/docs/vue-carousel

Checking Motion+ status…

Carousel

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

The Carousel component creates performant, accessible and fully-featured carousels in Vue. It's designed to be flexible and easy to use, supporting pointer, wheel and keyboard navigation out the box.

It allows you to go beyond the traditional limitations of CSS-only approaches, with support for infinitely-scrolling carousels and without limitations on styling.

### Features

  * **Lightweight:** Just `+5.8kb` on top of [the ](./vue-motion-component)`[motion](./vue-motion-component)`[ component](./vue-motion-component).

  * **Accessible:** Automatic ARIA labels, respects reduced motion, RTL layouts, and all major input methods.

  * **Performant:** Built on the same [unique rendering](../magazine/building-the-ultimate-ticker) used by the [Ticker](./vue-ticker) component that achieves infinite scrolling with while minimising or eliminating item cloning.

  * **Customisable:** Provides functions and state to easily create custom controls and pagination. 

## Install

npm install motion-plus-vue

## Usage

### Import

Import the `Carousel` component from "motion-plus-vue"`:
    
    
    import { Carousel } from "motion-plus-vue"

`Carousel` component receives its items via the `default slot`. You can pass any valid Vue nodes (components, strings, or numbers)
    
    
     <Carousel>
        <span>One</span>
        <span>Two</span>
        <span>Three</span>
     </Carousel>
    
    
    <Carousel>
      <Box src="sonic3" title="Sonic 3" />  <!-- This will be one Carousel item -->
      <div>Some text</div>                   <!-- This will be another Carousel item -->
      123                                    <!-- This will be a third Carousel item -->
    </Carousel>
    <
    
    
    
    
    <Carousel>
      <Box src="sonic3" title="Sonic 3" />
      <!-- This Fragment and its children will be treated as a single Carousel item -->
      <Fragment>
        <div>Some text</div>
        123
      </Fragment>
    </Carousel>

### Direction

By default, carousels will scroll horizontally. Setting the `axis` prop to `y`, we can make them vertical.
    
    
    <Carousel axis="y" />

### Layout

Items are laid out via flexbox. Passing `gap` and `align` will adjust the spacing and off-axis alignment of them items.
    
    
    <Carousel  :gap="0" align="start" />

### Overflow

By setting `overflow` to `true`, items will visually extend out from the container to the edges of the viewport.
    
    
    <Carousel  overflow />

This makes it straightforward to place a `Carousel` within a document flow but still extend the ticker effect across the full viewport.

### Infinite scrolling

By default, carousels will scroll infinitely. This can be disabled by setting `:loop="false"`.
    
    
    <Carousel :loop="false"/>

### Layout

By default, each item will be sized according to its contents. By setting `itemSize="fill"`, items will extend the match the width of the container.
    
    
    <Carousel itemSize="fill" />

### Snapping

By default, drag and wheel controls will snap between pages. By setting `:snap="false"`, snapping can be disabled and the carousel will freely scroll.
    
    
    <Carousel  :snap="false" />

### Custom controls

Custom controls can be passed to Carousel using the `after` slots. The `after` slot renders `after` the Carousel container:
    
    
    <Carousel :loop="false" >
        {{items}}
      <template #after>
        <Next/>
      </template>
    </Carousel>

Any component rendered within `Carousel` can call `useCarousel` to access state and pagination functions. This hook provides:

  * `nextPage`/`prevPage`: Paginate next/previous.

  * `gotoPage`: Pass it a page index to animate to this page.

  * `paginationState`:

    * `isNextActive`/`isPrevActive`: If `:loop="false"` then these will be false when we hit the limits of the carousel.

    * `currentPage`: Index of the current page

    * `totalPages`: Number of total pages.

    
    
    <script setup>
    import { useCarousel } from "motion-plus-vue"
    
    const { nextPage, isNextActive } = useCarousel()
    </script>
    
    <template>
      <button :disabled="!isNextActive" @click="nextPage">
        Next
      </button>
    </template>

### Autoplay

With `currentPage` and `nextPage` from `useCarousel`, we can also set up our own autoplay functionality.

By watching `currentPage` with `watch`, the timer will restart whenever the page changes, whether that's from a swipe/drag, or from the autoplay timer itself.
    
    
    const { paginationState, nextPage } = useCarousel()
    const progress = useMotionValue(0)
    
    watch(
      [() => paginationState.value.currentPage, () => props.duration],
      (_1,_2,onCleanup) => {
        const animation = animate(progress, [0, 1], {
          duration,
          ease: "linear",
          onComplete: nextPage,
        })
        
        onCleanup(() => {
          animation.stop()
        })
      },
      { immediate: true }
    )

### Pagination visualisation

By using `currentPage`, `totalPages` and `gotoPage` from `useCarousel`, a custom pagination indicator/navigator can be built.
    
    
    <script setup>
    import { useCarousel } from "motion-plus-vue"
    import { motion } from "motion-v"
    
    const { paginationState, gotoPage } = useCarousel()
    </script>
    
    <template>
      <ul class="dots">
        <li 
          v-for="(_, index) in Array.from({ length: paginationState.totalPages })" 
          :key="index"
          class="dot"
        >
          <motion.button
            :initial="false"
            :animate="{ opacity: paginationState.currentPage === index ? 1 : 0.5 }"
            tag="button"
            @click="gotoPage(index)"
          />
        </li>
      </ul>
    </template>
