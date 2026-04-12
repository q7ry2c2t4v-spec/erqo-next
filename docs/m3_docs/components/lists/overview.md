# Lists – Material Design 3

> Source: https://m3.material.io/components/lists/overview

link
 
Copy link Link copied
 
Use lists to help people find a specific item and act on it
 
Order list items in logical ways, like alphabetical or numerical
 
Keep items short and easy to scan
 
Show icons, text, and actions in a consistent format
 
Choose between standard and segmented styles
 
link
 
Copy link Link copied
 
A list item's label text, supporting text, image, and trailing icon can be customized to create a variety of lists
 
link
 
Copy link Link copied
 
## Availability & resources
 
link
 
Copy link Link copied
 
Type Resource Status Design [Design Kit (Figma)](https://www.figma.com/community/file/1035203688168086460) Available Implementation [Flutter](https://api.flutter.dev/flutter/material/ListTile-class.html) Available [android Jetpack Compose](https://developer.android.com/develop/ui/compose/lists) Available [android Jetpack Compose: Expressive](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ListItem%28kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.material3.ListItemColors,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp%29) Available [android MDC-Android](https://developer.android.com/develop/ui/views/layout/recyclerview) Available [android MDC-Android: Expressive](https://github.com/material-components/material-components-android/blob/master/docs/components/List.md#m3-expressive) Available [language Web](https://github.com/material-components/material-web/blob/main/docs/components/list.md) Available language Web: Expressive Unavailable
 
link
 
Copy link Link copied
 
## M3 Expressive update
 
link
 
Copy link Link copied
 
Lists have a new segmented visual style, improved selection treatment, and support for slots. [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive)
 
link
 
Copy link Link copied
 
December 2025
 
Variants:
 
Added expressive list
 
Recommended for new designs
 
List ( baseline Baseline variants are the original M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles. [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive ) ) is still available
 
New visual styles:
 
Standard or segmented
 
Highlighted selection states
 
Flexible slots
 
Supported platforms:
 
[MDC-Android](https://github.com/material-components/material-components-android/blob/master/docs/components/List.md#m3-expressive)
 
[Jetpack Compose](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ListItem%28kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.material3.ListItemColors,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp%29)
 
Expressive lists feature improved selection states
 
link
 
Copy link Link copied
 
## Differences from M2 to M3 baseline
 
link
 
Copy link Link copied
 
Color: New color mappings and compatibility with dynamic color Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI. [More on dynamic color](/m3/pages/dynamic/choosing-a-source)
 
Layout: Padding and spacing rules are updated to be more consistent
 
Height: The tallest element within a list item determines the list item’s height - either 56dp, 72dp, or 88dp
 
Alignment:
 
In most cases, elements in a list item are middle-aligned
 
If a list is 88dp or larger, or contains three or more lines of text, elements are top-aligned
 
link
 
Copy link Link copied
 
M2: Non-standard heights and alignments
 
M3 (baseline): Standardized heights and alignments
