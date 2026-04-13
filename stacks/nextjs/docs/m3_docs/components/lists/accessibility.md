# Lists – Material Design 3

> Source: https://m3.material.io/components/lists/accessibility

link
 
Copy link Link copied
 
## Use cases
 
link
 
Copy link Link copied
 
People should be able to do the following with assistive technology:
 
Navigate to a list item
 
Select a list item
 
link
 
Copy link Link copied
 
## Indicate selection with more than color
 
link
 
Copy link Link copied
 
To make selected items clear for everyone, don't rely on color as the only visual cue.
 
Use an additional indicator that an item is selected such as:
 
Radio buttons Radio buttons let people select one option from a set of options. [More on radio buttons](/m3/pages/radio-button/overview) or checkboxes Checkboxes let users select one or more items from a list, or turn an item on or off. [More on checkboxes](/m3/pages/checkbox/overview)
 
Leading or trailing icons
 
A visual style not related to color, like underlined text
 
Use two visual cues to show a list item is selected, like a leading checkmark and filled color
 
link
 
Copy link Link copied
 
## Interaction & style
 
link
 
Copy link Link copied
 
### Touch
 
When a person taps on a list item, a touch ripple appears, indicating interaction feedback.
 
pause
 A ripple appears when a person taps on a list item to select it
 
link
 
Copy link Link copied
 
### Cursor
 
When hovered, the hover A hover state communicates when a user has placed a cursor above an interactive element. [More on hover state](/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844) state provides a visual cue that a list item is interactive.
 
Cursor: Hover
 
Cursor: Selected
 
link
 
Copy link Link copied
 
### Keyboard & switch
 
When a person tabs to a single-action list, a focus indicator appears, providing a visual cue that the first list item is now focused A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice. [More on focused state](/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f) and action can be taken.
 
When a person interacts with the focused list item via Space or Enter , the action is performed.
 
pause
 Tab key navigates to the list. Space or Enter keys activate items.
 
link
 
Copy link Link copied
 
## Focus
 
link
 
Copy link Link copied
 
### Single-action lists
 
The first element in a list should always receive focus, unless the list has a selected element. In that case, focus should go to the selected list item instead. After an element is focused A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice. [More on focused state](/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f) , a person should be able to navigate within the list using arrow keys.
 
Tab key focuses on the first item or the selected item
 
Arrow keys navigate up and down through list items
 
link
 
Copy link Link copied
 
All list items must be able to be activated using the Space or Enter key. [More on single-action lists](/m3/pages/lists/guidelines#3e45f939-457a-44a8-8551-a2354c521d26)
 
Space or Enter keys activate an element in a list
 
link
 
Copy link Link copied
 
### Multi-action lists
 
Multi-action list items contain a primary action and at least one supplementary action. The list item as a whole isn't selectable; only the individual actions are.
 
A person should be able to use a keyboard to:
 
Tab to the list item, which focuses the first element
 
Move between between all focusable elements in the list using the Up , Down , Left , and Right arrow keys
 
Activate a focused element using Space or Enter
 
[More on multi-action lists](/m3/pages/lists/guidelines#db85439b-0e67-43b0-a2dc-61395738af64)
 
Tab brings the focus to the first action
 
Down and Right arrow keys move focus to the next action of the list item, or to the first action in the next item
 
link
 
Copy link Link copied
 
Up and Left arrow keys move focus to the previous action of the list item
 
If the focus is on a list item’s first action, the Up and Left arrows move focus back to the last action of the previous item
 
The Space or Enter key activates a selected action in a list
 
link
 
Copy link Link copied
 
## Keyboard navigation
 
link
 
Copy link Link copied
 
Keys Actions Tab To move focus to the first list item, last list item, or outside of the list component Down and right arrow keys Moves to the next element in the list; if the focused element is the last in the list, it wraps back to the top of the list Up and left arrow keys Moves to the previous element in the list; if the focused element is the first in the list, it wraps back to the bottom of the list Space or Enter To select a list item not yet selected
 
link
 
Copy link Link copied
 
## Labeling elements
 
link
 
Copy link Link copied
 
Accessibility Accessible design makes products usable for people with all kinds of abilities. [More on accessibility](/m3/pages/overview/principles) labels are used with assistive devices like screen readers.
 
The accessibility label for a list item is typically the same as the label text and supporting text .
 
Some labels, roles, and states are [dependent on platform](/m3/pages/lists/accessibility#09e32b7d-78a1-45c1-be12-4c6646cfe1d1) .
 
A list item’s label text and supporting text is used for its accessibility label
 
link
 
Copy link Link copied
 
### Platform-specific labels
 
link
 
Copy link Link copied
 
#### Single-select lists
 Trait Web MDC-Android Jetpack Compose Aria label Container label: Should describe selection type
 
List item: Should match the visible label text List item: Should match the visible label text List item: Should match the visible label text Role Container: List box List item: Option List item: Radio button List item: Radio button State Selected or Not-selected Checked or Not-checked Checked or Not-checked
 
link
 
Copy link Link copied
 
#### Multi-select lists
 Trait Web MDC-Android Jetpack Compose Aria label Container label: Should describe selection type
 
List item: Should match the visible label text List item: Should match the visible label text List item: Should match the visible label text Role Container: List box List item: Option List item: Checkbox List item: Checkbox State Selected or Not-selected Checked or Not-checked Checked or Not-checked
 
link
 
Copy link Link copied
 
On web, a list container’s accessibility label describes the type of selection that can be made, and the role is List box .
 
On web, a list container’s role is List box
 
link
 
Copy link Link copied
 
On Jetpack Compose, the role applies to the list item as a whole.
 
If a list isn't selectable, the label text is read out without a role.
 
When selectable, the role Checkbox applies to the entire list item on Jetpack Compose
 
link
 
Copy link Link copied
 
On MDC-Android, components contained within the list should be labeled according to that component’s specific guidelines:
 
[Checkbox](/m3/pages/checkbox/accessibility)
 
[Radio button](/m3/pages/radio-button/accessibility)
 
On MDC-Android, the accessibility label and role are applied to the interactive component by default
