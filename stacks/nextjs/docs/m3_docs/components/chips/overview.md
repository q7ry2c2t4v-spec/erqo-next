# Chips – Material Design 3

> Source: https://m3.material.io/components/chips/overview

link
 
Copy link Link copied
 
Use chips to show options for a specific context
 
Four variants: assist Assist chips represent smart or automated actions that can span multiple apps, such as opening a calendar event from the home screen. , filter Filter chips use tags or descriptive words to filter content. They can be a good alternative to toggle buttons or checkboxes. , input Input chips represent discrete pieces of information entered by a user, such as Gmail contacts or filter options within a search field. , and suggestion Suggestion chips help narrow a user’s intent by presenting dynamically generated suggestions, such as suggested responses or search filters.
 
Chip elevation Elevation is the distance between two surfaces on the z-axis. [More on elevation](/m3/pages/elevation/overview) defaults to 0 but can be elevated if they need more visual separation
 
link
 
Copy link Link copied
 
Assist chip
 
Filter chip
 
Input chip
 
Suggestion chip
 
link
 
Copy link Link copied
 
## Availability & resources
 
link
 
Copy link Link copied
 
Type Resource Status Design [Design Kit (Figma)](https://www.figma.com/community/file/1035203688168086460) Available Implementation [Flutter](https://api.flutter.dev/flutter/material/ThemeData/useMaterial3.html) Available [android Jetpack Compose](https://developer.android.com/develop/ui/compose/components/chip) Available [android MDC-Android](https://github.com/material-components/material-components-android/blob/master/docs/components/Chip.md) Available [language Web](https://github.com/material-components/material-web/blob/main/docs/components/chip.md) Available
 
link
 
Copy link Link copied
 
## Updates
 
link
 
Copy link Link copied
 
Aug 2024
 
Updated stroke color from outline to outline variant .
 
The stroke color was softened to improve visual hierarchy between chips and buttons
 
link
 
Copy link Link copied
 
## Differences from M2
 
link
 
Copy link Link copied
 
Color: New color mappings and compatibility with dynamic color Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI. [More on dynamic color](/m3/pages/dynamic/choosing-a-source)
 
Shape: Rounded rectangle
 
Variants: Action chips have been separated into assist chips Assist chips represent smart or automated actions that can span multiple apps, such as opening a calendar event from the home screen. and suggestion chips Suggestion chips help narrow a user’s intent by presenting dynamically generated suggestions, such as suggested responses or search filters. . Choice chips are now a subset of filter chips Filter chips use tags or descriptive words to filter content. They can be a good alternative to toggle buttons or checkboxes.
 
link
 
Copy link Link copied
 
M2: Variants of chips are input, choice, filter, and action chips
 
M3: Variants of chips updated to assist, filter, input, and suggestion chips
