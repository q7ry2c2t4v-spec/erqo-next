# Side sheets – Material Design 3

> Source: https://m3.material.io/components/side-sheets/overview

link
 
Copy link Link copied
 
Use side sheets to provide optional content and actions without interrupting the main content
 
Two variants: standard Standard side sheets display content without blocking access to the screen’s primary content, such as an audio player at the side of a music app. They're often used in medium and expanded window sizes like tablet or desktop. and modal Modal side sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken. They're often used in compact window sizes, like mobile, due to limited screen size.
 
People can navigate to another region within the sheet
 
Side sheets can contain a back icon for navigation
 
link
 
Copy link Link copied
 
Standard side sheet
 
Modal side sheet
 
link
 
Copy link Link copied
 
## Availability & resources
 
link
 
Copy link Link copied
 
Type Resource Status Design [Design Kit (Figma)](http://goo.gle/m3-design-kit) Available Implementation Flutter Unavailable android Jetpack Compose Unavailable [android MDC-Android](https://github.com/material-components/material-components-android/blob/master/docs/components/SideSheet.md) Available language Web Unavailable
 
link
 
Copy link Link copied
 
## Differences from M2
 
link
 
Copy link Link copied
 
Right-to-left (RTL) language support with left side sheet
 
Color: New color mappings and compatibility with dynamic color Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI. [More on dynamic color](/m3/pages/dynamic/choosing-a-source)
 
Shape: Modal side sheets Modal side sheets appear in front of app content, disabling all other app functionality when they appear, and remaining on screen until confirmed, dismissed, or a required action has been taken. They're often used in compact window sizes, like mobile, due to limited screen size. have a 16dp corner radius
 
Side sheets have new color mappings to support dynamic color
