# Inputs – Material Design 3

> Source: https://m3.material.io/foundations/interaction/inputs

link
 
Copy link Link copied
 
Design for touch, keyboard, and mouse interactions
 
Embrace multiple input methods and gestures within your app
 
link
 
Copy link Link copied
 
Designing for inputs allows people to use the inputs they prefer, like a mouse to highlight text on a tablet
 
link
 
Copy link Link copied
 
## External inputs for devices
 
link
 
Copy link Link copied
 
People can use external inputs like a mouse, keyboard, or stylus with their phone, tablet, foldable, TV, laptop, or desktop computer. When someone connects an external input to their device, they expect it to behave in familiar and useful ways. Designing for different input methods can make a product more usable and accessible on all screen sizes.
 
link
 
Copy link Link copied
 
### Common features of external inputs
 
link
 
Copy link Link copied
 
#### Mouse
 
Left and right click
 
Mouse wheel
 
Extra buttons
 
#### Trackpad
 
Left and right click
 
Gestures
 
Haptics
 
#### Physical keyboard
 
Replaces virtual keyboard
 
Media keys
 
Modifier keys
 
link
 
Copy link Link copied
 
link
 
Copy link Link copied
 
### Input device behaviors
 
Depending on the input device, designers and developers can implement behaviors that meet standard conventions and user expectations.
 
Input device action Anticipated behavior Mouse and trackpad movement Show a mouse cursor on the screen Primary click Treat mouse clicks differently than touch events Secondary click Activate context menus Hover Change component states Highlight Allow text to be selected by the mouse cursor Mouse wheel and trackpad two finger drag Scroll list vertically and horizontally Trackpad pinch Zoom an element or page Physical keyboard Hide and show on screen keyboard
 
link
 
Copy link Link copied
 
## Mouse and cursor interactions
 
link
 
Copy link Link copied
 
When an external mouse input device is used, a mouse cursor should be shown, regardless of the device type. A mouse may be connected to tablets, laptops, phones, foldables, and more. On some devices, it's possible to use an external input device simultaneously with touch input. On devices that don't specifically recognize mouse or stylus input, the mouse is treated as touch input.
 
link
 
Copy link Link copied
 
### Primary click
 
link
 
Copy link Link copied
 
A mouse click or stylus tap should demonstrate the same feedback as touch input. One example of this is showing the ripple for a pressed state.
 
A visible mouse cursor is seen when the external input is connected
 
link
 
Copy link Link copied
 
### Secondary click
 
link
 
Copy link Link copied
 
#### Context menus
 
A secondary click (whether using a single button or two fingers on a trackpad) should activate a context menu. The context menu shows additional options for the object that's clicked. See [menus](/m3/pages/menus/overview) for more usage and guidelines.
 
link
 
Copy link Link copied
 
The context menu should appear when right clicking with a mouse or trackpad
 
link
 
Copy link Link copied
 
### Hover
 
link
 
Copy link Link copied
 
When using a mouse cursor, help users discover interactive objects by enabling visual changes. When the mouse rests on an interactive element, the hover state is a valuable cue for interaction. See [states](/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844) for styles and guidelines. Hovering with a cursor (or stylus) should also invoke tooltips when applicable. See [tooltips](/m3/pages/tooltips/overview) for guidance.
 
Components without a hover state
 
Components with a hover state change applied
 
link
 
Copy link Link copied
 
### Cursors
 
link
 
Copy link Link copied
 
Cursors appear when using external input devices like a mouse or trackpad. The cursor can change to communicate more information about interactive elements.
 
link
 
Copy link Link copied
 
#### Pointer
 
By default, external input control should be rendered as a pointer.
 
A pointer provides a visible indicator for input controls
 
link
 
Copy link Link copied
 
#### Hand
 
The cursor should appear as a hand to indicate links or linked images.
 
The hand cursor is used for links and clickable images
 
link
 
Copy link Link copied
 
#### Resize arrows
 
The cursor should change to resize arrows on the boundaries of resizable elements.
 
Resize arrows indicate an element can be resized
 
link
 
Copy link Link copied
 
#### I-beam
 
The cursor should appear as an I-beam when hovering on text. When manipulating editable text, the following interactions apply:
 
Single click places the cursor
 
Double click selects a word
 
Triple click selects a paragraph
 
