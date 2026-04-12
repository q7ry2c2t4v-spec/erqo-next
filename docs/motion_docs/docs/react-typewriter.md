# Typewriter

> Source: https://motion.dev/docs/react-typewriter

Checking Motion+ status…

Typewriter

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

`Typewriter` is a 1.3kb React component for creating realistic typewriter animations. It emulates natural human typing behaviour, handles dynamic content (with intelligent backspacing), and provides full playback control for scroll-triggered effects. All while ensuring screen reader accessibility. 

<Typewriter>Hello world!</Typewriter>

`Typewriter` is exclusive to [Motion+](../plus) members. Motion+ is a one-time payment, lifetime membership that unlocks exclusive components, premium examples and access to a private Discord community.

## Features

  * **Natural animation:** Typing speeds and variance emulate real-world behaviour.

  * **Playback control:** Easily play and pause animations, perfect for scroll-triggered animations.

  * **Accessible:** Correct ARIA labels for screen reader compatibility.

  * **Reactive:** Will animate with backspace and typing to the latest provided value.

  * **Customisable:** Control everything from typing speed and variance to cursor style and blink speed.

## Install

First, add the `motion-plus` package to your project using your [private token](https://plus.motion.dev). You need to be a [Motion+ member](../plus) to generate a private token.
    
    
    npm install "https://api.motion.dev/registry.tgz?package=motion-plus&version=2.8.0&token=YOUR_AUTH_TOKEN"

## Usage

Import from `"motion-plus/react"`.
    
    
    import { Typewriter } from "motion-plus/react"

By passing a string as the `Typewriter` child, it will animate that text in character by character.
    
    
    <Typewriter>Hello world!</Typewriter>

### Dynamic content

When the `children` prop changes, `Typewriter` will intelligently animate from the old text to the new text. By default, it backspaces character by character to the point of difference and then types out the new content.

By default, each character will be backspaced individually. Using the `backspace` prop we can also backspace each word/special character:
    
    
    <Typewriter backspace="word">{text}</Typewriter>

Or remove all the mismatching content immediately:
    
    
    <Typewriter backspace="all">{text}</Typewriter>

### Adjust speed

The animation will emulate "normal" real-world typing speeds, based on real research. It's also possible to set speed as `"fast"`, `"slow"`, or a custom interval (in milliseconds).
    
    
    <Typewriter speed="slow">Hello world!</Typewriter>

By default, the typing speed will vary naturally per character, based on the type of content being "typed".

For example, typing will slow down while typing long words, while at the start/end of a word, when using punctuation, or when using uncommon character combinations.

This can be configured with the `variance` prop. This is a `0`-`1` factor applied to `speed`, to create a range of speeds that we can randomly select between.

So for instance if we want no variance then we can set this to `0`.
    
    
    <Typewriter variance={0}>Hello world!</Typewriter>

Or to have some variance it could be set to `0.5`:
    
    
    <Typewriter variance={0.5}>Hello world!</Typewriter>

###
