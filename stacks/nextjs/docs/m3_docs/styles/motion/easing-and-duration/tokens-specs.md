# Easing and duration – Material Design 3

> Source: https://m3.material.io/styles/motion/easing-and-duration/tokens-specs

link
 
Copy link Link copied
 
star
 
Note:
 
In the expressive update, components and motion now use the [motion physics system](/m3/pages/motion-overview/) , which uses springs. Products should migrate to the new system. The easing and duration system is still used for transitions and can be used by teams that haven't yet updated to GM3 Expressive, but is no longer maintained.
 
link
 
Copy link Link copied
 
## Tokens
 
link
 
Copy link Link copied
 
Motion easing and duration can be implemented using easing and duration tokens. [Learn more about design tokens](/m3/pages/design-tokens/overview)
 
link
 
Copy link Link copied
 
Motion arrow_drop_down
 
search view_list expand_all
 
Standard, Android arrow_drop_down
 
grid_3x3
 
Custom composite with 2 properties grid_3x3
 
Custom composite with 2 properties grid_3x3
 
Custom composite with 2 properties grid_3x3
 
Custom composite with 2 properties grid_3x3
 
Custom composite with 2 properties grid_3x3
 
Custom composite with 2 properties folder Spring
 keyboard_arrow_down folder Easing
 keyboard_arrow_down folder Duration
 keyboard_arrow_down folder Style
 keyboard_arrow_down
 
link
 
Copy link Link copied
 
## Easing
 
link
 
Copy link Link copied
 
### Emphasized easing set
 
This set is the most common because it captures the expressive style of M3.
 
link
 
Copy link Link copied
 
pause
 Emphasized
 
pause
 Emphasized decelerate
 
pause
 Emphasized accelerate
 
link
 
Copy link Link copied
 
