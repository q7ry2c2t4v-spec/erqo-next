# Date pickers – Material Design 3

> Source: https://m3.material.io/components/date-pickers/guidelines

link
 
Copy link Link copied
 
Docked date picker on desktop
 
link
 
Copy link Link copied
 
## Usage
 
link
 
Copy link Link copied
 
Date pickers let people select a date or range of dates. They should be suitable for the context in which they appear. Date pickers can be embedded into:
 
Dialogs Dialogs provide important prompts in a user flow. [More on dailogs](/m3/pages/dialogs/overview) on compact [window sizes](/m3/pages/applying-layout/window-size-classes#2bb70e22-d09b-4b73-9c9f-9ef60311ccc8) like mobile
 
Text field Text fields let users enter text into a UI. [More on text fields](/m3/pages/text-fields/overview) drop-downs on medium and expanded window sizes Window widths 840dp to 1199dp, such as a tablet or foldable in landscape orientation, or desktop. [More on expanded window size class](/m3/pages/applying-layout/expanded) like tablet and desktop
 
Date picker dialog on mobile
 
Date picker text field dropdown on desktop
 
link
 
Copy link Link copied
 
There are three variants of date pickers:
 
Docked date picker
 
Modal date picker
 
Modal date input
 
1. Docked date picker
 
link
 
Copy link Link copied
 
2. Modal date picker
 
3. Modal date input
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
### Docked date picker
 
link
 
Copy link Link copied
 
Text field
 
Menu button
 
Icon button
 
Label text
 
Menu
 
Text buttons
 
Container
 
1. Text field 2. Menu button 3. Menu
 
link
 
Copy link Link copied
 
### Modal date picker
 
link
 
Copy link Link copied
 
Headline
 
Supporting text
 
Container
 
Icon button
 
Previous/next month buttons
 
Day of week labels
 
Today’s date
 
Unselected date
 
Text buttons
 
Selected date
 
Menu button
 
Divider
 
Headline
 
Supporting text
 
Container
 
Icon button
 
Unselected year
 
Selected year
 
Text buttons
 
Divider
 
Menu button
 
link
 
Copy link Link copied
 
### Modal date input
 
link
 
Copy link Link copied
 
1. Headline 2. Supporting text 3. Container 4. Icon button 5. Date input 6. Text buttons 7. Divider
 
link
 
Copy link Link copied
 
### Full-screen date picker
 
link
 
Copy link Link copied
 
1. Headline 2. Supporting text 3. Icon button 4. Container 5. Text button 6. Icon button 7. Divider 8. Day of week labels 9. Today’s date 10. Selected date range 11. Unselected date 12. Text buttons 13. Selected date range start date 14. Month label
 
link
 
Copy link Link copied
 
## Docked date picker
 
link
 
Copy link Link copied
 
### Usage
 
Docked date pickers allow the selection Selection lets users choose specific items to act on. [More on selection](/m3/pages/selection) of a specific date and year. The docked date picker displays a date input Inputs are devices that provide interactive control of an app. Common inputs are a mouse, keyboard, and touchpad. field by default, and a dropdown calendar appears when the user taps on the input field. Either form of date entry can be interacted with. Docked date pickers are ideal for navigating dates in both the near future or past and the distant future or past, as they provide multiple ways to select dates.
 
Docked date picker on desktop
 
link
 
Copy link Link copied
 
### Behavior
 
Dates can be added by using a keyboard or by navigating the calendar UI; both options are immediately available when the docked date picker is accessed.
 
Docked date picker
 
link
 
Copy link Link copied
 
pause
 Docked date pickers adjust size dynamically
 
pause
 The year selection menu replaces the calendar view
 
link
 
Copy link Link copied
 
### Month selection
 
Month selection Selection lets users choose specific items to act on. [More on selection](/m3/pages/selection) can be navigated with the corresponding back and next arrows or by tapping the dropdown menu.
 
Docked date picker month selection
 
link
 
Copy link Link copied
 
### Year selection
 
Year selection can be navigated with the corresponding back and next arrows or by tapping the dropdown menu.
 
Docked date picker year selection
 
link
 
Copy link Link copied
 
## Modal date picker
 
link
 
Copy link Link copied
 
### Behavior
 
Modal date pickers navigate across dates in several ways:
 
To navigate across months, swipe horizontally
 
To navigate across years, scroll vertically
 
To access the year picker, tap the year
 
Don’t use a modal date picker to prompt for dates in the distant past or future, such as a date of birth. In these cases, use a modal input picker or a docked date picker instead.
 
link
 
Copy link Link copied
 
pause
 To navigate across months, swipe horizontally
 
pause
 To navigate across years, tap the year picker and scroll vertically
 
link
 
Copy link Link copied
 
### Date range selection
 
Date range selection provides a start and end date. Common use cases include:
 
Booking a flight
 
Reserving a hotel
 
Modal date pickers navigate across date ranges in several ways:
 
To select a range of dates, tap the start and end dates on the calendar
 
T o navigate across months, scroll vertically
 
link
 
Copy link Link copied
 
pause
 Modal date range picker
 
pause
 Modal date range picker with vertical scroll
 
link
 
Copy link Link copied
 
## Modal date input
 
link
 
Copy link Link copied
 
### Usage
 
Modal date inputs allow the manual entry of dates using the numbers on a keyboard. People can input a date or a range of dates in a dialog.
 
Modal date with manual input
 
link
 
Copy link Link copied
 
check Do For dates that don’t require a calendar view, the modal date input can be the default view
 
check Do Alternatively, a text field with appropriate hint text can prompt for dates, such as in a form
 
link
 
Copy link Link copied
 
### Behavior
 
link
 
Copy link Link copied
 
You can swap between the modal date picker Modal date pickers extend full-screen. They're often used for selecting a date range. [More on modal date pickers](/m3/pages/date-pickers/guidelines#ced55f72-28b5-4f5d-a347-fa38214ef2d4) and modal date input Modal date inputs allow the manual entry of dates using the numbers on a keyboard. They're often used in compact layouts. [More on modal date inputs](/m3/pages/date-pickers/guidelines#d91ce7bc-dbc7-43e3-a802-152f2f9c892a) using the edit or calendar icon.
 
link
 
Copy link Link copied
 
pause
 Switching from a modal date picker to a mobile date input for selecting ranges
 
pause
 Switching from a modal date picker to a modal date input for selecting a single date
 
link
 
Copy link Link copied
 
### Compact window size
 
On compact [window sizes](/m3/pages/applying-layout/window-size-classes#2bb70e22-d09b-4b73-9c9f-9ef60311ccc8) , such as mobile, a full-screen modal date picker Modal date pickers extend full-screen. They're often used for selecting a date range. [More on modal date picker](https://m3.material.io/m3/pages/date-pickers/guidelines#ced55f72-28b5-4f5d-a347-fa38214ef2d4) is recommended to increase readability and touch target size. It can cover the entire screen.
 
A full-screen modal date picker on mobile
 
link
 
Copy link Link copied
 
### Medium and expanded window sizes
 
The docked date picker works best for medium and expanded window sizes. It displays a date input field by default, and a dropdown calendar appears when a person taps on the input field. A person can interact with either form of date entry. Docked date pickers are ideal for navigating dates in both the near future or past, and in the distant future or past, as they provide multiple ways to select dates.
 
A docked date picker with a full calendar view is best used on larger devices
 
link
 
Copy link Link copied
 
### Selection
 
Selection is indicated through color, drawing visual attention. In date ranges, start and end dates are selected, while dates in-between appear connected with a subtle highlight.
 
pause
 Differences between selected the selected date range (August 17–23) and today's date (August 5) are shown through color and fill
 
link
 
Copy link Link copied
 
### Appearing and disappearing
 
Like other kinds of dialogs, modal date pickers use an enter and exit transition pattern to appear on the screen. To exit a date picker, the input can either be confirmed ( OK ) or dismissed ( Cancel ). Interacting outside of the dialog will also dismiss the time picker Time pickers help users select and set a specific time. . Unless one of these actions is taken, a time picker will continue to retain focus. Mobile full-screen pickers also have an additional close affordance (x) icon button and Save confirmation. Docked date pickers appear just below the input field.
 
link
 
Copy link Link copied
 
pause
 Modal date pickers can be dismissed through interacting with content outside the dialog, or with the action buttons in the lower right
 
pause
 Interacting with the input for a docked date picker makes the calendar view appear below
 
link
 
Copy link Link copied
 
### Responsive layout
 
The sizing of the docked and modal date picker components don’t scale responsively to different window sizes.
 
close Don’t Don’t scale the date picker responsively to a larger size
