# Lists – Material Design 3

> Source: https://m3.material.io/components/lists/specs

link
 
Copy link Link copied
 
## Variants
 
link
 
Copy link Link copied
 
### Expressive lists
 
Use the expressive list variant for more flexible styling, highlighted selection states, and customizable slots.
 
link
 
Copy link Link copied
 
An expressive list has a segmented style and round corners
 
link
 
Copy link Link copied
 
### Baseline lists
 
In M3 Expressive, baseline Baseline variants are the original M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles. [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive ) lists are still available to use, but don’t have the latest visual style, selection treatment, and slot functionality.
 
[See baseline list specs](/m3/pages/lists/specs#94cf7f4d-fe29-4fab-9aae-a99e9b754329)
 
link
 
Copy link Link copied
 
Baseline list items have square corners and standard colors
 
link
 
Copy link Link copied
 
Variants M3 M3 Expressive List (expressive) -- Available List (baseline) Available Available
 
link
 
Copy link Link copied
 
## Configurations
 
link
 
Copy link Link copied
 
### Styles
 
The standard and segmented styles are a visual choice, and don’t affect a list’s behavior.
 
link
 
Copy link Link copied
 
Standard
 
Segmented
 
link
 
Copy link Link copied
 
### List selection modes
 
A list can have only one selection mode at a time. For example, a single-action list can change to a multi-select list, but can’t be both at once.
 
link
 
Copy link Link copied
 
In a single-action list , each item is a single tappable area
 
Multi-action list items include a primary action and one or more secondary actions
 
link
 
Copy link Link copied
 
A single-select list
 
A multi-select list
 
link
 
Copy link Link copied
 
### List interactions
 
link
 
Copy link Link copied
 
#### Expand
 
On Android, lists can [expand and collapse](/m3/pages/lists/guidelines#90a236ee-b587-4361-8911-34006f25a6f1) .
 
pause
 A list can expand to include multiple items
 
link
 
Copy link Link copied
 
Category Configuration M3 M3 Expressive Styles Standard Available Available Segmented -- Available Selection modes Single-action, multi-action,
 
single-select, multi-select Available Available Interactions Expand Available Available
 
link
 
Copy link Link copied
 
## Tokens & specs
 
Use the table's menu to select a token set. The common set combines baseline tokens with new expressive shapes and sizes. The expand set has tokens for the expand interaction. [Learn about design tokens](/m3/pages/design-tokens/overview)
 
link
 
Copy link Link copied
 
List - Common arrow_drop_down
 
search visibility grid_view expand_all
 
Token
 
Default, Android, Light arrow_drop_down
 
folder Color
 keyboard_arrow_down folder Spacing
 keyboard_arrow_down folder Shape
 keyboard_arrow_down folder Size and typography
 keyboard_arrow_down
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
Container and label text are required. All other elements are optional:
 
Container
 
Overline
 
Label text
 
Trailing text
 
Supporting text
 
Trailing icon
 
Divider
 
Leading avatar
 
Leading icon
 
Leading media - image or video
 
link
 
Copy link Link copied
 
### Flexibility & slots
 
The [M3 Design Kit](https://www.figma.com/community/file/1035203688168086460) includes lists with custom slots for designing flexible item layouts. Think of a custom list as a container with three different slots: leading, content, and trailing. Each slot can hold a different element.
 
#### Slot accessibility
 
Slots are not accessible by default. Consider the following:
 
Elements must follow the rules, structure, and interaction patterns for lists
 
Use standard list item padding
 
Target size must be at least 48x48dp
 
Don't add interactive elements that make the list item difficult to navigate, especially for people using screen readers
 
[More on required accessibility guidelines](/m3/pages/lists/accessibility#538f23f7-689c-4516-bfc8-5f6933a43f5e)
 
exclamation Caution Reserve the use of slots for use cases that maintain the list’s accessibility and functionality
 
Leading slot
 
Content slot
 
Trailing slot
 
link
 
Copy link Link copied
 
warning
 
Caution:
 
Slots require custom code implementation that you must create and maintain
 
link
 
Copy link Link copied
 
The leading and trailing slot positions must be a smaller width than the content section.
 
1. Leading slots can contain:
 
Visual elements: Avatar, icon, image, or video thumbnail
 
Selection Selection lets users choose specific items to act on. [More on selection](/m3/pages/selection) controls: Checkbox, radio button, or switch
 
Customizations: Badge or larger image
 
2. Content slots must be the largest-width slot and can contain:
 
Default content: Label text, supporting text
 
Optional add-ons: Badge, icon, in-line label, or more text elements
 
Avoid long lines of text to preserve readability
 
3. Trailing slots can contain:
 
Action elements or text: Icon, icon button, or trailing text
 
Selection controls: Checkbox, radio button, or switch
 
The content slot must be the largest section, placed in the middle of the list item
 
link
 
Copy link Link copied
 
#### Selection lists
 
For selection lists, use only one selection interaction per list item.
 
check Do Use only one selection interaction per list item
 
close Don’t Don't use multiple selection interactions in one item
 
link
 
Copy link Link copied
 
## Color
 
link
 
Copy link Link copied
 
Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)
 
link
 
Copy link Link copied
 
List color roles used for light and dark themes:
 
Surface
 
On surface variant
 
On surface
 
On surface variant
 
On surface variant
 
On surface variant
 
Outline variant
 
Primary container
 
On primary container
 
On surface variant
 
link
 
Copy link Link copied
 
## States
 
link
 
Copy link Link copied
 
States are visual representations used to communicate the status of a component or an interactive element. [Learn more about interaction states](/m3/pages/interaction-states/overview)
 
link
 
Copy link Link copied
 
### Default list items
 
link
 
Copy link Link copied
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
Dragged
 
link
 
Copy link Link copied
 
### Selected list items
 
link
 
Copy link Link copied
 
Enabled
 
Disabled
 
Hovered
 
Focused
 
Pressed
 
Dragged
 
link
 
Copy link Link copied
 
## Measurements
 
link
 
Copy link Link copied
 
List item alignment, padding, and size measurements. The icon button height is dynamic, and automatically adjusts to fill the list item height.
 
link
 
Copy link Link copied
 
## List (baseline)
 
link
 
Copy link Link copied
 
The baseline Baseline variants are the original M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles. [More on M3 Expressive](https://m3.material.io/blog/building-with-m3-expressive) list variant is available and continues to work in existing products. However, the [expressive list](/m3/pages/lists/specs#ebf87f58-d5bf-4cb5-a856-d2bb104eec4d) variant is recommended for new designs.
 
link
 
Copy link Link copied
 
### Tokens & specs
 
Baseline list tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) are in the common token set. Note: This set also includes several expressive tokens.
 
link
 
Copy link Link copied
 
List - Common arrow_drop_down
 
search visibility grid_view expand_all
 
Token
 
Default, Light arrow_drop_down
 
folder Color
 keyboard_arrow_down folder Spacing
 keyboard_arrow_down folder Shape
 keyboard_arrow_down folder Size and typography
 keyboard_arrow_down
 
link
 
Copy link Link copied
 
### Color
 
Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)
 
link
 
Copy link Link copied
 
List color roles used for light and dark themes:
 
Surface
 
On surface
 
On surface variant
 
On surface variant
 
On surface variant
 
Outline variant
 
Primary container
 
On primary container
 
On surface variant
 
link
 
Copy link Link copied
 
### States
 
States are visual representations used to communicate the status of a component or interactive element.
 
link
 
Copy link Link copied
 
1. Enabled
 
2. Disabled
 
3. Hovered
 
4. Focused
 
5. Pressed
 
6. Dragged
 
link
 
Copy link Link copied
 
### Layout
 
#### One-line lists
 
link
 
Copy link Link copied
 
Baseline one-line list alignment, padding, and size measurements
 
link
 
Copy link Link copied
 
Baseline list item measurements and padding
 
link
 
Copy link Link copied
 
#### Two-line lists
 
link
 
Copy link Link copied
 
Baseline two-line list alignment, padding, and size measurements
 
link
 
Copy link Link copied
 
Baseline list item measurements and padding
 
link
 
Copy link Link copied
 
#### Three-line lists
 
link
 
Copy link Link copied
 
Baseline three-line list alignment, padding, and size measurements
 
link
 
Copy link Link copied
 
Baseline list item measurements and padding
 
link
 
Copy link Link copied
 
Attribute Value Label alignment Center Label alignment when height is 88dp or taller Top Label left padding 16dp Leading element alignment (vertical) Center Leading element alignment (vertical) when height is 88dp or taller Top Leading element left padding 16dp Leading icon alignment (vertical) Top Leading icon top padding 8dp Leading icon top padding when height is 88dp or taller 12dp Trailing element alignment (vertical) Center Trailing element alignment (vertical) when height is 88dp or taller Top Trailing element left padding 16dp Trailing element right padding 24dp Padding above/below divider 0dp Targets 48dp Divider full-width 100% Divider inset left padding 16dp Divider inset right padding 24dp
 
link
 
Copy link Link copied
 
### Configurations
 
link
 
Copy link Link copied
 
#### Leading avatar
 
link
 
Copy link Link copied
 
With leading avatar
 
With leading avatar and trailing checkbox
 
link
 
Copy link Link copied
 
#### Leading image or thumbnail
 
link
 
Copy link Link copied
 
With leading image
 
With leading image and trailing checkbox
 
link
 
Copy link Link copied
 
#### Leading video
 
link
 
Copy link Link copied
 
With leading video
 
With leading video and trailing checkbox
 
link
 
Copy link Link copied
 
#### Leading icon
 
link
 
Copy link Link copied
 
With leading icon
 
With leading icon and trailing checkbox
 
link
 
Copy link Link copied
 
#### Text-only
 
link
 
Copy link Link copied
 
With text only
 
With text and trailing checkbox
 
link
 
Copy link Link copied
 
#### Leading checkbox
 
link
 
Copy link Link copied
 
With leading checkbox
 
With leading checkbox and trailing text
 
link
 
Copy link Link copied
 
#### Leading radio button
 
link
 
Copy link Link copied
 
With leading radio button
 
With leading radio button and trailing text
 
link
 
Copy link Link copied
 
#### Trailing switch
 
link
 
Copy link Link copied
 
With trailing switch
 
With leading icon and trailing switch
