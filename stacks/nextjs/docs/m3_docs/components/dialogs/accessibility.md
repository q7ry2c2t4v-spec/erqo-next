# Dialogs – Material Design 3

> Source: https://m3.material.io/components/dialogs/accessibility

link
 
Copy link Link copied
 
## Use cases
 
link
 
Copy link Link copied
 
People should be able to use assistive technology to:
 
Open and close a dialog
 
Provide and submit other inputs if the dialog is interactive, such as a text field Text fields let users enter text into a UI. [More on text fields](/m3/pages/text-fields/overview) or selectable list Lists are continuous, vertical indexes of text and images. [More on lists](/m3/pages/lists/overview)
 
Scroll the dialog to access all of its contents if that content extends beyond the container of the dialog
 
link
 
Copy link Link copied
 
## Interaction & style
 
link
 
Copy link Link copied
 
### Use sparingly
 
Dialogs are purposefully interruptive. This means they appear in front of app content and disrupt the flow of content for people who may, for example, be using a screen reader to navigate the page.
 
As such, dialogs should be used sparingly and only to provide critical information. Less critical information should be presented in a non-blocking way within the flow of app content.
 
check Do Present non-critical information using other UI within the flow of app content
 
close Don’t Avoid putting non-critical information in a dialog
 
link
 
Copy link Link copied
 
### 200% text size
 
Avoid excessive text wrapping or truncation by choosing concise strings.
 
On Android, headlines should be kept concise enough to fit within four lines after the text size is increased to 200%. If a headline exceeds this limit and gets truncated, provide an alternative way to access the full content in a single tap.
 
exclamation Caution Avoid excessive text wrapping or truncation by choosing concise strings
 
link
 
Copy link Link copied
 
### Elements within dialogs
 
Because dialogs can contain various elements within them, refer to the relevant accessibility Accessible design makes products usable for people with all kinds of abilities. [More on accessibility](/m3/pages/overview/principles) guidelines for each element. Some common examples include:
 
Text fields Text fields let users enter text into a UI. [More on text fields](/m3/pages/text-fields/overview)
 
Typography Material's typography follows a type scale with accessibility considerations baked in. [More on typography](/m3/pages/text-fields/accessibility)
 
Buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview)
 
Full-screen dialogs can contain various elements such as (1) text fields, (2) typography, and (3) buttons, which each may have their own accessibility guidelines
 
link
 
Copy link Link copied
 
## Initial focus
 
link
 
Copy link Link copied
 
When a dialog appears, focus should automatically land on the first interactive element within the dialog.
 
Initial focus lands on the first interactive element within a dialog. The tab key moves focus through the next interactive elements in a cycle.
 
The shift and tab keys together move focus in the opposite direction. The space or enter key triggers or commits the action of the focused element.
 
link
 
Copy link Link copied
 
## Keyboard navigation
 
link
 
Copy link Link copied
 
Keys Actions Tab Focus lands on the next interactive element contained in the dialog, or the first element if focus is currently on the last element Shift + Tab Focus lands on the previous interactive element contained in the dialog, or the last element if focus is currently on the first element Space or Enter Triggers or commits the action of the focused A focused state communicates when a user has highlighted an element, using an input method such as a keyboard or voice. [More on focused state](/m3/pages/interaction-states/applying-states#bfc1624f-6bcc-4306-b0c1-425e2d8a1bf9) element Escape Closes the dialog
 
link
 
Copy link Link copied
 
## Labeling elements
 
link
 
Copy link Link copied
 
The accessibility Accessible design makes products usable for people with all kinds of abilities. [More on accessibility](/m3/pages/overview/principles) label for a dialog is typically the same as the dialog’s title or headline.
 
On web, basic dialogs should have the alert dialog role.
 
Basic dialogs are known as alert dialogs on web
 
link
 
Copy link Link copied
 
Components contained within the dialog, such as buttons, should be labeled according to the guidelines specific to those components.
 
For common examples, see:
 
Buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/specs)
 
Text fields Text fields let users enter text into a UI. [More on text fields](/m3/pages/text-fields/overview)
 
Elements within a dialog should be labeled according to their guidelines
