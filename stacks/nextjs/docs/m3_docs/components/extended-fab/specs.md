# Extended FAB – Material Design 3

> Source: https://m3.material.io/components/extended-fab/specs

link
 
Copy link Link copied
 
## Variants
 
link
 
Copy link Link copied
 
Small extended FAB
 
Medium extended FAB
 
Large extended FAB
 
link
 
Copy link Link copied
 
### Baseline variants
 
link
 
Copy link Link copied
 
The baseline extended FAB is no longer recommended in the M3 expressive update. Use a small extended FAB; the type style was updated from label large to title medium , and the inner padding was reduced. [View baseline extended FAB specs](/m3/pages/extended-fab/specs#01e114e6-8c3d-4d39-9376-65aa5c10e01b)
 
link
 
Copy link Link copied
 
Extended FAB
 
link
 
Copy link Link copied
 
Variant M3 M3 Expressive Small extended FAB -- Available Medium extended FAB -- Available Large extended FAB -- Available Extended FAB (baseline) Available Not recommended. Use small extended FAB.
 
link
 
Copy link Link copied
 
## Tokens & specs
 
link
 
Copy link Link copied
 
Use the table's menu to select a token set. Extended FAB tokens are organized by size and color.
 
link
 
Copy link Link copied
 
Extended FAB - Size - Small arrow_drop_down
 
search visibility grid_view
 
Token
 
Value
 
Extended FAB small container height
 
md.comp.extended-fab.small.container.height content_copy
 
56dp Extended FAB small label text
 
md.comp.extended-fab.small.label-text content_copy
 
Aa Extended FAB small icon size
 
md.comp.extended-fab.small.icon.size content_copy
 
24dp Extended FAB small container shape
 
md.comp.extended-fab.small.container.shape content_copy Extended FAB small leading space
 
md.comp.extended-fab.small.leading-space content_copy
 
16dp Extended FAB small icon label space
 
md.comp.extended-fab.small.icon-label-space content_copy
 
8dp Extended FAB small trailing space
 
md.comp.extended-fab.small.trailing-space content_copy
 
16dp
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
Container
 
Label text
 
Icon
 
link
 
Copy link Link copied
 
## Color
 
link
 
Copy link Link copied
 
Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview/)
 
link
 
Copy link Link copied
 
### Color styles
 
Extended FABs can use several combinations of color and on color styles, such as primary and on primary . The following color mappings provide the same level of contrast and functionality, so choose a color mapping based on visual preference.
 
link
 
Copy link Link copied
 
Extended FAB color roles used for light and dark schemes:
 
Primary container & on primary container (default)
 
Secondary container & on secondary container
 
Tertiary container & on tertiary container
 
Primary & on primary
 
Secondary & on secondary
 
Tertiary & on tertiary
 
link
 
Copy link Link copied
 
### Baseline color styles
 
link
 
Copy link Link copied
 
Extended FABs should no longer use surface color styles. They’re still available, but not recommended.
 
link
 
Copy link Link copied
 
Surface container FAB
 
link
 
Copy link Link copied
 
## States
 
link
 
Copy link Link copied
 
States are visual representations used to communicate the status of a component or interactive element. [Learn more about interaction states](/m3/pages/interaction-states/overview)
 
link
 
Copy link Link copied
 
When using a non-default color mapping for extended FABs, make sure the state layer color is the same as the icon color. For example, the state layer color for primary mapping should be md.sys.color.primary.
 
link
 
Copy link Link copied
 
Enabled
 
Hovered - elevation 4
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
## Measurements
 
link
 
Copy link Link copied
 
Size and padding measurements of the small, medium, and large extended FABs
 
link
 
Copy link Link copied
 
Extended FABs should have margins of 16dp
 
link
 
Copy link Link copied
 
## Baseline extended FAB
 
link
 
Copy link Link copied
 
Container
 
Label text
 
Icon
 
link
 
Copy link Link copied
 
### Baseline configurations
 
link
 
Copy link Link copied
 
With icon
 
Without icon
 
link
 
Copy link Link copied
 
### Baseline tokens
 
link
 
Copy link Link copied
 
Use the table's menu to select a token set. The baseline extended FAB token sets are organized by common tokens, then by surface and branded color styles. Other color styles like primary, secondary, and tertiary are still used by the latest extended FABs.
 
link
 
Copy link Link copied
 
search visibility grid_view
 
Token
 
Default, Standard, Light arrow_drop_down
 
link
 
Copy link Link copied
 
### Baseline colors
 
Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview/)
 
link
 
Copy link Link copied
 
Extended FAB color roles used for light and dark schemes:
 
Primary container + shadow
 
On primary container
 
On primary container
 
link
 
Copy link Link copied
 
#### Additional color mappings
 
Extended FABs can use other combinations of container and icon colors. The color mappings below provide the same legibility and functionality as the default, so the color mapping you use depends on style alone.
 
link
 
Copy link Link copied
 
Extended FABs can use different combinations of container and icon colors
 
link
 
Copy link Link copied
 
### Baseline states
 
States are visual representations used to communicate the status of a component or interactive element. [Learn more about interaction states](/m3/pages/interaction-states)
 
link
 
Copy link Link copied
 
Enabled
 
Hovered
 
Focused
 
Pressed
 
link
 
Copy link Link copied
 
### Baseline measurements
 
link
 
Copy link Link copied
 
Extended FABs have a padding of 16dp
 
Extended FAB height, width, and icon size
 
link
 
Copy link Link copied
 
Attribute Value Container height 56dp Container width Dynamic, 80dp min Container shape 16dp corner radius Icon size 24dp Padding 16dp
