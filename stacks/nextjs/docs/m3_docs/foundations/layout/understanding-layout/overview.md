# Layout – Material Design 3

> Source: https://m3.material.io/foundations/layout/understanding-layout/overview

link
 
Copy link Link copied
 
Use layout to direct attention to the action users want to take
 
Adapt layouts to compact Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact window size class](/m3/pages/applying-layout/compact) , medium Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation. [More on medium window size class](/m3/pages/applying-layout/medium) , expanded Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded window size class](/m3/pages/applying-layout/expanded) , large Window widths 1200dp to 1599dp, such as desktop. [More on large window size](/m3/pages/applying-layout/large-extra-large) , and extra-large Window widths 1600dp and larger, such as ultra-wide monitors. [More on extra-large window size](/m3/pages/applying-layout/large-extra-large) window size classes
 
Build from an established canonical layout Designs for common screen layouts across window size classes
 
Consider how spacing and the parts of the layout work together
 
Material layout guidance applies to Android and the web
 
link
 
Copy link Link copied
 
Column
 
Fold
 
Margin
 
Pane
 
Drag handle
 
Spacer
 
Window
 
link
 
Copy link Link copied
 
## What’s new
 
link
 
Copy link Link copied
 
When creating new layouts, begin from a [canonical layout](/m3/pages/canonical-layouts/overview) rather than a layout grid. This helps ensure that your layouts can scale across devices and form factors.
 
[Window size classes](/m3/pages/applying-layout/window-size-classes) are opinionated breakpoints. Material Design recommends you create layouts for five window size classes: compact Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact window size class](/m3/pages/applying-layout/compact) , medium Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation. [More on medium window size class](/m3/pages/applying-layout/medium) , expanded Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded window size class](/m3/pages/applying-layout/expanded) , large Window widths 1200dp to 1599dp, such as desktop. [More on large window size](/m3/pages/applying-layout/large-extra-large) , and extra-large Window widths 1600dp and larger, such as ultra-wide monitors. [More on extra-large window size](/m3/pages/applying-layout/large-extra-large)
 
Layouts with multiple panes of content can be resized with a drag handle
 
M3 considers multiple layouts for a variety of sizes
 
link
 
Copy link Link copied
 
## Layout terms
 
link
 
Copy link Link copied
 
Column : one or more vertical blocks of content within a pane
 
Drag handle: The component that resizes panes
 
Fold : on foldable devices, a flexible area of the screen or, on dual-screen devices, a hinge that separates two displays
 
Margin : the space between the edge of the screen and any elements inside of it
 
Multi-window mode : enables multiple apps to share the same screen simultaneously
 
Pane : a layout container that houses other components and elements within a single app. A pane can be: fixed, flexible, floating, or semi permanent
 
Spacer : the space between two panes
 
Window size class : opinionated breakpoint, the window size at which a layout needs to change to match available space, device conventions, and ergonomics
