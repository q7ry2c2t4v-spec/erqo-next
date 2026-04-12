# Radix UI & Motion

> Source: https://motion.dev/docs/radix

[Radix](https://www.radix-ui.com/primitives) is one of the most popular component libraries for React, with pre-built, accessible components for common UI patterns like Accordion, Switch etc.

It doesn't come with animations out of the box, but in this guide we'll show how to integrate Motion for React with Radix UI to add a layer of polish to these components.

In this guide, we'll learn how to use `[motion](./react-motion-component)`[ components](./react-motion-component) with Radix primitives, as well as specific setups for exit and layout animations.

## Setup `motion` components with Radix

Most Radix components render and control their own DOM elements. But they also provide [the ](https://www.radix-ui.com/primitives/docs/guides/composition)`[asChild](https://www.radix-ui.com/primitives/docs/guides/composition)`[ prop](https://www.radix-ui.com/primitives/docs/guides/composition) that, when set to `true`, will make the component use the first provided child as its DOM node instead.

By passing a `[motion](./react-motion-component)`[ component](./react-motion-component) as this child, we can now use all of its animation props as normal:

<Toast.Root asChild>

<motion.div

initial={{ opacity: 0 }}

animate={{ opacity: 1 }}

layout

## Add exit animations to Radix

Many Radix components, like [Toast](https://www.radix-ui.com/primitives/docs/components/toast) or [Tooltip](https://www.radix-ui.com/primitives/docs/components/tooltip), would be perfect for exit animations, but can't perform them without Motion's `[AnimatePresence](./react-animate-presence)`.

`AnimatePresence` works by mounting and unmounting its children. This is how it tracks which components are exiting:
    
    
    <AnimatePresence>
      {isOpen && <motion.div exit={{ opacity: 0 }} />}
    </AnimatePresence>

By default Radix tends to control state like this `isOpen` internally. However, it provides some helper props for us to track or control this state externally.

For instance, the Tooltip component provides the `open` and `onOpenChange` props, which makes it easy to track the tooltip state:
    
    
    const [isOpen, setOpen] = useState(false)
    
    return (
      <Tooltip.Provider>
        <Tooltip.Root open={isOpen} onOpenChange={setOpen}>

Now we can use this state to conditionally render the tooltip contents.
    
    
    <AnimatePresence>
      {isOpen && (
        <Tooltip.Portal forceMount>
          <Tooltip.Content asChild>
            <motion.div
                exit={{ opacity: 0 }}

You can see in the above example we use the `forceMount` prop on the `Tooltip.Portal` component. Because Radix expects all its children to be rendered at all times, when we're conditionally rendering children like this, setting `forceMount` to `true` allows our enter/exit animations to work correctly.

## Create layout animations with Radix

[Layout animations](./react-layout-animations) also require this same pattern of hoisting state out of the component.
    
    
    const [tab, setTab] = useState("account")
    
    return (
      <Tabs.Root value={tab} onValueChange={setTab} asChild>
        <motion.div layout>

This is to ensure `motion` components know to perform layout animations when the state changes. You can even pass this state to `layoutDependency` for better performance.
    
    
    <motion.div layout layoutDependency={tab}>

## Radix x Motion examples

[Motion+](../plus) is a one-time payment, lifetime membership that gains you access to the source code of an ever-growing library of [Motion examples](../examples), as well as premium components like `[Cursor](./cursor)` and `[AnimateNumber](./react-animate-number)`.

Check out all the [Motion x Radix examples](https://motion.dev/examples?platform=react#radix).