Info/Platform Emphasized Emphasized decelerate Emphasized accelerate Token md.sys.motion.easing.emphasized md.sys.motion.easing.emphasized.decelerate md.sys.motion.easing.emphasized.accelerate Android [pathInterpolator(M 0,0 C 0.05, 0, 0.133333, 0.06, 0.166666, 0.4 C 0.208333, 0.82, 0.25, 1, 1, 1)](https://developer.android.com/reference/android/view/animation/PathInterpolator) [PathInterpolator(0.05f, 0.7f, 0.1f, 1f)](https://developer.android.com/reference/android/view/animation/PathInterpolator) [PathInterpolator(0.3f, 0f, 0.8f, 0.15f)](https://developer.android.com/reference/android/view/animation/PathInterpolator) CSS N/A (Use Standard as a fallback) [cubic-bezier(0.05, 0.7, 0.1, 1.0)](https://www.w3schools.com/cssref/func_cubic-bezier.asp) [cubic-bezier(0.3, 0.0, 0.8, 0.15)](https://www.w3schools.com/cssref/func_cubic-bezier.asp) Flutter [easeInOutCubicEmphasized](https://api.flutter.dev/flutter/animation/Curves/easeInOutCubicEmphasized-constant.html) [Cubic(0.05, 0.7, 0.1, 1.0);](https://api.flutter.dev/flutter/animation/Cubic-class.html) [Cubic(0.3, 0.0, 0.8, 0.15);](https://api.flutter.dev/flutter/animation/Cubic-class.html) iOS N/A (Use Standard as a fallback) [ControlPoints:0.05f:0.7f:0.1f:1.0f];](https://developer.apple.com/documentation/quartzcore/camediatimingfunction) [ControlPoints:0.3f:0.0f:0.8f:0.15f];](https://developer.apple.com/documentation/quartzcore/camediatimingfunction) After Effects Use [After Effects Easing Panel](https://storage.googleapis.com/material-io-static/resources/material-easing-1.1.3.zxp) (download)
 
link
 
Copy link Link copied
 
### Standard easing set
 
This set is used for simple, small, or utility-focused transitions.
 
link
 
Copy link Link copied
 
pause
 Standard
 
pause
 Standard decelerate
 
pause
 Standard accelerate
 
link
 
Copy link Link copied
 
Standard Standard decelerate Standard accelerate Token md.sys.motion.easing.standard md.sys.motion.easing.standard.decelerate md.sys.motion.easing.standard.accelerate Android [PathInterpolator(0.2f, 0f, 0f, 1f)](https://developer.android.com/reference/android/view/animation/PathInterpolator) [PathInterpolator(0f, 0f, 0f, 1f)](https://developer.android.com/reference/android/view/animation/PathInterpolator) [PathInterpolator(0.3f, 0f, 1f, 1f)](https://developer.android.com/reference/android/view/animation/PathInterpolator) CSS [cubic-bezier(0.2, 0.0, 0, 1.0);](https://www.w3schools.com/cssref/func_cubic-bezier.asp) [cubic-bezier(0, 0, 0, 1);](https://www.w3schools.com/cssref/func_cubic-bezier.asp) [cubic-bezier(0.3, 0, 1, 1);](https://www.w3schools.com/cssref/func_cubic-bezier.asp) Flutter [Cubic(0.2, 0.0, 0, 1.0);](https://api.flutter.dev/flutter/animation/Cubic-class.html) [Cubic(0, 0, 0, 1);](https://api.flutter.dev/flutter/animation/Cubic-class.html) [Cubic(0.3, 0, 1, 1);](https://api.flutter.dev/flutter/animation/Cubic-class.html) iOS [ControlPoints:0.2f:0.0f:0.0f:1.0f](https://developer.apple.com/documentation/quartzcore/camediatimingfunction) [ControlPoints:0.0f:0.0f:0.0f:1.0f](https://developer.apple.com/documentation/quartzcore/camediatimingfunction) [ControlPoints:0.3f:0.0f:1.0f:1.0f];](https://developer.apple.com/documentation/quartzcore/camediatimingfunction) After Effects Use [After Effects Easing Panel](https://storage.googleapis.com/material-io-static/resources/material-easing-1.1.3.zxp) (download)
 
link
 
Copy link Link copied
 
## Duration
 
link
 
Copy link Link copied
 
### Short durations
 
These are used for small utility-focused transitions.
 
link
 
Copy link Link copied
 
Token Value md.sys.motion.duration.short1 50ms md.sys.motion.duration.short2 100ms md.sys.motion.duration.short3 150ms md.sys.motion.duration.short4 200ms
 
pause
 Selection controls have a short duration of 200ms with Standard easing
 
link
 
Copy link Link copied
 
### Medium durations
 
These are used for transitions that traverse a medium area of the screen.
 
link
 
Copy link Link copied
 
Token Value md.sys.motion.duration.medium1 250ms md.sys.motion.duration.medium2 300ms md.sys.motion.duration.medium3 350ms md.sys.motion.duration.medium4 400ms
 
pause
 A FAB expanding into a Sheet uses a 400ms duration with Emphasized easing
 
link
 
Copy link Link copied
 
### Long durations
 
These durations are often paired with Emphasized easing. They're used for large expressive transitions.
 
link
 
Copy link Link copied
 
Token Value md.sys.motion.duration.long1 450ms md.sys.motion.duration.long2 500ms md.sys.motion.duration.long3 550ms md.sys.motion.duration.long4 600ms
 
pause
 A Card expanding to full screen uses a long 500ms duration with Emphasized easing
 
link
 
Copy link Link copied
 
### Extra long durations
 
Though rare, some transitions use durations above 600ms. These are usually used for ambient transitions that don't involve user input.
 
link
 
Copy link Link copied
 
Token Value md.sys.motion.duration.extra-long1 700ms md.sys.motion.duration.extra-long2 800ms md.sys.motion.duration.extra-long3 900ms md.sys.motion.duration.extra-long4 1000ms
 
pause
 An ambient carousel auto-advance transition uses an extra long 1000ms duration with emphasized easing
