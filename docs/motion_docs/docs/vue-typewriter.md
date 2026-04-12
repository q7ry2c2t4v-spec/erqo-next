# Typewriter

> Source: https://motion.dev/docs/vue-typewriter

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

`Typewriter` is a 1.5kb Vue component for creating realistic typewriter animations.

## Features

  * **Natural animation:** Typing speeds and variance emulate real-world behaviours

  * **Playback control:** For easy scroll-triggered animations

  * **Accessible:** Correct ARIA labels for screen reader compatibility

  * **Reactive:** Will animate with backspace and typing to the latest provided value

`Typewriter` has a simple API.

<Typewriter>Hello world!</Typewriter>

When its content changes, it'll naturally type from the current content to the new content.

Typing speed is naturally variable, for example taking slight pauses between sentences and slowing down during longer words.

The text and cursor can be styled independently, and everything about the animation and typing behaviour can be modified. 
    
    
    <Typewriter
      speed="fast"
      :variance="0.8"
      backspace="word"
      :cursorBlinkSpeed="2"
    >
      {{text}}
    </Typewriter>

It's exclusive to [Motion+](../plus) members. Motion+ is a one-time fee, all-in membership that offers exclusive components, premium examples and access to a private Discord community.
