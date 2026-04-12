# Material Components for Android 1.2.0

> Source: https://m3.material.io/blog/android-stable-release-1-2

Posted by
 Nick Rout , Material Developer Advocate
 We’re excited to announce the release of Material Components for Android (MDC-Android) `1.2.0` ! A host of exciting new features have been added along with many bug fixes and accessibility improvements. Get the rundown below.
 
Be sure to check out the [release notes](https://github.com/material-components/material-components-android/releases/tag/1.2.0) . If you’re using MDC for the first time, also take a look at our [getting started guide](https://material.io/develop/android/docs/getting-started) .
 
link
 
Copy link Link copied
 
## What’s new in 1.2.0?
 
A fair bit has changed since we launched `[1.1.0](https://medium.com/google-design/material-design-components-for-android-1-1-0-are-now-available-45e1d576037c)` in February — we added the motion system, slider component, a widget for image shape theming, and more. The things you loved from the alpha, beta, and RC releases of `1.2.0` are now officially stable. If you haven’t yet started using version `1.2.0` of MDC, there’s never been a better time to update.
 
link
 
Copy link Link copied
 
## Material motion
 
[Material’s motion system](https://material.io/design/motion/the-motion-system.html) includes a set of four transition patterns. They can help users understand and navigate an app, and reinforce relationships between components or full-screen views. The transition patterns are:
 
[Container transform](https://material.io/design/motion/the-motion-system.html#container-transform)
 
[Shared axis](https://material.io/design/motion/the-motion-system.html#shared-axis)
 
[Fade through](https://material.io/design/motion/the-motion-system.html#fade-through)
 
[Fade](https://material.io/design/motion/the-motion-system.html#fade)
 
MDC `1.2.0` enables Material motion in your Android app. The four transition patterns are implemented as classes built on top of both the AndroidX Transition library ( `androidx.transition` ) ( `androidx.transition` ), available in the `com.google.android.material.transition package` , and the Android Framework Transition library ( `android.transition` ), available in the `com.google.android.material.transition.platform` package. They can be used to transition between Fragments (including [Jetpack Navigation](https://developer.android.com/guide/navigation) ), Activities, and Views.
 
Container transform between Fragments (using Jetpack Navigation)
 
`<!-- fragment_a.xml -->` `< View` `android : id = "@+id/start_view"` `android : transitionName = "start_container" />` `<!-- fragment_b.xml -->` `< View` `android : id = "@+id/end_view"` `android : transitionName = "end_container" />` `// FragmentB.kt` `override fun onCreate ( savedInstanceState : Bundle ? ) {` `super . onCreate ( savedInstanceState )` `...` `sharedElementEnterTransition = MaterialContainerTransform ()` `}` `// FragmentA.kt` `fun onCreate ( savedInstanceState : Bundle ? ) {` `super . onCreate ( savedInstanceState )` `...` `exitTransition = Hold ()` `}` `...` `val directions = FragmentADirections . actionFragmentAToFragmentB ()` `val extras = FragmentNavigatorExtras ( startView to "end_container" )` `findNavController (). navigate ( directions , extras )`
 
Shared Z-axis between Fragments
 
`xxxxxxxxxx`
 
`// FragmentA.kt` `override fun onCreate ( savedInstanceState : Bundle ? ) {` `super . onCreate ( savedInstanceState )` `...` `reenterTransition = MaterialSharedAxis (` `MaterialSharedAxis . Z , /* forward = */ false )` `exitTransition = MaterialSharedAxis (` `MaterialSharedAxis . Z , /* forward = */ true )` `}` `// FragmentB.kt` `override fun onCreate ( savedInstanceState : Bundle ? ) {` `super . onCreate ( savedInstanceState )` `...` `enterTransition = MaterialSharedAxis (` `MaterialSharedAxis . Z , /* forward = */ true )` `returnTransition = MaterialSharedAxis (` `MaterialSharedAxis . Z , /* forward = */ false )` `}`
 
Fade through between Fragments
 
`xxxxxxxxxx`
 
`// FragmentA.kt` `override fun onCreate ( savedInstanceState : Bundle ? ) {` `super . onCreate ( savedInstanceState )` `...` `exitTransition = MaterialFadeThrough ()` `}` `// FragmentB.kt` `override fun onCreate ( savedInstanceState : Bundle ? ) {` `super . onCreate ( savedInstanceState )` `...` `enterTransition = MaterialFadeThrough ()` `}`
 
Fade a target View (using `TransitionManager` )
 
`xxxxxxxxxx`
 
`val fade = MaterialFade ()` `TransitionManager . beginDelayedTransition ( container , fade )` `view . visibility = View . VISIBLE // Use View.GONE to fade out`
 
Learn more about [how to implement motion for Android](https://material.io/develop/android/theming/motion) .
 
link
 
Copy link Link copied
 
## Slider
 
[Sliders](https://material.io/components/sliders) allow users to make selections from a range of values. They are ideal for adjusting settings such as volume, brightness, or applying image filters.
 
MDC `1.2.0` allows you to use sliders in your Android app with the `[Slider](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/slider/Slider.java)` and `[RangeSlider](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/slider/RangeSlider.java)` widgets. They’re similar to `SeekBar` but have additional features and support [Material Theming](https://material.io/design/material-theming/overview.html) .
 
`xxxxxxxxxx`
 
`<!-- In layout -->` `< com . google . android . material . slider . Slider` `android : id = ” @+ id / slider”` `...` `android : valueFrom = "0.0"` `android : valueTo = "100.0"` `android : stepSize = "10.0" />` `...` `< com . google . android . material . slider . RangeSlider` `android : id = ” @+ id / rangeSlider”` `...` `android : valueFrom = "0.0"` `android : valueTo = "100.0"` `android : stepSize = "10.0"` `app : values = "@array/initial_slider_values" />` `<!-- In res/values/arrays.xml -->` `< resources >` `...` `< array name = "initial_slider_values" >` `< item > 20.0 < /item>` `< item > 70.0 < /item>` `< /array>` `< /resources>` `// In code` `slider . addOnChangeListener { slider , value , fromUser ->` `// Respond to change in slider's value` `}` `...` `val values = rangeSlider . values`
 
Learn more about [how to implement sliders](https://material.io/develop/android/components/slider) .
 
link
 
Copy link Link copied
 
## ShapeableImageView
 
The new `[ShapeableImageView](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/imageview/ShapeableImageView.java)` widget is an extension of `AppCompatImageView` which understands shape theming. A common use case is to apply circular clips to rectangular source images. However, it also supports varying corner sizes, cut corners, as well as different stroke widths and colors.
 
`xxxxxxxxxx`
 
`<!-- res/values/shape.xml -->` `< style name = ”ShapeAppearanceOverlay . App . CornerSize50Percent”` `parent = ”” >` `<!--` `Sets size of corners to be 50 % of min ( width , height ) of widget` `-->` `< item name = ”cornerSize” > 50 %< /item>` `< /style>` `<!-- res/values/styles.xml -->` `< style name = ”Widget . App . ShapeableImageView”` `parent = ”Widget . MaterialComponents . ShapeableImageView” >` `< item name = ”shapeAppearance” >` `? attr / shapeAppearanceSmallComponent` `< /item>` `< item name = ”shapeAppearanceOverlay” >` `@ style / ShapeAppearanceOverlay . App . CornerSize50Percent` `< /item>` `< item name = ”strokeWidth” > 1 dp < /item>` `< item name = ”strokeColor” >? attr / colorPrimary < /item>` `< /style>` `<!-- In layout -->` `< com . google . android . material . imageview . ShapeableImageView` `...` `style = ” @ style / Widget . App . ShapeableImageView”` `app : srcCompat = ” @ drawable / image” />`
 
link
 
Copy link Link copied
 
## MaterialColors
 
The `[MaterialColors](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/color/MaterialColors.java)` utility class was made public in MDC `1.2.0` . It gives you a variety of useful static methods to use when dealing with colors programmatically in your app.
 
`xxxxxxxxxx`
 
`// Resolve color from theme attr` `val primaryColor = MaterialColors . getColor (` `view , R . attr . colorPrimary )` `// Layer background color with overlay color + alpha` `val overlayedColor = MaterialColors . layer (` `view , R . attr . colorSurface , R . attr . colorPrimary , 0.38 f )`
 
link
 
Copy link Link copied
 
## Support for materialThemeOverlay in all components
 
The `materialThemeOverlay` attribute allows you to apply [theme overlays](https://medium.com/androiddevelopers/android-styling-themes-overlay-1ffd57745207) . Unlike `android:theme` , it can be used in default component styles (e.g., `materialButtonStyle` ). By default it can only be used with MDC; full support for all components was added in `1.2.0` . You can use `[MaterialThemeOverlay#wrap](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/theme/overlay/MaterialThemeOverlay.java#L61)` to add this functionality to custom views.
 
link
 
Copy link Link copied
 
## MaterialButton respects android:background
 
`[MaterialButton](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/MaterialButton.java)` previously ignored custom background drawables applied with `android:background` . This has been fixed in MDC `1.2.0` . A `[MaterialShapeDrawable](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/shape/MaterialShapeDrawable.java)` will still be used as the default background if no custom background is set.
 
Note: The default style for `MaterialButton` includes a `backgroundTint` which will also be applied to a custom background drawable. You may need to change this to a different color or set it as `@empty` to remove it.
 
`xxxxxxxxxx`
 
`<!--` `Note : Button is auto - inflated as` `MaterialButton by MaterialComponentsViewInflater` `-->` `< Button` `...` `android : background = ” @ drawable / custom_background”` `app : backgroundTint = ” @ empty” />`
 
link
 
Copy link Link copied
 
## What’s next for MDC?
 
The next feature release of MDC— `1.3.0` — is well underway with multiple [alpha releases](https://github.com/material-components/material-components-android/releases/) out at the time of writing. Exciting new updates include `[ProgressIndicator](https://github.com/material-components/material-components-android/blob/master/docs/components/ProgressIndicator.md)` , `[MaterialTimePicker](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/timepicker/MaterialTimePicker.java)` , and various improvements to existing components. As always, we encourage you to file [bug reports](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BComponent+name%5D+Short+description+of+issue) and [feature requests](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=feature+request&template=feature_request.md&title=%5BComponent+name%5D+Short+description+of+request) on GitHub. Also be sure to check out our Android [example apps](https://github.com/material-components/material-components-android-examples) and how to [Build a Material Theme](https://material.io/resources/build-a-material-theme/) .
 
We highly encourage trying out MDC `1.2.0` . If you’re using its features in your Android app, reach out to us on Twitter [@materialdesign](https://twitter.com/materialdesign) . We’d love to see it.
