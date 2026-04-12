# Sliders – Material Design 3

> Source: https://m3.material.io/components/sliders/accessibility

link
 
Copy link Link copied
 
## Use cases
 
link
 
Copy link Link copied
 
People should be able to do the following using assistive technology :
 
Navigate to a slider
 
Select a range by controlling a handle along a track
 
Get appropriate feedback based on input type
 
link
 
Copy link Link copied
 
## Interaction & style
 
link
 
Copy link Link copied
 
The slider handle shrinks in width and the value appears to provide a visual cue to the user that the handle is being pressed.
 
Touch
 
When tapped or dragged, the handle width shrinks to provide interaction feedback, and the value appears.
 
Cursor
 
When hovered, the cursor changes. When clicked and dragged, the handle width shrinks, and the value appears.
 
pause
 The slider handle changes width during interaction
 
link
 
Copy link Link copied
 
### Focus and navigation
 
Initial focus lands directly on the handle, since it’s the primary interactive element of the slider.
 
The slider value can then be adjusted using the arrow keys or other keyboard navigation options.
 
pause
 Use arrow keys to change the slider value
 
link
 
Copy link Link copied
 
## Color contrast
 
link
 
Copy link Link copied
 
Use visual anchors so the end of the slider’s inactive track has at least 3:1 contrast with the background. The stop indicator makes the end easily visible on most backgrounds.
 
A stop indicator on the inactive track makes it easier to identify the end of the slider on a low-contrast background
 
link
 
Copy link Link copied
 
Alternatively, icons or other elements that have a 3:1 contrast with the background can be used to indicate the ends of the slider’s inactive track.
 
Icons make it easier to identify the ends of the slider on a low-contrast background
 
link
 
Copy link Link copied
 
## Keyboard navigation
 
link
 
Copy link Link copied
 
Keys Actions Tab Moves focus to the slider handle Arrows Increase and decrease the value by one value or one stop indicator Space & Arrows Increase and decrease the value by one interval or one stop indicator Home or End Set the slider to the first and last values on the slider
 
link
 
Copy link Link copied
 
## Labeling elements
 
link
 
Copy link Link copied
 
The accessibility label for a slider is typically the same as the slider's adjacent text label. It should have the slider role.
 
A slider’s accessibility label should match the adjacent UI text
 
link
 
Copy link Link copied
 
If the UI text is correctly linked to the slider, assistive tech (such as a screenreader) will read the UI text followed by the component’s role.
 
Icon buttons placed outside the slider should have the button role
