# Lists – Material Design 3

> Source: https://m3.material.io/components/lists/guidelines

link
 
Copy link Link copied
 
Lists can include a range of layout combinations:
 
Leading images, videos, icons, or avatars
 
Trailing text, icons, or icon buttons
 
link
 
Copy link Link copied
 
## Usage
 
link
 
Copy link Link copied
 
Lists are vertical groups of text, icons, images, and other elements, optimized for reading comprehension.
 
List items can contain multiple actions at once, like selection, icon buttons, overflow menus, and more.
 
A clear visual hierarchy makes lists easy to scan and read
 
link
 
Copy link Link copied
 
Use lists for communicating or selecting discrete items, such as choosing from a set of colors.
 
Lists are an organized way to add imagery and supporting elements to selection. In this color selection example, the list contains color swatches, color names, and a checkbox action.
 
link
 
Copy link Link copied
 
A list should be easy to scan. Any element can be used to anchor and align list item content.
 
Place supporting visuals and primary text in the same position in each list item.
 
Don’t vary the position of elements within a list.
 
Sample list
 
Content placement in a row
 
Supporting visuals are aligned for easy scanning
 
Primary text is aligned for easy scanning
 
link
 
Copy link Link copied
 
List items can adapt to different lengths of text:
 
Label text only A list item can contain a single line of label text. If the text doesn’t fit on one line, it can wrap or be truncated.
 
Label text with supporting text A list item can include supporting text below the label text. Both the label and supporting text can wrap or be truncated.
 
Three examples of list item sizes:
 
Label text only
 
Label text with supporting text on one line
 
Label text with supporting text that wraps to two lines
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
Container and label text are required. All other elements are optional:
 
Container
 
Label text
 
Supporting text
 
Trailing text
 
Trailing icon
 
Trailing selection control - checkbox, radio button, switch
 
Leading avatar container
 
Leading avatar text
 
Leading icon
 
Leading media - image or video
 
link
 
Copy link Link copied
 
### Container
 
List containers hold all list items and their elements. List item size is determined by the tallest element within the list item. [See layout measurements](/m3/pages/lists/specs#1824b94d-7d17-4a29-889f-d277037a1313)
 
When a list item features an image, consider customizing the container color to use a content-based color scheme. This should be applied to either the enabled state or for an interaction.
 
pause
 A list item can include a leading image and a vibrant color
 
link
 
Copy link Link copied
 
### Label & supporting text
 
Keep label text brief. To ensure list items are scannable:
 
Limit supporting text to one to three lines
 
Truncate supporting text, depending on screen size
 
[See adaptive guidance](/m3/pages/lists/guidelines#561cc637-aa43-4055-be1e-0716faeef7af)
 
Limit supporting text to one to three lines
 
link
 
Copy link Link copied
 
### Icons
 
Leading icon A leading icon should provide a quick visual cue that relates to the item's label text, helping people scan the list.
 
Trailing icon A trailing icon is often used to communicate status or indicate an action, like Show more .
 
Leading icons should relate to the label text
 
Trailing icons can communicate an action
 
link
 
Copy link Link copied
 
### Leading media
 
List items can contain a leading avatar, image, or video. Anchor visuals to the leading edge of the list to improve scannability.
 
Leading video thumbnails can open a video player or even play within the list.
 
check Do Place supporting visuals, like thumbnails, at the leading edge of a row to improve scannability
 
exclamation Caution Avoid placing visuals in the center of a row because it makes the list difficult to scan
 
link
 
Copy link Link copied
 
Avatars List items can include images in circular or expressive shapes to represent a person or entity.
 
Use square or rectangular images for other content, such as products or videos.
 
Use an expressive, circular avatar to represent a person or entity
 
link
 
Copy link Link copied
 
Primary & secondary actions
 
Use spacing to draw attention to the most important aspect of the list item, usually the primary action area or key content.
 
The primary action takes up more space:
 
1. Primary action area
 
2. Secondary action area
 
Align content by importance:
 
1. More distinguishing content
 
2. Less distinguishing content
 
link
 
Copy link Link copied
 
### Trailing text
 
Trailing text can provide additional meta-information about a list item, such as a price, count, or other details.
 
Use trailing text for supplemental details, like a price, count, or date
 
link
 
Copy link Link copied
 
### Selection controls
 
Selection Selection lets users choose specific items to act on. [More on selection](/m3/pages/selection) controls display list item actions. Position controls at the leading or trailing end of a list item:
 
Use checkboxes Checkboxes let users select one or more items from a list, or turn an item on or off. [More on checkboxes](/m3/pages/checkbox/overview) to select multiple items
 
Use switches Switches toggle the state of an item on or off. [More on switches](/m3/pages/switch/overview) to toggle settings on or off
 
Use radio buttons Radio buttons let people select one option from a set of options. [More on radio buttons](/m3/pages/radio-button/overview) to select a single item
 
List items with:
 
Checkboxes
 
Switches
 
Radio buttons
 
link
 
Copy link Link copied
 
### Gaps & dividers
 
Gaps or dividers can separate lists into items and groups:
 
Use gaps for contained lists. Gaps leverage expressive shape and containment tactics.
 
Limit dividers to uncontained or complex lists, only when a stronger visual separation is necessary.
 
check Do Use segmented gaps and filled list items to define a list group
 
exclamation Caution Limit the use of dividers to uncontained lists
 
link
 
Copy link Link copied
 
## Adaptive design
 
link
 
Copy link Link copied
 
### Line length
 
In fluid layouts Layout is the visual arrangement of elements on the screen. [More on layout](/m3/pages/understanding-layout/overview) , avoid excessively long lines of text when expanding containers and text-heavy components. This often means changing margins Margins are the spaces between the edge of a nested element and its parent element, such as the space between a button's label text and the edge of its container. [More on margins](/m3/pages/understanding-layout/spacing#0678ba2e-1bce-49b8-8591-e471d6417011) and typography properties as the container scales.
 
check Do Adjust margins to create a more comfortable line length for reading
 
link
 
Copy link Link copied
 
Adapt the width of the list container based on a line’s length, or by switching to a multi-column layout.
 
link
 
Copy link Link copied
 
check Do A multi-column layout can help break up content when needed
 
link
 
Copy link Link copied
 
The ideal line length for text is typically between 40 to 60 characters, but large-screen devices can accommodate up to 120 characters per line. If a line of text is close to 120 characters in length, consider increasing the line height to improve readability .
 
link
 
Copy link Link copied
 
close Don’t Don’t scale components without adjusting other affected areas of the screen, such as text length. This can result in line lengths that make reading difficult.
 
link
 
Copy link Link copied
 
A list in a compact window Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact window sizes](/m3/pages/applying-layout/compact) can become part of a two-column layout in an expanded window Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded window sizes](/m3/pages/applying-layout/expanded) , adjusting the amount of information shown in each list item.
 
