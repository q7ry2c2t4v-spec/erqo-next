# Segmented button – Material Design 3

> Source: https://m3.material.io/components/segmented-buttons/specs

link
 
Copy link Link copied
 
star
 
Note:
 
Segmented buttons are no longer recommended in the Material 3 expressive update. For those who have updated, use the [connected button group](/m3/pages/button-groups/overview/) instead, which has mostly the same functionality but with an updated visual design.
 
link
 
Copy link Link copied
 
Container
 
Icon (optional for unselected state)
 
Label text
 
link
 
Copy link Link copied
 
## Tokens and specs
 
link
 
Copy link Link copied
 
Browse the component elements, attributes, tokens, and their values. [Learn more about design tokens](/m3/pages/design-tokens/overview)
 
link
 
Copy link Link copied
 
Segmented button - Outlined arrow_drop_down
 
search visibility grid_view expand_all
 
Token
 
Default, Light arrow_drop_down
 
folder Enabled
 keyboard_arrow_down folder Disabled
 keyboard_arrow_down folder Hovered
 keyboard_arrow_down folder Focused
 keyboard_arrow_down folder Pressed (ripple)
 keyboard_arrow_down
 
link
 
Copy link Link copied
 
## Color
 
Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)
 
link
 
Copy link Link copied
 
Segmented button color roles used for light and dark schemes:
 
On surface
 
Outline
 
Secondary container
 
On secondary container
 
link
 
Copy link Link copied
 
## States
 
States States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) are visual representations used to communicate the status of a component or interactive element. [Learn more about interaction states](/m3/pages/interaction-states/overview)
 
link
 
Copy link Link copied
 
### Unselected
 
link
 
Copy link Link copied
 
Unselected button states:
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
### Selected
 
link
 
Copy link Link copied
 
Selected button states:
 
Selected
 
Hovered on selected
 
Focused on selected
 
Pressed on selected
 
link
 
Copy link Link copied
 
## Measurements
 
link
 
Copy link Link copied
 
Padding and container size
 
Target size
 
link
 
Copy link Link copied
 
Attribute Value Container width Dynamic based on labels Segment width Container width / total segments (Example: 1/3) Height 40dp Outline width 1dp Label alignment Center Left/right padding Min 12dp Padding between elements 8dp Target size 48dp
 
link
 
Copy link Link copied
 
### Density
 
Density can be used in denser UIs where space is limited. Density is only applied to the height.
 
Each step down in density removes 4dp from the height
