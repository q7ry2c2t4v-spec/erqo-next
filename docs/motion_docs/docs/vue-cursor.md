# Cursor

> Source: https://motion.dev/docs/vue-cursor

Checking Motion+ status…

Cursor

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

Cursor is a creative cursor component for Vue. It makes it quick and simple to build custom cursors, or cursor-following animations.

It's exclusive to [Motion+](../plus) members. Motion+ is a one-time fee, all-in membership that offers exclusive components, premium examples and access to a private Discord community.

With its default settings, it replaces the browser cursor with a dynamic cursor.

<Cursor />

This cursor automatically detects the types of content it's hovering over. When hovering a link or button, it grows. When it's pressed, it shrinks. It also detects `disabled` status.

When hovering selectable text, it transforms into a text selector that grows with the size of the text.

  

The cursor can be fully styled with CSS and animated using Motion's variants. It's also possible to set custom content when hovering over specific elements.

With only a prop, we can create a follow cursor effect. Great for previews or popup information.
    
    
    <Cursor follow />

We can also render as many cursors as we like, all at the same time. Attaching them to the cursor with springs of varying strengths.

In this guide, we'll learn how to install `Cursor`, customise it with its various options and `useCursorState` hook.
