# Extended FAB – Material Design 3

> Source: https://m3.material.io/components/extended-fab/overview

link
 
Copy link Link copied
 
Use for the most common or important action on a screen
 
Three variants: small, medium, and large
 
Use instead of FAB when label text is needed to understand action
 
link
 
Copy link Link copied
 
Small extended FAB
 
Medium extended FAB
 
Large extended FAB
 
link
 
Copy link Link copied
 
## Availability & resources
 
link
 
Copy link Link copied
 
Type Resource Status Design [Design Kit (Figma)](https://www.figma.com/community/file/1035203688168086460) Available Implementation [Flutter](https://api.flutter.dev/flutter/material/FloatingActionButton-class.html) Available [android Jetpack Compose](https://developer.android.com/develop/ui/compose/components/fab?hl=en#extended) Available [android Jetpack Compose: Expressive](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ExtendedFloatingActionButton(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) Available [android MDC-Android](https://github.com/material-components/material-components-android/blob/master/docs/components/FloatingActionButton.md#extended-fabs) Available [android MDC-Android: Expressive](https://github.com/material-components/material-components-android/blob/master/docs/components/FloatingActionButton.md#extended-fabs) Available [language Web](https://github.com/material-components/material-web/blob/main/docs/components/fab.md) Available language Web: Expressive Unavailable
 
link
 
Copy link Link copied
 
## M3 Expressive update
 
link
 
Copy link Link copied
 
May 2025
 
The extended FAB now has three sizes: small, medium, and large, each with updated type styles. These align with the FAB Floating action buttons (FABs) help people take primary actions. [More on FABs](/m3/pages/fab/overview) sizes for an easier transition between FABs. The baseline extended FAB is no longer recommended and should be replaced with the small extended FAB. Surface and FABs are also no longer recommended. [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive)
 
link
 
Copy link Link copied
 
Variants and naming:
 
Added new sizes
 
Small: 56dp
 
Medium: 80dp
 
Large: 96dp
 
No longer recommended
 
Baseline extended FAB (56dp)
 
Surface extended FAB
 
Updates:
 
Adjusted typography to be larger
 
The baseline extended FAB is replaced with a set of small, medium, and large extended FABs with new typography
 
link
 
Copy link Link copied
 
## Differences from M2
 
link
 
Copy link Link copied
 
Color: New color mappings and compatibility with dynamic color
 
Layout: Extended FAB is the same height as the FAB
 
Shape: Boxier style with smaller corner radius
 
link
 
Copy link Link copied
 
M2: Extended FABs are pill-shaped and have a different height and elevation
 
M3: Extended FABs share the same height, boxier shape, and simpler elevation model as FABs
