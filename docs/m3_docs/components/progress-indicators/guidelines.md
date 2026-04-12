# Progress indicators – Material Design 3

> Source: https://m3.material.io/components/progress-indicators/guidelines

link
 
Copy link Link copied
 
pause
 Progress indicators communicate the status of an ongoing process
 
link
 
Copy link Link copied
 
## Usage
 
link
 
Copy link Link copied
 
Use progress indicators to show the status of ongoing processes, such as loading an app, submitting a form, or saving updates.
 
When multiple items are loading, use a single progress indicator to show progress for the group. Don’t add progress indicators to every activity.
 
pause
 check Do Indicate overall progress of a group of items
 
pause
 close Don’t Don’t show the progress of each activity in a group
 
link
 
Copy link Link copied
 
Choose a loading Loading indicators show the progress of a process with a short wait time. [More on loading indicators](/m3/pages/loading-indicator/overview) or progress indicator Progress indicators show the status of a process in real time. [More on progress indicators](/m3/pages/progress-indicators/overview) that corresponds to the expected wait time and kind of process.
 
If the wait is very long, consider allowing people to navigate away from the page while the process finishes up.
 
Expected wait time Recommendation Instant (under 200ms) No indicator Short (between 200ms and 5s) Loading indicator Long (Over 5s) Progress indicator
 
link
 
Copy link Link copied
 
pause
 Instant (under 200ms): Display the content immediately
 
pause
 Short (between 200ms and 5s): Use a loading indicator
 
pause
 Long (over 5s): Use a progress indicator
 
link
 
Copy link Link copied
 
There are two variants of progress indicators:
 
Linear
 
Circular
 
Linear indicators are best when placed on the edge of a container.
 
Circular indicators are best when centered in an element.
 
A process should be represented by the same variant of progress indicator throughout the product. For example, if refreshing uses a circular indicator in one place, it should use circular indicators everywhere.
 
Linear indicator
 
Circular indicator
 
link
 
Copy link Link copied
 
Progress indicators behave differently based on the time of progress being tracked:
 
Determinate : Known progress and wait time
 
Indeterminate : Unknown progress and wait time
 
When using a determinate indicator, the indicator must accurately represent the progress of what it's measuring.
 
Use indeterminate indicators to show that a process is happening, but the wait time is unknown.
 
pause
 Determinate progress indicators fill from 0% to 100%
 
Indeterminate progress indicators move along a fixed track, growing and shrinking in size
 
link
 
Copy link Link copied
 
As more information about a process becomes available, a progress indicator should change from indeterminate to determinate .
 
pause
 A linear progress indicator changes from indeterminate to determinate while loading a screen
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
pause
 Active indicator
 
Track
 
Stop indicator
 
link
 
Copy link Link copied
 
### Active indicator
 
The active indicator shows the progress that has been made so far.
 
In indeterminate processes, it grows and shrinks along the track repeatedly.
 
pause
 Linear indicators animate from the leading to the trailing edge along the track. Circular indicators animate from the top of the track, clockwise by default.
 
link
 
Copy link Link copied
 
The active indicator appears as soon as progress begins. At low percentages where space is limited, this should appear as a dot to help people understand that there’s progress underway.
 
When progress first begins, the active indicator appears as a dot
 
link
 
Copy link Link copied
 
The active indicator has two shape options: flat and wavy . Use the shape that best fits the product’s tone.
 
The wavy shape can make longer processes feel less static and is best used when a more expressive style is appropriate.
 
When using the wavy shape, the overall height of the component changes. At very small sizes, the wavy shape may not be as visible.
 
pause
 Wavy linear indicators increase the height of the overall container
 
link
 
Copy link Link copied
 
### Stop indicator
 
The stop indicator is a 4dp circle that marks the end of a linear determinate progress indicator to meet Material's accessibility standards.
 
It's not used for indeterminate or circular progress indicators.
 
The stop indicator is required if the track has a contrast below 3:1 with its container or the surface behind the container.
 
check Do Use a stop indicator when placing the progress indicator inside a container with low contrast
 
exclamation Caution Only remove the end stop indicator if there's a visual contrast of at least 3:1 with surrounding surfaces
 
link
 
Copy link Link copied
 
## Placement
 
link
 
Copy link Link copied
 
Place a linear progress indicator along the edge of a container that’s loading. If the container changes shape, place it on the edge that animates. It can also be placed in the middle of a container.
 
Use a single progress indicator at the top of a page to show progress of the whole group. Don’t add one for every element unless they’re activated independently.
 
pause
 When at the top of a screen, a progress indicator shows that all of the page content is loading
 
pause
 When attached to a card, a progress indicator shows that just the card content is loading
 
link
 
Copy link Link copied
 
pause
 A progress indicator on the expanding edge of a card shows that the edge may expand to show the loaded content
 
link
 
Copy link Link copied
 
Circular progress indicators should be centered directly on the container or page that's loading, such as a button or card.
 
When loading more items on a page, place the circular progress indicator in the empty space where the new content will appear, not overlapping existing content.
 
However, if the content does not take long to load, consider using a loading indicator instead.
 
pause
 A circular progress indicator can show that the page is loading
 
pause
 A circular progress indicator can show where new items will appear on a page. A loading indicator also works well in this space.
 
link
 
Copy link Link copied
 
### Progress indicators in buttons
 
A circular indicator can be placed in a button to show that the button’s action is currently in progress.
 
In very small buttons, use the flat shape since the wavy shape is not as visible at that size.
 
To ensure a minimum 3:1 contrast ratio, change the active indicator color to be the same color as the button’s icon or label text, and remove the track.
 
pause
 check Do Use circular indicators for short, indeterminate activities under 5 seconds
 
pause
 close Don’t Avoid applying progress indicators to every button in a list
 
link
 
Copy link Link copied
 
## Responsive layout
 
link
 
Copy link Link copied
 
### Right-to-left languages
 
Linear progress indicators should be mirrored horizontally for products using right-to-left (RTL) languages.
 
Circular progress indicators don’t need to be mirrored.
 
Linear progress indicators can flow from right to left in right-to-left (RTL) languages
 
link
 
Copy link Link copied
 
### Large screens
 
Circular progress indicators have flexible sizes. They can range from 24dp to 240dp, depending on the placement and the window size. Avoid exceeding the minimum and maximum sizes.
 
Reserve very large progress indicators for large and extra-large windows, such as desktop.
 
The waveform should scale with the size so the proportions look the same across sizes
 
link
 
Copy link Link copied
 
Linear progress indicators dynamically adjust to fit the width of the window or element they’re placed within, such as a card. They shouldn’t be used in any elements smaller than 40dp.
 
The padding on each end should be 4dp minimum, but can be modified.
 
The linear progress indicator should always span the width of the UI element it’s placed within
