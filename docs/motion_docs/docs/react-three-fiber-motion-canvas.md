# MotionCanvas

> Source: https://motion.dev/docs/react-three-fiber-motion-canvas

Deprecated

React Three Fiber (R3F) uses the [Canvas component](https://docs.pmnd.rs/react-three-fiber/api/canvas) to establish a 3D scene. Using this component will break context with parent components.

To link Motion 3D context with DOM Motion, for example to share a default transition or link the [LayoutCamera](./react-three-fiber-layout-cameras) with layout animations, the `MotionCanvas` component can be used instead.

import { MotionConfig, motion } from "motion/react"

import { MotionCanvas, motion as motion3d } from "framer-motion-3d"

  

export function App() {

return (

<MotionConfig transition={{ type: "spring" }}>

<motion.div animate={{ scale: 2 }}>

<MotionCanvas>

<motion3d.boxGeometry animate={{ x: 1 }} />

</MotionCanvas>

</motion.div>

</MotionConfig>

)

}

It shares all the same props as R3F's `Canvas` component, with the omission of `resize`, as `MotionCanvas` implements its own resize options to sync with Framer Motion's layout animations.

It's also mandatory to enable [3D scenes within layout animations](./react-three-fiber-layout-cameras).
