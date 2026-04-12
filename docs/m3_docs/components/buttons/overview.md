# Buttons – Material Design 3

> Source: https://m3.material.io/components/buttons/overview

link
 
Copy link Link copied
 
Two variants: default and toggle
 
Can contain an optional leading icon
 
Five color options: elevated, filled, tonal, outlined, and text
 
Five size recommendations: extra small, small, medium, large, and extra large
 
Two shape options: round and square
 
Keep labels concise and use sentence case
 
link
 
Copy link Link copied
 
Elevated button
 
Filled button
 
Filled tonal button
 
Outlined button
 
Text button
 
link
 
Copy link Link copied
 
## Availability & resources
 
link
 
Copy link Link copied
 
Type Resource Status Design [Design Kit (Figma)](https://www.figma.com/community/file/1035203688168086460) Available Implementation [Flutter](https://api.flutter.dev/flutter/material/ThemeData/useMaterial3.html) Available [android Jetpack Compose](https://developer.android.com/develop/ui/compose/components/button) Available [android Jetpack Compose: Expressive](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.material3.ButtonColors,androidx.compose.material3.ButtonElevation,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) Available [android MDC-Android](https://github.com/material-components/material-components-android/blob/master/docs/components/Button.md) Available [android MDC-Android: Expressive](https://github.com/material-components/material-components-android/blob/master/docs/components/Button.md) Available [language Web](https://github.com/material-components/material-web/blob/main/docs/components/button.md) Available language Web: Expressive Unavailable
 
link
 
Copy link Link copied
 
## M3 Expressive update
 
link
 
Copy link Link copied
 
May 2025
 
Buttons now have a wider variety of shapes and sizes, toggle functionality, and can change shape when selected. [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive)
 
link
 
Copy link Link copied
 
Variants and naming:
 
Default and toggle (selection)
 
Color styles are now configurations. (elevated, filled, tonal, outlined, text)
 
Shapes:
 
Round and square
 
Shape morphs when pressed
 
Shape morphs when selected
 
Sizes:
 
Extra small
 
Small (existing, default)
 
Medium
 
Large
 
Extra large
 
New padding for small buttons:
 
16dp (recommended to match padding of new sizes)
 
24dp (not recommended)
 
Five sizes
 
Toggle (selection)
 
Two shapes
 
Two small padding widths
 
link
 
Copy link Link copied
 
## Differences from M2
 
link
 
Copy link Link copied
 
Color: New color mappings and compatibility with dynamic color. Icons and labels now share the same color. Neutral text button is no longer recommended.
 
Icons: Standard size for leading and trailing icons is now 20dp
 
Shape: Fully-rounded corner radius and additional height options
 
link
 
Copy link Link copied
 
M2: Buttons have a height of 36dp and slightly rounded corner radius
 
M3: Default buttons are taller at 40dp and have fully rounded corners
