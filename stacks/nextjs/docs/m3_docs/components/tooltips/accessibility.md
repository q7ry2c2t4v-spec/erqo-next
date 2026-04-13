# Tooltips – Material Design 3

> Source: https://m3.material.io/components/tooltips/accessibility

link
 
Copy link Link copied
 
## Use cases
 
link
 
Copy link Link copied
 
People should be able to do the following using assistive technology:
 
Receive a tooltip message
 
Activate a tooltip with a keyboard or switch input
 
link
 
Copy link Link copied
 
## Interaction & style
 
link
 
Copy link Link copied
 
Plain and rich tooltips without required actions should remain on screen long enough for people to receive the information without disrupting their existing flow or task.
 
pause
 check Do Plain tooltips should remain on the screen temporarily after the cursor moves away
 
link
 
Copy link Link copied
 
Tooltips can appear when an actionable element, like a button or navigation rail, is hovered or focused. However, this tooltip shouldn’t hide crucial information.
 
Rich tooltips can also appear by selecting an element instead of hovering or focusing on it.
 
Tooltips can appear on hover or focus to explain actions
 
Rich tooltips can appear when an element is selected
 
link
 
Copy link Link copied
 
## Focus order
 
link
 
Copy link Link copied
 
Tooltip containers should not block important information or prevent a person from completing an action.
 
Focus order within the rich tooltip moves top to bottom between interactive elements.
 
Avoid trapping screen reader and keyboard focus on rich tooltips.
 
People should be able to move linearly through the rest of the page.
 
Parent element
 
Inline link
 
Text button
 
link
 
Copy link Link copied
 
## Keyboard navigation
 
link
 
Copy link Link copied
 
Keys Actions Tab Focus lands on button, if available Space or Enter Activates the focused element
 
link
 
Copy link Link copied
 
link
 
Copy link Link copied
 
## Labeling elements
 
link
 
Copy link Link copied
 
Tooltips should have the Tooltip role, or similar.
 
Label all elements in the tooltip according to their own accessibility guidance.
 
The tooltip container should have the Tooltip role
