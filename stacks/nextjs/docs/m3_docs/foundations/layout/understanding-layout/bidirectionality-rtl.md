# Layout – Material Design 3

> Source: https://m3.material.io/foundations/layout/understanding-layout/bidirectionality-rtl

link
 
Copy link Link copied
 
[Over 2 billion people](https://www.w3.org/International/questions/qa-scripts.en.html) read and write in right-to-left (RTL) languages like Arabic, Hebrew, Farsi and Urdu. Layouts should support both left-to-right (LTR) and RTL languages through mirroring and other best practices to ensure content is easy for global audiences to understand and navigate. Consider the holistic experience including [global writing](/m3/pages/global-writing/overview#0d0f8403-e5ff-4579-be74-0c4dbcef7fcb) , localizing voice and [design principles for culturally appropriate icons](/m3/pages/icons/designing-icons#1056d971-81ca-4abe-b931-42185dd76638) . Material's components are built to support RTL, such as naming elements and tokens as "leading" and "trailing." However, extra configuration may be needed to achieve specific RTL situations.
 
link
 
Copy link Link copied
 
## Mirroring
 
link
 
Copy link Link copied
 
When a layout is changed from LTR to RTL (or vice-versa), and flipped horizontally, it’s often called mirroring. UI elements and text that typically appear on the left in LTR aligns to the right. Reading flow starts from the top right corner, instead of the top left. Not all elements mirror with RTL languages. For example, graphs and charts maintain a LTR directionality for Persian and Urdu.
 
A mirrored layout in an RTL language reverses the alignment and ordering of elements.
 
link
 
Copy link Link copied
 
## Text rendering
 
link
 
Copy link Link copied
 
Correct text rendering is foundational for a great user experience and it’s critical for readability and usability. Text rendering has two parts:
 
Alignment: How the edges of the text box are placed alongside other elements.
 
Directionality: How text and other elements flow within a text box, like left-to-right, or right-to-left.
 
In RTL languages, text is usually right-aligned, and elements flow from right-to-left.   Common issues with RTL language rendering are text entry, cursor position, punctuation, phone numbers, and URLs.   Improperly rendering text in RTL languages can create cognitive overload and negatively impact user sentiment and trust.
 
close Don’t Don't reverse the order of the email username and domain (@google.com). The domain should always be to the right of the username.  Usernames can still be written RTL, with the cursor moving to the left. Note this example is not translated to illustrate a common issue with text rendering
 
close Don’t Don’t apply LTR directionality to RTL content because it may scramble word order. To ensure readability across all languages. The content should have both RTL alignment and directionality.
 
Note this example is not translated to illustrate a common issue with text rendering
 
link
 
Copy link Link copied
 
## Icons and symbols
 
link
 
Copy link Link copied
 
In RTL languages, directional UI icons, like back and forward, should be mirrored. However, in Hebrew timelines and media controls on a page should retain left-to-right directionality. The meaning of icons and symbols can vary significantly across cultures.
 
Back and foward icons are mirrored in RTL
 
Send buttons are mirrored in RTL. Help icons are mirrored in some RTL languages, like Urdu and Persian.
 
link
 
Copy link Link copied
 
## Time
 
link
 
Copy link Link copied
 
Linear representations of time are often mirrored in RTL language experiences. Linear progress indicators should move from right to left for most RTL languages, except Hebrew where it should remain LTR. Circular representations of time remain the same.
 
RTL linear progress indicator starts to fill progress from the right
 
Circular progress indicators move clockwise
 
link
 
Copy link Link copied
 
### Media players
 
Media controls for video or audio players are always LTR.
 
In Urdu, controls and progress for media and a podcast title are shown in LTR, while all other content is RTL.
 
link
 
Copy link Link copied
 
### Clock
 
For RTL languages, the directionality of time remains LTR, and clocks still turn clockwise. However, the AM/PM symbols for 12h clocks should be placed to the left. The 24-hour clock is often used in countries where the primary language is not English. Clock icons, circular refresh icons, and progress indicators with arrows pointing clockwise should not be mirrored.
 
24-hour clocks in RTL move clockwise, but mirror elements such as buttons
 
12-hour clocks in RTL move clockwise, but mirror UI elements such as AM/PM and buttons
 
link
 
Copy link Link copied
 
## Canonical layout examples
 
link
 
Copy link Link copied
 
### List-detail
 
The [list-detail](/m3/pages/canonical-layouts/list-detail) layout divides the app window into two side-by-side panes, and is mirrored in RTL.
 
List-detail mirrored for RTL, where text and other elements are aligned to the right and flow from right to left
 
link
 
Copy link Link copied
 
### Feed
 
Use a [feed layout](/m3/pages/canonical-layouts/feed) to arrange content elements like cards in a configurable grid for quick, convenient viewing of a large amount of content. The feed layout is mirrored in RTL.
 
Feed layout mirrored for RTL, where the order of text, grid, and other elements align to the right and flow from right to left
 
link
 
Copy link Link copied
 
### Supporting pane
 
Use the [supporting pane](/m3/pages/canonical-layouts/supporting-pane) layout to organize app content into primary and secondary display areas. The supporting pane layout is mirrored in RTL.
 
Supporting pane to the left of the primary content. Text and other elements within the pane are aligned to the right and flow from right to left.
 
link
 
Copy link Link copied
 
## Component examples
 
link
 
Copy link Link copied
 
### Badges
 
Change the position and alignment of [badges](/m3/pages/badges/specs) for RTL languages.
 
Small badge appears on the top left of the icon
 
Large badge appears on the top left of the icon
 
link
 
Copy link Link copied
 
### Toolbar
 
[Toolbars](/m3/pages/toolbars/guidelines) provide actions related to the current page. For RTL languages, mirror the order of the tools.
 
Mirrored floating toolbar, where the FAB appears on the left of the screen
 
link
 
Copy link Link copied
 
### App bar
 
[App bars](/m3/pages/app-bars/overview) are placed at the top of the screen to help people navigate through a product. Mirror app bar layout in RTL, and flip appropriate icons, such as arrows.
 
RTL center-aligned/small
 
RTL medium flexible
 
RTL large flexible
 
link
 
Copy link Link copied
 
### Navigation drawer
 
[Navigation drawers](/m3/pages/navigation-drawer) that open from the side are always placed on the leading edge of the screen, on the left for LTR languages, and on the right for RTL.
 
RTL navigation drawer, including a mirrored icon for outbox
 
link
 
Copy link Link copied
 
### Navigation rail
 
The [navigation rail](/m3/pages/navigation-rail/guidelines) is placed on the leading edge of the screen, on the left side for LTR, and on the right for RTL.
 
Based on the language being used, a navigation rail is set on a screen’s leading edge. This is the right side for RTL languages, and left side for LTR languages.
 
link
 
Copy link Link copied
 
### Text fields
 
Icons in [text fields](/m3/pages/text-fields/guidelines#5c8a5f07-b1a5-455f-bf76-7ff0d724f6b0) are optional. Leading and trailing icons change their position based on LTR or RTL contexts.
 
Icons, symbols and label text for RTL:
 
Icon signifier
 
Valid or error icon
 
Clear icon
 
Voice input icon
 
Dropdown icon
 
Image
 
link
 
Copy link Link copied
 
### Chips
 
The leading icon of input chips can be an icon, logo, or circular image. The trailing icon is always aligned to the end side of the container. It’s placed on the right for LTR and on the left for RTL.
 
Filter chips shown in an RTL layout. Note this example is not translated to help illustrate mirroring.
 
link
 
Copy link Link copied
 
## Swipe gestures
 
link
 
Copy link Link copied
 
Gestures are the ways people interact with UI elements using touch or body motion. People can navigate horizontally between peer views like tabs, and to complete actions. RTL swiping and gestures should mirror their counterparts in LTR. If an app includes a "delete" icon revealed when swiped from the right for LTR languages, the same should be possible on the left for RTL languages.
 
Swiping reveals additional action in RTL list layout
 
link
 
Copy link Link copied
 
On Android, [predictive back](https://github.com/material-components/material-components-android/blob/master/docs/foundations/PredictiveBack.md) allows people to swipe left or right on the screen to go back or dismiss modal components. RTL predictive back features should mirror those found in a LTR context.
 
pause
 Preview of the result of the gesture for RTL languages
