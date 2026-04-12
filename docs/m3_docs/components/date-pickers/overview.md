# Date pickers – Material Design 3

> Source: https://m3.material.io/components/date-pickers/overview

link
 
Copy link Link copied
 
Date pickers can display past, present, or future dates
 
Three variants: docked Docked date pickers open from an onscreen input similar to a text field. They're often used within forms. [More on docked date pickers](/m3/pages/date-pickers/guidelines#8d78696c-a756-4a4d-b7dd-846d866ba985) , modal Modal date pickers extend full-screen. They're often used for selecting a date range. [More on modal date pickers](/m3/pages/date-pickers/guidelines#ced55f72-28b5-4f5d-a347-fa38214ef2d4) , modal input Modal date inputs allow the manual entry of dates using the numbers on a keyboard. They're often used in compact layouts. [More on modal date inputs](/m3/pages/date-pickers/guidelines#d91ce7bc-dbc7-43e3-a802-152f2f9c892a)
 
Clearly indicate important dates, such as current and selected days
 
Follow common patterns, like a calendar view
 
link
 
Copy link Link copied
 
Docked date picker
 
Modal date picker
 
Modal date input
 
link
 
Copy link Link copied
 
## Availability & resources
 
link
 
Copy link Link copied
 
Type Resource Status Design [Design Kit (Figma)](https://www.figma.com/community/file/1035203688168086460) Available Implementation [Flutter](https://api.flutter.dev/flutter/material/DatePickerDialog-class.html) Available [android Jetpack Compose](https://developer.android.com/develop/ui/compose/components/datepickers) Available [android MDC-Android](https://github.com/material-components/material-components-android/blob/master/docs/components/DatePicker.md) Available language Web Unavailable
 
link
 
Copy link Link copied
 
## Differences from M2
 
link
 
Copy link Link copied
 
Typography and spacing: Titles and labels are larger and have increased spacing to accommodate 48dp target size
 
Color: New color mappings and compatibility with dynamic color Dynamic color takes a single color from a user's wallpaper or in-app content and creates an accessible color scheme assigned to elements in the UI. [More on dynamic color](/m3/pages/dynamic/choosing-a-source)
 
Variants: The three variants of date pickers have been renamed to not be device-dependent. The former desktop date picker is now known as the docked date picker Docked date pickers open from an onscreen input similar to a text field. They're often used within forms. [More on docked date picker](https://m3.material.io/m3/pages/date-pickers/guidelines#8d78696c-a756-4a4d-b7dd-846d866ba985) . The former mobile date picker and date input are now known as modal date picker Modal date pickers extend full-screen. They're often used for selecting a date range. [More on modal date picker](https://m3.material.io/m3/pages/date-pickers/guidelines#ced55f72-28b5-4f5d-a347-fa38214ef2d4) and modal date input Modal date inputs allow the manual entry of dates using the numbers on a keyboard. They're often used in compact layouts. [More on modal date input](https://m3.material.io/m3/pages/date-pickers/guidelines#d91ce7bc-dbc7-43e3-a802-152f2f9c892a) to reinforce that the user must take an action.
 
link
 
Copy link Link copied
 
M2: Date pickers had a drop shadow and different color mappings
 
M3: Date pickers have larger typography, no shadow, and new color mappings compatible with dynamic color
