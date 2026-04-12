# Segmented button – Material Design 3

> Source: https://m3.material.io/components/segmented-buttons/guidelines

link
 
Copy link Link copied
 
star
 
Note:
 
Segmented buttons are no longer recommended in the Material 3 expressive update. For those who have updated, use the [connected button group](/m3/pages/button-groups/overview/) instead, which has mostly the same functionality but with an updated visual design.
 
link
 
Copy link Link copied
 
Single-select
 
Multi-select
 
link
 
Copy link Link copied
 
## Usage
 
link
 
Copy link Link copied
 
Segmented buttons help people select options, switch views, or sort elements.
 
A segmented button can help switch between viewing restaurant and bar options
 
link
 
Copy link Link copied
 
There are 2 variants of segmented buttons:
 
Single-select
 
Multi-select
 
Single-select segmented button can only have 1 segment selected
 
Multi-select segmented button can have multiple segments selected
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
Segment
 
Container
 
Icon (optional)
 
Label text (optional)
 
Selected icon
 
link
 
Copy link Link copied
 
### Segments
 
Segmented buttons can have 2-5 segments. Each segment is clearly divided and contains label text, an icon, or both.
 
There can be anywhere from 2 to 5 segments in single-select and multi-select segmented buttons
 
link
 
Copy link Link copied
 
check Do Segmented buttons are best used for selecting between 2 and 5 choices
 
close Don’t Don’t use more than five segments in a single segmented button. Choices should be scoped. If you have more than five choices, consider using another component, such as chips.
 
link
 
Copy link Link copied
 
### Container
 
Like common buttons Buttons let people take action and make choices with one tap. , segmented buttons have fully rounded corners by default.
 
Segmented buttons have fully rounded corners
 
link
 
Copy link Link copied
 
### Icons
 
Icons may be used as labels by themselves or alongside text.
 
If an icon is used without label text, it must clearly communicate the option it represents.
 
Segmented buttons can include icons
 
link
 
Copy link Link copied
 
### Label text
 
Labels should be short and succinct. If a label is too long to fit within its segment, consider using an icon alone.
 
Use labels that are as clear and short as possible
 
link
 
Copy link Link copied
 
check Do Keep labels short and consistent in length
 
close Don’t Don’t allow segments to wrap onto a new line
 
link
 
Copy link Link copied
 
check Do Use consistent label types
 
exclamation Caution Icons can be used in place of labels, but they must clearly communicate their meaning
 
close Don’t Avoid mixing icon-only labels with text labels. Choose one label type and use that type for all segments.
 
link
 
Copy link Link copied
 
## Single-select
 
link
 
Copy link Link copied
 
Use a single-select segmented button to select one option from a set, switch between views, or sort elements from up to five options.
 
For example, use a single-select segmented button to choose one of a set of sizes, such as this beverage size selector.
 
A single select segmented button for choosing beverage size
 
link
 
Copy link Link copied
 
## Multi-select
 
link
 
Copy link Link copied
 
Use a multi-select segmented button to select or sort from two to five options. Unlike single-select, selection is not required and a user may concurrently select anywhere from all to none of the options.
 
For example, multi-select segmented buttons can be used to filter by price range when searching for a restaurant.
 
A multi-select segmented button for filtering restaurant search options
 
link
 
Copy link Link copied
 
## Placement
 
link
 
Copy link Link copied
 
Segmented buttons should have adequate margins Margins are the spaces between the edge of a nested element and its parent element, such as the space between a button's label text and the edge of its container. [More on margins](/m3/pages/understanding-layout/spacing#38a538d7-991f-4c39-8449-195d32caf397) from the edge of the viewport or frame.
 
On larger screens, set a maximum padding for all button segments so the set doesn't fill the screen.
 
check Do Allow adequate space for margins. The button container shouldn’t reach the edge of the viewport.
 
link
 
Copy link Link copied
 
check Do Set a maximum padding within the segments to ensure usability on larger screens
 
close Don’t Don’t allow segmented buttons to span the full width of larger screens or panes. This can leave too much padding on either side of the segment label, making the button less usable.
 
link
 
Copy link Link copied
 
Segmented buttons can be placed on other components, such as bottom sheets Bottom sheets show secondary content anchored to the bottom of the screen. [More on bottom sheets](/m3/pages/bottom-sheets/overview) or full-screen dialogs Full-screen dialogs fill the entire screen, displaying actions that require a series of tasks to complete. They're often used for creating a calendar entry. .
 
A segmented button can be placed on a bottom sheet
 
link
 
Copy link Link copied
 
## Behavior
 
link
 
Copy link Link copied
 
When using both icons and label text in segmented buttons, the icon label is replaced by the checkmark icon when the segment is selected.
 
pause
 Icons become checkmarks when selected in buttons that also use label text
