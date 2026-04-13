# Top app bar – Material Design 3

> Source: https://m3.material.io/components/app-bars/specs

link
 
Copy link Link copied
 
## Variants
 
link
 
Copy link Link copied
 
Search app bar
 
Small
 
Medium flexible
 
Large flexible
 
link
 
Copy link Link copied
 
### Baseline variants
 
The baseline M3 medium and large app bars are no longer recommended in M3 Expressive, and should be replaced with medium flexible and large flexible app bars, which are similar visually, but have multi-line support, a shorter height, and can contain a wide variety of elements, like images. [Jump to baseline app bar specs](/m3/pages/app-bars/specs#faec9baf-140f-41dc-8b88-2792e90d9d5d)
 
link
 
Copy link Link copied
 
Baseline variants
 
Medium
 
Large
 
link
 
Copy link Link copied
 
Variant M3 M3 Expressive Search app bar -- Available Small Available Available Center-aligned Available Merged into small . Use centered-text configuration. Medium (baseline) Available Not recommended.
 
Use medium flexible Medium flexible -- Available Large (baseline) Available Not recommended.
 
Use large flexible Large flexible -- Available
 
link
 
Copy link Link copied
 
## Configurations
 
link
 
Copy link Link copied
 
### Text alignment
 
link
 
Copy link Link copied
 
Text labels, including supporting text, can be aligned to the leading edge or centered
 
link
 
Copy link Link copied
 
Category Configuration M3 M3 Expressive Text alignment Leading edge (default) Available Available Centered -- Available
 
link
 
Copy link Link copied
 
## Tokens & specs
 
Select a token set to view in the table's menu. App bar token sets are organized into a common token set, and size-specific tokens. [Learn about design tokens](/m3/pages/design-tokens/overview)
 
link
 
Copy link Link copied
 
App bar - Common arrow_drop_down
 
search visibility grid_view expand_all
 
Token
 
Value
 
folder Color
 keyboard_arrow_down folder Spacing
 keyboard_arrow_down folder Shape
 keyboard_arrow_down folder Size
 keyboard_arrow_down
 
link
 
Copy link Link copied
 
### Search component tokens & specs
 
The default search Search lets people enter a keyword or phrase to get relevant information. [More on search](/m3/pages/search/overview) component tokens are used in the search app bar.
 
link
 
Copy link Link copied
 
Search - View arrow_drop_down
 
search visibility grid_view expand_all
 
Token
 
Default, Light arrow_drop_down
 
Search view container surface tint layer color 
warning
 
md.comp.search-view.container.surface-tint-layer.color content_copy
 
#6750A4 folder Color
 keyboard_arrow_down folder Layout and Text
 keyboard_arrow_down
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
Container
 
Leading button
 
Trailing elements
 
Headline
 
Subtitle
 
link
 
Copy link Link copied
 
App bars can be customized to include:
 
An image or logo
 
A subtitle
 
A filled icon button
 
Avoid customizing the size of the heading and subtitle, or adding too many actions.
 
The app bar can have different layouts depending on which elements are shown
 
link
 
Copy link Link copied
 
### Search
 
link
 
Copy link Link copied
 
The search app bar can include trailing actions inside and outside the search bar. When the search bar is selected, it should open the search view The search view is a full-screen modal often used to display a list of search results. It can also be opened by selecting a search icon. [More on search view](/m3/pages/search/overview) component.
 
link
 
Copy link Link copied
 
Container
 
Leading icon button
 
Hinted search text
 
Trailing icon or avatar
 
Search container
 
link
 
Copy link Link copied
 
A leading element and a trailing element outside search
 
A leading element, a trailing element inside search, and a trailing element outside search
 
A leading element and two trailing elements outside search
 
link
 
Copy link Link copied
 
### Image
 
An image can be placed in the app bar. In small app bars, this can replace the label text.
 
link
 
Copy link Link copied
 
Images can be added to app bars and can replace label text on small app bars
 
link
 
Copy link Link copied
 
### Filled trailing icon button
 
The app bar's trailing icon buttons can be replaced with a single, primary, or tonal filled icon button in default or wide sizes.
 
link
 
Copy link Link copied
 
The trailing icons can be configured to be a single filled icon button
 
link
 
Copy link Link copied
 
### Subtitle
 
link
 
Copy link Link copied
 
The medium flexible and large flexible app bars hug the text contents, so they are taller when a subtitle is visible
 
Small
 
Small with subtitle
 
Medium flexible
 
Medium flexible with subtitle
 
Large flexible
 
Large flexible with subtitle
 
link
 
Copy link Link copied
 
## Color
 
Color values are implemented through design tokens. For design, this means working with color values that correspond with tokens. For implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)
 
