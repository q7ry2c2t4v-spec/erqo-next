# FAB – Material Design 3

> Source: https://m3.material.io/components/floating-action-button/specs

link
 
Copy link Link copied
 
## Variants
 
link
 
Copy link Link copied
 
FAB
 
Medium FAB
 
Large FAB
 
link
 
Copy link Link copied
 
### Baseline variants
 
The small FAB is still available, but no longer recommended. [Jump to baseline specs](/m3/pages/fab/specs#cd336045-e97d-4a6d-ac23-f778fa695e3c)
 
link
 
Copy link Link copied
 
1. Small FAB
 
link
 
Copy link Link copied
 
Variant M3 M3 Expressive FAB Available Available Medium FAB -- Available Large FAB Available Available Small FAB Available Not recommended.
 
Use a larger size.
 
link
 
Copy link Link copied
 
## Configurations
 
link
 
Copy link Link copied
 
In the expressive update, the primary , secondary , and tertiary set colors were renamed to primary container , secondary container , and tertiary container to match the actual color roles used. New primary, secondary, and tertiary color styles were created to match the corresponding color roles. [View details in the color styles section](/m3/pages/fab/specs#67e71ec7-b520-405a-aa06-2decfa0b92a3)
 
link
 
Copy link Link copied
 
Category Configuration M3 M3 Expressive Color Primary container, secondary container, tertiary container Available as primary, secondary, tertiary Available Primary. secondary, tertiary -- Available
 
link
 
Copy link Link copied
 
## Tokens & specs
 
Use the table's menu to select a token set. FAB tokens are organized by size and color. [Learn more about design tokens](/m3/pages/design-tokens/overview/)
 
link
 
Copy link Link copied
 
FAB - Size - Medium arrow_drop_down
 
search visibility grid_view
 
Token
 
Value
 
FAB medium container height
 
md.comp.fab.medium.container.height content_copy
 
80dp FAB medium container width
 
md.comp.fab.medium.container.width content_copy
 
80dp FAB medium icon size
 
md.comp.fab.medium.icon.size content_copy
 
28dp FAB medium container shape
 
md.comp.fab.medium.container.shape content_copy
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
1. Container
 
2. Icon
 
link
 
Copy link Link copied
 
## Color
 
Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens)
 
link
 
Copy link Link copied
 
### Color styles
 
FABs can use several combinations of color and on-color styles, such as primary and on-primary . The following color mappings provide the same legibility and functionality, so the color mapping you use depends on style alone.
 
link
 
Copy link Link copied
 
Primary container & On primary container (default)
 
Secondary container & On secondary container
 
Tertiary container & On tertiary container
 
Primary & On primary
 
Secondary & On secondary
 
Tertiary & On tertiary
 
link
 
Copy link Link copied
 
### Baseline color styles
 
link
 
Copy link Link copied
 
Surface FAB color styles are still available, but no longer recommended.
 
link
 
Copy link Link copied
 
Surface FABs
 
link
 
Copy link Link copied
 
## States
 
States are visual representations used to communicate the status of a component or interactive element. When using a non-default color mapping for FABs, make sure the state layer color is the same as the icon color. For example, the state layer color for the primary color style should be md.sys.color.primary .
 
link
 
Copy link Link copied
 
Enabled
 
Hovered (8% state layer) - elevation 4
 
Focused (10% state layer)
 
Pressed (10% state layer)
 
link
 
Copy link Link copied
 
## Measurements
 
link
 
Copy link Link copied
 
### FAB
 
link
 
Copy link Link copied
 
FAB size measurements
 
FAB padding measurements
 
link
 
Copy link Link copied
 
### Medium FAB
 
link
 
Copy link Link copied
 
Medium FAB size measurements
 
Medium FAB padding measurements
 
link
 
Copy link Link copied
 
### Large FAB
 
link
 
Copy link Link copied
 
Large FAB size measurements
 
Large FAB padding measurements
 
link
 
Copy link Link copied
 
## Baseline tokens & specs
 
link
 
Copy link Link copied
 
Use the table's menu to select a token set. This only includes baseline tokens, including small and surface FABs. It doesn't include large or regular FABs, since those are still currently used.
 
link
 
Copy link Link copied
 
[Deprecated] FAB - Primary, small arrow_drop_down
 
search visibility grid_view expand_all
 
Token
 
Default, Light arrow_drop_down
 
folder [Deprecated] Enabled
 keyboard_arrow_down folder [Deprecated] Hovered
 keyboard_arrow_down folder [Deprecated] Focused
 keyboard_arrow_down folder [Deprecated] Pressed (ripple)
 keyboard_arrow_down
