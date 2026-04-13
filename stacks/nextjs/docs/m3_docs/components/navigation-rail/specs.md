# Navigation rail – Material Design 3

> Source: https://m3.material.io/components/navigation-rail/specs

link
 
Copy link Link copied
 
## Variants
 
link
 
Copy link Link copied
 
Collapsed navigation rail
 
Expanded navigation rail
 
link
 
Copy link Link copied
 
### Baseline variants
 
link
 
Copy link Link copied
 
The baseline navigation rail is no longer recommended, and should be replaced by the collapsed navigation rail. [View baseline tokens](/m3/pages/navigation-rail/specs#d4d97764-20ec-496f-a6f3-0d423940ec5a)
 
link
 
Copy link Link copied
 
The baseline navigation rail is no longer recommended
 
link
 
Copy link Link copied
 
Variant M3 M3 Expressive Collapsed navigation rail -- Available Expanded navigation rail -- Available Navigation rail (baseline) Available Not recommended.
 
Use collapsed navigation rail .
 
link
 
Copy link Link copied
 
## Configurations
 
link
 
Copy link Link copied
 
Expanded layout: standard
 
Expanded layout: modal
 
link
 
Copy link Link copied
 
Category Configuration M3 M3 Expressive Expanded layout Standard (default) Available as navigation drawer Navigation drawers let people switch between UI views on larger devices. In the expressive update, use an expanded navigation rail. [More on navigation drawers](/m3/pages/navigation-drawer/overview) Available Modal Available as navigation drawer Navigation drawers let people switch between UI views on larger devices. In the expressive update, use an expanded navigation rail. [More on navigation drawers](/m3/pages/navigation-drawer/overview) Available Expanded behavior Hide when collapsed -- Available
 
link
 
Copy link Link copied
 
## Tokens and specs
 
link
 
Copy link Link copied
 
Browse the component elements, attributes, tokens, and their values. [Learn about design tokens](/m3/pages/design-tokens/overview/)
 
link
 
Copy link Link copied
 
Nav rail item - Common arrow_drop_down
 
search visibility grid_view
 
Token
 
Value
 
Nav rail item icon size
 
md.comp.nav-rail.item.icon.size content_copy
 
24dp Nav rail item active indicator shape
 
md.comp.nav-rail.item.active-indicator.shape content_copy Nav rail item active indicator leading space
 
md.comp.nav-rail.item.active-indicator.leading-space content_copy
 
16dp Nav rail item active indicator icon label space
 
md.comp.nav-rail.item.active-indicator.icon-label-space content_copy
 
8dp Nav rail item active indicator trailing space
 
md.comp.nav-rail.item.active-indicator.trailing-space content_copy
 
16dp Nav rail item container height
 
md.comp.nav-rail.item.container.height content_copy
 
64dp Nav rail item short container height
 
md.comp.nav-rail.item.short.container.height content_copy
 
56dp Nav rail item container shape
 
md.comp.nav-rail.item.container.shape content_copy Nav rail item container vertical space
 
md.comp.nav-rail.item.container.vertical-space content_copy
 
6dp Nav rail item header space minimum
 
md.comp.nav-rail.item.header-space-minimum content_copy
 
40dp
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
Collapsed and expanded navigation rail elements:
 
Container
 
Menu (optional)
 
FAB or Extended FAB (optional)
 
Icon
 
Active indicator
 
Label text
 
Large badge (optional)
 
Large badge label (optional)
 
Small badge (optional)
 
link
 
Copy link Link copied
 
## Color
 
Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens; in implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)
 
link
 
Copy link Link copied
 
Navigation rail color roles used for light and dark schemes:
 
Surface container (optional)
 
On secondary container
 
Secondary container
 
Secondary
 
On surface variant
 
On surface variant
 
Error
 
On error
 
Error
 
link
 
Copy link Link copied
 
## States
 
States States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) are visual representations used to communicate the status of a component or an interactive element. The navigation item’s target area always spans the full width of the nav rail, even if the item container hugs its contents.
 
link
 
Copy link Link copied
 
link
 
Copy link Link copied
 
Enabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
## Measurements
 
link
 
Copy link Link copied
 
Navigation rail padding and size measurements
 
link
 
Copy link Link copied
 
## Common layouts
 
link
 
Copy link Link copied
 
link
 
Copy link Link copied
 
Three navigation items
 
Three navigation items with a menu
 
Three navigation items with a FAB
 
Three navigation items with a menu and FAB
 
link
 
Copy link Link copied
 
link
 
Copy link Link copied
 
## Baseline navigation rail
 
link
 
Copy link Link copied
 
Container
 
Menu icon (optional)
 
Icon
 
Active indicator
 
Label text
 
Large badge label (optional)
 
Large badge (optional)
 
Badge (optional)
 
link
 
Copy link Link copied
 
### Tokens & specs
 
link
 
Copy link Link copied
 
search visibility grid_view
 
Token
 
Default, Standard, Light arrow_drop_down
 
link
 
Copy link Link copied
 
### Color
 
link
 
Copy link Link copied
 
Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)
 
link
 
Copy link Link copied
 
Navigation rail color roles used for light and dark themes:
 
On secondary container
 
Secondary container
 
On surface
 
On surface variant
 
On surface variant
 
Error
 
On error
 
Error
 
link
 
Copy link Link copied
 
### States
 
link
 
Copy link Link copied
 
States are visual representations used to communicate the status of a component or interactive element.
 
link
 
Copy link Link copied
 
Navigation rail states:
 
Enabled (on active destination)
 
Hovered (on active destination)
 
Focused (on active destination)
 
Pressed (on active destination)
 
Enabled (on inactive destination)
 
Hovered (on inactive destination)
 
Focused (on inactive destination)
 
Pressed (on inactive destination)
 
link
 
Copy link Link copied
 
### Measurements
 
link
 
Copy link Link copied
 
Navigation rail size measurements
 
Navigation rail padding and margin measurements
 
link
 
Copy link Link copied
 
### Configurations
 
Common arrangements of elements within a navigation rail.
 
link
 
Copy link Link copied
 
With a menu
 
With a FAB
 
With menu and FAB, without labels
 
All destinations with text labels
 
With menu, FAB, and label text for all destinations
