# Material Design 3 for Compose gets new components and features

> Source: https://m3.material.io/blog/material-3-compose-1-1

Posted by
 Gurupreet Singh , Material Design, Developer Advocate
 The 1.1 release of [Compose Material 3](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary) is here, bringing new components, improved APIs, and many other updates and enhancements you’ve been asking us for. Material Design 3 is the next evolution of Material Design, enabling you to build expressive, spirited, and personal apps. Start using [Material Design 3](https://m3.material.io/) in your production apps today!
 
Note: The terms "Material Design 3", "Material 3", and "M3" are used interchangeably.
 
link
 
Copy link Link copied
 
## New components
 
With the 1.1 release, Material 3 Compose provides all types of components needed to make your production-ready apps, with additions like bottom sheet, date and time pickers, and many others. Let’s dive into some of these additions.
 
Bottom sheets
 
There are two variations of bottom sheet available: standard and modal bottom sheet.
 
The [standard bottom sheet](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#BottomSheetScaffold(kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.material3.BottomSheetScaffoldState,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,kotlin.Function0,kotlin.Boolean,kotlin.Function0,kotlin.Function1,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) is great for use cases where you need to interact with both the bottom sheet and main UI region. You can use the standard bottom sheet with BottomSheetScaffold by providing sheet UI in the sheetContent parameter. You can also provide an optional drag handle to easily interact with the sheet.
 Standard bottom sheet `BottomSheetScaffold (` `sheetPeekHeight = 128. dp ,` `sheetDragHandle = {},` `sheetContent = {` `// Bottom sheet content` `}` `) {` `// Scaffold content` `}` 
The [modal bottom sheet](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalBottomSheet(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.SheetState,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,kotlin.Function0,kotlin.Function1)) overlays the main UI and can be dismissed when users interact outside of the sheet region, similar to a dialog. It provides clear separation from the main UI, making it easy for users to focus on the sheet content.
 Modal bottom sheet 
You can use the modal bottom sheet as a standalone component and invoke it using `ModalBottomSheetState` . The component also provides `onDismissRequest` function to be invoked on dismiss.
 ​ x
 
`val modalBottomSheetState = rememberModalBottomSheetState ()` `​` `ModalBottomSheet (` `onDismissRequest = { /*dismiss request*/ },` `sheetState = modalBottomSheetState ,` `dragHandle = { BottomSheetDefaults . DragHandle () },` `) {` `// Sheet content` `}` 
Date pickers
 
The 1.1 release also brings brand new date selection components: [`DatePicker()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DatePicker(androidx.compose.material3.DatePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.DatePickerFormatter,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.DatePickerColors)) and [`DateRangePicker()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DateRangePicker(androidx.compose.material3.DateRangePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.DatePickerFormatter,kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Boolean,androidx.compose.material3.DatePickerColors)) .
 `xxxxxxxxxx`
 
`val datePickerState = rememberDatePickerState ()` `DatePicker ( state = datePickerState )` `​` `val dateRangePickerState = rememberDateRangePickerState ()` `DateRangePicker ( state = dateRangePickerState )` `​` `// Date picker with initial input display mode` `val datePickerState = rememberDatePickerState (` `initialDisplayMode = DisplayMode . Input` `)` `DatePicker ( state = datePickerState )` 
Both the date picker and date range picker support date input mode by updating the `initalDisplayMode` parameter to input type, which sets the initial display mode to input type. The user can switch back to default selection mode by toggle.
 Left: Date picker in input mode, Middle: Date picker in display mode, Right: Date range picker 
Compose Material 3 also provides a [`DatePickerDialog()`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DatePickerDialog(kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.material3.DatePickerColors,androidx.compose.ui.window.DialogProperties,kotlin.Function1)) composable to show a date picker in  a dialog, with the option to confirm or dismiss it.
 `xxxxxxxxxx`
 
`val datePickerState = rememberDatePickerState ()` `val showDialog = rememberSaveable { mutableStateOf ( false ) }` `if ( showDialog . value ) {` `DatePickerDialog (` `onDismissRequest = { showDialog . value = false },` `confirmButton = {` `TextButton ( onClick = { showDialog . value = false }) {` `Text ( "Ok" )` `}` `},` `dismissButton = {` `TextButton ( onClick = { showDialog . value = false }) {` `Text ( "Cancel" )` `}` `}` `) {` `DatePicker ( state = datePickerState )` `}` `}` Date picker dialog switching between picker and input display mode 
Time pickers
 
Compose Material 3 also includes new time picker components for choosing the desired time.
 
There are two versions available: one with a horizontal layout in which users enter the time using the keyboard, and another with a vertical layout in which users can also use a slide dial to select the time.
 Left: Time picker in vertical layout, Right: Time picker in horizontal layout 
Compose provides a single [`TimePicker`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TimePicker(androidx.compose.material3.TimePickerState,androidx.compose.ui.Modifier,androidx.compose.material3.TimePickerColors,androidx.compose.material3.TimePickerLayoutType)) composable function, where you can define the layoutType parameter to choose between a horizontal or vertical layout.
 `xxxxxxxxxx`
 
`val timePickerStateHorizontal = rememberTimePickerState ()` `TimePicker (` `state = timePickerStateHorizontal ,` `layoutType = TimePickerLayoutType . Horizontal` `)` `​` `val timePickerStateVertical = rememberTimePickerState ()` `TimePicker (` `state = timePickerStateVertical ,` `layoutType = TimePickerLayoutType . Vertical` `)` 
Search bars
 
The 1.1 release brings new search bar components, which provide users the ability to search queries and display dynamic search results.
 Search bar and search result view 
Material 3 provides two options, [search bar](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SearchBar(kotlin.String,kotlin.Function1,kotlin.Function1,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SearchBarColors,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) and [docked search bar](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DockedSearchBar(kotlin.String,kotlin.Function1,kotlin.Function1,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SearchBarColors,androidx.compose.ui.unit.Dp,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) , to give you the flexibility to choose the right fit for your product.
 
When active, the search bar expands into a search view that displays dynamic results. The active search bar takes up all available space to display the results, and can also expand to full screen.
 `xxxxxxxxxx`
 
`var text by rememberSaveable { mutableStateOf ( "" ) }` `var active by rememberSaveable { mutableStateOf ( false ) }` `SearchBar (` `query = text ,` `onQueryChange = { text = it },` `onSearch = { active = false },` `active = active ,` `onActiveChange = {` `active = it` `}` `) {` `// Search result shown when active` `LazyColumn (` `modifier = Modifier . fillMaxWidth (),` `contentPadding = PaddingValues ( 16. dp ),` `verticalArrangement = Arrangement . spacedBy ( 4. dp )` `) {` `items ( 4 ) { idx ->` `// Search result` `​` `}` `}` `}` 
The docked search bar is great for medium to large devices where the search view doesn’t need to take up all the screen space and results can be shown in a docked view.
 Docked search bar and search view on a tablet 
The implementation of the docked search bar is similar to the search bar to keep both the components consistent.
 `xxxxxxxxxx`
 
`var text by rememberSaveable { mutableStateOf ( "" ) }` `var active by rememberSaveable { mutableStateOf ( false ) }` `​` `DockedSearchBar (` `query = text ,` `onQueryChange = { text = it },` `onSearch = { active = false },` `active = active ,` `onActiveChange = { active = it },` `) {` `LazyColumn (` `modifier = Modifier . fillMaxWidth (),` `contentPadding = PaddingValues ( 16. dp ),` `verticalArrangement = Arrangement . spacedBy ( 4. dp )` `) {` `// Search result content` `}` `}` 
Tooltips
 
Tooltips are another new addition to the latest 1.1 release. Tooltips are informative text labels that provide additional context to a button or other UI element.
 
Material 3 provides two types of tooltips: [plain tooltip](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#PlainTooltipBox(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.PlainTooltipState,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) and [rich tooltip](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#RichTooltipBox(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.RichTooltipState,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.material3.RichTooltipColors,kotlin.Function1)) .
 
Plain tooltips briefly describe a UI element. Plain tooltips are great for labeling UI elements with no text, like icon-only and field elements.
 Plain tooltip on an icon button 
You can use the `PlainTooltipBox()` composable to add a plain tooltip. To apply the tooltip to any component, wrap the component with the tooltip composable and add `Modifier.tooltipAnchor()` to the component’s modifier.
 `xxxxxxxxxx`
 
`PlainTooltipBox (` `tooltip = { Text ( "Present now" ) }` `) {` `IconButton (` `onClick = { /* Icon button's click event */ },` `modifier = Modifier . tooltipTrigger ()` `) {` `Icon (` `imageVector = Icons . Filled . FilePresent ,` `contentDescription = "Present now"` `)` `}` `}` 
Rich tooltips are great for longer texts like definitions or explanations. Rich tooltips provide additional context to a UI element and can include a button or hyperlink.
 Rich tooltip with description and text button as action 
You can have either persistent or non-persistent rich tooltips by providing the isPersistent parameter to `RichTooltipState()` . To dismiss persistent tooltips, you need to tap outside the tooltip area or invoke the dismiss action on tooltip state.
 
Non-persistent tooltips will be dismissed automatically after a short duration.
 
To add rich tooltips, you can use the `RichTooltipBox()` composable and modify tooltip state to control the visibility of the tooltip.
 `xxxxxxxxxx`
 
`val tooltipState = remember { RichTooltipState () }` `val scope = rememberCoroutineScope ()` `RichTooltipBox (` `title = { Text ( "Add others" ) },` `action = {` `TextButton (` `onClick = { scope . launch { tooltipState . dismiss () } }` `) { Text ( "Learn More" ) }` `},` `text = { Text ( "Share this collection with friends..." ) },` `tooltipState = tooltipState` `) {` `IconButton (` `onClick = { /* Icon button's click event */ },` `modifier = Modifier . tooltipTrigger ()` `) {` `Icon (` `imageVector = Icons . Filled . People ,` `contentDescription = "Add others"` `)` `}` `}` 
link
 
Copy link Link copied
 
## Stable components
 
With the 1.1 release, many key components have graduated from the experimental stage and are ready for production apps.
 
Components like Scaffold, Surface, Navigation drawers, and many others are building blocks of your apps, and you can now be assured that they will not have any major breaking changes.
 Navigation rail and Navigation drawer 
When updating to the latest release, you can remove the `@OptIn(ExperimentalMaterial3Api::class)` annotation from the stable components.
 
link
 
Copy link Link copied
 
## Motion and animations
 
Material 3 components in Compose come with built-in motion and animations to provide interactive and expressive experiences to users.
 
Components also provide behavior control to give you flexibility in choosing the animation you need for your product.
 
Top app bar motion and animation
 
For top app bars, you can choose between pinned scroll behavior or enter always scroll behavior.
 
In pinned scroll behavior, the top app bar is always pinned at the top, but changes its container color when content is scrolled.
 Top app bar with pinned scroll behavior 
To add the behavior to the app bar, define a scroll behavior `TopAppBarDefaults.pinnedScrollBehavior()` that links to the scaffold’s `Modifier.nestedScroll()` to listen to the scrolling changes.
 `xxxxxxxxxx`
 
`@ OptIn ( ExperimentalMaterial3Api :: class )` `@ Composable` `fun PinnedTopAppBar () {` `val scrollBehavior = TopAppBarDefaults . pinnedScrollBehavior ()` `Scaffold (` `modifier = Modifier . nestedScroll ( scrollBehavior . nestedScrollConnection ),` `topBar = {` `TopAppBar (` `scrollBehavior = scrollBehavior` `)` `},` `content = { /* Scrollable content */ }` `)` `}` 
In the enter always scroll behavior, the top app bar disappears when the user scrolls through the content, and shows up again when the user scrolls down.
 Top app bar with enter-always scroll behavior. 
To achieve the enter always behavior, define a scroll behavior `TopAppBarDefaults.enterAlwaysScrollBehavior()` that links to the scaffold’s `Modifier.nestedScroll()` to listen to the scrolling changes.
 `xxxxxxxxxx`
 
`@ Composable` `fun EnterAlwaysTopAppBar () {` `val scrollBehavior = TopAppBarDefaults . enterAlwaysScrollBehavior ()` `Scaffold (` `modifier = Modifier . nestedScroll ( scrollBehavior . nestedScrollConnection ),` `topBar = {` `TopAppBar (` `scrollBehavior = scrollBehavior` `)` `},` `content = { /* Scrollable content */ }` `)` `}` 
Material 3 provides all these animations as part of the components, with easy ways to customize them for your project.
 
link
 
Copy link Link copied
 
## Resources
 
With the latest 1.1 release, Compose Material 3 is ready for production apps. Check out the resources below for more information:
 
Fully Material 3 and Compose sample: [Reply 💌](https://github.com/android/compose-samples/tree/main/Reply)
 
[Theming in Compose](https://developer.android.com/codelabs/jetpack-compose-theming#0) codelab
 
The [Material 3 guidance](https://developer.android.com/jetpack/compose/themes/material3) to start adding Material 3 to your apps
 
The Material 2 to Material 3 [migration guide](https://developer.android.com/jetpack/compose/themes/material2-material3)
 
The [Jetpack Compose Samples GitHub repository](https://github.com/android/compose-samples) , where you’ll find a variety of up-to-date samples using Material 3
 
The Compose community on [StackOverflow](https://stackoverflow.com/questions/tagged/material-design) and the [Kotlin Slack group](http://slack.kotlinlang.org/)
 
The [bug tracker](https://issuetracker.google.com/issues/new?component=742043) , where you can report an issue and track feature request
