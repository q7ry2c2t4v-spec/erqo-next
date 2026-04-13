# Extended FAB – Material Design 3

> Source: https://m3.material.io/components/extended-fab/guidelines

link
 
Copy link Link copied
 
Extended FABs are more prominent than regular FABs
 
link
 
Copy link Link copied
 
## Usage
 
link
 
Copy link Link copied
 
Use an extended FAB on screens with long, scrolling views that require persistent access to an action, such as a checkout screen.
 
Use it when label text helps understand the main action, or to add further emphasis to the button.
 
Extended FABs ensure the main action is visible at all times
 
link
 
Copy link Link copied
 
Use an extended FAB to provide constant access to a primary action above long-scrolling surface content
 
Use an extended FAB to emphasize a page’s primary action
 
link
 
Copy link Link copied
 
### Additional emphasis
 
The extended FAB can provide more emphasis and clarity to a product’s primary action.
 
Since it has room for both a text label and icon, the extended FAB can be effective where an icon alone is ambiguous. However, the relationship between an extended FAB's icon and label should be clear.
 
An extended FAB can be effective where an icon alone is too vague
 
link
 
Copy link Link copied
 
Like the regular FAB, only one extended FAB should be used per screen.
 
Multiple FABs compete for attention.
 
If additional high-level actions are required, consider adding more buttons elsewhere on the page.
 
check Do Only show one prominent action at a time with the extended FAB
 
close Don’t Don’t use multiple extended FABs in one screen as it disrupts visual hierarchy
 
link
 
Copy link Link copied
 
The extended FAB shouldn't be used as an option in a set of actions.
 
Instead, use filled buttons for a similar level of emphasis.
 
check Do Use a button with appropriate styling to emphasize it in a group of buttons
 
close Don’t Don’t use the extended FAB to convey an option in a set of actions
 
link
 
Copy link Link copied
 
### Choosing a size
 
There are three variants of extended FABs: small, medium, and large.
 
Choose an appropriately-sized extended FAB to add the right amount of emphasis for an action.
 
In compact windows with one prominent action, the large extended FAB can be appropriate.
 
In larger window sizes, use a medium or large extended FAB.
 
There are three sizes of extended FABs
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
Container
 
Label text
 
Icon (optional)
 
link
 
Copy link Link copied
 
### Container
 
The extended FAB container is a rounded rectangle that hugs its contents.
 
The extended FAB grows and shrinks with text length.
 
The extended FAB container hugs the icon and text
 
link
 
Copy link Link copied
 
### Icon (optional)
 
An extended FAB's icon should intuitively represent its action.
 
link
 
Copy link Link copied
 
check Do Unlike standard FABs, extended FABs don't require an icon
 
close Don’t An extended FAB can't have an icon without a text label
 
link
 
Copy link Link copied
 
### Label text
 
The extended FAB’s label should clearly describe its action.
 
Use 1–2 words at most. Keep in mind that localization may increase the amount of characters and width of the extended FAB.
 
check Do Shorten the text as much as needed. Include an icon for additional context.
 
close Don’t Avoid wrapping or truncating text
 
link
 
Copy link Link copied
 
## Placement
 
link
 
Copy link Link copied
 
check Do Place the extended FAB above the rest of the UI, off of elements like app bars
 
close Don’t Don’t place the extended FAB on top of toolbars. It disrupts the consistency of the elevation and surface layers.
 
link
 
Copy link Link copied
 
close Don’t Don’t place the extended FAB in the upper half of a mobile screen, as it disrupts the reading of the UI
 
close Don’t Don’t place extended FABs on cards or inside other containers
 
link
 
Copy link Link copied
 
Avoid putting other floating components, like the floating toolbar Floating toolbars float on top of page content and can provide contextual, dynamic actions. [More on toolbars](/m3/pages/toolbars/overview) , on screen with the extended FAB.
 
close Don’t Floating toolbars can be paired with FABs, but not extended FABs
 
link
 
Copy link Link copied
 
## Responsive layout
 
link
 
Copy link Link copied
 
The FAB and extended FAB can transform into each other depending on available space and layout.
 
In a collapsed navigation rail Collpased navigation rails take up minimal space and are best for medium windows and wider. [More on navigation rails](/m3/pages/navigation-rail/overview) , a FAB would be used. When the rail is expanded, the FAB can transform into an extended FAB.
 
When space is limited, an extended FAB can transform into a FAB
 
link
 
Copy link Link copied
 
### Right-to-left languages
 
Extended FABs should mirror their elements in right-to-left (RTL) languages.
 
Icons should be placed to the left of labels for left-to-right (LTR) languages
 
Icons should be placed to the right of labels for RTL languages
 
link
 
Copy link Link copied
 
### Window sizes
 
In compact Window widths smaller than 600dp, such as a phone in portrait orientation. [More on compact window size class](/m3/pages/applying-layout/compact) and medium window sizes Window widths from 600dp to 839dp, such as a tablet or foldable in portrait orientation. [More on medium window size class](/m3/pages/applying-layout/medium) , the extended FAB should be placed at the bottom of the screen, either center-aligned or aligned to the trailing edge of the window.
 
The extended FAB can be center-aligned
 
The extended FAB can be aligned to the trailing edge of the window
 
link
 
Copy link Link copied
 
In expanded Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded window size class](/m3/pages/applying-layout/expanded) and larger window sizes, the extended FAB should appear either:
 
At the bottom right edge of the window, in both LTR and RTL languages
 
Within the navigation rail
 
The extended FAB can be right-aligned in both LTR and RTL languages
 
The extended FAB can be at the top of the expanded navigation rail
 
link
 
Copy link Link copied
 
## Behavior
 
link
 
Copy link Link copied
 
### Appearing
 
The extended FAB surface expands when appearing on screen using an [enter and exit](/m3/pages/motion-transitions/transition-patterns#e1c2a650-d7a4-4a6d-9025-e6b7845291ed) transition pattern.
 
pause
 An extended FAB expands when appearing on screen
 
link
 
Copy link Link copied
 
### Expanding
 
The extended FAB can expand and adapt to any shape using a [container transform](/m3/pages/motion-transitions/transition-patterns) transition pattern.
 
This includes a surface that is part of the app structure, or a surface that spans the entire screen.
 
pause
 An extended FAB can expand and adapt to any shape
 
link
 
Copy link Link copied
 
### Transforming
 
The extended FAB can transform into a FAB on scroll to temporarily take up less space on screen.
 
pause
 An extended FAB can transform into a FAB
 
link
 
Copy link Link copied
 
### Scrolling
 
The extended FAB can transform into a FAB when scrolling down, and back to an extended FAB when scrolling up.
 
pause
 An extended FAB collapses and expands when scrolling
 
link
 
Copy link Link copied
 
When the FAB switches to an extended FAB, the following transitions occur:
 
The FAB shape changes
 
FAB icon moves to the left
 
FAB text label fades in
 
pause
 FAB switches to an extended FAB
