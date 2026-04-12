# Ticker

> Source: https://motion.dev/docs/react-ticker

Checking Motion+ status…

Ticker

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

The `Ticker` component for React creates performant, flexible, and fully accessible ticker and marquee animations. It's perfect for showcasing logos, photos, testimonials, news headlines, and more.

`Ticker`'s simple API makes these infinitely-scrolling animations easy to build.

<Ticker items={items} />

It intelligently clones only the minimum number of items needed to create a seamless loop, ensuring optimal performance. Because it's powered by Motion, you can take full manual control with a [motion value](./react-motion-value) to create scroll-driven or draggable effects.

`Ticker` is exclusive to [Motion+](../plus) members. Motion+ is a one-time payment, lifetime membership that unlocks exclusive components, premium examples and access to a private Discord community.

## Features

`Ticker` is a production-ready component built with performance and accessibility at its core.

  * **Lightweight:** Just `+2.1kb` on top of Motion for React.

  * **Accessible:** Automatic support for "reduced motion" and intelligent keyboard focus-trapping means your site is inclusive for all users.

  * **Flexible:** Animate horizontally or vertically. Control the animation with velocity, scroll position, or drag gestures.

  * **Performant:** Creates the absolute minimum number of cloned elements required to fill the viewport. [Read more about Motion+ Ticker's unique renderer.](../magazine/building-the-ultimate-ticker) More efficient and maintainable than hand-rolled CSS tickers.

  * **Full-width overflow:** Easily create tickers that are contained within your layout but visually extend to the edges of the viewport.

  * **RTL-compatible:** Automatically adapts to RTL layouts.

## Install

First, add the `motion-plus` package to your project using your [private token](https://plus.motion.dev). You need to be a [Motion+ member](../plus) to generate a private token.
    
    
    npm install "https://api.motion.dev/registry.tgz?package=motion-plus&version=2.0.2&token=YOUR_AUTH_TOKEN"

## Usage

`Ticker` accepts on mandatory prop, `items`. This is a list of valid React nodes (which can be components, strings or numbers):
    
    
    const items = [
      <span>One</span>,
      <span>Two</span>,
      <span>Three</span>
    ]
    
    return <Ticker items={items} />

### Direction

By default, tickers will scroll horizontally, but via the `axis` prop we can lay out and animate items on the `"y"` axis too.
    
    
    <Ticker items={items} axis="y" />

### Adjust speed

Setting the `velocity` prop (in pixels per second) will change the speed and direction of the ticker animation.
    
    
    <Ticker items={items} velocity={100} />

Flipping this to a negative value will reverse the direction of the ticker.
    
    
    <Ticker items={items} velocity={-100} />

Whereas setting it to `0` will stop all motion.
    
    
    <Ticker items={items} velocity={0} />
