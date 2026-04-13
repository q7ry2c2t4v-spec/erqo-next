# Jetpack Compose: Now in Beta

> Source: https://m3.material.io/blog/jetpack-compose-beta

Posted by
 Nick Rout , Material Developer Advocate
 Today marks the first [beta release](http://goo.gle/Compose-Beta-Blog) of [Jetpack Compose](https://developer.android.com/jetpack/compose) , Android’s modern, declarative toolkit designed to simplify and accelerate UI development. With Jetpack Compose, you can quickly bring your apps to life with less code, powerful tools, intuitive Kotlin APIs, and built-in support for Material Design, dark theme, animations, and more.
 
link
 
Copy link Link copied
 
## Compose Material
 
Jetpack Compose offers an implementation of Material Design and [provides](https://developer.android.com/jetpack/androidx/releases/compose-material) all the components you need to create beautiful apps, following the guidance described at [material.io.](https://material.io)
 `// Add dependency in module build.gradle` `implementation “androidx . compose . material : material : $compose_version”` 
link
 
Copy link Link copied
 
## Material Theming
 
Jetpack Compose implements [Material Theming](https://material.io/design/material-theming/overview.html) and supports [dark theme](https://material.io/design/color/dark-theme.html) by default. You can customize color, typography, and shape theming values to fit your product's brand, and get access to convenient functions for working with [system dark theme](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) (like [`isSystemInDarkTheme`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#issystemindarktheme) , [`lightColors`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#lightcolors) , and [`darkColors`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#darkcolors) ).
 ​ x
 
`// In Colors.kt` `​` `val Navy500 = Color ( 0xFF64869B )` `val Navy700 = Color ( 0xFF37596D )` `val Navy900 = Color ( 0xFF073042 )` `val Green300 = Color ( 0xFF3DDC84 )` `val Green900 = Color ( 0xFF00A956 )` `​` `val LightColors = lightColors (` `primary = Navy700 ,` `primaryVariant = Navy900 ,` `secondary = Green300 ,` `secondaryVariant = Green900` `// Using default values for onPrimary, surface, error, etc.` `)` `​` `val DarkColors = darkColors (` `primary = Navy500 ,` `primaryVariant = Navy900 ,` `secondary = Green300` `// secondaryVariant == secondary in dark theme` `)` `xxxxxxxxxx`
 
`// In Type.kt` `​` `val H6 = TextStyle (` `fontWeight = FontWeight . Medium ,` `fontSize = 20. sp ,` `letterSpacing = 0.15 . sp` `)` `val Body2 = TextStyle (` `fontWeight = FontWeight . Normal ,` `fontSize = 14. sp ,` `letterSpacing = 0.25 . sp` `)` `val Button = TextStyle (` `fontWeight = FontWeight . Medium ,` `fontSize = 14. sp ,` `letterSpacing = 1.25 . sp` `)` `​` `val Typography = Typography (` `h6 = H6 ,` `body2 = Body2 ,` `button = Button ,` `defaultFontFamily = FontFamily ( Font ( R . font . roboto_mono ))` `// Using default values for subtitle1, caption, etc.` `)` `xxxxxxxxxx`
 
`// In Shape.kt` `​` `val Shapes = Shapes (` `small = RoundedCornerShape ( percent = 50 ),` `medium = RoundedCornerShape ( 0 f ),` `large = CutCornerShape (` `topStart = 16. dp ,` `topEnd = 0. dp ,` `bottomStart = 16. dp ,` `bottomEnd = 0. dp` `)` `)` `xxxxxxxxxx`
 
`// In Theme.kt` `​` `@ Composable` `fun MyTheme (` `darkTheme : Boolean = isSystemInDarkTheme (),` `content : @ Composable () -> Unit` `) {` `val colors = if ( darkTheme ) {` `DarkColors` `} else {` `LightColors` `}` `​` `MaterialTheme (` `colors = colors ,` `typography = Typography ,` `shapes = Shapes ,` `content = content` `)` `}` 
When creating new screens in Compose, you should ensure that you apply your custom `MaterialTheme` before any UI-emitting Material composables. The Material components ( `Button` , `Checkbox` , `BottomNavigation` , etc.) depend on a `MaterialTheme` being in place and their behavior is undefined without it.
 `xxxxxxxxxx`
 
`class MyActivity : ComponentActivity () {` `override fun onCreate ( savedInstanceState : Bundle ? ) {` `super . onCreate ( savedInstanceState )` `​` `setContent {` `MyTheme {` `// Material components like Button, Checkbox, Card, etc.` `}` `}` `}` `}` 
Check out the [Theming in Compose guide](https://developer.android.com/jetpack/compose/themes) for more information, and try the [Jetpack Compose Theming codelab](https://developer.android.com/codelabs/jetpack-compose-theming) .
 
link
 
Copy link Link copied
 
## Material Components
 
Jetpack Compose offers implementations of [Material Components](https://material.io/components) . See the table below for composables available in the beta release, or check out the full list in the [API reference](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary) .
 
[App bars: bottom](https://material.io/components/app-bars-bottom) [`BottomAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#bottomappbar) [App bars: top](https://material.io/components/app-bars-top) [`TopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#topappbar) [Backdrop](https://material.io/components/backdrop) [`Backdrop`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#backdropscaffold) [Banners](https://material.io/components/banners) Not available yet [Bottom navigation](https://material.io/components/bottom-navigation) [`BottomNavigation`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#bottomnavigation) [Buttons](https://material.io/components/buttons) [`Button`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#button) [`OutlinedButton`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#outlinedbutton) [`TextButton`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#textbutton) [Buttons: floating action button](https://material.io/components/buttons-floating-action-button) [`FloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#floatingactionbutton) [`ExtendedFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#extendedfloatingactionbutton) [Cards](https://material.io/components/cards) [`Card`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#card) [Checkboxes](https://material.io/components/checkboxes) [`Checkbox`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#checkbox) [`TriStateCheckbox`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#tristatecheckbox) [Chips](https://material.io/components/chips) Not available yet [Data tables](https://material.io/components/data-tables) Not available yet [Date pickers](https://material.io/components/date-pickers) Not available yet [Dialogs](https://material.io/components/dialogs) [`AlertDialog`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#alertdialog) [Dividers](https://material.io/components/dividers) [`Divider`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#divider) [Image lists](https://material.io/components/image-lists) Not available yet [Lists](https://material.io/components/lists) [`ListItem`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#listitem) [Menus](https://material.io/components/menus) [`DropdownMenu`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#dropdownmenu) [`DropdownMenuItem`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#dropdownmenuitem) [Navigation drawer](https://material.io/components/navigation-drawer) [`ModalDrawerLayout`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#modaldrawerlayout) [`BottomDrawerLayout`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#bottomdrawerlayout) [Navigation rail](https://material.io/components/navigation-rail) Not available yet [Progress indicators](https://material.io/components/progress-indicators) [`CircularProgressIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#circularprogressindicator) [`LinearProgressIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#linearprogressindicator) [Radio buttons](https://material.io/components/radio-buttons) [`RadioButton`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#radiobutton) [Sheets: bottom](https://material.io/components/sheets-bottom) [`BottomSheetScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#bottomsheetscaffold) [`ModalBottomSheetLayout`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#modalbottomsheetlayout) [Sheets: side](https://material.io/components/sheets-side) Not available yet [Sliders](https://material.io/components/sliders) [`Slider`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#slider) [Snackbars](https://material.io/components/snackbars) [`Snackbar`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#snackbar) [`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#scaffold) [Switches](https://material.io/components/switches) [`Switch`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#switch) [Tabs](https://material.io/components/tabs) `[Tab](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#tab)` [`TabRow`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#tabrow) [`ScrollableTabRow`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#scrollabletabrow) [Text fields](https://material.io/components/text-fields) [`TextField`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#textfield) [`OutlinedTextField`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#outlinedtextfield) [Time pickers](https://material.io/components/time-pickers) Not available yet [Tooltips](https://material.io/components/tooltips) Not available yet
 
These components can be combined—using layouts and composables like `Scaffold` —as the building blocks for beautiful UIs.
 `xxxxxxxxxx`
 
`val scaffoldState = rememberScaffoldState ()` `val scope = rememberCoroutineScope ()` `Scaffold (` `scaffoldState = scaffoldState ,` `drawerContent = { Text ( "Drawer content" ) },` `topBar = {` `TopAppBar (` `title = { Text ( "Top app bar" ) },` `navigationIcon = {` `IconButton (` `onClick = {` `scope . launch { scaffoldState . drawerState . open () }` `}` `) {` `Icon ( Icons . Filled . Menu , contentDescription = stringResource ( R . string . label_nav_menu ))` `}` `}` `)` `},` `floatingActionButtonPosition = FabPosition . End ,` `floatingActionButton = {` `ExtendedFloatingActionButton (` `text = { Text ( "Extended FAB" ) },` `onClick = { /* Handle FAB click */ }` `)` `},` `content = { innerPadding ->` `LazyColumn ( contentPadding = innerPadding ) {` `items ( count = 20 ) {` `Card (` `modifier = Modifier` `. fillMaxWidth ()` `. wrapContentHeight ()` `. padding ( 16. dp )` `) { /* Card content */ }` `}` `}` `}` `)` 
Check out the [Layouts in Compose guide](https://developer.android.com/jetpack/compose/layout) for more information.
 
link
 
Copy link Link copied
 
## Dark theme
 
Material composables that make use of a `Surface` (like `Card` , `TopAppBar` , etc.) automatically include dark theme properties like desaturated colors for accessibility, elevation overlays, and limited color accents. You can also incorporate these in custom scenarios.
 `xxxxxxxxxx`
 
`// Background color of components that are primary in light theme, and surface in dark theme` `val primarySurface = MaterialTheme . colors . primarySurface` `​` `// Utility for applying elevation overlays to colors` `val elevationOverlay = LocalElevationOverlay . current` `val color = MaterialTheme . colors . surface` `val elevation = 4. dp` `val overlaidColor = elevationOverlay . apply ( color , elevation )` 
link
 
Copy link Link copied
 
## Material Icons
 
Jetpack Compose also provides a convenient means of using icons listed in the [Material Icons tool](https://material.io/resources/icons) , including all icon styles—filled, outlined, rounded, two-tone, and sharp. With this artifact, you can use icons directly, without the need to download SVGs and convert them to `VectorDrawable` s in Android Studio.
 `xxxxxxxxxx`
 
`// Add dependency in module build.gradle` `implementation “androidx . compose . material : material - icons - extended : $compose_version”` `xxxxxxxxxx`
 
`Icon ( Icons . Default . Add ) // Default == Filled` `Icon ( Icons . Outlined . Notifications )` `Icon ( Icons . Rounded . ArrowForward )` `Icon ( Icons . TwoTone . Menu )` `Icon (` `Icons . Sharp . Edit ,` `tint = MaterialTheme . colors . primary` `)` 
link
 
Copy link Link copied
 
## Interoperability
 
Jetpack Compose is designed to work with Android Views. If you're building a new app, the best option might be to implement your entire UI with Compose. But if you're modifying an existing app, you might not want to migrate your app straight away. Instead, you can combine Compose with your existing UI design and adopt it at your own pace.
 
If you’re using [Material Components for Android](https://github.com/material-components/material-components-android) in your app—in particular [Material Theming](https://material.io/develop/android/theming/theming-overview) —the [MDC-Android Compose Theme Adapter library](https://github.com/material-components/material-components-android-compose-theme-adapter) allows you to easily re-use the color, typography and shape definitions from your existing XML themes, from within your composables, so you don’t need to declare them again and have a single source of truth.
 `xxxxxxxxxx`
 
`// Add dependency in module build.gradle` `implementation “com . google . android . material : compose - theme - adapter : $compose_version”` `xxxxxxxxxx`
 
`class MyActivity : AppCompatActivity () {` `override fun onCreate ( savedInstanceState : Bundle ? ) {` `super . onCreate ( savedInstanceState )` `​` `setContent {` `// We use the MdcTheme composeable instead of MaterialTheme` `// This extracts Material Theming definitions from the current Context` `MdcTheme {` `MyComposable ( /*...*/ )` `}` `}` `}` `}` 
If you’re using [AppCompat](https://developer.android.com/jetpack/androidx/releases/appcompat) , you can access similar functionality by using the `AppCompatTheme` composable from the [AppCompat Compose Theme Adapter library](https://github.com/chrisbanes/accompanist/tree/main/appcompat-theme) .
 `xxxxxxxxxx`
 
`// Add dependency in module build.gradle` `implementation "dev.chrisbanes.accompanist:accompanist-appcompat-theme:$accompanist_version"` 
Check out the [Compose interoperability guide](https://developer.android.com/jetpack/compose/interop) for more information.
 
link
 
Copy link Link copied
 
## Resources
 
With Jetpack Compose reaching beta, it’s a great time to start learning all about it and get ready to adopt it in your apps. Check out the resources below to get started.
 
Develop knowledge and skills at your own pace with the [Jetpack Compose Pathway](https://developer.android.com/courses/pathways/compose) , through sequential learning experiences that include articles, codelabs, quizzes, and videos.
 
Visit the [Jetpack Compose Samples GitHub repository](https://github.com/android/compose-samples) , where you’ll find a variety of up-to-date samples including Material Studies like [Owl](https://github.com/android/compose-samples/blob/main/Owl) , [Crane](https://github.com/android/compose-samples/blob/main/Crane) , and [Rally](https://github.com/android/compose-samples/blob/main/Rally) .
 
Get setup using the [Android Studio with Jetpack Compose guide](https://developer.android.com/jetpack/compose/setup) .
 
View the [Converting an existing app screen to Jetpack Compose video](https://www.youtube.com/watch?v=7alO6TQDWQQ) on the Material Design YouTube channel.
 
Join the Compose community on [StackOverflow](https://stackoverflow.com/questions/tagged/android-jetpack-compose) and the [Kotlin Slack group](http://slack.kotlinlang.org/) .
 
Report an issue and track bugs on the [bug tracker](https://issuetracker.google.com/issues/new?component=612128) .
