# resize

> Source: https://motion.dev/docs/resize

`resize` allows you to monitor and react to size changes in the viewport, or specific HTML and SVG elements.

// Viewport

resize(() => {})

  

// Specific elements

resize("li", () => {})

For optimal performance, all resize handlers are triggered via a single, shared `[ResizeObserver](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver)`.

## Usage

Import `resize` from `"motion"`.

import { resize } from "motion"

### Tracking viewport changes

Changes to the viewport can be detected by passing just a callback to `resize`:

resize(() => console.log("viewport change detected"))

The callback is provided a single argument, containing `width` and `height` getters.

resize(({ width, height }) => console.log(width, height))

### Tracking element changes

By passing an element or CSS selector, `resize` can detect changes on specific elements.

resize("li", (element) => console.log(element, "change detected"))

This function is also provided `width` and `height` getters for each `element`:

resize(".drawer", (element, { width, height }) => {

console.log(element, " is now ", width, height)

})

The returned `width` and `height` are the element's **border box** , which is the size of the element including the border.

### Responding to size changes

For best performance, subsequent renders should be performed with the [Motion frameloop](./frame). This ensures DOM reads and writes are correctly batched to prevent layout and style thrashing.
    
    
    resize(".drawer", (element, { width, height }) => {
      frame.render(() => {
        element.style.height = Math.max(400, height)
      })
    })

### Cleanup

`resize` returns a function that will, when called, remove the attached listeners.
    
    
    const stop = resize(log)
    stop()

When there are no more listeners on an element, the element will be removed from the `ResizeObserver`, and when there are no more listeners at all, the `ResizeObserver` will be stopped.
