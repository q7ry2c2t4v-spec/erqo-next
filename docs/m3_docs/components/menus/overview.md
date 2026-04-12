# Menus – Material Design 3

> Source: https://m3.material.io/components/menus/overview

link
 
Copy link Link copied
 
Use a menu to show a temporary set of actions. To show actions on screen at all times, use a toolbar Toolbars display frequently used actions relevant to the current page. [More on toolbars](/m3/pages/toolbars/overview) instead
 
Menus can open from many components, including icon buttons Icon buttons help people take minor actions with one tap. [More on icon buttons](/m3/pages/icon-buttons/overview) , split buttons The split button opens a menu to give people more options related to an action. [More on split buttons](/m3/pages/split-buttons/overview) , and text fields Text fields let users enter text into a UI. [More on text fields](/m3/pages/text-fields/overview)
 
Context menus provide actions for a specific element, like an image or highlighted text, and usually open with a secondary click
 
link
 
Copy link Link copied
 
Vertical menus can include vibrant colors, gaps, dividers, and submenus to organize a list of choices
 
link
 
Copy link Link copied
 
## Availability & resources
 
link
 
Copy link Link copied
 
Type Resource Status Design [Design Kit (Figma)](https://www.figma.com/community/file/1035203688168086460) Available Implementation [Flutter](https://api.flutter.dev/flutter/material/ThemeData/useMaterial3.html) Available [android Jetpack Compose](https://developer.android.com/develop/ui/compose/components/menu) Available [android Jetpack Compose: Expressive](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DropdownMenuGroup%28androidx.compose.material3.MenuGroupShapes,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1%29) Available [android MDC-Android](https://github.com/material-components/material-components-android/blob/master/docs/components/Menu.md) Available android MDC-Android: Expressive Unavailable [language Web](https://github.com/material-components/material-web/blob/main/docs/components/menu.md) Available language Web: Expressive Unavailable
 
link
 
Copy link Link copied
 
## M3 Expressive update
 
link
 
Copy link Link copied
 
November 2025
 
Vertical menus were introduced with new shapes, color styles, selection states, and refined submenu motion. Gaps can be used for a more flexible layout on Android. [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive)
 
link
 
Copy link Link copied
 
Variants:
 
Added vertical menus , recommended for new designs
 
Baseline Baseline variants are the M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles. [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive) menu is still available
 
Color styles:
 
Standard
 
Vibrant
 
Vibrant colors help selected menu items stand out
 
link
 
Copy link Link copied
 
## Differences from M2
 
link
 
Copy link Link copied
 
Color : New color mappings and compatibility with dynamic color Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI. [More on dynamic color](/m3/pages/dynamic/choosing-a-source)
 
Variants : Dropdown menu and exposed dropdown menu are now both referred to as menu, since they differ only in the element which opens the menu surface
 
M2: Former menu colors don’t contrast with the background
 
M3: Menus feature new color mappings and dynamic color
