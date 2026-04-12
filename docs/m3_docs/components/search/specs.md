# Search – Material Design 3

> Source: https://m3.material.io/components/search/specs

link
 
Copy link Link copied
 
## Variants
 
link
 
Copy link Link copied
 
pause
 When a person executes a search , results appear in a list below the search bar
 
link
 
Copy link Link copied
 
Variant M3 M3 Expressive Search Available Available
 
link
 
Copy link Link copied
 
## Configurations
 
link
 
Copy link Link copied
 
### Style
 
link
 
Copy link Link copied
 
Search comes in two styles:
 
Contained: Has an expressive M3 Expressive is a major update to Material 3, adding visually stunning features, components, and variants, plus updates to the shape, motion, and typography systems. [More on M3 expressive](https://m3.material.io/blog/building-with-m3-expressive) look and feel. It uses a filled container to separate a search bar from a list Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview) of suggestions or results
 
Divided ( baseline Baseline variants and styles are the original M3 component designs. They may not have the latest features introduced in M3 Expressive, like updated motion, shapes, type, and styles. ): Doesn’t have the latest visual style, motion, or flexibility
 
link
 
Copy link Link copied
 
The contained style has a persistent, filled container, expressive motion, and rounded shape
 
The divided (baseline) style uses a divider to separate the search bar from suggestions and results
 
link
 
Copy link Link copied
 
### Layout
 
link
 
Copy link Link copied
 
Search suggestions and results appear in customizable lists, with two layout options: full-screen and docked. [More on search layouts](/m3/pages/search/guidelines#4f6c921c-795f-4e06-9b12-27ae7d502adb)
 
link
 
Copy link Link copied
 
Full-screen layout in the contained style
 
Docked layout in the contained style
 
link
 
Copy link Link copied
 
Full-screen layout in the divided style
 
Docked layout in the divided style
 
link
 
Copy link Link copied
 
Category Configuration M3 M3 Expressive Style Contained -- Available Divided Available Not recommended. Use contained. Layout Docked, full-screen Available Available
 
link
 
Copy link Link copied
 
## Tokens & specs
 
Use the table's menu to select a token set. The search bar set only contains tokens for the unfocused search bar. The search view set contains all other tokens when interacting with search, including all styles and layouts. [Learn more about design tokens](/m3/pages/design-tokens/overview)
 
link
 
Copy link Link copied
 
Search - View arrow_drop_down
 
search visibility grid_view expand_all
 
Token
 
Default, Android, Light arrow_drop_down
 
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
 
Search includes a search bar and a container for suggestions and results. The container is empty by default. Use the list Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview) component to add content. In the divided (baseline) style, a divider separates the search bar and results.
 
link
 
Copy link Link copied
 
Search bar container
 
Leading icon
 
Supporting text
 
Trailing icon and avatar (optional)
 
Input text
 
Container for search suggestions or results
 
link
 
Copy link Link copied
 
### Examples
 
With avatar
 
With one trailing icon button Icon buttons help people take minor actions with one tap. [More on icon buttons](/m3/pages/icon-buttons/overview)
 
With two trailing icon buttons
 
With trailing icon button and avatar
 
link
 
Copy link Link copied
 
## Color
 
link
 
Copy link Link copied
 
Color values are implemented through design tokens Design tokens are the building blocks of all UI elements. The same tokens are used in designs, tools, and code. [More on tokens](/m3/pages/design-tokens/overview) . For designers, this means working with color values that correspond with tokens. In implementation, a color value will be a token that references a value.
 
link
 
Copy link Link copied
 
### Full-screen layout
 
link
 
Copy link Link copied
 
Full-screen search color roles used in light and dark themes:
 
Surface container low
 
On surface variant
 
On surface variant
 
Surface container high
 
On surface variant
 
On surface
 
link
 
Copy link Link copied
 
### Docked layout
 
link
 
Copy link Link copied
 
Docked search color roles used in light and dark themes:
 
Surface container high
 
On surface variant
 
On surface variant
 
Surface container high
 
On surface variant
 
On surface
 
link
 
Copy link Link copied
 
## States
 
link
 
Copy link Link copied
 
States are visual representations used to communicate the status of a component or an interactive element. In [focused search](/m3/pages/search/guidelines#a9b2df31-8561-4326-82cd-41ed6532b765) , individual elements maintain their own interaction states. [Learn more about interaction states](/m3/pages/interaction-states/overview)
 
link
 
Copy link Link copied
 
### Search bar
 
link
 
Copy link Link copied
 
Enabled
 
Hovered
 
Focused
 
Pressed (ripple)
 
link
 
Copy link Link copied
 
### Search suggestions & results
 
link
 
Copy link Link copied
 
Search includes a container for suggestions and results. The container is empty by default. Use the list component to add content.
 
link
 
Copy link Link copied
 
Enabled
 
Hovered
 
Focused
 
Pressed (ripple)
 
link
 
Copy link Link copied
 
## Measurements
 
link
 
Copy link Link copied
 
### Search bar
 
link
 
Copy link Link copied
 
Unfocused search bar with leading and trailing icon measurements
 
Unfocused search bar with avatar measurements
 
link
 
Copy link Link copied
 
In M3 Expressive, the search bar expands when focused. The margins change from 24dp to 12dp.
 
link
 
Copy link Link copied
 
Unfocused search bar margin measurements
 
Focused search bar margin measurements
 
link
 
Copy link Link copied
 
Element Attribute Value Container Width Min: 360dp, max: 720dp Height 56dp Label alignment Start-aligned Leading padding Unfocused: 24dp, focused: 12dp Trailing padding Unfocused: 24dp, focused: 12dp Leading icon and label padding (from tap target) 4dp Label and trailing icon padding (from tap target) 4dp Avatar Size 30dp
 
link
 
Copy link Link copied
 
### Focused search
 
link
 
Copy link Link copied
 
#### Contained style
 
link
 
Copy link Link copied
 
Full-screen search padding and size measurements for contained style
 
Docked search padding and size measurements for contained style
 
link
 
Copy link Link copied
 
Element Attribute Value Full-screen container Width Full width Height Full height Docked container Width Min: 360dp, max: 720dp Height Min: 240dp, max: 2/3 of screen height Search bar container Height 56dp Label alignment Start-aligned Leading padding 16dp Trailing padding 16dp Leading icon and label padding (from tap target) 4dp Leading icon and label padding (from tap target) 4dp
 
link
 
Copy link Link copied
 
#### Divided style
 
link
 
Copy link Link copied
 
Full-screen search padding and size measurements for divided style
 
Docked search padding and size measurements for divided style
