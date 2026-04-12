# Carousel

> Source: https://motion.dev/docs/react-carousel

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

The Carousel component creates performant, accessible and fully-featured carousels in React. It's designed to be flexible and easy to use, supporting pointer, wheel and keyboard navigation out the box.

It allows you to go beyond the traditional limitations of CSS-only approaches, with support for infinitely-scrolling carousels and without limitations on styling.

### Features

  * **Lightweight:** Just `+5.5kb` on top of [the ](./react-motion-component)`[motion](./react-motion-component)`[ component](./react-motion-component).

  * **Accessible:** Automatic ARIA labels, respects reduced motion, RTL layouts, and all major input methods.

  * **Performant:** Built on the same [unique rendering](../magazine/building-the-ultimate-ticker) used by the [Ticker](./react-ticker) component that achieves infinite scrolling with while minimising or eliminating item cloning.

  * **Customisable:** Provides functions and state to easily create custom controls and pagination. 

## Install

First, add the `motion-plus` package to your project using your [private token](https://plus.motion.dev). You need to be a [Motion+ member](../plus) to generate a private token.

npm install "https://api.motion.dev/registry.tgz?package=motion-plus&version=2.11.0&token=YOUR_AUTH_TOKEN"

## Usage

### Import

Import the `Carousel` component from "motion-plus/react"`:
    
    
    import { Carousel } from "motion-plus/react"

`Carousel` accepts a single mandatory prop, `items`. This is a list of valid React nodes (which can be components, strings or numbers):
    
    
    const items = [
      <span>One</span>,
      <span>Two</span>,
      <span>Three</span>
    ]
    
    return <Carousel items={items} />

### Direction

By default, carousels will scroll horizontally. Setting the `axis` prop to `y`, we can make them vertical.
    
    
    <Carousel items={items} axis="y" />

### Layout

Items are laid out via flexbox. Passing `gap` and `align` will adjust the spacing and off-axis alignment of them items.
    
    
    <Carousel items={items} gap={0} align="start" />

### Overflow

By setting `overflow` to `true`, items will visually extend out from the container to the edges of the viewport.
    
    
    <Carousel items={items} overflow />

This makes it straightforward to place a `Carousel` within a document flow but still extend the ticker effect across the full viewport.

### Infinite scrolling

By default, carousels will scroll infinitely. This can be disabled by setting `loop={false}`.
    
    
    <Carousel items={items} loop={false} />

### Layout

By default, each item will be sized according to its contents. By setting `itemSize="fill"`, items will extend the match the width of the container.
    
    
    <Carousel items={items} itemSize="fill" />

### Snapping

By default, drag and wheel controls will snap between pages. By setting `snap={false}`, snapping can be disabled and the carousel will freely scroll.
    
    
    <Carousel items={items} snap={false} />

### Custom controls

Custom controls can be passed to `Carousel` as children. 
    
    
    <Carousel loop={false} items={items}>
      <Next />
    </Carousel>

Any component rendered within `Carousel` can call `useCarousel` to access state and pagination functions. This hook provides:

  * `nextPage`/`prevPage`: Paginate next/previous.

  * `gotoPage`: Pass it a page index to animate to this page.

  * `isNextActive`/`isPrevActive`: If `loop={false}` then these will be false when we hit the limits of the carousel.

  * `currentPage`: Index of the current page

  * `totalPages`: Number of total pages.

    
    
    import { useCarousel } from "motion-plus/react"
    
    function Next() {
      const { nextPage, isNextActive } = useCarousel()
      
      return (
        <button disabled={!isNextActive} onClick={nextPage}>
          Next
        </button>
      )
    }

### Autoplay

With `currentPage` and `nextPage` from `useCarousel`, we can also set up our own autoplay functionality.

By passing `currentPage` to the `useEffect`, the timer will restart whenever the page changes, whether that's from a swipe/drag, or from the autoplay timer itself.
    
    
    const { currentPage, nextPage } = useCarousel()
    const progress = useMotionValue(0)
    
    useEffect(() => {
        const animation = animate(progress, [0, 1], {
            duration,
            ease: "linear",
            onComplete: nextPage,
        })
    
        return () => animation.stop()
    }, [duration, nextPage, progress, currentPage])

### Pagination visualisation

By using `currentPage`, `totalPages` and `gotoPage` from `useCarousel`, a custom pagination indicator/navigator can be built.
    
    
    function Pagination() {
      const { currentPage, totalPages, gotoPage } = useCarousel()
    
      return (
        <ul className="dots">
          {Array.from({ length: totalPages }, (_, index) => (
            <li className="dot">
              <motion.button
                  initial={false}
                  animate={{ opacity: currentPage === index ? 1 : 0.5 }}
                  onClick={() => gotoPage(index)}
              />
            </li>
          )}
        </ul>
      )
    }

###