Single click deselects text and repositions the cursor
 
An I-beam cursor indicates selectable text
 
link
 
Copy link Link copied
 
### Text selection
 
When selecting text using a mouse, trackpad, or stylus:
 
Highlight the selected area using a single color
 
Don’t show touch controls next to the highlighted area
 
Selected text shows a visible highlight
 
link
 
Copy link Link copied
 
### Text selection with touch control
 
link
 
Copy link Link copied
 
When interacting using touch, always show touch controls, even if other inputs are connected. When using a mouse, trackpad, or stylus, show the I-beam and context menu, even if it's a touch device.
 
link
 
Copy link Link copied
 
When using a touchscreen to select text, show touch controls
 
When using a mouse, trackpad, or stylus to select text, use the right-click context menu
 
link
 
Copy link Link copied
 
### Stylus input
 
When using a stylus, cursors are usually not necessary, unless they communicate tool properties such as brush size or shape.
 
The circle cursor indicates the selected stylus tool and size
 
link
 
Copy link Link copied
 
## Mouse wheel and trackpad gestures
 
link
 
Copy link Link copied
 
When an external mouse or touchpad is used, the mouse wheel and trackpad gesture allow more actions.
 
link
 
Copy link Link copied
 
### Vertical scroll
 
When a cursor is positioned on a list, the mouse wheel and two-finger touchpad gesture should allow vertical scrolling of the list.
 
pause
 Scrolling a vertical list using the mouse wheel or trackpad gestures. Note that only the detail panel under the cursor scrolls.
 
link
 
Copy link Link copied
 
### Touch scroll & mouse text selection
 
Upon touch and drag gesture, the text area will scroll. With a mouse interaction, dragging in a text area will select the text.
 
link
 
Copy link Link copied
 
pause
 On a touch screen, dragging upward scrolls the field down
 
pause
 When using a mouse, dragging upward selects text and images
 
link
 
Copy link Link copied
 
### Horizontal scroll
 
Mouse users should be able to scroll with a mouse wheel to navigate horizontally scrolling fields. Trackpad users should be able to scroll using a two-finger horizontal gesture.
 
link
 
Copy link Link copied
 
pause
 Carousels can scroll horizontally using a scroll wheel or trackpad
 
link
 
Copy link Link copied
 
## Physical keyboard
 
link
 
Copy link Link copied
 
When a physical keyboard is connected to a device, either externally or as a built-in laptop keyboard, users should be able to perform any actions that the virtual keyboard provides, and more.
 
link
 
Copy link Link copied
 
### Show and hide virtual keyboard
 
A virtual keyboard should appear or hide in response to the presence of a physical keyboard.
 
link
 
Copy link Link copied
 
check Do When a physical keyboard is attached, hide the virtual keyboard
 
check Do When a physical keyboard is removed, show the virtual keyboard
 
link
 
Copy link Link copied
 
### Common keyboard interactions
 
link
 
Copy link Link copied
 
#### Enter key
 
People typically expect the E nter key on a physical keyboard to be enabled by developers to allow a common function like sending a message.
 
link
 
Copy link Link copied
 
pause
 The Enter key typically triggers actions like sending a message
 
link
 
Copy link Link copied
 
#### Spacebar control
 
People typically expect the Spacebar (or available media keys) to be enabled to play and pause music or video.
 
link
 
Copy link Link copied
 
pause
 Pressing Space usually pauses and plays media
 
link
 
Copy link Link copied
 
#### Tab focus
 
When keyboard users navigate a page using Tab , the focus on interactive items must follow a logical order. On most pages, that means left to right, top to bottom. When focused from a keyboard or other input device, the focus state includes a ring-like keyboard focus indicator.
 
link
 
Copy link Link copied
 
Tab focus includes a visible keyboard focus indicator
 
The focus state moves elements as the user presses Tab on their keyboard
 
link
 
Copy link Link copied
 
#### Escape key
 
link
 
Copy link Link copied
 
People typically expect the Escape key on a physical keyboard to dismiss elements, remove focus, or clear selections.
 
link
 
Copy link Link copied
 
pause
 The Escape key should dismiss any visible modal elements like menus, dialogs, or bottom sheets
 
pause
 The Escape key should remove any visible focus indicators and set the focus order to 0
 
pause
 The Escape key should remove the text cursor when typing, but should not remove already-typed text
