# Navigation drawer – Material Design 3

> Source: https://m3.material.io/components/navigation-drawer/overview

link
 
Copy link Link copied
 
star
 
Note:
 
The navigation drawer is no longer recommended in the Material 3 expressive update. For those who have updated, use an [expanded navigation rail](/m3/pages/navigation-rail/overview/) , which has mostly the same functionality of the navigation drawer and adapts better across window size classes.
 
link
 
Copy link Link copied
 
Use standard navigation drawers in expanded Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded window size class](/m3/pages/applying-layout/expanded) , large Window widths 1200dp to 1599dp, such as desktop. [More on large window size class](/m3/pages/applying-layout/large-extra-large) , and extra-large window sizes Window widths 1600dp and larger, such as ultra-wide monitors. [More on extra-large window size class](/m3/pages/applying-layout/large-extra-large)
 
Use modal navigation drawers in compact Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact window size class](/m3/pages/applying-layout/compact) and medium Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation. [More on medium window size class](/m3/pages/applying-layout/medium) window sizes
 
Can be open or closed by default
 
Two variants: standard and modal
 
Put the most frequent destinations at the top and group related destinations together
 
link
 
Copy link Link copied
 
Standard navigation drawer
 
Modal navigation drawer
 
link
 
Copy link Link copied
 
## Availability & resources
 
link
 
Copy link Link copied
 
Type Resource Status Design [Design Kit (Figma)](https://www.figma.com/community/file/1035203688168086460) Available Implementation [Flutter](https://api.flutter.dev/flutter/material/NavigationDrawer-class.html) Available [android Jetpack Compose](https://developer.android.com/develop/ui/compose/components/drawer) Available [android MDC-Android](https://github.com/material-components/material-components-android/blob/master/docs/components/NavigationDrawer.md) Available language Web Unavailable
 
link
 
Copy link Link copied
 
## M3 Expressive update
 
link
 
Copy link Link copied
 
May 2025
 
The navigation drawer is no longer recommended. Use the expanded navigation rail Expanded navigation rails show text labels and an extended FAB, and can be default or modal. [More on navigation rails](/m3/pages/navigation-rail/overview) instead. [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive)
 
link
 
Copy link Link copied
 
## Differences from M2
 
link
 
Copy link Link copied
 
Color: New color mappings and compatibility with dynamic color Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI. [More on dynamic color](/m3/pages/dynamic/choosing-a-source)
 
Variants: Distinguishes two separate variants of navigation drawer: Standard and modal
 
Shape: Rounded corners at the ending edge of the drawer
 
States States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) : Updated color and shape for indicating selected state
 
link
 
Copy link Link copied
 
M2: Navigation drawer had square corners and a rectangular shape indicating the active destination
 
M3: Navigation drawer has rounded corners, new color mappings, and an updated style for indicating the active destination
 
link
 
Copy link Link copied
