# Buttons – Material Design 3

> Source: https://m3.material.io/components/buttons/guidelines

link
 
Copy link Link copied
 
Buttons and icon buttons come in many shapes, styles, and sizes
 
link
 
Copy link Link copied
 
## Usage
 
link
 
Copy link Link copied
 
Buttons communicate actions that people can take. They are typically placed throughout the UI, in places like:
 
Dialogs Dialogs provide important prompts in a user flow. [More on dialogs](/m3/pages/dialogs/overview)
 
Modal windows
 
Forms
 
Cards Cards display content and actions about a single subject [More on cards](/m3/pages/cards/overview)
 
Toolbars Toolbars display frequently used actions relevant to the current page [More on toolbars](/m3/pages/tooltips/overview)
 
They can also be placed within standard button groups Standard button groups add interactions between adjacent buttons when they're pressed. [More on button groups](/m3/pages/button-groups/overview) .
 
pause
 Use visually-prominent filled buttons for the most important actions
 
link
 
Copy link Link copied
 
Buttons are just one option for representing actions in a product and shouldn’t be overused. Too many buttons on a screen can disrupt the visual hierarchy. Consider placing additional actions in a navigation rail Navigation rails let people switch between UI views on mid-sized devices [More on navigation rail](/m3/pages/navigation-rail/overview) , set of chips Chips help people enter information, make selections, filter content, or trigger actions. [More on chips](/m3/pages/chips/overview) , text links, or icon buttons Icon buttons help people take minor actions with one tap. [More on icon buttons](/m3/pages/icon-buttons/overview) .
 
check Do Use buttons for discrete actions
 
close Don’t Don’t clutter your UI with too many buttons. Consider presenting low-priority actions in overflow menus or as icon buttons.
 
link
 
Copy link Link copied
 
check Do A button container’s width is dynamically set to fit its label text
 
check Do Button container width can be responsive, which allows it to stretch horizontally
 
close Don’t A button container’s width shouldn’t be narrower than its label text
 
link
 
Copy link Link copied
 
There are five button styles, in order of emphasis:
 
Elevated button
 
Filled button
 
Filled tonal button
 
Outlined button
 
Text button
 
Buttons have default and toggle behaviors: A. Default button B. Toggle (unselected) C. Toggle (selected)
 
link
 
Copy link Link copied
 
A button group Button groups organize buttons and add interactions between them. [More on button groups](/m3/pages/button-groups/overview) is a collection of buttons that relate to each other and can respond to one another. Both buttons and icon buttons can be used inside a button group. In some cases, there are primary and secondary actions within a button group. Buttons with primary actions should have a higher visual emphasis through size, color, or shape.
 
[More on button groups](/m3/pages/button-groups/overview)
 
Different sized buttons in a button group help emphasize the main action from secondary actions
 
link
 
Copy link Link copied
 
## Toggle buttons
 
link
 
Copy link Link copied
 
Toggle buttons should be used for binary selections, such as Save or Favorite . When toggle buttons are pressed, they can change color, shape, and labels.
 
Toggle buttons should use an outlined icon when unselected, and a filled version of the icon when selected. If a filled version doesn’t exist, increase the weight instead.
 
By default, toggle buttons change from round to square when selected.
 
pause
 Use toggle buttons for binary actions
 
link
 
Copy link Link copied
 
If the label changes on selected or unselected states, be mindful of the character count. Changing the label significantly is disruptive to the user and the page layout.
 
check Do When using toggleable buttons, keep the label character count a similar length for both states
 
close Don’t The label length shouldn’t change dramatically to be longer or shorter
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
Label text
 
Container
 
Icon (optional)
 
link
 
Copy link Link copied
 
### Label text
 
Label text is the most important element of a button. It describes the action that will occur if someone taps a button. It should be very brief, ideally 1–3 words.
 
Use sentence case, which only capitalizes the first word and proper nouns. This allows the text to distinguish proper nouns, for example: Book with Flights , not BOOK WITH FLIGHTS .
 
Don’t truncate or wrap label text. It should always be fully visible on a single line.
 
check Do Use sentence case for button label text, capitalizing the first word and proper nouns
 
close Don’t Don’t wrap text. For maximum legibility, label text should remain on a single line.
 
link
 
Copy link Link copied
 
Buttons with the outlined and text color style depend on the colors to be recognizable from other text and elements. Use caution when putting these buttons next to visually similar elements, such as chips or large text.
 
exclamation Caution The outlined button style is very similar to chips. Consider using a filled or tonal button instead.
 
link
 
Copy link Link copied
 
### Container
 
Button containers hold the label text and optional icon. Buttons with the text color style have a visible container only when hovered, focused, or pressed.
 
Buttons with a round shape have containers with fully rounded corners.
 
Round buttons have containers with fully rounded corners
 
link
 
Copy link Link copied
 
Square buttons have containers with more subtle rounding that changes based on button size.
 
Square button have square containers and change radius as the button size changes
 
link
 
Copy link Link copied
 
check Do A button’s width dynamically adjusts to the label text
 
close Don’t Avoid setting a fixed width smaller than the label text
 
link
 
Copy link Link copied
 
### Icon (optional)
 
Icons visually communicate the button’s action and help draw attention. They should be placed on the leading side of the button, before the label text.
 
check Do Place the icon to the left of the label in buttons with text in left-to-right languages
 
check Do Place the icon to the right of the label in buttons with text in right-to-left languages
 
link
 
Copy link Link copied
 
check Do Use icons that clearly communicate their meaning
 
close Don’t Don’t vertically align an icon and text in the center of a button
 
close Don’t Don’t use two icons in the same button
 
link
 
Copy link Link copied
 
