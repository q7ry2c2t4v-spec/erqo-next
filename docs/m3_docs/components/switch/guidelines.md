# Switch – Material Design 3

> Source: https://m3.material.io/components/switch/guidelines

link
 
Copy link Link copied
 
Switches change settings and other options immediately
 
link
 
Copy link Link copied
 
## Usage
 
link
 
Copy link Link copied
 
Switches are best used to adjust settings and other standalone options.
 
They make a binary selection Selection lets users choose specific items to act on. [More on selection](/m3/pages/selection) :
 
On and off
 
True and false
 
The effects of a switch should start immediately, without needing to save.
 
pause
 Use a switch to turn an option on and off
 
link
 
Copy link Link copied
 
Use switches to:
 
Toggle a single item on or off
 
Immediately activate or deactivate something
 
Switches are commonly used on mobile to turn settings on or off
 
link
 
Copy link Link copied
 
Switches control binary options, not opposing ones. A binary option represents a single selection Selection lets users choose specific items to act on. [More on selection](/m3/pages/selection) that's either on or off.
 
Opposing options are when only one option in a set can be selected at a time, like a list Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview) or map view. Use a connected button group Connected button groups have smaller inner corners and are best used for selection. [More on button groups](/m3/pages/button-groups/overview) instead.
 
check Do Use a connected button group to choose between opposing options
 
close Don’t Avoid using switches to toggle between opposing options
 
link
 
Copy link Link copied
 
### Alternate selection controls
 
Checkboxes Checkboxes let users select one or more items from a list, or turn an item on or off. [More on checkboxes](/m3/pages/checkbox/overview) , radio buttons Radio buttons let people select one option from a set of options. [More on radio buttons](/m3/pages/radio-button/overview) , and switches are the three main kinds of selection controls. They help people make choices, like selecting options or turning settings on and off.
 
Use checkboxes to select multiple related options in a list.
 
Use radio buttons to select a single option in a list.
 
Use switches to select standalone or more verbose options in a list, like settings.
 
Checkboxes
 
Radio buttons
 
link
 
Copy link Link copied
 
check Do Use checkboxes (not switches) to let people select one or more options from a list
 
close Don’t A switch can't replace a button. People expect a call to action to be a button, not a switch.
 
link
 
Copy link Link copied
 
check Do Use radio buttons (not switches) when only one item can be selected from a list
 
close Don’t Avoid using a switch to select multiple options that require people to save. Switches should be immediate. Use checkboxes instead.
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
Track
 
Handle
 
Icon (optional)
 
link
 
Copy link Link copied
 
### Icon (optional)
 
The switch handle can contain an optional icon.
 
pause
 The icon within the handle should always communicate the switch's selection
 
link
 
Copy link Link copied
 
Icons can be used to visually emphasize the switch’s selection Selection lets users choose specific items to act on. [More on selection](/m3/pages/selection) . The icon’s meaning should be clear and unambiguous to help the people understand whether switch is on or off.
 
check Do Use icons that clearly communicate whether the switch is on or off, such as an X and a checkmark
 
close Don’t Avoid using more ambiguous or non-binary icons, such as a moon or edit icon
 
link
 
Copy link Link copied
 
### Label text
 
Switches should always be paired with an inline label describing what the switch controls when selected.
 
check Do Keep labels short and direct. A label should describe what the control does when the switch is on.
 
link
 
Copy link Link copied
 
close Don’t Don't add label text into the switch; the font size would be too small to be accessible. Use an appropriate icon instead.
 
link
 
Copy link Link copied
 
## Placement
 
link
 
Copy link Link copied
 
Switches are often arranged in stacked layouts Layout is the visual arrangement of elements on the screen. [More on layout](/m3/pages/understanding-layout/overview) .
 
Settings screens are common places to use switches
 
link
 
Copy link Link copied
 
## Behavior
 
link
 
Copy link Link copied
 
A switch is successfully toggled when the handle slides to the other side of the track after an interaction.
 
pause
 When selected, the switch handle slides to the opposite end of the track
 
link
 
Copy link Link copied
 
When a person toggles a switch, its handle size changes and the corresponding action takes effect immediately.
 
pause
 The on state of the switch is indicated by a larger handle size
