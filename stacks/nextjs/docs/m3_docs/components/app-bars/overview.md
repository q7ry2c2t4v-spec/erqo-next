# Top app bar – Material Design 3

> Source: https://m3.material.io/components/app-bars/overview

link
 
Copy link Link copied
 
Focus on describing the current page and provide 1–2 essential actions
 
Displays labels and page navigation controls at the top of the page. (Use a toolbar Toolbars display frequently used actions relevant to the current page. [More on toolbars](/m3/pages/toolbars/overview) to display page actions)
 
Four variants: Search app bar, small, medium flexible, large flexible
 
On scroll, apply a fill color to separate from body content
 
Can animate on and off screen with another bar of controls, like a row of chips Chips help people enter information, make selections, filter content, or trigger actions. [More on chips](/m3/pages/chips/overview)
 
link
 
Copy link Link copied
 
Search app bar
 
Small
 
Medium flexible
 
Large flexible
 
link
 
Copy link Link copied
 
## Availability & resources
 
link
 
Copy link Link copied
 
Type Resource Status Design [Design Kit (Figma)](https://www.figma.com/community/file/1035203688168086460) Available Implementation [Flutter](https://api.flutter.dev/flutter/material/AppBar-class.html) Available [android Jetpack Compose](https://developer.android.com/develop/ui/compose/components/app-bars?hl=en) Available [android Jetpack Compose: Expressive](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#AppBarRow(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)) Available [android MDC-Android](https://github.com/material-components/material-components-android/blob/master/docs/components/TopAppBar.md) Available [android MDC-Android: Expressive](https://github.com/material-components/material-components-android/blob/master/docs/components/TopAppBar.md) Available language Web Unavailable language Web: Expressive Unavailable
 
link
 
Copy link Link copied
 
## M3 Expressive update
 
May 2025 The new search app bar supports icons inside and outside the search bar, and centered text. It opens the [search view](/m3/pages/search/overview) component when selected. The new medium flexible and large flexible app bars come with significant improvements, and should replace medium and large app bars, which are no longer recommended. The small app bar is updated with the same flexible improvements. [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive)
 
link
 
Copy link Link copied
 
Variants and naming:
 
Renamed component from top app bar to app bar
 
Added search app bar
 
M edium and large app bars are no longer recommended
 
Added medium flexible and large flexible app bars with:
 
Reduced overall height
 
Larger title text
 
Subtitle
 
Left- and center-aligned text options
 
Text wrapping
 
More flexible elements for imagery and filled buttons
 
Added features to small app bar:
 
Subtitle
 
Center-aligned text option
 
More flexible elements for imagery and filled buttons
 
Search app bar
 
Small
 
Medium flexible
 
Large flexible
 
link
 
Copy link Link copied
 
## Differences from M2
 
link
 
Copy link Link copied
 
Color: New color mappings and compatibility with dynamic color
 
On scroll: No drop shadow, instead a color fill creates separation from content
 
Typography: Larger default text
 
Layout: Smaller default height
 
link
 
Copy link Link copied
 
M2: Elevation and a drop shadow raise the top app bar when content is present underneath
 
M3: On scroll, a color fill overlay separates the app bar from the content beneath
