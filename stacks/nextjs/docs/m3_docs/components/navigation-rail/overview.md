# Navigation rail – Material Design 3

> Source: https://m3.material.io/components/navigation-rail/overview

link
 
Copy link Link copied
 
Use navigation rails in medium, expanded, large, or extra-large window sizes
 
Can contain 3-7 destinations plus an optional FAB
 
Always put the rail in the same place, even on different screens of an app
 
link
 
Copy link Link copied
 
pause
 Collapsed and expanded navigation rails can transition between each other on any device, including:
 
1. Large or medium window size classes like tablets 2. Compact window size classes like phones in portrait orientation
 
link
 
Copy link Link copied
 
## Availability & resources
 
link
 
Copy link Link copied
 
Type Resource Status Design [Design Kit (Figma)](https://www.figma.com/community/file/1035203688168086460) Available Implementation [Flutter](https://api.flutter.dev/flutter/material/NavigationRail-class.html) Available [android Jetpack Compose](https://developer.android.com/develop/ui/compose/components/navigation-rail) Available [android Jetpack Compose: Expressive](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#NavigationRail(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) Available [android MDC-Android](https://github.com/material-components/material-components-android/blob/master/docs/components/NavigationRail.md) Available [android MDC-Android: Expressive](https://github.com/material-components/material-components-android/blob/master/docs/components/NavigationRail.md) Available language Web Unavailable language Web: Expressive Unavailable
 
link
 
Copy link Link copied
 
## M3 Expressive update
 
link
 
Copy link Link copied
 
May 2025
 
A collapsed and expanded navigation rail have been introduced to replace the baseline nav rail. The expanded nav rail is meant to replace the navigation drawer Navigation drawers let people switch between UI views on larger devices. In the expressive update, use an expanded navigation rail. [More on navigation drawers](/m3/pages/navigation-drawer/overview) . [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive)
 
link
 
Copy link Link copied
 
Variants and naming:
 
The baseline navigation rail is no longer recommended
 
Added two wider navigation rails:
 
Collapsed: replaces baseline nav rail
 
Expanded : replaces navigation drawer Navigation drawers let people switch between UI views on larger devices. In the expressive update, use an expanded navigation rail. [More on navigation drawers](/m3/pages/navigation-drawer/overview)
 
Configurations:
 
Expanded rail modality:
 
Non-modal
 
Modal
 
Expanded behavior:
 
Transition to collapsed navigation rail
 
Hide when collapsed
 
Color:
 
Active label on vertical items changed from on surface variant to secondary
 
The collapsed and expanded navigation rails match visually and can transition into each other
 
link
 
Copy link Link copied
 
## Differences from M2
 
link
 
Copy link Link copied
 
Behavior: Predictive back interaction
 
Color: New color mappings and compatibility with dynamic color
 
States: The active destination can be indicated with a pill shape in a contrasting color
 
link
 
Copy link Link copied
 
M2: The navigation rail uses icon color, weight, and fill to communicate which destination is active
 
M3: The navigation rail uses a pill-shaped active indicator to communicate which destination is active
