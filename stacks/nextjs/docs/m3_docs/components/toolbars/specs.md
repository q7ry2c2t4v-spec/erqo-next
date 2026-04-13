# Toolbar

> Source: https://m3.material.io/components/toolbars/specs

link
 
Copy link Link copied
 
## Variants
 
link
 
Copy link Link copied
 
Docked toolbar
 
Floating toolbar
 
link
 
Copy link Link copied
 
### Baseline variant
 
link
 
Copy link Link copied
 
The baseline bottom app bar is no longer recommended. It should be replaced with the docked toolbar, which is very similar and more flexible.
 
link
 
Copy link Link copied
 
Bottom app bar (not recommended)
 
link
 
Copy link Link copied
 
Variant M3 M3 Expressive Docked toolbar -- Available Floating toolbar -- Available Bottom app bar Available Not recommended.
 
Use docked toolbar .
 
link
 
Copy link Link copied
 
star
 
Note:
 
Implementation differs per platform. On Jetpack Compose, the floating toolbar is a separate component from the docked toolbar and bottom app bar.
 
link
 
Copy link Link copied
 
## Configurations
 
link
 
Copy link Link copied
 
Standard and vibrant toolbars
 
Vertical floating toolbar
 
Floating toolbar with FAB
 
link
 
Copy link Link copied
 
Category Configuration M3 M3 Expressive Color Standard (default) Available as bottom app bar Available Vibrant -- Available Floating toolbar layout Horizontal (default) -- Available Vertical -- Available Other elements With FAB Available as bottom app bar Available*
 
link
 
Copy link Link copied
 
star
 
Note:
 
*Implementation differs per platform. On Jetpack Compose, floating toolbar with FAB is [fully supported](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#HorizontalFloatingToolbar(kotlin.Boolean,androidx.compose.ui.Modifier,androidx.compose.material3.FloatingToolbarColors,androidx.compose.foundation.layout.PaddingValues,androidx.compose.material3.FloatingToolbarScrollBehavior,androidx.compose.ui.graphics.Shape,kotlin.Function1,kotlin.Function1,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,kotlin.Function1)) . On other platforms, each component needs to be added separately.
 
link
 
Copy link Link copied
 
## Tokens & specs
 
Browse the component elements, attributes, tokens, and their values. [Jump to baseline bottom app bar specs](/m3/pages/toolbars/specs#ad142675-3e3b-43b8-ba53-12c1f0b7138d)
 
link
 
Copy link Link copied
 
Toolbar - Color - Standard arrow_drop_down
 
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
 
Placed components
 
link
 
Copy link Link copied
 
### Flexibility & slots
 
link
 
Copy link Link copied
 
When configuring a toolbar, think of it as a container with several slots.
 
Each slot can be a different element. The most common elements are icon buttons When configuring a toolbar, think of it as a container with several slots. Each slot can be a different element. The most common elements are icon buttons, buttons, and text fields. [More on icon buttons](/m3/pages/icon-buttons/specs) , buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/specs) , and text fields Text fields let users enter text into a UI. [More on text fields](/m3/pages/text-fields/overview) .
 
A toolbar is essentially a container with configurable slots
 
link
 
Copy link Link copied
 
## Color
 
link
 
Copy link Link copied
 
Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)
 
link
 
Copy link Link copied
 
### Standard
 
link
 
Copy link Link copied
 
Standard color schemes and icon button types:
 
Surface container
 
Filled button (Primary, On primary)
 
Toggle tonal button (Secondary container, On secondary container)
 
Standard button (Primary)
 
link
 
Copy link Link copied
 
### Vibrant
 
link
 
Copy link Link copied
 
Vibrant color scheme and icon button types:
 
Primary container
 
Filled button (Primary, On primary)
 
Toggle tonal button: (Surface container, On surface)
 
Standard button (On primary container)
 
link
 
Copy link Link copied
 
## Measurements
 
link
 
Copy link Link copied
 
By default all toolbars are 64dp high, center-aligned, have equal padding between items, and have a minimum outside padding of 16dp.
 
link
 
Copy link Link copied
 
### Docked toolbar
 
link
 
Copy link Link copied
 
Default margins and padding
 
Margins and padding with leading, middle, and trailing content
 
link
 
Copy link Link copied
 
Alignment and padding can be configured to create unique layouts:
 
Left and right alignment
 
Center-aligned, 8dp padding between items
 
link
 
Copy link Link copied
 
### Floating toolbar
 
link
 
Copy link Link copied
 
Default padding of floating toolbar
 
link
 
Copy link Link copied
 
Floating toolbar size and padding measurements
 
link
 
Copy link Link copied
 
Floating toolbar margins
 
link
 
Copy link Link copied
 
## Bottom app bar (baseline)
 
link
 
Copy link Link copied
 
Container
 
link
 
Copy link Link copied
 
### Tokens & specs
 
link
 
Copy link Link copied
 
Bottom app bar tokens are in one token set.
 
link
 
Copy link Link copied
 
search visibility grid_view
 
Token
 
Default, Standard, Static, Light arrow_drop_down
 
link
 
Copy link Link copied
 
### Color
 
link
 
Copy link Link copied
 
Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)
 
link
 
Copy link Link copied
 
Bottom app bar color role used for light and dark themes:
 
Surface container
 
link
 
Copy link Link copied
 
### Measurements
 
link
 
Copy link Link copied
 
Bottom app bar padding and size measurements
 
link
 
Copy link Link copied
 
### Common layouts
 
link
 
Copy link Link copied
 
Icon buttons and FAB
 
Icon buttons and no FAB
