# splitText

> Source: https://motion.dev/docs/split-text

`splitText` is a tiny (+0.7kb) utility that makes it simple to create complex, beautiful split text animations with Motion.

Break down text into individual characters, words, and lines, to create staggered enter or scroll-driven text effects with just a few lines of code.

`splitText` is exclusive to [Motion+](../plus) members. Motion+ is a one-time payment, lifetime membership that unlocks exclusive components, premium examples and access to a private Discord community.

## Features

  * **Animate anything:** Split text into characters, words and lines to animate each independently.

  * **Lightweight** : Only adds 0.7kb to your project bundle.

  * **Simple API:** A clean API leaves your code maintainable.

  * **Accessible:** Correctly applies ARIA tags to leave your text readable for all users.

  * **Flexible:** Animate with Motion, CSS, or a library of your choice.

## Install

First, add the Motion+ library to your project using your [private token](https://plus.motion.dev). You need to be a [Motion+ member](../plus) to generate a private token.

npm install https://api.motion.dev/registry\?package\=motion-plus\&version\=2.4.0\&token=YOUR_AUTH_TOKEN

Once installed, `splitText` can be imported via `motion-plus`:
    
    
    import { splitText } from "motion-plus"

## Usage

`splitText` accepts a CSS selector or an HTML Element. It replaces the element's text content with `<span>` tags that wrap individual characters, words, and (optionally) lines.

It returns an object containing `chars`, `words`, and `lines` as arrays of elements, so they can be animated right away with Motion's `animate` and `stagger` functions.
    
    
    const { chars } = splitText("h1")
    
    animate(
      chars,
      { opacity: [0, 1], y: [10, 0] },
      { duration: 1, delay: stagger(0.05) }
    )

The returned arrays are regular elements so you're not limited to animating them with Motion. You could animate them with CSS, or another animation library of your choice. Or, you could attach gesture recognisers to each element individually, for instance with Motion's `[hover](./hover)`[ function](./hover).
    
    
    const { words } = splitText("h1")
    
    hover(words, (wordElement) => {
      // Hover logic
    })

## Techniques & troubleshooting

### Enter animations

To perform enter animations, it might be necessary to set the container to `visibility: hidden` via CSS until we're ready to animate. 
    
    
    .container {
      visibility: hidden;
    }
    
    
    document.querySelector(".container").style.visibility = "visible"
    
    const { words } = splitText(".container")
    animate(words, { opacity: [0, 1] })

Otherwise we might see a flash of visible text until our JS has loaded.

### Working with custom fonts

If you have custom fonts that download **after** `splitText` is executed, it can be that the text is split incorrectly because the dimensions of the text have changed.

To fix this, we can await the browser's `document.fonts.ready` promise:
    
    
    document.fonts.ready.then(() => {
      const { words } = splitText(element)
    
      animate(
        words,
        { y: [-10, 10] },
        { delay: stagger(0.04) }
      )
    })

### Targeting with CSS

Each split component will receive `split-char`, `split-word` and `split-line` classes so you can select them with CSS. Each component additionally receives a `data-index` of its position within the overall character, word or line lists respectively.
    
    
    .split-char[data-index=3] {
      color: red;
    }

The provided classes are configurable with the `charClass`, `wordClass` and `lineClass` options.
    
    
    splitText(element, { charClass: "my-char-class" })

### Links/spans are being removed

`splitText` doesn't currently preserve existing tags within the text, so links and other styling spans will be removed.

It's possible to fix this by wrapping the text before/after the tag with its own `span` and splitting these individually: 
    
    
    <h2>
      <span class="before">Before</span>
      <a href="#">Link</a>
      <span class="after">After</span>
    </h2>
    
    <script>
      const chars = [
        ...splitText(".before").chars,
        ...splitText("a").chars,
        ...splitText(".after").chars,
      ]
    </script>

### SVG `<text />` isn't working

`<text />` elements are not supported.

### Hyphenation is being removed

By default, `splitText` wraps each character in its own element, which breaks CSS hyphenation and soft hyphens (`&shy;`).

To preserve hyphenation, set `preserveHyphens: true`:
    
    
    splitText(element, { preserveHyphens: true })

This skips character splitting, keeping words intact so the browser can hyphenate them.

When setting `preserveHyphens` to `true`, the `chars` array will be empty.

### `text-align: justify` is being lost

Splitting test in this way is incompatible with how browsers handle `text-align: justify`. You can implement something similar by adding styles for `split-line`:
    
    
    .align-justify .split-line {
      display: flex;
      justify-content: space-between;
    }

## Options

### `splitBy`

**Default:** `" "` (space)

The string to split the text by. 
    
    
    <p>My+custom+text</p>
    
    
    splitText(paragraph, { splitBy: "+" })

When splitting with a custom character, lines might start to wrap. Ensure the wrapper element is set to `text-wrap: nowrap` to keep text on a single line.

### `charClass`

**Default:** `"split-char"`

A class to apply to each split `char` component.

### `wordClass`

**Default:** `"split-word"`

A class to apply to each split `word` component.

### `lineClass`

**Default:** `"split-line"`

A class to apply to each split `line` component.

### `preserveHyphens`

**Default:**`false`

Set to `true` to preserve soft and automatic hyphenation.

When setting `preserveHyphens` to `true`, the `chars` array will be empty.
