# Add animations to your Squarespace site

> Source: https://motion.dev/docs/squarespace

Many [Squarespace](https://squarespace.com) templates come with in-built animations, but often they lack customisation options and rely on old and bloated animation libraries like jQuery which can lead to negative SEO and performance impacts.

By using Motion, you gain:

  * **Flexibility:** You're not limited to the template's in-built options (if any). You can design any animation you want using any of Motion's APIs like [scroll](./scroll) and [timeline sequencing](./animate).

  * **Performance:** Motion is built on the latest browser APIs for hardware accelerated performance.

  * **Improved SEO:** Motion's tiny `animate()` function is just 2.6kb, and the rest of the library is small too. This leads to better SEO scores.

Motion is also free and open source!

## Installation

Installing Motion on a Squarespace site is super-easy. In the bottom of your admin menu, there's an option for "Custom Code".

![](https://framerusercontent.com/images/93ksiIggFVGS9hicCjVve0ILZY.png?width=672&height=606)

Clicking on this reveals a "Code Injection" option.

![](https://framerusercontent.com/images/eYloUHHlZzf0znnpAjq9xhhSux0.png?width=674&height=766)

Here, in the Footer box, add:
    
    
    <script type="module" defer>
        import { animate } from "https://cdn.jsdelivr.net/npm/motion@11.13.5/+esm"
    
        // Your animation code here
        animate("h1", { opacity: [0, 1] })
    </script>

You can replace `11.13.5` here with whichever version you want to install. The latest published version can be found on the [npm package page](https://www.npmjs.com/package/motion).

This script contains all the Motion imports, but you can also achieve even greater filesize savings if you want to use just the mini version of the `animate` function, which is just 2.6kb, by importing from `https://cdn.jsdelivr.net/npm/motion@11.13.5/mini/+esm`:
    
    
    <script type="module" defer>
        import { animate } from "https://cdn.jsdelivr.net/npm/motion@11.13.5/mini/+esm"
    
        // Your animation code here
        animate("h1", { opacity: [0, 1] })
    </script>

## Selecting elements

In order to animate elements, we need to **select** them first.

We can select them generically using a tag selector, like `"a"` for selecting all the links on a page. For instance we can use `animate` and `press` to scale links in and out when they're pressed and de-pressed:
    
    
    <script type="module" defer>
        import { animate, press } from "https://cdn.jsdelivr.net/npm/motion@11.13.5/+esm"
    
        press("a", (element) => {
          animate(element, { scale: 0.7 })
    
          return () => animate(element, { scale: 1 })
        })
    </script>

## Custom scripts

By importing scripts directly from this URL, you're importing everything, even the bits of Motion you're not using. But, one of the great things about Motion is it's **tree-shakable**. This means you can use a bundler like [Vite](https://vite.dev/) or [Rollup](https://rollupjs.org/) to only include the bits you use.

In fact, this is a good practise for all of your Squarespace custom code. It will ensure you package everything into one neat bundle and only package the bits you need.

For example, if you only wanted to use the `[animate](./animate)`[ function](./animate), you could replace the above code with this:
    
    
    import { animate } from "motion"
    
    animate("header", { opacity: 1 })

Building this with Rollup, uploading to a CDN, and then including with an `async` JS tag will boost SEO scores even further:
    
    
    <script async src="https://yourdomain.com/my-script.js"></script>

## Next

Now that you have Motion running in your Squarespace project, you can follow our [quick start guide](./quick-start) to start making more complex animations.