## Color styles
 
link
 
Copy link Link copied
 
### Elevated style
 
link
 
Copy link Link copied
 
The elevated button style is the same as the tonal button, but with a shadow.
 
To avoid overusing shadows, use the elevated style only when absolutely necessary, such as when the button requires visual separation from a visually prominent background.
 
Elevated buttons provide separation from a visually prominent background
 
link
 
Copy link Link copied
 
Buttons at higher elevations typically have more emphasis in a design, and should be used sparingly. For high emphasis, consider the filled style instead.
 
exclamation Caution Higher elevation increases the emphasis of a button
 
link
 
Copy link Link copied
 
### Filled style
 
link
 
Copy link Link copied
 
The filled button style has the most visual impact after the FAB Floating action buttons (FABs) help people take primary actions. [More on FABs](/m3/pages/fab/overview) , and should be used for important, final actions that complete a flow, like Save , Join now , or Confirm .
 
Filled buttons have high visual impact when used for important actions
 
link
 
Copy link Link copied
 
Since they have such strong emphasis, the filled style should be used sparingly, ideally for only one action on a page.
 
In some cases, filled buttons can use tertiary colors.
 
Filled buttons can be responsive to the layout grid and help emphasize main actions
 
link
 
Copy link Link copied
 
### Tonal style
 
link
 
Copy link Link copied
 
The tonal button style is useful in contexts where a lower-priority button requires slightly more emphasis than an outline would give, such as Next in an onboarding flow. Tonal buttons use the secondary color mapping.
 
The tonal style has less emphasis than filled or emphasis
 
link
 
Copy link Link copied
 
### Outlined style
 
link
 
Copy link Link copied
 
The outlined style is ideal for medium-emphasis buttons which contain actions that are important, but aren’t the primary action in a product.
 
Outlined buttons pair well with filled buttons to indicate alternative, secondary actions.
 
Outlined buttons contain less important supporting actions
 
link
 
Copy link Link copied
 
Outlined buttons display a stroke around the button container, and have no fill by default. They should be placed on simple backgrounds, not visually prominent backgrounds such as images or videos.
 
Outlined buttons display a stroke around the button container
 
link
 
Copy link Link copied
 
check Do Outlined buttons can be used on backgrounds with a color gradient
 
exclamation Caution Use caution when placing outlined buttons on top of images. Customizing the button to have a contrasting container fill can help ensure legibility of label text. Or, use a filled button instead.
 
link
 
Copy link Link copied
 
### Text style
 
link
 
Copy link Link copied
 
The text button style should be used for the lowest priority actions, especially when presenting multiple options.
 
They should be placed on simple backgrounds, not visually prominent backgrounds such as images or videos. The container isn’t visible until someone interacts with the button.
 
Don’t underline the text button. Use hyperlinked body text instead to emphasize links. [More on hyperlinks](/m3/pages/typography/applying-type#24856f70-f759-45df-a06c-92018f286083)
 
Use text buttons for the lowest priority actions
 
link
 
Copy link Link copied
 
Text buttons are often placed within components such as cards Cards display content and actions about a single subject. [More on cards](/m3/pages/cards/overview) , dialogs Dialogs provide important prompts in a user flow. [More on dialogs](/m3/pages/dialogs/overview) , and snackbars Snackbars show short updates about app processes at the bottom of the screen. [More on snackbars](/m3/pages/snackbar/overview) . Since text buttons don’t have a visible container in their default state States show the interaction status of a component or UI element. [More on states](/m3/pages/interaction-states/overview) , they don’t distract from nearby content.
 
However, since there’s no container, the label text color must always be recognizable from non-button text and elements.
 
Text button in a snackbar
 
Text button against an image background
 
link
 
Copy link Link copied
 
In cards, text buttons help maintain an emphasis on card content.
 
Text button in a card
 
link
 
Copy link Link copied
 
Dialogs use text buttons because the absence of a container helps unify the action with the dialog text.
 
Align text buttons to the trailing edge of dialogs, on the right for left-to-right languages and on the left for right-to-left languages.
 
Text buttons in a dialog
 
link
 
Copy link Link copied
 
## Adaptive design
 
link
 
Copy link Link copied
 
### Resizing
 
link
 
Copy link Link copied
 
When scaling layouts for large screen devices, buttons can adapt their visual presentation, size, alignment, and arrangement to fit different contexts and user needs.
 
link
 
Copy link Link copied
 
Choose the best button position based on screen size.
 
Filled buttons are end-aligned below flight information in a compact window
 
link
 
Copy link Link copied
 
Filled buttons are start-aligned beside flight information in a large window
 
link
 
Copy link Link copied
 
The icon and label text in a button stay centered and grouped as the button's width changes.
 
check Do Keep the icon and label text grouped and centered
 
close Don’t Don't ungroup the icon and label text or let them anchor to opposite sides of the button
 
link
 
Copy link Link copied
 
Buttons can be customized to change size and scaling behavior across different window sizes Window size classes are opinionated breakpoints where layouts need to change to optimize for available space, device conventions, and ergonomics. [More on window size classes](/m3/pages/applying-layout/window-size-classes) .
 
To avoid creating very long buttons in large windows, constrain button width or place buttons beside other elements.
 
close Don’t Don’t allow the button to stretch in a way that creates long, flat buttons with very little content inside
 
link
 
Copy link Link copied
 
### Presentation
 
link
 
Copy link Link copied
 
The size and placement of buttons can change as parent containers, such as cards, adapt for larger screens. Keep items, including buttons, in the same order between large and small screens to provide a consistent experience for screen readers and keyboard navigation.
 
Buttons can move in the layout, but elements should remain in the same order