link
 
Copy link Link copied
 
pause
 Reduce the amount of information shown in compact window sizes
 
link
 
Copy link Link copied
 
### Adapt list elements & layout
 
Lists can change their layout to adapt to different window sizes. This affects the size and placement of content.
 
For example, a list in a compact window can adjust margins Margins are the spaces between the edge of a nested element and its parent element, such as the space between a button's label text and the edge of its container. [More on margins](/m3/pages/understanding-layout/spacing#0678ba2e-1bce-49b8-8591-e471d6417011) , spacing, or density to better fit an expanded window.
 
pause
 On larger screens, lists can show more content, like supporting text and larger imagery
 
link
 
Copy link Link copied
 
### Swap components
 
Lists are just a compact composition of images, text, and actions. Other components, like cards and carousels, use the same elements but take up more space.
 
On large screens, consider swapping a list to a component with a similar purpose to take advantage of available space.
 
pause
 Information displayed in list items on mobile can change to cards on tablet and desktop
 
link
 
Copy link Link copied
 
### Compact window size
 
Lists should extend edge-to-edge in compact windows. Selecting a list item should open a page with the details.
 
pause
 On small screens, people can navigate between lists and full-screen detailed views
 
link
 
Copy link Link copied
 
### Medium & expanded window sizes
 
Medium Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation. [More on medium window size class](/m3/pages/applying-layout/medium) and expanded window sizes Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded window size class](/m3/pages/applying-layout/expanded) , such as tablet and desktop screens, can display primary and secondary content in the same view.
 
For example, a list and the detailed information can appear side-by-side.
 
On larger screens, a list-detail view can be more appropriate
 
link
 
Copy link Link copied
 
On a larger window size, a list may transform into a carousel.
 
pause
 Lists can transform into carousels in expanded windows
 
link
 
Copy link Link copied
 
Lists can also show more or less content as they scale up and down in size.
 
For example, a list item can reveal more content when the component expands.
 
pause
 List items reveal supporting text in expanded window sizes
 
link
 
Copy link Link copied
 
## Behavior
 
link
 
Copy link Link copied
 
### List selection modes
 
The selected state applies to the entire list item. For example, when an item with a checkbox is selected, both the list item and the checkbox show a selected state.
 
link
 
Copy link Link copied
 
Single-select
 
Lists can feature a single-selection component such as a radio button Radio buttons let people select one option from a set of options. [More on radio buttons](/m3/pages/radio-button/overview) .
 
Single-select list items:
 
Don’t support multi-actions
 
Can’t have secondary nested actions
 
Shouldn’t use checkboxes
 
Use radio buttons to allow a single selection in a list
 
link
 
Copy link Link copied
 
Multi-select
 
Multi-select lists allow for multiple list items to be toggled on.
 
Multi-select list items:
 
Pair well with checkboxes and switches
 
Can’t have secondary nested actions
 
Shouldn’t use radio buttons
 
Use checkboxes or switches for multi-select lists
 
link
 
Copy link Link copied
 
Single-action
 
In a single-action list, the entire list item performs one action, such as navigating to a new page.
 
Single-action list items:
 
Can’t have secondary nested actions
 
Can’t be toggled into a persistent selected state
 
Use a single-action list for a primary action, like navigation
 
link
 
Copy link Link copied
 
Multi-action
 
Multi-action lists can support multiple nested actions within a list item.
 
The primary action should take up the majority of the space in the leading and content positions.
 
Place supplementary actions, like a bookmark or menu, in the trailing position.
 
[More on multi-action accessibility](/m3/pages/lists/accessibility#b69b89a9-7ca0-4249-b25b-2d0c85a41dc0)
 
Place supplementary actions in the trailing position of a list item
 
link
 
Copy link Link copied
 
Non-interactive
 
Non-interactive lists can organize information in a scannable way. They don’t perform any actions and can’t be selected.
 
Use non-interactive lists to make information easy to scan
 
link
 
Copy link Link copied
 
### List interactions
 
link
 
Copy link Link copied
 
Expand & collapse
 
List items containing other list items can expand and collapse in a folder-like manner, to reveal or hide content.
 
Tapping a list item expands it vertically across the entire screen using a container transform transition pattern.
 
pause
 To expand a list item, display a parent-child transition
