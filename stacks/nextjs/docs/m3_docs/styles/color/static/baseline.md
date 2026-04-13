# Dynamic color - Material Design 3

> Source: https://m3.material.io/styles/color/static/baseline

link
 
Copy link Link copied
 
Baseline is the default static color scheme. It uses accessible color pairings and includes colors for both light and dark themes.
 
With the baseline color scheme, end-users see
 
An accessible UI with static colors
 
link
 
Copy link Link copied
 
Music app with the static baseline color scheme
 
News app with the static baseline color scheme
 
link
 
Copy link Link copied
 
## Baseline colors
 
Get baseline colors in Figma using the Material Theme Builder Material Theme Builder (MTB) is a Figma plugin that allows markers to emulate the color extraction process for dynamic color and create custom tonal schemes. [Get the MTB](https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder) .
 
link
 
Copy link Link copied
 
Baseline scheme colors in light theme
 
link
 
Copy link Link copied
 
Baseline scheme colors in dark theme
 
link
 
Copy link Link copied
 
## Baseline color tokens
 
link
 
Copy link Link copied
 
Color schemes arrow_drop_down
 
search view_list expand_all
 
Default, Light arrow_drop_down
 
folder Primary colors
 keyboard_arrow_down folder Secondary colors
 keyboard_arrow_down folder Tertiary colors
 keyboard_arrow_down folder Error colors
 keyboard_arrow_down folder Surface colors
 keyboard_arrow_down folder Outline colors
 keyboard_arrow_down folder Add-ons
 keyboard_arrow_down
 
link
 
Copy link Link copied
 
## Design with baseline
 
link
 
Copy link Link copied
 
### Use the Design Kit and M3 baseline colors in new design files
 
Create your Figma file. Enable the [M3 Design Kit](https://www.figma.com/community/file/1035203688168086460) in your Assets panel.
 
Compose screens and layouts using Material Components from the design kit
 
Apply M3 baseline color roles to custom components and UI elements by hovering on the element's color property in the Design panel on the right of the screen and selecting the Style icon (four dots). This opens a selection dialog.
 
Search for "M3" to see the baseline color roles
 
Select the baseline color role that most closely matches the use case and intent (see [Color roles](/m3/pages/color-roles) for more information on what color to use where)
 
Repeat until all custom elements are using M3 baseline color roles
 
### Apply baseline colors to an existing file
 
First, get the M3 baseline colors into your file
 
Open your Figma design file. Select the Actions menu (or Ctrl/Command+K).
 
Find the [Material Theme Builder plugin](https://www.figma.com/community/plugin/1034969338659738588/material-theme-builder) and select Run . This will open a plugin dialog showing the default color scheme, including Core colors and Extended colors.
 
Open the plugin's Settings (gear icon at lower right of dialog) and select the checkbox for Generate State Layers . This makes sure there are color for the state layers needed to design interactions. [Learn more about state layers](/m3/pages/interaction-states/state-layers)
 
Navigate out of settings.
 
With the Current Theme dropdown at the top of the dialog, select Baseline.
 
Select the frames or components in your file and then hit Swap in the bottom right of the dialog. This will automatically update the colors for any M3 Design Kit components.
 
Then, update any remaining non-M3 color styles
 
Manually change any hex values or non-M3 color styles by selecting all and looking through the Selection colors in the Design panel on the right of the screen.
 
Any colors that don't start with "M3" need to be replaced with a corresponding baseline color.
 
Hover on a non-M3 color row in the Design panel and select the Style icon (four dots). This opens a selection dialog.
 
Search for "M3" to see the baseline color roles.
 
Select the baseline color role that most closely matches that color's use case (see [Color roles](/m3/pages/color-roles) for more information on what color to use where) and select Use style to apply it to the selected objects.
 
Repeat until all non-M3 colors in the file have been replaced with M3 baseline color roles.
 
Need to make adjustments to the scheme? Check out [Advanced customizations](/m3/pages/advanced/overview)
