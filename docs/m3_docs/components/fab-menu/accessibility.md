# FAB menu

> Source: https://m3.material.io/components/fab-menu/accessibility

link
 
Copy link Link copied
 
## Use cases
 
link
 
Copy link Link copied
 
People should be able to do the following using assistive technology:
 
Navigate and interact with the FAB menu
 
Ensure focus is correct when navigating through the menu
 
link
 
Copy link Link copied
 
## Interaction & style
 
link
 
Copy link Link copied
 
FAB menu elements meet the minimum target size of 48dp.
 
FAB menus have 48x48dp minimum width and sufficient spacing by default
 
link
 
Copy link Link copied
 
When the FAB menu can scroll, make sure the items scroll behind the close button.
 
The close button should always be easy to access and unobstructed.
 
check Do Allow the menu items to scroll behind the close button
 
close Don’t Don’t obstruct the close button in short screens like horizontal orientation
 
link
 
Copy link Link copied
 
## Initial focus
 
link
 
Copy link Link copied
 
When the FAB is selected, the FAB menu opens, and initial focus remains on the close button, which takes the place of the original FAB.
 
Then the focus moves from the top menu item to the bottom.
 
Focus lands on the close button. People can then navigate through all the items.
 
Close button
 
First menu item
 
Second menu item
 
Third menu item
 
link
 
Copy link Link copied
 
## Keyboard navigation
 
link
 
Copy link Link copied
 
Keys Actions Tab Navigate to the next interactive element Space or Enter Activate the focused button or item
 
link
 
Copy link Link copied
 
## Labeling elements
 
link
 
Copy link Link copied
 
The close button of the FAB menu should have the button role and label close .
 
Label the close button with the button role
 
link
 
Copy link Link copied
 
On mobile web, the items should have the menu item roles.
 
The menu items should have labels matching the UI text.
 
Label each FAB menu item with the menu item role
