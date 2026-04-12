# Buttons – Material Design 3

> Source: https://m3.material.io/components/buttons/specs

link
 
Copy link Link copied
 
## Variants
 
link
 
Copy link Link copied
 
Default button
 
Toggle button
 
link
 
Copy link Link copied
 
Variants M3 M3 Expressive Default Available Available Toggle (selection) -- Available
 
link
 
Copy link Link copied
 
## Configurations
 
link
 
Copy link Link copied
 
Size
 
Shape
 
Color
 
Small button padding
 
link
 
Copy link Link copied
 
Category Configuration M3 M3 Expressive Size Small (default) Available Available XS, M, L, XL -- Available Shape Round (default) Available Available Square -- Available Color Elevated, filled (default), tonal, outlined, standard Available Available Small button padding 24dp Available Not recommended.
 
Use 16dp 16dp -- Available
 
link
 
Copy link Link copied
 
## Tokens & specs
 
Use the table's menu to select a token set. Button token sets are separated into common tokens, color, and size. [View baseline tokens](/m3/pages/common-buttons/specs#c305d304-a6c0-466a-a48c-8d0718a29ae2)
 
link
 
Copy link Link copied
 
Button - Color - Elevated arrow_drop_down
 
search visibility grid_view expand_all
 
Token
 
Default, Light arrow_drop_down
 
folder Enabled
 keyboard_arrow_down folder Disabled
 keyboard_arrow_down folder Hovered
 keyboard_arrow_down folder Focused
 keyboard_arrow_down folder Pressed
 keyboard_arrow_down
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
Container
 
Label text
 
Icon (optional)
 
link
 
Copy link Link copied
 
## Color
 
link
 
Copy link Link copied
 
Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value.
 
There are five built-in button color styles: elevated, filled, tonal, outlined, and text
 
The default and toggle buttons use different colors
 
Toggle buttons don’t use the text style
 
link
 
Copy link Link copied
 
star
 
Note:
 
These color roles were chosen to create design coherence and familiarity. Other color roles can be used as long as the container and text have a 3:1 contrast ratio. For example, tertiary and on tertiary.
 
link
 
Copy link Link copied
 
A. Elevated, B. Filled, C. Tonal, D. Outlined, E. Text
 
Default
 
Toggle: unselected
 
Toggle: selected
 
link
 
Copy link Link copied
 
1. Default 2. Toggle unselected 3. Toggle selected Elevated container
 
Elevated icon & label Surface container low
 
Primary Surface container low
 
Primary Primary
 
On primary Filled container
 
Filled icon & label Primary
 
On primary Surface container
 
On surface variant Primary
 
On primary Tonal container
 
Tonal icon & label Secondary container
 
On secondary container Secondary container
 
On secondary container Secondary
 
On secondary Outlined container
 
Outlined icon & label Outline variant (outline)
 
On surface variant Outline variant (outline)
 
On surface variant Inverse surface
 
Inverse on surface Text icon & label Primary -- --
 
link
 
Copy link Link copied
 
## States
 
link
 
Copy link Link copied
 
States States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) are visual representations used to communicate the status of a component or interactive element.
 
link
 
Copy link Link copied
 
### Elevated button states
 
The elevated button style has an elevation of 1 by default and has no elevation when disabled.
 
link
 
Copy link Link copied
 
#### Default
 
link
 
Copy link Link copied
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
#### Toggle
 
link
 
Copy link Link copied
 
A. Unselected, B. Selected
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
### Filled button states
 
link
 
Copy link Link copied
 
#### Default
 
link
 
Copy link Link copied
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
#### Toggle
 
link
 
Copy link Link copied
 
A. Unselected, B. Selected
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
### Tonal button states
 
link
 
Copy link Link copied
 
#### Default
 
link
 
Copy link Link copied
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
#### Toggle
 
link
 
Copy link Link copied
 
A. Unselected, B. Selected
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
### Outlined button states
 
link
 
Copy link Link copied
 
The outlined button’s container fill is invisible at rest, but the opacity and state layers behave the same as other button styles when disabled, hovered, focused, or pressed.
 
link
 
Copy link Link copied
 
#### Default
 
link
 
Copy link Link copied
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
#### Toggle
 
link
 
Copy link Link copied
 
A. Unselected, B. Selected
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
### Text button style states
 
link
 
Copy link Link copied
 
The text button’s container is invisible at rest, but the opacity and state layers behave the same as other button styles when disabled, hovered, focused, or pressed. There is no toggle text button.
 
link
 
Copy link Link copied
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
## Shape morph
 
link
 
Copy link Link copied
 
### Pressed state
 
When pressed, buttons can morph to become more square. Both round and square buttons should have the same pressed shape.
 
The corner radius value differs for each button size. [See full button corner measurements](/m3/pages/common-buttons/specs#b1f39738-6f3a-409b-8f08-4cab6d78d756)
 
A. Round button, B. Square button
 
Enabled
 
Hovered
 
Pressed
 
link
 
Copy link Link copied
 
### When selected
 
In addition to changing shape when pressed, toggle buttons also change the resting shape from round (unselected) to square (selected).
 
If the resting unselected shape is square, the selected shape should be round.
 
A. Round button, B. Square button
 
Enabled
 
Hovered
 
Pressed
 
Selected
 
link
 
Copy link Link copied
 
## Measurements
 
link
 
Copy link Link copied
 
Padding and size measurements of each button size
 
Extra small
 
Small
 
Medium
 
Large
 
Extra large
 
link
 
Copy link Link copied
 
### Target areas
 
link
 
Copy link Link copied
 
Extra small and small icon buttons must have a target size of 48x48dp or larger to be accessible.
 
A. Extra small  B. Small
 
Round button
 
Button with icon
 
Square button
 
link
 
Copy link Link copied
 
### Corner sizes
 
link
 
Copy link Link copied
 
link
 
Copy link Link copied
 
XS S M L XL A. Round button Full Full Full Full Full B. Square button 12dp 12dp 16dp 28dp 28dp C. Pressed state 8dp 8dp 12dp 16dp 16dp
 
link
 
Copy link Link copied
 
## Baseline tokens
 
link
 
Copy link Link copied
 
Use the table's menu to switch token sets. The baseline button token sets are deprecated, and organized by color.
 
link
 
Copy link Link copied
 
[Deprecated] Button - Elevated arrow_drop_down
 
search visibility grid_view expand_all
 
Token
 
Default, Light arrow_drop_down
 
folder [Deprecated] Enabled
 keyboard_arrow_down folder [Deprecated] Disabled
 keyboard_arrow_down folder [Deprecated] Hovered
 keyboard_arrow_down folder [Deprecated] Focused
 keyboard_arrow_down folder [Deprecated] Pressed (ripple)
 keyboard_arrow_down
