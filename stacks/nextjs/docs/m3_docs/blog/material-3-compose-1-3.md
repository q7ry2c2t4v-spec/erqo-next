# Material Design 3 for Compose version 1.3

> Source: https://m3.material.io/blog/material-3-compose-1-3

Posted by
 Rebecca Franks , Developer Relations Engineer, Android
 Version 1.3 of the Compose Material 3 Components is here and with it come a few changes for Material Components and theming!
 
Version 1.3 introduces:
 
Behavior changes for ripple APIs for performance improvements
 
A brand-new component: Carousel
 
Built-in predictive back support for some Material Components.
 
Color token alignment to be more colorful while still having accessible color contrast
 
Previously experimental APIs have been stabilized
 
link
 
Copy link Link copied
 
## Breaking API changes
 
To improve performance, the Material components have been migrated to use the new Ripple APIs, and no longer query `RippleTheme` . If you have set a custom ripple in your applications, you will need to perform a migration to use the new APIs as Material will no longer query `LocalRippleTheme` . See the “ [Migrate to Indication and Ripple APIs](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/migrate-indication-ripple) ” documentation for more information about how to migrate your ripple theme.
 
link
 
Copy link Link copied
 
## Carousel component
 
pause
 
Material 1.3 introduces two experimental versions of the [Material 3 Carousel](https://m3.material.io/components/carousel/overview) - `HorizontalMultiBrowseCarousel` and `HorizontalUncontainedCarousel` .
 
The [`HorizontalMultiBrowseCarousel`](https://developer.android.com/reference/kotlin/androidx/compose/material3/carousel/package-summary#HorizontalMultiBrowseCarousel(androidx.compose.material3.carousel.CarouselState,androidx.compose.ui.unit.Dp,androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.foundation.gestures.TargetedFlingBehavior,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.PaddingValues,kotlin.Function2)) shows at least one large, medium, and small carousel item.
 
pause
 
The [`HorizontalUncontainedCarousel`](https://developer.android.com/reference/kotlin/androidx/compose/material3/carousel/package-summary#HorizontalUncontainedCarousel(androidx.compose.material3.carousel.CarouselState,androidx.compose.ui.unit.Dp,androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.foundation.gestures.TargetedFlingBehavior,androidx.compose.foundation.layout.PaddingValues,kotlin.Function2)) displays its items at a given size and one item at the end that peeks in to show that there are more items in the list.
 
Similar to using the `HorizontalPager` , the Carousel applies a few design specifications on top of the `Pager` , such as the parallax effect for item content and how the items on each end should size themselves. An example of using the `HorizontalUncontainedCarousel` can be found below:
 ​ x
 
`@ OptIn ( ExperimentalMaterial3Api :: class )` `@ Preview` `@ Composable` `private fun CarouselExamples () {` `data class CarouselItem (` `val id : Int ,` `@ DrawableRes val imageResId : Int ,` `val contentDescription : String` `)` `​` `val items = remember {` `listOf (` `CarouselItem ( 0 , R . drawable . cupcake , "cupcake" ),` `CarouselItem ( 1 , R . drawable . donut , "donut" ),` `CarouselItem ( 2 , R . drawable . eclair , "eclair" ),` `CarouselItem ( 3 , R . drawable . froyo , "froyo" ),` `CarouselItem ( 4 , R . drawable . gingerbread , "gingerbread" ),` `)` `}` `​` `HorizontalUncontainedCarousel (` `state = rememberCarouselState { items . count () },` `modifier = Modifier . fillMaxWidth ()` `. wrapContentHeight ()` `. padding ( top = 16. dp , bottom = 16. dp ),` `itemWidth = 186. dp ,` `itemSpacing = 8. dp ,` `contentPadding = PaddingValues ( start = 16. dp )` `) { i ->` `val item = items [ i ]` `Image (` `modifier = Modifier . height ( 205. dp )` `. maskClip ( MaterialTheme . shapes . extraLarge ),` `painter = painterResource ( id = item . imageResId ),` `contentDescription = item . contentDescription ,` `contentScale = ContentScale . Crop` `)` `}` `}` 
pause
 
As part of the Carousel component, we’ve added two new modifiers to `CarouselItemScope` - [maskClip](https://developer.android.com/reference/kotlin/androidx/compose/material3/carousel/CarouselItemScope#(androidx.compose.ui.Modifier).maskClip(androidx.compose.ui.graphics.Shape)) and [maskBorder](https://developer.android.com/reference/kotlin/androidx/compose/material3/carousel/CarouselItemScope#(androidx.compose.ui.Modifier).maskBorder(androidx.compose.foundation.BorderStroke,androidx.compose.ui.graphics.Shape)) - to easily add a shape and border to any carousel item. This is needed over the regular `clip` and `border` modifiers to be able to apply it on a container level as the item moves inside the Carousel, if you had to apply the standard `clip` modifier, the items would be statically clipped and not apply the parallax effect that this component introduces.
 
For example, if you wanted to surround your Carousel items with a border, you can do so by placing the `maskBorder` modifier onto the individual item, as well as provide a different shape to the items with `maskClip` :
 `xxxxxxxxxx`
 
`HorizontalUncontainedCarousel (` `state = rememberCarouselState { items . count () },` `modifier = Modifier . fillMaxWidth ()` `. wrapContentHeight ()` `. padding ( top = 16. dp , bottom = 16. dp ),` `itemWidth = 186. dp ,` `itemSpacing = 8. dp ,` `contentPadding = PaddingValues ( horizontal = 16. dp )` `) { i ->` `val item = items [ i ]` `Image (` `modifier = Modifier . height ( 205. dp )` `. maskClip ( MaterialTheme . shapes . extraLarge )` `. maskBorder ( BorderStroke ( 1. dp , MaterialTheme . colorScheme . secondary ), MaterialTheme . shapes . extraLarge ),` `painter = painterResource ( id = item . imageResId ),` `contentDescription = item . contentDescription ,` `contentScale = ContentScale . Crop` `)` `}` 
link
 
Copy link Link copied
 
## Component updates
 
The following components have been updated to match the Material 3 specification, there are also contrast updates to these components to improve accessibility out of the box.
 
Progress Indicator
 
The [progress indicator](https://m3.material.io/components/progress-indicators/overview) components have been updated to a new visual style to match the Material 3 specification:
 
[`LinearProgessIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LinearProgressIndicator(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color)) is a straight line progress indicator, the visual style has changed to use rounded `strokeCap` by default, this can be changed with the `strokeCap` parameter. New parameter for specifying the `gapSize` between the progress indicator and track is now available. To change or disable the visual indicator at the end - use the `drawStopIndicator` parameter.
 
[`CircularProgressIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#CircularProgressIndicator(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp)) is a circle shaped progress indicator, the visual style has changed to use rounded `strokeCap` , this can be changed with the `strokeCap` parameter. New parameter for specifying the `gapSize` between the progress indicator and track is now available.
 
Slider
 
The [slider](https://m3.material.io/components/sliders/overview) component has been updated to a new visual style to match the Material 3 specification, including more prominent handles and an updated shape spec that can be customized:
 
Continuous slider: `Slider`
 
Discrete slider: `Slider` with `steps` parameter set
 
Range slider: `RangeSlider`
 
Bottom Sheet
 
Bottom sheets have been updated to fix bugs and offer improvements to the API. [`ModalBottomSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalBottomSheet(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.SheetState,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,kotlin.Function0,kotlin.Function0,androidx.compose.material3.ModalBottomSheetProperties,kotlin.Function1)) more accurately draws scrim over status bar when edge to edge is enabled.
 
Modal bottom sheet content can now consume window insets, allowing for visible content above the navigation bar. `ModalBottomSheet` parameter `windowInsets` is renamed to `contentWindowInsets` to specify where the insets will be applied, and the insets are no longer tied to window logic. In addition, the bottom sheet includes predictive back support.
 
Pull to refresh API changes
 
The pull to refresh experimental APIs have been overhauled and updated to fix a few bugs with the component. The updated APIs for [`PullToRefreshBox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/pulltorefresh/package-summary#PullToRefreshBox(kotlin.Boolean,kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.pulltorefresh.PullToRefreshState,androidx.compose.ui.Alignment,kotlin.Function1,kotlin.Function1)) simplify the state to use fractional values instead of dp units, and separate out the nested scroll connection from `PullToRefreshState` . A simple example of using pull to refresh:
 `xxxxxxxxxx`
 
`@ Composable` `fun PullToRefreshDemo () {` `var itemCount by remember { mutableIntStateOf ( 15 ) }` `var isRefreshing by remember { mutableStateOf ( false ) }` `val state = rememberPullToRefreshState ()` `val coroutineScope = rememberCoroutineScope ()` `​` `val onRefresh : () -> Unit = {` `isRefreshing = true` `coroutineScope . launch {` `delay ( 1500 )` `itemCount += 5` `isRefreshing = false` `}` `}` `​` `Scaffold (` `topBar = {` `TopAppBar (` `title = { Text ( "Title" ) },` `// Provide an accessible alternative to trigger refresh.` `actions = {` `IconButton ( onClick = onRefresh ) {` `Icon ( Icons . Filled . Refresh , "Trigger Refresh" )` `}` `}` `)` `}` `) {` `PullToRefreshBox (` `modifier = Modifier . padding ( it ),` `state = state ,` `isRefreshing = isRefreshing ,` `onRefresh = onRefresh ,` `) {` `LazyColumn ( Modifier . fillMaxSize ()) {` `if ( ! isRefreshing ) {` `items ( itemCount ) {` `ListItem ({ Text ( text = "Item ${itemCount - it}" ) })` `}` `}` `}` `}` `}` `}` 
link
 
Copy link Link copied
 
## Predictive back support
 
Support for predictive back is now built into some of the Material Components.  Predictive back allows a user to swipe left or right on certain components as a way to navigate to a previous destination. Before completing the swipe, the user can decide to continue to the previous view or stay in the current view, where the component will indicate a preview of where going back would take the user.
 
pause
 
The following components will now automatically handle predictive back on devices that support it:
 
`ModalBottomSheet`
 
`SearchBar`
 
`ModalDrawerSheet`
 
`DismissibleDrawerSheet`
 
link
 
Copy link Link copied
 
## Color Token Alignment / Tonal Surface Colors
 
[Tone-based surface color roles](https://material.io/blog/tone-based-surface-color-m3) have replaced the previous “surfaces at +1 to +5 elevation” approach. The new color roles are not tied to elevation, and offer more flexibility and support for color features such as user-controlled contrast. All Material Components will automatically update to use the new surface container color roles .
 
For developers using the previous opacity-based surface model for custom color mappings, we recommend remapping these to the new roles:
 
Instead of using `ColorScheme.surfaceColorAtElevation()` , use the following colors instead:
 
`surfaceContainerLowest` is a new role
 
Surface at elevation +1 becomes `surfaceContainerLow`
 
Surface at elevation +2 becomes `surfaceContainer`
 
Surface at elevation +3 becomes `surfaceContainerHigh`
 
Surface at elevation +4 and +5 are being deprecated, it is recommended to use `surfaceContainerHighest` by default as a replacement. As an alternative `surfaceContainerHigh` , or `surfaceDim` can be used depending on the specific use case.
 
Surface Variant becomes `surfaceContainerHighest`
 
For more information on tone-based surface color roles and the exact changes, see [the blog post](https://material.io/blog/tone-based-surface-color-m3) .
 
In addition to the introduction of tone based surface color roles, the following color roles have been updated in the default `lightColorScheme` to be more colorful while still having accessible color contrast:
 
`onPrimaryContainer`
 
`onSecondaryContainer`
 
`onTertiaryContainer`
 
`onErrorContainer`
 
Affected components:
 
Badges
 
Bottom app bar
 
Buttons
 
Common buttons
 
Extended FAB
 
FAB
 
Icon buttons
 
Segmented buttons
 
Chips
 
Lists
 
Menus
 
Navigation bar
 
Navigation drawer
 
Navigation rail
 
Switches
 
Promotion of experimental APIs to Stable
 
The experimental Material components continue to be evaluated and adjusted based on your feedback and bug reports. In this release, we’ve graduated more APIs and removed the experimental annotations from:
 
`SegmentedButton` and associated APIs are now stable.
 
`SwipeToDismissBox` and associated APIs are now stable.
 
link
 
Copy link Link copied
 
## Learn more
 
The components or features that are highlighted in these posts are only a subset of the work that lands in each release. Check out the [release notes](https://developer.android.com/jetpack/androidx/releases/compose-material3) for a full listing of all the changes.
 
You can file [bug reports](https://issuetracker.google.com/issues/new?component=742043&template=1590761) and follow [open issues](https://issuetracker.google.com/issues?q=componentid:742043%20status:open) on Buganizer. You can also follow the progress of new versions on [cs.android.com](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/;bpv=1;bpt=0) . Install the [catalog app](https://play.google.com/store/apps/details?id=androidx.compose.material.catalog) on Google play to see the latest components in action.
