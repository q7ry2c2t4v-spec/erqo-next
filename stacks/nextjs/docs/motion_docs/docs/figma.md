# Animate your Figma projects with Motion

> Source: https://motion.dev/docs/figma

Figma offers powerful [site-building](https://www.figma.com/sites/) and [code generation](https://www.figma.com/make/) features. Motion is available to use in both.

When adding effects via the Figma Sites Interactions menu, you're generating Motion animations with no-code!

![Screenshot of Figma Sites interface, highlighting Hover effect](https://framerusercontent.com/images/r6kq04Sawfi36eiGmq1gAZS3134.png)

In upcoming versions of Figma, it'll be possible to generate and write your own Motion code into your Figma site.

For now, you can already add Motion code via the [Figma Make](https://www.figma.com/make/) beta. 

## Figma Make

Figma Make is an AI code generator that can generate React code from text, image, and Figma artboard prompts.

In general, it will produce Motion code simply by asking it to animate something. For instance, you can give it a screenshot of the [Motion homepage](../) and tell it to animate:

![](https://framerusercontent.com/images/I9UrB7u2e1BkL2tS96LYDd7ms.png)

This will produce a code file with Motion already imported:
    
    
    <motion.div
      className={className}
      variants={container}
      initial="hidden"
      animate="visible"
    >
      {words.map((word, index) => (
        <motion.span
          key={index}
          variants={child}
          style={{ display: "inline-block", marginRight: "0.25em" }}
        >
          {word}
        </motion.span>
      ))}
    </motion.div>

If your generated Make project doesn't include a `motion` import then you can either ask the AI to add it for you, or simply add an import to the top of your component:
    
    
    import { motion } from "motion/react"

### Imports

As with many AI generators, Figma Make has the tendency to import Motion via `"framer-motion"`. This is okay! This import will work for many versions to come.

However, you can also change this manually to `"motion/react"` and your project will continue to work the same.

## Next

With Motion set up in your Figma project, we recommend you follow the rest of the [Quick Start](./react) guide to begin learning Motion for React.
