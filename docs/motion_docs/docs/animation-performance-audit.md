# Animation Performance Audit

> Source: https://motion.dev/docs/animation-performance-audit

The Animation Performance Audit is an AI skill that will audit every Motion & CSS animation in your codebase (or selected files), [classify their performance](../magazine/web-animation-performance-tier-list), and then generate a report including scorecard and available improvements.

/motion-audit

Your LLM can then follow this report to fix slow animations in your codebase.

Without exceptionally deep knowledge about the rendering pipeline, it's difficult to know how all the various methods of animating, and the CSS values that can be animated, are going to perform.

The [Web Animation Performance Tier List](../magazine/web-animation-performance-tier-list) covers the theory, but performance gotchas are everywhere and tends to slip as codebases and team sizes grow. This audit catches what manual review misses.

## Install

The Animation Performance Audit skill is available to [Motion+](../plus) and [MotionScore](https://score.motion.dev) members. Install it by running the following command in your terminal - it will auto-detect and configure all supported editors.

curl -sL "http://api.motion.dev/registry/skills/motion-audit?token=YOUR_TOKEN" | bash

Supported editors:

  * Cursor

  * Claude Code

  * Windsurf

  * Amp

  * OpenCode

  * Gemini CLI

## Usage

Run the audit inside a project using the `/motion-audit` command:

/motion-audit

By default, this will run a broad search of CSS, Motion, GSAP and Anime.js APIs in your codebase.

It's possible to limit the scope by passing a directory or filename:

Additionally, you can request to scope the audit to specific types of animations, or specific APIs:
    
    
    Can you perform a /motion-audit of all scroll animations

### Overall rank

The report starts with an easily-scannable letter ranking. This represents an average ranking of all discovered animations.
    
    
    
    

### Breakdown

Next, you'll receive a full breakdown describing the absolute number of animations for each tier, and the percentage of animations that this tier represents. The idea is for this graph to be top-heavy (more S, A and B tier animations than below).
    
    
    
    

### Findings

In findings, there's an entry for every actionable animation that explains: 

  * **What:** Filename, line numbers and tier

  * **Why:** The values being animated, what parts of the render pipeline they trigger

  * **Impact:** Is it worth fixing/changing?

  * **Improvements:** How to improve performance (where possible)

For instance, an animation like this:
    
    
    <motion.div
      animate={{
        scale: [1, 2, 2, 1, 1],
        rotate: [0, 0, 180, 180, 0],
        borderRadius: ["0%", "0%", "50%", "50%", "0%"],
      }}
      transition={{ repeat: Infinity }}
    />

Will flag that as these `scale` and `rotate` values are always animating together, we can animate `transform` directly to run this entirely on the GPU:
    
    
    <motion.div
      animate={{
        transform: [
          "scale(1) rotate(0deg)",
          "scale(2) rotate(0deg)",
          "scale(2) rotate(180deg)",
          "scale(2) rotate(180deg)",
          "scale(1) rotate(0deg)",
        ],
        borderRadius: ["0%", "0%", "50%", "50%", "0%"],
      }}
      transition={{ repeat: Infinity }}
    />

### Anti-patterns

This lists general patterns that can affect animation performance, like detecting `filter: blur(>10px)`, long running off-screen animations, excessive use of `will-change` etc.

For example, the animation from before is `repeat: Infinity`, so this part of the report will suggest that performance could be improved by swapping `animate` to `whileInView`, thereby only running the animation while inside the viewport.
    
    
    <motion.div
      whileInView={keyframes}
      transition={{ repeat: Infinity }}
    />

### Accessibility

This part of the report looks for things like support for `prefers-reduced-motion` or rapidly flashing animations and suggest ways to fix.

### Top 3 Recommendations

The report concludes with the top 3 priority fixes. This is a summary of the worst offenders, so you can ask your LLM to "fix the top 3 issues", or simply "fix" to fix everything in the report.

## Tiers

The broad tier list used for grading animations is as follows:

Tier| Cost| Animated properties  
---|---|---  
**S**|  Compositor only| `transform`, `opacity`, `filter`, `clip-path`, `ScrollTimeline`  
**A**|  JS → Compositor| Same properties, but set from JavaScript each frame  
**B**|  One-time layout read → S/A| `layout`, `layoutId`  
**C**|  Repaint each frame| `background-color`, `color`, `border-radius`, `box-shadow`, CSS variables, SVG attributes, View Transitions  
**D**|  Layout + repaint each frame| `width`, `height`, `margin`, `padding`, `top`/`left`, `font-size`, `gap`  
**F**|  Forced sync layout per cycle| Interleaved DOM reads/writes, `:root` CSS variable animation  
  
The full explanation of these can be found in the [Web Animation Performance Tier List](../magazine/web-animation-performance-tier-list).

## MotionScore

The Animation Performance Audit analyses your source code. To measure how your animations actually perform in the browser, run your live site through [MotionScore](https://score.motion.dev) \- it grades your site's animations, scroll animations, GPU pressure and style/layout thrashing, and suggests fixes you can copy/paste straight into your LLM.

#### Check your MotionScore

Enter a URL to audit your site's animation performance.

Check
