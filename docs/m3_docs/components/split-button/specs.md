# Split buttons

> Source: https://m3.material.io/components/split-button/specs

link
 
Copy link Link copied
 
## Variants
 
link
 
Copy link Link copied
 
link
 
Copy link Link copied
 
Variant M3 M3 Expressive Split button -- Available
 
link
 
Copy link Link copied
 
## Configurations
 
link
 
Copy link Link copied
 
Color configurations: Elevated, filled, tonal, outlined
 
Size configurations: XS, S, M, L, XL
 
link
 
Copy link Link copied
 
Category Configuration M3 M3 Expressive Size XS, S, M, L, XL -- Available Color Elevated, filled, tonal, outlined -- Available
 
link
 
Copy link Link copied
 
## Tokens & specs
 
link
 
Copy link Link copied
 
Use the table's menu to select a token set. Split button token sets are organized by size. [Learn about design tokens](/m3/pages/design-tokens/overview/)
 
link
 
Copy link Link copied
 
Split button - Size - Xsmall arrow_drop_down
 
search visibility grid_view
 
Token
 
Value
 
Split button xsmall container height
 
md.comp.split-button.xsmall.container.height content_copy
 
32dp Split button xsmall between space
 
md.comp.split-button.xsmall.between-space content_copy
 
2dp Split button xsmall container shape
 
md.comp.split-button.xsmall.container.shape content_copy Split button xsmall inner corner size
 
md.comp.split-button.xsmall.inner-corner.corner-size content_copy
 
4dp Split button xsmall outer corner size
 
md.comp.split-button.xsmall.outer-corner.corner-size content_copy
 
50% Split button xsmall leading button leading space
 
md.comp.split-button.xsmall.leading-button.leading-space content_copy
 
12dp Split button xsmall leading button trailing space
 
md.comp.split-button.xsmall.leading-button.trailing-space content_copy
 
10dp Split button xsmall trailing button icon size
 
md.comp.split-button.xsmall.trailing-button.icon.size content_copy
 
22dp Split button xsmall trailing button leading space
 
md.comp.split-button.xsmall.trailing-button.leading-space content_copy
 
13dp Split button xsmall trailing button trailing space
 
md.comp.split-button.xsmall.trailing-button.trailing-space content_copy
 
13dp Split button xsmall inner corner hovered size
 
md.comp.split-button.xsmall.inner-corner.hovered.corner-size content_copy
 
8dp Split button xsmall inner corner pressed size
 
md.comp.split-button.xsmall.inner-corner.pressed.corner-size content_copy
 
8dp Split button xsmall trailing button inner corner selected size
 
md.comp.split-button.xsmall.trailing-button.inner-corner.selected.corner-size content_copy
 
50%
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
Leading button
 
Icon
 
Label text
 
Trailing button
 
link
 
Copy link Link copied
 
The leading button in split buttons can have an icon, label text, or both. The trailing button should always have a menu icon.
 
Label + icon
 
Label
 
Icon
 
link
 
Copy link Link copied
 
## Color
 
link
 
Copy link Link copied
 
Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For designers, this means working with color values that correspond with tokens; in implementation, a color value will be a token that references a value.
 
link
 
Copy link Link copied
 
Split buttons use the same color schemes as standard buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) . However, unlike toggle buttons, the split button color doesn’t change when selected—only a state layer is applied.
 
Split buttons use the same colors and state layers as buttons, shown in the following token module. [Go to buttons](/m3/pages/common-buttons/overview) for more details.
 
A: Unselected, B: Selected trailing icon
 
Elevated
 
Filled
 
Tonal
 
Outlined
 
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
 
## States
 
States States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) are visual representations used to communicate the status of a component or an interactive element.
 
Split button states use the same colors and state layers as buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/specs) and icon buttons Icon buttons help people take minor actions with one tap. [More on icon buttons](/m3/pages/icon-buttons/specs) . Go to those specs for details.
 
link
 
Copy link Link copied
 
### Leading button shape
 
The inner corners change shape for hovered, focused, and pressed states.
 
link
 
Copy link Link copied
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed, pressed with focus
 
link
 
Copy link Link copied
 
### Trailing button shape
 
The inner corners change shape for hovered, focused, and pressed states, and the icon becomes centered when selected.
 
link
 
Copy link Link copied
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed, pressed with focus
 
Selected, selected with focus
 
link
 
Copy link Link copied
 
## Measurements
 
link
 
Copy link Link copied
 
Text and icons are optically centered when the buttons are asymmetrical. They’re centered normally when symmetrical.
 
link
 
Copy link Link copied
 
Menu icon offset when unselected:
 
XS: -1dp from center
 
S: -1dp from center
 
M: -2dp from center
 
L: -3dp from center
 
XL: -6dp from center
 
link
 
Copy link Link copied
 
The inner corner radius changes depending on button sizing. The space should always be 2dp.
 
link
 
Copy link Link copied
 
Extra small 4dp
 
Small 4dp
 
Medium 4dp
 
Large 8dp
 
Extra large 12dp
