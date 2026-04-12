# Material Design Components for Android 1.6.1

> Source: https://m3.material.io/blog/android-stable-release-1-6-1

Posted by
 James Williams , Material Developer Advocate
 After cooling down from Google I/O, we have a pair of Material Design Components(MDC) releases to share with you: [1.6.0](https://github.com/material-components/material-components-android/releases/tag/1.6.0) and [1.6.1](https://github.com/material-components/material-components-android/releases/tag/1.6.1) . As was the case with MDC 1.5.0, color is again a major theme with new APIs targeting [dynamic color](https://m3.material.io/styles/color/dynamic-color/overview) and [color harmony](https://material.io/blog/dynamic-color-harmony) .
 
Other notable highlights include Material3 style updates of various components and various bug fixes, like resolving issues on Android Oreo(8) and Pie(9), underscoring our commitment to more than just the most recent release.
 
Alongside the documentation we host on [Github](https://github.com/material-components/material-components-android/tree/master/docs) , the [Material Design 3 site](https://m3.material.io/) is an additional source for the styling guidance and availability of components. For components available on MDC Views, the implementation page will contain code snippets showing you how to implement that component and common use cases. Below is some of the code you can find on the [implementation page for Chips](https://m3.material.io/components/chips/implementation) .
 
link
 
Copy link Link copied
 
## Color Harmony
 
In the [blog post](https://material.io/blog/android-stable-release-1-5) announcing MDC 1.5.0, we discussed using tooling to select colors beyond the core colors that exist in every Material3 theme. Custom or extended color inside of a dynamic theme presents an interesting question: “How do we guarantee that a reserved color will look well alongside a dynamic theme AND still be legible?”
 
The algorithm we use to create Material3 themes can handle this situation using a concept called color harmony. This harmonization works by shifting a target color towards a source color. Colors that are closer to each other appear more harmonious whereas colors that are further apart appear more discordant.
 
To read more about color science and the whys and hows of color harmony, check out [The Science of Color & Design](https://material.io/blog/science-of-color-design) and [Designing Harmony into Dynamic Color](https://material.io/blog/dynamic-color-harmony) .
 
### Applying Color Harmony On Demand
 
Using the functions [`harmonizeWithPrimary`](https://github.com/material-components/material-components-android/blob/948d5dac03a55971338d36bb52f1f49bd448ebd7/lib/java/com/google/android/material/color/MaterialColors.java#L185) and [`harmonize`](https://github.com/material-components/material-components-android/blob/948d5dac03a55971338d36bb52f1f49bd448ebd7/lib/java/com/google/android/material/color/MaterialColors.java#L199) , you can harmonize a given color with the primary color for the theme or an arbitrary color.
 ​ x
 
`@ ColorInt` `public static int harmonizeWithPrimary ( @ NonNull Context context , @ ColorInt int colorToHarmonize ) { }` `​` `​` `@ ColorInt` `public static int harmonize ( @ ColorInt int colorToHarmonize , @ ColorInt int colorToHarmonizeWith ) { }` 
### Applying Color Harmony Systematically
 
In most cases, instead of calculating harmonized colors on demand, you’ll want to leverage helper classes in MDC 1.6.0 that can take in a set of attributes or colors and return harmonized versions to your theme seamlessly. HarmonizedColorAttributes and HarmonizedColorOptions are two builder classes you can use to enable harmonization when you retrieve a dynamic color Context.
 
The snippet below shows how to build a dynamic context that automatically harmonizes to two specified colors.
 `xxxxxxxxxx`
 
`val dynamicColorsContext = DynamicColors . wrapContextIfAvailable ( requireContext ())` `​` `val harmonizedOptions = HarmonizedColorsOptions . Builder ()` `. setColorResourceIds ( intArrayOf ( R . color . custom1 , R . color . custom2 ))` `. build ();` `​` `harmonizedContext =` `HarmonizedColors . wrapContextIfAvailable ( dynamicColorsContext , harmonizedOptions )` 
For a more detailed discussion of how to apply color harmonization in code, check out the [Color Harmonization section](https://github.com/material-components/material-components-android/blob/master/docs/theming/Color.md#using-color-harmonization) of our developer documentation on color or the [codelab](https://codelabs.developers.google.com/harmonize-color-android-views#2) that demonstrates both methods.
 
link
 
Copy link Link copied
 
## What’s next for MDC ?
 
We’re fast at work on the next major version of MDC. You can follow the progress, file [bug reports](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BComponent+name%5D+Short+description+of+issue) and [feature requests](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=feature+request&template=feature_request.md&title=%5BComponent+name%5D+Short+description+of+request) on GitHub. Also feel free to reach out to us on Twitter [@materialdesign](https://twitter.com/materialdesign) .
