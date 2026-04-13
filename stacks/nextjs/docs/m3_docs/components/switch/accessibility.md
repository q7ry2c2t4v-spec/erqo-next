# Switch – Material Design 3

> Source: https://m3.material.io/components/switch/accessibility

link
 
Copy link Link copied
 
## Use cases
 
People should be able to do the following with assistive technology:
 
Navigate to a switch with a keyboard or switch input
 
Toggle the switch on and off
 
Get appropriate feedback based on input type documented under [Interaction & style](/m3/pages/switch/accessibility#c0e9fae1-48df-428b-b028-4f7be071ada3)
 
link
 
Copy link Link copied
 
## Interaction & style
 
link
 
Copy link Link copied
 
The switch handle increases in size to indicate interactivity for both touch and cursor control interactions.
 
Touch When tapped or dragged A dragged state communicates when a user presses and moves an element. [More on dragged state](/m3/pages/interaction-states/applying-states#c97582c4-5fef-42ce-9c34-71f8dcc5b8ad) , the handle size grows, providing interaction feedback.
 
Cursor When hovered (in both on and off states States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) ), the hover A hover state communicates when a user has placed a cursor above an interactive element. [More on hover state](/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844) area grows, providing a visual cue that the handle is interactive. When clicked, the handle size grows.
 
Touch: Tap, Drag
 
Cursor: Hover, Click
 
link
 
Copy link Link copied
 
### Avoid applying density by default
 
Don't apply density to switches by default — this lowers their targets below our best practice of 48x48 CSS pixels. Instead, give people a way to choose a higher density, like selecting a denser layout or changing the theme.
 
To ensure that this density setting can easily be reverted when it's active, keep all targets to change it at a minimum 48x48 CSS pixels each.
 
link
 
Copy link Link copied
 
## Initial focus
 
link
 
Copy link Link copied
 
Initial focus lands directly on the switch’s handle, since it’s the primary interactive element of the component.
 
Focus lands on the switch handle
 
The switch is toggled using Space or Enter
 
link
 
Copy link Link copied
 
## Keyboard navigation
 
link
 
Copy link Link copied
 
Keys Actions Tab Focus lands on the switch handle Space or Enter Toggles the handle on and off
 
link
 
Copy link Link copied
 
## Labeling elements
 
link
 
Copy link Link copied
 
The accessibility Accessible design makes products usable for people with all kinds of abilities. [More on accessibility](/m3/pages/overview) label for a switch uses the adjacent label text if implemented correctly.
 
Assistive tech such as a screen reader will read the UI text followed by the component’s role.
 
A switch’s accessibility label can incorporate its adjacent UI text
 
link
 
Copy link Link copied
 
When the visible UI text is ambiguous, accessibility labels need to be more descriptive. For example, a switch visibly labelled Photo album would benefit from additional information to clarify the switch’s function.
 
Consider making the adjacent label text more descriptive when possible. This reduces the need for different accessibility text.
 
While the visible label text reads Photo album , the accessibility label for this switch clarifies its function: Photo album access
