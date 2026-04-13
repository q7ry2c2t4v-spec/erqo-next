# AnimateView

> Source: https://motion.dev/docs/react-animate-view

Checking Motion+ status…

Unlocks for everyone in

378 Days 21 Hours 40 Minutes

Or

[Get Motion+ for instant access](../plus)

One-time payment, lifetime updates

Already joined?

[Login](https://plus.motion.dev/login)

`AnimateView` allows you to animate elements between different views using the browser's native [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API).

It's a 3kb component built on top of Motion's mini `[animate()](./animate)` function and React's `[ViewTransition](https://react.dev/reference/react/ViewTransition)` component, providing a simple API for adding values like `clipPath` and configuring animations with Motion's [transitions](./react-transitions), including springs.

It's possible to write specific animations for when elements enter and exit the DOM, when they update, or when performing shared element animations.

{isOpen && (

<AnimateView transition={{ type: spring }}>

<div className="modal" />

</AnimateView>

)}

`AnimateView` is currently available in [Motion+](../plus) Early Access. As an Early Access API, expect changes as we receive feedback.

## Install

First, add the `motion-plus` package to your project using your [private token](https://plus.motion.dev). You need to be a [Motion+ member](../plus) to generate a private token.

npm install "https://api.motion.dev/registry.tgz?package=motion-plus&version=2.8.0&token=YOUR_AUTH_TOKEN"

Once installed, `AnimateView` can be imported via `motion-plus/animate-view`.

`AnimateView` is built on React's `ViewTransition` component and therefore requires `motion@12.34.0` and `react@canary` or above.

Once out of alpha, `AnimateView` will be imported from the main `"motion"` package.

## Usage

Import `AnimateView` from `"motion-plus/animate-view"`.
    
    
    import { AnimateView } from "motion-plus/animate-view"

### Enter/exit animations

To animate an element as it enters and exits the DOM, we can just wrap it in `<AnimateView>`.
    
    
    {show && (
      <AnimateView>
        <div className="box" />
      </AnimateView>
    )}

Now, when `show` is changed within a React `startTransition`, the element will perform the browser's default fade in/out animation as it enters and leaves the DOM.
    
    
    startTransition(() => setShow(!show))

View transitions will only trigger when state changes are wrapped in `startTransition`.

The full setup looks like this:
    
    
    import { AnimateView } from "motion-plus/animate-view"
    import { startTransition, useState } from "react"
    
    function Example() {
      const [show, setShow] = useState(true)
      
      return (
        <>
          <button onClick={() => startTransition(() => setShow(!show))}>
            Toggle
          </button>
          {show && (
            <AnimateView>
              <div className="box" />
            </AnimateView>
          )}
        </>
      )
    }

### Configure the transition

It's possible to set a default transition for all view transitions via the `transition` prop. This accepts all Motion's [transition options](./react-transitions).
    
    
    <AnimateView transition={{ duration: 1, ease: "easeOut" }}>
      <div className="box" />
    </AnimateView>

You can also set a `transition` for specific `enter`, `exit`, `share` and `update` animations:
    
    
    <AnimateView enter={{
      transition: { type: spring, bounce: 0, duration: 0.6 }
    }}>
      <div className="box" />
    </AnimateView>

`AnimateView` is built on Motion's mini `animate()` function for a tiny filesize. Therefore, `spring` must be explicitly imported from `"motion"` and passed to the `type` transition option. 

### Setting values

By default, `AnimateView` will animate elements using the browser's default opacity animation. But, if you set your own values within `enter`, `exit`, `share` or `update` then this crossfade will be disabled.
    
    
    <AnimateView enter={{ clipPath: ["inset(0 50% 0 100%)", "inset(0 0% 0 0%)"] }}>

You can re-enable a `opacity` animation by also passing this to the prop:
    
    
    <AnimateView enter={{
      opacity: 1,
      clipPath: ["inset(0 50% 0 100%)", "inset(0 0% 0 0%)"]
    }}>

### Animating updates

Elements wrapped in `AnimateView` will also animate whenever their content or visual styles change, crossfading between the two views. This animation can be customised with the `update` prop.
    
    
    <AnimateView update={{ ease: "easeInOut" }}>
      <div style={{ backgroundColor }} />
    </AnimateView>

If the element physically moves or changes size, this change will also be animated. We can use this to create, for example, reorder list animations.
    
    
    function ReorderList({ items }) {
      return (
        <div className="list">
          {items.map((item) => (
            <AnimateView
              key={item.id}
              transition={{ type: spring, bounce: 0.2 }}
            >
              <div className="list-item">{item.label}</div>
            </AnimateView>
          ))}
        </div>
      )
    }

### Shared element animations

When an `AnimateView` component with a `name` prop exits the DOM, and another one with the same `name` enters it within the same transition, the two elements will perform a shared element animation.
    
    
    if (selectedItem) {
      return <Modal selectedItem={selectedItem} />
    }
    
    return <Items setSelectedItem={setSelectedItem} />
    
    
    function Item({ setSelectedItem }) {
      return (
        <AnimateView name="item-1">
          <div
            className="item"
            onClick={() => startTransition(() => setSelectedItem("item-1"))}
          />
        </AnimateView>
      )
    }
    
    function Modal({ selectedItem }) {
      return (
        <AnimateView name={selectedItem}>
          <div className="modal" />
        </AnimateView>
      )
    }

If there is more than one element with a specific `name` either before, or after the transition, the animation will fail.

The animation can be configured via the `transition` or `share` props on the entering element:
    
    
    <AnimateView name="item-1" transition={{ duration: 0.4 }}>

### Transition types

React's `addTransitionType` lets you set contextual information (like navigation direction) to the current transition.
    
    
    startTransition(() => {
      addTransitionType("next")
      setItem(2)
    })

`enter`, `exit`, `share` and `update` props can all resolve dynamically, with a list of values set via `addTransitionType`. You can use this information to generate different animations.
    
    
    <AnimateView
      key={index}
      exit={(types) => ({
          transform: `translateX(${types.includes("prev") ? 100 : -100}%)`,
      })}
      enter={(types) => ({
          transform: [
              `translateX(${types.includes("next") ? 100 : -100}%)`,
              "translateX(0%)",
          ],
      })}
    >

### Suspense

`AnimateView` integrates with `Suspense`. You can crossfade between content and fallback by wrapping them both in `Suspense`:
    
    
    <AnimateView>
      <Suspense fallback={<Placeholder />}>
        <Content />
      </Suspense>
    </AnimateView>

## Performance

The React docs state:

> `<ViewTransition>` creates an image that can be moved around, scaled and cross-faded. Unlike Layout Animations you may have seen in React Native or Motion, this means that not every individual Element inside of it animates its position. This can lead to better performance and a more continuous feeling, smooth animation compared to animating every individual piece.

Neither of these claims are true.

From our own stress test benchmarking, creating image bitmaps and constructing a pseudo-DOM is more memory intensive and slower than the equivalent layout measurements used by Motion's [layout animations](./layout-animations).

The claim of "a more continuous feeling" is also not right. Layout animations are ** **interruptible** **, which means you can change direction mid-animation and they respond immediately. View transitions are ** **not interruptible** **, meaning they must complete before a new transition can begin. This makes layout animations a far better candidate for micro-interactions where responsiveness matters.

View transitions are best suited for ** **page-level transitions** ** (route changes, full-view swaps) where the non-interruptible nature is acceptable and the snapshot-based approach avoids complex per-element coordination.

## Props

### `transition`

Default transition for all animation types. Accepts any Motion transition, including springs.
    
    
    <AnimateView transition={{ type: spring, visualDuration: 0.4, bounce: 0.3 }}>

### `enter`

**Default:**`{ opacity: 1 }`

An animation to use when the wrapped element enters the DOM.
    
    
    <AnimateView enter={{ 
      opacity: 1,
      transform: ["translateX(-100%)", "none"]
    }}>

Can also be a function that resolves with the list of current transition types.
    
    
    <AnimateView
      enter={(types) => ({
        transform: [
          `translateX(${types.includes("next") ? 100 : -100}%)`,
          "none",
        ],
      })}
    >

###
