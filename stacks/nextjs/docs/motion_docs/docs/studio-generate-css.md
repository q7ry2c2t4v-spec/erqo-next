# Generate CSS

> Source: https://motion.dev/docs/studio-generate-css

Motion Studio can generate Motion springs and other easing functions as CSS `[linear()](https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function/linear)`[ easing function](https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function/linear) \- no animation library required!

For example, you can ask your LLM to "Make a CSS spring curve, snappy but bouncy" and it will generate a `linear()` curve with the right duration and resolution to ensure your animation is smooth:

// LLM receives:

500ms linear(0, 0.009, 0.035 2.1%, /* ... */)

`linear()` can create all kinds of easing curves that were previously impossible with CSS, like spring and bounce effects.

The downside to `linear()` is its maintainability. With Motion, it's usually easy to write and understand this kind of animation:

{ type: "spring", bounce: 0.2 }

However, with CSS and `linear()`, you need to visit a generation tool to output a property that looks like this:

linear(

0, 0.009, 0.035 2.1%, 0.141, 0.281 6.7%, 0.723 12.9%, 0.938 16.7%, 1.017,

1.077, 1.121, 1.149 24.3%, 1.159, 1.163, 1.161, 1.154 29.9%, 1.129 32.8%,

1.051 39.6%, 1.017 43.1%, 0.991, 0.977 51%, 0.974 53.8%, 0.975 57.1%,

0.997 69.8%, 1.003 76.9%, 1.004 83.8%, 1

)

Tweaking this animation involves bouncing back and forth between your code editor and the curve generator tool. But Motion Studio allows you to do this directly in your editor.

## Usage

Once [installed](./studio-install), you can give your LLM commands like "generate a CSS spring that is very bouncy" and it'll either reply with a `linear()` easing curve or insert it directly into your code.

### Springs

For CSS generation, Motion's [springs](./spring) are defined with two parameters, `visualDuration` and `bounce`.

Ask the LLM to generate a spring that "lasts 0.2 seconds and is very bouncy" will generate a CSS animation that **appears** to take 0.2 seconds to reach its target value, with oscillation taking place after this duration. This makes it easy to compose the spring animation with other time-based animations, and to tweak the bounciness without having to change the duration of the spring to compensate.

### Bounce

Not to be confused with the bounciness of a spring, a bounce easing function can make something look like it's bouncing against a hard surface.

Ask to "generate a bounce easing curve" or similar. It will default to longer durations, like 1 second, as this makes for more realistic gravity-like motion.

You can ask it to feel heavier or lighter and it will adjust the time accordingly.
