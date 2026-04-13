# Ticker

> Source: https://motion.dev/docs/vue-ticker

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

Ticker makes it quick and simple to build infinitely-scrolling marquee-style animations.

It's exclusive to [Motion+](../plus) members. Motion+ is a one-time fee, all-in membership that offers exclusive components, premium examples and access to a private Discord community.

Motion+ Ticker is:

  * **Lightweight:** Just `+2.6kb` on top of Motion for Vue.

  * **Accessible:** Focus trapping for unobtrusive keyboard navigation and mandatory respect for "reduced motion" OS settings.

  * **Multiaxis:** Create either vertical or horizontal tickers.

  * **Flexible:** Defaults to a velocity-based animation but can be powered by your own [motion values](./vue-motion-value).

  * **Performant:** Clones the theoretical minimum of elements.

Its simple API makes infinite tickers quick to make. Items are automatically repeated, meaning the absolute minimum number of clones are created for the current viewport.

<Ticker>

😂

</Ticker>

Powered by `[<motion>](./vue-motion-component)`[ components](./vue-motion-component), it's straightforward to drive the ticker offset with motion values to create scroll-driven or draggable tickers.
    
    
    <script setup>
    const { scrollY } = useScroll()
    </script>
    
    <template>
     <Ticker :offset="scrollY" />  
    </template>

In this guide, we'll learn how to install `Ticker` and use it to create various animation effects.
