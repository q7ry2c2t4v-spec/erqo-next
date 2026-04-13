# useAnimationFrame

> Source: https://motion.dev/docs/vue-use-animation-frame

`useAnimationFrame` runs a callback once every animation frame.

useAnimationFrame((time) => {

domRef.value.style.transform = `rotateY(${time}deg)`

})

The callback is provided two arguments:

  * `time`, the total duration of time since the callback was first called.

  * `delta`, the total duration of time since the last animation frame.

<script setup>

import { useAnimationFrame } from 'motion-v'

  

const domRef = ref()

  

useAnimationFrame((time, delta) => {

domRef.value.style.transform = `rotateY(${time}deg)`

})

</script>

  

<template>

<div :ref="domRef" />

</template>
