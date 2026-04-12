# GSAP vs Motion: Which should you use?

> Source: https://motion.dev/docs/gsap-vs-motion

Ready to migrate? Check out our simple [GSAP to Motion migration guide](./migrate-from-gsap-to-motion).

When deciding which JavaScript animation library to trust for your project, two libraries often get mentioned because of their feature set and popularity: **Motion** (formerly Framer Motion) and **GSAP** (formerly GreenSock).

Both can create stunning animations, but they have fundamental differences. This guide compares Motion and GSAP on **adoption** , **licensing** , **performance** , and **features** (complete with full comparison table), to help you decide which is right for your project.

## Adoption

Before delving into the libraries themselves, it's helpful to see what other developers are choosing. For modern applications, [npm](https://www.npmjs.com/package/framer-motion) is a great measure of a library's adoption and momentum.

Here, the numbers are clear: **Motion is growing exponentially,** making it the most-used and fastest-growing animation library in the ecosystem. It even just passed **16 million downloads per month**.

![Graph of Motion npm downloads 2021-2025](https://framerusercontent.com/images/mnKpEm91tNi6LNEueLOI8jxUp5k.png)

## Licensing

Motion is **fully independent** and **MIT open source**. It's financially supported by a mix of incredible industry-leading sponsors like [Framer](https://framer.com), [Figma](https://figma.com), [Sanity](https://www.sanity.io/), [Tailwind CSS](https://tailwindcss.com) and [LottieFiles](https://lottiefiles.com), as well as sales from [Motion+](../plus).

GSAP, by contrast, is **closed source** and **owned and funded by Webflow**. While it can be used for free in many projects, [its license](https://gsap.com/community/standard-license/) contains a critical restriction: You're prohibited from using GSAP in any tool that competes with Webflow. Furthermore, its license states that **Webflow can terminate it at its discretion**.

With Motion, you have a **guarantee of freedom**. That MIT license is irrevocable. You will never be forced to remove and replace your animation library because of a business decision made by another company. This provides the stability and peace of mind that professional development teams require.

Motion's independence and self-sufficiency also means we work with a broad base of users and companies, creating a library that works for the whole web, rather than the interests of a single company.

## Performance

Performance is more than just smooth animations. It's about providing a flawless 120fps, faster start-up times, and minimal bundle sizes. This is where Motion's modern architecture provides an advantage.

### Hardware accelerated animations

You might already know that for best animation performance you should stick to animating `opacity` , `transform`, `filter` and `clipPath`, because these styles [can be rendered entirely on the GPU](https://developers.google.com/web/fundamentals/performance/rendering/avoid-large-complex-layouts-and-layout-thrashing).

But when animating with Motion, these values can enjoy an extra performance boost using "hardware accelerated" animations. This means the animations themselves also run entirely the GPU - separate from the JavaScript running on your CPU.

This means if your website or app is performing heavy work, **animations remain smooth**. 

To illustrate, in the following example the ball on the left is animated with Motion, and the ball on the right by a traditional animation library. Press the "Block JavaScript" button to block JS execution for two seconds:

Motion

Other JavaScript libraries

Block JavaScript

In the majority of browsers, the left ball will continue animating at 60/120fps, even as the website becomes unresponsive. Traditional animation libraries like GSAP will pause and stutter where Motion remains perfectly smooth.

What's more, Motion can even perform hardware accelerated [scroll animations](./scroll). Because browsers render all scroll on the GPU, JS-based scroll animations are always slightly out-of-sync. Not so with Motion.
    
    
    const animation = animate(element, { opacity: [0, 1] })
    
    scroll(animation)

### Start-up time

Two animate any two values, they have to be mixable. Think, two numbers, or two colors. But what if we want to perform an animation where we don't even know the initial value? Or we do - but it's a value like `height: auto`, or a color defined in a CSS variable like `var(—my-color)`?

To make these values mixable, the library first needs to **measure** them. But measuring something that's just been rendered forces a layout or style calculation. These are slow.

To solve this, Motion introduced **deferred keyframe resolution**. This ensures we batch all measurements into a single operation, drastically reducing style and layout calculations.

In benchmarks, Motion is **2.5x faster** than GSAP at animating from unknown values, and **6x faster** at animating between different value types.

![Comparison between Motion 10/GSAP and Motion 11's deferred keyframe resolution. Motion 11 is 2.5x faster to animate unknown values and 6x faster at unit conversion.](https://framerusercontent.com/images/muzCL6FZAQhe3Hsd69UMFkFag.png)

This is great for user experience, and also great for performance scores like Interaction to Next Paint (INP).

### Bundle size

Motion is built with a modern, modular architecture. If your bundler supports tree-shaking (like Vite, Rollup or Webpack), you only ever include the code you actually use. GSAP's older architecture, by contrast, means that importing any part of the library includes all of it.

This, combined with Motion's focus on leveraging native browser APIs, results in a significantly smaller footprint.

Library| Size  
---|---  
`animate()` (mini)| 2.6kb  
`animate()` (full)| 18kb  
GSAP| 23kb  
  
A smaller bundle means a **faster site load and a better user experience** , especially on mobile devices. With Motion, you can deliver stunning animations with a minimal performance cost.

## Features

Of course, performance means little if a library can't deliver the features you need. While there is plenty of overlap, both libraries have unique strengths.

### React & Vue APIs

Motion provides a first-class, declarative API that is a natural extension of [React](./react) and [Vue](./vue). Animations are defined directly in your components via props, keeping your code clean, readable and easy to maintain.
    
    
    <motion.div animate={{ x: 100 }} />

GSAP, by contrast, uses an imperative model. While it has a `useGSAP` hook to help integrate into React's lifecycles, it still requires using refs. Mixing its imperative API into React's declarative components leads to more verbose and error-prone code.
    
    
    const container = useRef()
    
    useGSAP(() => {
      gsap.to(".box", { x: 100 })
    }, { scope: container })
    
    return (
      <div ref={container}>
        <div className="box"></div>
      </div>
    );

Furthermore, Motion for React and Vue features an **industry-leading**[**layout animation**](./react-layout-animations)**engine** , which goes far beyond the FLIP animations in GSAP.

### Timelines & sequencing

GSAP is famous for its powerful timeline function, which uses an imperative, chain-based API to build complex animation sequences. It's mature, and an industry standard for good reason.
    
    
    const tl = gsap.timeline()
    tl.to("h1", { opacity: 1 })
    tl.to("p", { y: 0 }, "-=0.5")

Motion provides a modern, declarative alternative. Instead of chain-based commands, `animate()` accepts a simple JavaScript array, making it easy to read, modify and dynamically generate animation sequences.
    
    
    animate([
      ["h1", { opacity: 1 }],
      ["p", { y: 0 }, { at: "-0.5" }]
    ])

This timeline can animate anything the `animate()` function can, mixing HTML elements, SVG elements, [motion values](./motion-value), and even 3D objects from libraries like Three.js - all within the same sequence. As mentioned earlier, it's also 5kb lighter.

The benefit to GSAP's timeline API is that it's **mutable**. Once playback has begun, individual tracks can be added and removed to the overarching sequence, an ability that Motion doesn't yet offer.

### Full feature comparison table

This table compares Motion's mini and full-size `animate` functions functions with GSAP's `gsap` object.

#### Key

  * ✅ Supported

  * ❌ Not supported

  * ⏩ Support relies on modern browser features

  * 🚧 In development

  * ⚠ Partial support

  * ⚛️ React/Vue only

  
| `animate` mini| `animate`| GSAP  
---|---|---|---  
Core bundlesize (kb)| 2.6| 18| 23.5  
  
#### General

|   
|   
|   
  
MIT license| ✅| ✅| ❌  
Accelerated animations| ✅| ✅| ❌  
[React API](./react)| ❌| ✅ (+15kb)| ❌  
[Vue API](./vue)| ❌| ✅ (+15kb)| ❌  
  
#### Values

|   
|   
|   
  
Individual transforms| ❌| ✅| ✅  
[Complex transform  
interpolation](https://codesandbox.io/s/transform-interpolation-motion-concept-c-vs-greensock-vs-anime-js-m90tc)| ✅| ❌| ✅  
[Named colors](https://codesandbox.io/s/named-color-animations-comparison-motion-concept-c-vs-greensock-vs-anime-js-vbkey)| ✅| ❌| ⚠ (20)  
[Color type  
conversion](https://codesandbox.io/s/animation-between-color-types-motion-concept-c-vs-greensock-vs-anime-js-gvip9)| ✅| ✅| ✅  
[To/from CSS  
variables](https://codesandbox.io/s/animating-to-from-css-variables-motion-concept-c-vs-greensock-vs-anime-js-yxz1z)| ✅| ✅| ❌  
To/from CSS  
functions| ✅| ❌| ❌  
Animate CSS  
variables| ✅ ⏩| ✅| ✅  
Simple keyframessyntax| ✅| ✅| ✅  
Wildcard keyframes| ✅| ✅| ❌  
Relative values| ❌| ❌| ✅  
  
#### Output

|   
|   
|   
  
Element styles| ✅| ✅| ✅  
Element attributes| ❌| ✅| ✅  
Custom animations| ❌| ✅| ✅  
  
#### Options

|   
|   
|   
  
Duration| ✅| ✅| ✅  
Direction| ✅| ✅| ✅  
Repeat| ✅| ✅| ✅  
Delay| ✅| ✅| ✅  
End delay| ✅| ❌| ✅  
Repeat delay| ❌| ✅| ✅  
  
#### Stagger

|   
|   
|   
  
Stagger| ✅ (+0.1kb)| ✅ (+0.1kb)| ✅  
Min delay| ✅| ✅| ✅  
Ease| ✅| ✅| ✅  
Grid| ❌| ❌| ✅  
  
#### Layout

|   
|   
|   
  
Animate layout| ❌| ⚠ (View)| ⚠ (FLIP)  
Transform-only| ❌| ✅ ⚛️| ❌  
Scale correction| ❌| ✅ ⚛️| ❌  
  
#### Timeline

|   
|   
|   
  
Timeline| ✅ (+0.6kb)| ✅| ✅  
Selectors| ✅| ✅| ✅  
Relative offsets| ✅| ✅| ✅  
Absolute offsets| ✅| ✅| ✅  
Start of previous  
offset| ✅| ✅| ✅  
Percentage offsets| ❌| ❌| ✅  
Label offsets| ✅| ✅| ✅  
Segment stagger| ✅| ✅| ✅  
Segment keyframes| ✅| ✅| ❌  
  
#### Controls

|   
|   
|   
  
Play| ✅| ✅| ✅  
Pause| ✅| ✅| ✅  
Finish| ✅| ✅| ✅  
Reverse| ❌| ❌| ✅  
Stop| ✅| ✅| ✅  
Playback rate| ✅| ✅| ✅  
  
#### Easing

|   
|   
|   
  
Linear| ✅| ✅| ✅  
Cubic bezier| ✅| ✅| ✅  
Steps| ✅| ✅| ✅  
Spring| ✅ (+1kb)| ✅| ❌  
Spring physics| ❌| ✅| ❌  
Inertia| ❌| ✅| ✅  
Custom easing  
functions| ✅ ⏩| ✅| ✅  
  
#### Events

|   
|   
|   
  
Complete| ✅| ✅| ✅  
Cancel| ✅| ✅| ✅  
Start| ❌| ✅| ✅  
Update| ❌| ✅| ✅  
Repeat| ❌| ❌| ✅  
  
#### Path

|   
|   
|   
  
Motion path| ✅ ⏩| ✅ ⏩| ✅ (+9.5kb)  
[Path morphing](https://codesandbox.io/s/motion-one-morph-svg-paths-qldsz?file=/src/index.js)| ❌| ✅ (+[Flubber](https://examples.motion.dev/react/path-morphing))| ✅   
Path drawing| ✅| ✅| ✅  
  
#### Scroll

|   
|   
|   
  
[Scroll trigger](https://motion.dev/dom/in-view)| ✅ (+0.5kb)| ✅ (+0.5kb)| ✅ (+12kb)  
[Scroll-linked  
animations](https://motion.dev/dom/scroll)| ✅ (+2.5kb)| ✅ (+2.5kb)| ✅ (+12kb)  
Hardware accelerated  
animations| ✅| ✅| ❌  
  
#### Extra Features

|   
|   
|   
  
AnimateNumber| ⚛️ ([Motion+](../))| ⚛️ ([Motion+](../))| ❌  
Cursor| ⚛️ ([Motion+](../))| ⚛️ ([Motion+](../))| ❌  
Split Text| ✅ ([Motion+](../))| ✅ ([Motion+](../))| ✅  
Ticker| ⚛️ ([Motion+](../))| ⚛️ ([Motion+](../))| ❌  
Typewriter| ⚛️ ([Motion+](../))| ⚛️ ([Motion+](../))| ❌  
View animations| ⚛️ ([Motion+](../))| ⚛️ ([Motion+](../))| ❌  
  
## Conclusion

**Both Motion and GSAP are powerful, production-ready libraries capable of creating stunning, award-winning animations.** The best choice depends entirely on the priorities of your project and team.

### When to use Motion?

You should choose **Motion** if your priority is **overall performance, a smaller bundle size, and a modern developer experience.** Its use of native browser APIs, first-class React/Vue support, and truly open-source MIT license make it the definitive choice for building fast, modern web applications.

### When to use GSAP?

You might still prefer **GSAP** if your project requires **intricate, timeline-sequenced animations on non-React sites**. Its maturity and long history mean it is a reliable, if more traditional, choice.
