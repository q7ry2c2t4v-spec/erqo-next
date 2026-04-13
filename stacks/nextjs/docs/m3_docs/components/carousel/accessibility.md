# Carousel – Material Design 3

> Source: https://m3.material.io/components/carousel/accessibility

link
 
Copy link Link copied
 
## Use cases
 
link
 
Copy link Link copied
 
Users should be able to do the following with assistive technology:
 
Navigate to the carousel container
 
Navigate between different carousel items
 
Activate a carousel item
 
Skip over the carousel items
 
link
 
Copy link Link copied
 
## Requirements on scrolling pages
 
link
 
Copy link Link copied
 
On vertically-scrolling pages, carousels require an accessible way to view all the items without horizontally scrolling. (This requirement doesn't apply to full-screen carousels The full-screen carousel layout shows one edge-to-edge large item at a time and scrolls vertically. .)
 
Material recommends adding a Show all button below the carousel, which opens a dedicated vertically-scrolling page of all carousel items.
 
pause
 Carousels without headers should use a Show all button to view all carousel items
 
link
 
Copy link Link copied
 
The Show all button should have a padding of 4dp
 
link
 
Copy link Link copied
 
If the carousel has a header, you can use an arrow icon button instead. Place the arrow icon directly next to the header or in the same row.
 
Make sure the header is also displayed on the page of all carousel items.
 
pause
 Carousels with headers should use an arrow to view all carousel items
 
link
 
Copy link Link copied
 
Headers should align with the leading edge, and the arrow icon should have a size of 48dp
 
link
 
Copy link Link copied
 
Avoid customizing the accessibility solution when possible. However, if your product needs an alternative solution, consider adding a Show all button in nearby navigation, or add alternative control buttons close to the carousel.
 
Avoid adding UI elements, like arrows or other icons, within or beside the carousel.
 
close Don’t Avoid adding buttons into the carousel container or beside it. Place any buttons above or below the carousel.
 
close Don’t Don't cover the carousel with buttons or other UI
 
link
 
Copy link Link copied
 
## Interaction & style
 
link
 
Copy link Link copied
 
### Touch
 
Tapping on a carousel item changes the shape slightly, and creates a touch ripple for interaction feedback.
 
pause
 Touch: Tap
 
link
 
Copy link Link copied
 
### Cursor
 
The hover state A hover state communicates when a user has placed a cursor above an interactive element. [More on hover state](/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844) provides a visual cue that the carousel item is interactive.
 
When the carousel item is clicked (in both active and inactive states), a ripple appears for interaction feedback.
 
pause
 Cursor: Hover, click
 
link
 
Copy link Link copied
 
### Initial focus
 
When navigating to a carousel using assistive technology, use Tab to place initial focus on the first carousel item. Then, use Tab or the arrow keys to navigate the carousel items.
 
Use the up and down arrow keys to leave the carousel and focus on the next element on the page, like the Show all button.
 
check Do Set initial focus on the first carousel item, and use arrows to navigate items
 
link
 
Copy link Link copied
 
close Don’t Avoid focusing on the carousel container
 
link
 
Copy link Link copied
 
## Keyboard navigation
 
link
 
Copy link Link copied
 
Keys Actions Tab or Arrows Moves to the previous or next carousel item Space or Enter Activates the focused A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice. [More on focused state](/m3/pages/interaction-states/applying-states#bc6d6853-48ef-490e-8076-448e89e69f0f) carousel item
 
link
 
Copy link Link copied
 
## Labeling elements
 
link
 
Copy link Link copied
 
The carousel container has the container role.
 
The carousel container is labelled appropriately and has the container role
 
link
 
Copy link Link copied
 
Each carousel may have a different number of items, so the label reads out the total amount of items and the current item in focus.
 
The carousel item label indicates the current item in focus and the total number of items
 
link
 
Copy link Link copied
 
## Reduced motion
 
link
 
Copy link Link copied
 
When reduced motion settings are turned on, the parallax effect should be removed and carousel items should no longer expand as they come into view. All items are the same size.
 
Make sure carousels with reduced motion reach the edges of the window to avoid clipping visuals.
 
pause
 Default carousel for multi-scroll
 
Carousel with reduced motion settings turned on
 
link
 
Copy link Link copied
 
For hero carousels The hero carousel layout shows at least one large and one small item at a time. with reduced motion, the small carousel item is only partially shown on screen.
 
pause
 Default carousel for single-scroll
 
Carousel with reduced motion settings turned on
