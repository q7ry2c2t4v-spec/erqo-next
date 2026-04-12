# Integrate Motion with Webflow

> Source: https://motion.dev/docs/webflow

[Webflow](https://webflow.com) already comes with some animation capabilities, but it can be that you want to go that little bit further by introducing custom code:

  * Animate previously unanimatable values (like gradients and masks)

  * Hardware accelerated [scroll animations](./scroll)

  * Complex timeline sequences

  * Three.js

If you're [migrating from GSAP](./migrate-from-gsap-to-motion), you'll achieve better Lighthouse Performance scores, and you can even use Motion without a business license.

In this guide, we'll walk through how you can add Motion to your project, and give an overview of how to optionally generate custom scripts for even better performance.

## Install

First, open the Pages dialog in your project and click "Edit page settings" on the page you want to add Motion to.

![](https://framerusercontent.com/images/JklBq7olyYn08WgdTuLrP709fuk.png?width=684&height=506)

Scroll down until you find the "Before `<body />` tag" dialog. In here, we can add our Motion code.

![](https://framerusercontent.com/images/4EuH3OU34DaMXdSy0wGhL66l2U.png?width=1276&height=694)

Here, you can add a new `script` block that imports Motion.
    
    
    <script type="module">
      import { animate, scroll } from "https://cdn.jsdelivr.net/npm/motion@11.13.5/+esm"
    
      animate("header", { opacity: 1 })
    </script>

You can replace `11.13.5` here with whichever version you want to install. The latest published version can be found on the [npm package page](https://www.npmjs.com/package/motion).

This script contains all the Motion imports, but you can also achieve even greater filesize savings if you want to use just the mini version of the `animate` function, which is just 2.3kb, by importing from `https://cdn.jsdelivr.net/npm/motion@11.13.5/mini/+esm`:
    
    
    <script type="module">
      import { animate } from "https://cdn.jsdelivr.net/npm/motion@11.13.5/mini/+esm"
    </script>

## Custom scripts

By importing scripts directly from this URL, you're importing everything, even the bits of Motion you're not using. But, one of the great things about Motion is it's **tree-shakable**. This means you can use a bundler like [Vite](https://vite.dev/) or [Rollup](https://rollupjs.org/) to only include the bits you use.

In fact, this is a good practise for all of your Webflow custom code. It will ensure you package everything into one neat bundle and only package the bits you need.

For example, if you only wanted to use the `[animate](./animate)`[ function](./animate), you could replace the above code with this:
    
    
    import { animate } from "motion"
    
    animate("header", { opacity: 1 })

Building this with Rollup, uploading to a CDN, and then including with an `async` JS tag will boost SEO scores even further:
    
    
    <script async src="https://yourdomain.com/my-script.js"></script>

## Next

Now that you have Motion running in your Webflow project, you can follow our [quick start guide](./quick-start) to start making animations!
