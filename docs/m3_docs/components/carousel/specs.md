# Carousel – Material Design 3

> Source: https://m3.material.io/components/carousel/specs

link
 
Copy link Link copied
 
Container
 
Large carousel item
 
Medium carousel item
 
Small carousel item
 
link
 
Copy link Link copied
 
## Tokens & specs
 
link
 
Copy link Link copied
 
Browse the component elements, attributes, tokens, and their values.
 
link
 
Copy link Link copied
 
Carousel item arrow_drop_down
 
search visibility grid_view expand_all
 
Token
 
Default, Light arrow_drop_down
 
folder Enabled
 keyboard_arrow_down folder Hover
 keyboard_arrow_down folder Focus
 keyboard_arrow_down folder Pressed (ripple)
 keyboard_arrow_down folder Disabled
 keyboard_arrow_down
 
link
 
Copy link Link copied
 
## Color
 
Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview/)
 
link
 
Copy link Link copied
 
Carousel color roles used for light and dark schemes:
 
Container
 
Surface
 
link
 
Copy link Link copied
 
## States
 
States States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) are visual representations used to communicate the status of a component or interactive element. [Learn more about interaction states](/m3/pages/interaction-states/overview)
 
link
 
Copy link Link copied
 
Enabled
 
Hovered
 
Focused
 
Pressed
 
Disabled
 
link
 
Copy link Link copied
 
## Carousel item dynamic widths
 
link
 
Copy link Link copied
 
All kinds of carousel items dynamically adapt to the width of the container.
 
Large items have a customizable maximum width that's used to optimally fit carousel items into the available space.
 
Small carousel items have a minimum width of 40dp and a maximum width of 56dp.
 
Items change size as they move through the carousel layout.
 
Small carousel items have a minimum and maximum width
 
link
 
Copy link Link copied
 
## Multi-browse
 
The multi-browse layout The multi-browse carousel layout shows at least one large, medium, and small carousel item at a time. shows at least one large, medium, and small carousel item.
 
link
 
Copy link Link copied
 
Container
 
Large carousel item
 
Medium carousel item
 
Small carousel item
 
link
 
Copy link Link copied
 
### Measurements
 
link
 
Copy link Link copied
 
Multi-browse carousels have padding on both sides of the container
 
link
 
Copy link Link copied
 
Attribute Value Alignment Vertically centered Leading/trailing padding 16dp Top/bottom padding 8dp Padding between elements 8dp Large item width Dynamic, or user-set Medium item width Dynamic Small item width 40–56dp, dynamic Item corner radius 28dp
 
link
 
Copy link Link copied
 
## Uncontained
 
The uncontained The uncontained carousel layout show items that scroll to the edge of the container. layout shows items that scroll to the edge of the container.
 
link
 
Copy link Link copied
 
Container
 
Large carousel item
 
link
 
Copy link Link copied
 
### Measurements
 
link
 
Copy link Link copied
 
Uncontained carousel items bleed over the padding on each side when scrolling
 
link
 
Copy link Link copied
 
Attribute Value Alignment Vertically centered Leading padding 16dp Top/bottom padding 8dp Padding between elements 8dp Item corner radius 28dp
 
link
 
Copy link Link copied
 
## Uncontained mutli-aspect ratio
 
The uncontained multi-aspect ratio layout shows carousel items of various widths.
 
link
 
Copy link Link copied
 
Container
 
Carousel item (16:9)
 
Carousel item (9:16)
 
Carousel item (1:1)
 
Carousel item (3:4)
 
link
 
Copy link Link copied
 
### Measurements
 
link
 
Copy link Link copied
 
Uncontained multi-aspect ratio carousels only have leading padding, with 8dp of padding between items.
 
link
 
Copy link Link copied
 
Attribute Value Alignment Vertically centered Leading padding 16dp Top/bottom padding 8dp Padding between elements 8dp Item corner radius 28dp
 
link
 
Copy link Link copied
 
## Hero
 
The hero layout The hero carousel layout shows at least one large and one small item at a time. shows at least one large item and one small item.
 
link
 
Copy link Link copied
 
Container
 
Large carousel item
 
Small carousel item
 
link
 
Copy link Link copied
 
### Measurements
 
link
 
Copy link Link copied
 
Hero carousels have padding on both sides of the container
 
link
 
Copy link Link copied
 
Attribute Value Alignment Vertically centered Leading/Trailing padding 16dp Top/bottom padding 8dp Padding between elements 8dp Large item width Dynamic Small item width 40-56dp, dynamic Item corner radius 28dp
 
link
 
Copy link Link copied
 
## Center-aligned hero
 
The center-aligned hero layout shows at least one large item and two small items.
 
link
 
Copy link Link copied
 
Container
 
Large carousel item
 
Small carousel item
 
link
 
Copy link Link copied
 
### Measurements
 
link
 
Copy link Link copied
 
Center-aligned hero carousels have padding on both sides of the container
 
link
 
Copy link Link copied
 
Attribute Value Alignment Vertically centered Leading/Trailing padding 16dp Top/bottom padding 8dp Padding between elements 8dp Large item width Dynamic Small item width 40-56dp, dynamic Item corner radius 28dp
 
link
 
Copy link Link copied
 
## Full-screen
 
The full-screen layout The full-screen carousel layout shows one edge-to-edge large item at a time and scrolls vertically. shows one edge-to-edge large item.
 
link
 
Copy link Link copied
 
Container
 
Large carousel item
 
link
 
Copy link Link copied
 
### Measurements
 
link
 
Copy link Link copied
 
Full-screen carousels fill the window edge-to-edge
 
link
 
Copy link Link copied
 
Attribute Value Alignment Centered Leading/Trailing padding 0dp Top/bottom padding 0dp Padding between elements 16dp
