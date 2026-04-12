# Button groups

> Source: https://m3.material.io/components/button-groups/specs

link
 
Copy link Link copied
 
## Variants
 
link
 
Copy link Link copied
 
Standard button group
 
Connected button group
 
link
 
Copy link Link copied
 
Variant M3 M3 Expressive Standard button group -- Available Connected button group Available as segmented button Segmented buttons help people select options, switch views, or sort elements. Note: They're deprecated in the expressive update. Use a nav rail instead. [More on segmented buttons](/m3/pages/segmented-buttons/overview) Available
 
link
 
Copy link Link copied
 
## Configurations
 
link
 
Copy link Link copied
 
Configurations for both variants of button groups:
 
Extra small
 
Small
 
Medium
 
Large
 
Extra large
 
Single-select and multi-select
 
Round and square
 
link
 
Copy link Link copied
 
Category Configuration M3 M3 Expressive Size XS, S, M, L, XL -- Available Default shape Round, square -- Available Selection Single-select, multi-select, selection-required Available as segmented button Segmented buttons help people select options, switch views, or sort elements. Note: They're deprecated in the expressive update. Use a nav rail instead. [More on segmented buttons](/m3/pages/segmented-buttons/overview) Available
 
link
 
Copy link Link copied
 
## Tokens & specs
 
link
 
Copy link Link copied
 
Standard and connected button group tokens are organized by size. Select the variant and size from the token set menu. Go to the [button](/m3/pages/common-buttons/specs/) and [icon button](/m3/pages/icon-buttons/specs/) pages to view their tokens. [Learn about design tokens](/m3/pages/design-tokens/overview/)
 
link
 
Copy link Link copied
 
Button group standard - Size - Xsmall arrow_drop_down
 
search visibility grid_view expand_all
 
Token
 
Value
 
Button group xsmall container height
 
md.comp.button-group.standard.xsmall.container.height content_copy
 
32dp Button group xsmall between space
 
md.comp.button-group.standard.xsmall.between-space content_copy
 
18dp folder Pressed
 keyboard_arrow_down
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
Button groups are invisible containers that add padding between buttons and modify button shape. They don’t contain any buttons by default.
 
link
 
Copy link Link copied
 
Container
 
link
 
Copy link Link copied
 
### Common layouts
 
Mix and match buttons and icon buttons for different scenarios.
 
link
 
Copy link Link copied
 
Label buttons
 
Label buttons and icon buttons
 
Extra small icon buttons
 
Large icon buttons
 
link
 
Copy link Link copied
 
### Color
 
Button groups have no color properties. They can use the default button or toggle button color styles, like filled, tonal, and outlined. Avoid using standard icon buttons or text buttons, as they have no container treatment.
 
link
 
Copy link Link copied
 
Filled
 
Tonal
 
Outlined
 
Elevated
 
link
 
Copy link Link copied
 
## Selection & activation
 
link
 
Copy link Link copied
 
Standard button groups add interaction between adjacent buttons when a button is selected or activated. This interaction changes the width, shape, and padding of the selected or activated button, which adjusts the width of buttons directly next to it.
 
pause
 A selected button changes shape, and briefly changes the width of itself and adjacent buttons
 
link
 
Copy link Link copied
 
Connected button groups don’t add any interaction between buttons when selected or activated.
 
They only affect the shape of the button being selected or activated.
 
pause
 A selected button changes shape without affecting adjacent buttons
 
link
 
Copy link Link copied
 
## States
 
link
 
Copy link Link copied
 
### Standard button group
 
link
 
Copy link Link copied
 
When a button is pressed, standard button groups modify the width and shape of that button and adjacent buttons.
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
When a toggle button is selected in a standard button group , its shape should change between square and round. The color should change according to the [button specs](/m3/pages/common-buttons/specs) .
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
### Connected button group
 
link
 
Copy link Link copied
 
Connected button groups have different shape changes than standard button groups. Selecting a button does not affect adjacent buttons.
 
link
 
Copy link Link copied
 
Connected button group unselected states:
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
Connected button group selected states:
 
Enabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
## Measurements
 
link
 
Copy link Link copied
 
### Standard button group
 
link
 
Copy link Link copied
 
Standard groups apply padding between all buttons. The amount of padding changes based on button size to ensure a minimum accessible target size of 48dp. More details on padding: [Button specs](/m3/pages/common-buttons/specs) , [icon button specs](/m3/pages/icon-buttons/specs)
 
link
 
Copy link Link copied
 
Standard button group inner padding:
 
XS: 18dp
 
S: 12dp
 
M: 8dp
 
L: 8dp
 
XL: 8dp
 
link
 
Copy link Link copied
 
### Connected button group
 
link
 
Copy link Link copied
 
For all connected button groups, use 2dp padding. This provides visual consistency at scale.
 
link
 
Copy link Link copied
 
Round connected button group inner padding is 2dp at every size. The outer shape is fully round, and the inner shape remains square with the following corner sizes:
 
XS: 4dp
 
S: 8dp
 
M: 8dp
 
L: 16dp
 
XL: 20dp
 
link
 
Copy link Link copied
 
Square connected button group inner padding is 2dp at every size. The outer shape has the following corner sizes:
 
XS: 4dp
 
S: 8dp
 
M: 8dp
 
L: 16dp
 
XL: 20dp
 
link
 
Copy link Link copied
 
### Minimum widths
 
link
 
Copy link Link copied
 
Extra small and small connected button groups have 48dp target areas and a minimum width of 48dp.
 
link
 
Copy link Link copied
 
Extra small
 
Small
 
link
 
Copy link Link copied
 
## Density
 
Button groups adapt to density of the buttons inside. [More on density](/m3/pages/understanding-layout/density/)
 
Button groups adapt to the height of the buttons inside, including when density is applied
