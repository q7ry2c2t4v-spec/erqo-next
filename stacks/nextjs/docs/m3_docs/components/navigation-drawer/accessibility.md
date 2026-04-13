# Navigation drawer – Material Design 3

> Source: https://m3.material.io/components/navigation-drawer/accessibility

link
 
Copy link Link copied
 
star
 
Note:
 
The navigation drawer is no longer recommended in the Material 3 expressive update. For those who have updated, use an [expanded navigation rail](/m3/pages/navigation-rail/overview/) , which has mostly the same functionality of the navigation drawer and adapts better across window size classes.
 
link
 
Copy link Link copied
 
## Use cases
 
link
 
Copy link Link copied
 
Users should be able to:
 
Move between navigation destinations with assistive technology
 
Select a particular navigation destination from a set
 
Get appropriate feedback based on input Device inputs provide interactive control of an app. Common inputs include a mouse, keyboard, and touchpad. [More on inputs](/m3/pages/inputs) type
 
link
 
Copy link Link copied
 
## Interaction & style
 
link
 
Copy link Link copied
 
Touch
 
When a navigation item is tapped, the active indicator appears in place, providing feedback to the user that it is selected
 
A touch ripple passes through the indicator
 
The icon switches from outlined to filled
 
The icon changes color, becoming darker
 
pause
 Touch: Tap
 
link
 
Copy link Link copied
 
Cursor
 
When hovered, the hover A hover state communicates when a user has placed a cursor above an interactive element. [More on hover state](/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844) indicator appears providing a visual cue that the destination is interactive
 
When clicked, a ripple passes through the indicator
 
The icon switches from outlined to filled
 
The icon changes color, becoming darker in light theme and lighter in dark theme, to increase the contrast
 
pause
 Cursor: Hover, Click
 
link
 
Copy link Link copied
 
## Initial focus
 
link
 
Copy link Link copied
 
Initial focus lands directly on the first navigation item, since that is the first interactive element of the component.
 
Focus lands on first navigation item
 
link
 
Copy link Link copied
 
## Closing
 
link
 
Copy link Link copied
 
The modal navigation drawer can be dismissed by selecting the scrim that covers the rest of the screen.
 
Select the scrim to close the navigation drawer
 
link
 
Copy link Link copied
 
## Visual indicators
 
link
 
Copy link Link copied
 
Icons are the primary focus of the navigation and such give the dominant cue of its state States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) . Use a filled icon for the selected destination to differentiate from the outlined icons of non-selected destinations.
 
The navigation item is selected via Space / Enter
 
link
 
Copy link Link copied
 
check Do Use a filled icon for the selected navigation destination to differentiate from the other destinations
 
close Don’t Avoid keeping the icon style for the selected navigation destination the same as unselected destination's icons. This removes an important visual indicator of which destination is active.
 
link
 
Copy link Link copied
 
When selected, the icon fills, darkens in light theme (or lightens in dark theme), and is backed by an active indicator shape
 
link
 
Copy link Link copied
 
## Keyboard navigation
 
link
 
Copy link Link copied
 
Keys Actions Tab Focus lands on the first navigation destination Space or Enter Selects the focused A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice. [More on focused state](/m3/pages/interaction-states/applying-states#bfc1624f-6bcc-4306-b0c1-425e2d8a1bf9) navigation destination, and focus moves to the newly opened section (if applicable) Arrow Navigate between destinations within the navigation drawer
 
link
 
Copy link Link copied
 
## Labeling elements
 
link
 
Copy link Link copied
 
The accessibility Accessible design makes products usable for people with all kinds of abilities. [More on accessibility](/m3/pages/overview/principles) label for a navigation item is typically the same as the destination name. If the UI text is correctly linked, assistive tech (such as a screenreader) will read the UI text followed by the component’s role. For MDC-Android, a more descriptive accessibility label is not available to be set and the role is not announced.
 
A navigation drawer’s accessibility label can incorporate its adjacent UI text
 
link
 
Copy link Link copied
 
When the visible UI text is ambiguous, accessibility labels need to be more descriptive. For example, a navigation destination visibly labeled Recents would benefit from additional information in its accessibility label to clarify the destination’s intent.
 
While the visible label text reads Recents, the accessibility label for this destination clarifies its function: Recent images