All app bars share the same color roles. On scroll, the container changes color to surface container .
 
link
 
Copy link Link copied
 
App bar color roles used for light and dark themes:
 
Surface
 
On surface
 
On surface variant
 
On surface
 
On surface variant
 
Surface container (on scroll)
 
link
 
Copy link Link copied
 
Search app bar color roles used for light and dark themes:
 
Surface
 
On surface variant
 
On surface variant
 
On surface variant
 
Surface container
 
Surface container
 
Surface container highest
 
link
 
Copy link Link copied
 
### Scroll states
 
link
 
Copy link Link copied
 
The app bar changes color when flat or on scroll. The search bar can also change color on scroll.
 
Flat
 
On scroll
 
link
 
Copy link Link copied
 
## Measurements
 
link
 
Copy link Link copied
 
### Search app bar
 
link
 
Copy link Link copied
 
Search app bar padding and size measurements
 
link
 
Copy link Link copied
 
### Small app bar
 
link
 
Copy link Link copied
 
Small app bar padding and size measurements
 
link
 
Copy link Link copied
 
### Medium flexible app bar
 
link
 
Copy link Link copied
 
Medium flexible app bar padding and size measurements
 
link
 
Copy link Link copied
 
### Large flexible app bar
 
link
 
Copy link Link copied
 
Large flexible app bar padding and size measurements
 
link
 
Copy link Link copied
 
## Baseline app bars
 
link
 
Copy link Link copied
 
The medium and large app bars are no longer recommended in M3 Expressive. Use the medium flexible and large flexible app bars in their place.
 
link
 
Copy link Link copied
 
Medium and large app bars have the same elements:
 
Container
 
Leading button
 
Trailing icons
 
Headline
 
link
 
Copy link Link copied
 
### Tokens & specs
 
link
 
Copy link Link copied
 
Select a token set to view in the table's menu. Baseline app bar token sets are organized into medium, large, and older baseline token sets. [Learn about design tokens](/m3/pages/design-tokens/overview)
 
link
 
Copy link Link copied
 
App bar - Size - Medium (baseline) arrow_drop_down
 
search visibility grid_view
 
Token
 
Value
 
App bar medium container height
 
md.comp.app-bar.medium.container.height content_copy
 
112dp App bar medium title font
 
md.comp.app-bar.medium.title.font content_copy
 
Aa App bar medium icon button size 
warning
 
md.comp.app-bar.medium.icon.size content_copy
 
24dp App bar medium subtitle font 
warning
 
md.comp.app-bar.medium.subtitle.font content_copy
 
Aa
 
link
 
Copy link Link copied
 
### Color
 
link
 
Copy link Link copied
 
Color values are implemented through design tokens. For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value. [Learn more about design tokens](/m3/pages/design-tokens/overview)
 
link
 
Copy link Link copied
 
Medium top app bar color roles used for light and dark schemes:
 
Surface
 
On surface
 
On surface
 
On surface variant
 
link
 
Copy link Link copied
 
### Measurements
 
link
 
Copy link Link copied
 
#### Medium app bar
 
link
 
Copy link Link copied
 
Medium app bar padding and size measurements
 
link
 
Copy link Link copied
 
#### Large app bar
 
link
 
Copy link Link copied
 
Large app bar padding and size measurements
