# Tooltips – Material Design 3

> Source: https://m3.material.io/components/tooltips/guidelines

link
 
Copy link Link copied
 
Plain and rich tooltips serve different purposes
 
link
 
Copy link Link copied
 
## Usage
 
link
 
Copy link Link copied
 
A tooltip provides additional context for a UI element.
 
Plain tooltips Plain tooltips briefly describe a UI element. They're best used for labelling UI elements with no text, like icon-only buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) and fields.
 
Rich tooltips Rich tooltips provide additional context about a UI element. They can optionally contain a subhead, buttons, and hyperlinks.
 
Rich tooltips are best used for longer text like definitions or explanations.
 
Plain tooltip
 
Rich tooltip
 
link
 
Copy link Link copied
 
check Do Use plain tooltips to label icon-only buttons
 
close Don’t Plain tooltips aren't needed when the UI element already has label text
 
link
 
Copy link Link copied
 
check Do Use rich tooltips to provide extra information and actions about a UI element or new feature
 
close Don’t Don't hide critical information within tooltips as it’s easy to miss. Use an interruptive dialog instead.
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
### Plain tooltip
 
link
 
Copy link Link copied
 
Container
 
Supporting text
 
link
 
Copy link Link copied
 
### Supporting text
 
link
 
Copy link Link copied
 
check Do Briefly describe a UI element
 
exclamation Caution Avoid wrapping text to multiple lines or including many pieces of information
 
link
 
Copy link Link copied
 
### Rich tooltip
 
link
 
Copy link Link copied
 
Subhead (optional)
 
Container
 
Supporting text
 
Text button (optional)
 
link
 
Copy link Link copied
 
### Subhead (optional)
 
Keep subheads brief, ideally to one line. They should summarize or describe the message of the rich tooltip Rich tooltips provide additional context about a UI element. They can optionally contain a subhead, buttons, and hyperlinks. .
 
Subheads are important to include when the rich tooltip appears automatically, like when the page loads.
 
check Do Summarize the message in a few words
 
close Don’t Avoid wrapping to more than one line
 
link
 
Copy link Link copied
 
### Text buttons (optional)
 
Rich tooltips can have up to two text buttons Buttons let people take action and make choices with one tap. [More on buttons](/m3/pages/common-buttons/overview) . These should be brief and relevant to the message in the supporting text.
 
Keep buttons short so they can be side by side. Avoid stacking them when possible.
 
exclamation Caution Avoid stacking buttons
 
link
 
Copy link Link copied
 
## Placement
 
link
 
Copy link Link copied
 
### Plain tooltips
 
By default, plain tooltips are positioned directly above the parent element.
 
If there's a visual boundary, like a button, the distance is 4dp
 
If there's no visual boundary, like with text baselines, the distance is 8dp
 
If the element is in an app bar App bars contain page navigation and information at the top of a screen. [More on app bars](/m3/pages/app-bars/overview) , the plain tooltip appears below the element at the same distance.
 
Plain tooltip with a 4dp distance between the target and tooltip
 
link
 
Copy link Link copied
 
### Rich tooltips
 
By default, rich tooltips are positioned to the bottom right of the parent element. They adjust position to avoid going off screen.  Tooltips shouldn't cover the parent element.
 
Dynamic positioning The position of the tooltip adjusts in increments of 8dp to avoid going off-screen.
 
Desktop placement On desktop, tooltips may appear centered below the parent element and remain visible while moving within the target region.
 
Four different rich tooltip locations based on dynamic positioning
 
link
 
Copy link Link copied
 
## Behavior
 
link
 
Copy link Link copied
 
To show a tooltip, hover A hover state communicates when a user has placed a cursor above an interactive element. [More on hover state](/m3/pages/interaction-states/applying-states#71c347c2-dd75-485b-892e-04d2900bd844) on the parent element on desktop, or tap and hold the element on mobile. Persistent rich tooltips Rich tooltips provide additional context about a UI element. They can optionally contain a subhead, buttons, and hyperlinks. only appear when clicked or tapped.
 
link
 
Copy link Link copied
 
### Transient by default
 
Both plain Plain tooltips briefly describe a UI element. They're often used for labelling UI elements with no text, like icon-only buttons and fields. and rich tooltips disappear 1.5 seconds after navigating away from the target region.
 
Triggering a new tooltip immediately closes any other open tooltip.
 
pause
 Tooltips disappear after a 1.5 second delay when no other element is hovered
 
link
 
Copy link Link copied
 
close Don’t Only display one tooltip at a time
 
link
 
Copy link Link copied
 
### Persistent rich tooltips
 
Persistent rich tooltips appear when either:
 
The parent element is clicked
 
The page loads and a new feature is being explained
 
Persistent rich tooltips remain active even when leaving the target region. They only disappear once a person interacts with another UI element. Hovering doesn't trigger the tooltip.
 
When appearing on page load, the tooltip can introduce and explain new features on various parent elements.
 
Avoid using persistent rich tooltips on icon buttons.
 
close Don’t Don’t use a persistent rich tooltip on icon buttons
