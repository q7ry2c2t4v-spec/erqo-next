# Building a Material Theme on Android: Typography

> Source: https://m3.material.io/blog/android-material-theme-type

Posted by
 Nick Rout , Material Developer Advocate
 [Material Theming](https://material.io/design/material-theming/overview.html#material-theming) is a way to customize [Material Components](https://material.io/components) to align with your brand. A Material theme includes [color](https://material.io/design/color/) , [typography](https://material.io/design/typography/) and [shape](https://material.io/design/shape/) parameters which you can adjust to get near-infinite variations of the components – all while maintaining their core anatomy and usability.
 
On Android, Material Theming can be implemented using the [Material Components (MDC) library](https://github.com/material-components/material-components-android) , from version `1.0.0` onwards. If you’re looking to migrate from the Design Support Library or MDC `1.0.0` , take a look at [our migration guide](https://medium.com/androiddevelopers/migrating-to-material-components-for-android-ec6757795351) .
 
This article will be focusing on type theming.
 
link
 
Copy link Link copied
 
## Type attributes
 
Material Design provides 13 type “styles” that are applied to all the text in your app. Each of these have a design term (eg. “Body 1”) along with a corresponding type attribute that can be overridden in your app theme (eg. `textAppearanceBody1` ). There are default “baseline” values (text size, letter spacing, capitalization, etc.) for each style.
 MDC type attributes with baseline styling 
Material Components use these type attributes to style textual elements of the widgets (those parts that subclass or comprise one or more `TextView` s).
 Type attributes used by a button 
They are applied in layouts and widget styles like this, for example:
 `android : textAppearance = ” ? attr / textAppearanceBody1”` 
Take a look at Nick Butcher’s “ [What’s your text’s appearance?](https://medium.com/androiddevelopers/whats-your-text-s-appearance-f3a1729192d) ” article for more information on using this and the order of precedence with other styling techniques.
 
In the MDC themes these attributes map to styles, eg.
 `xxxxxxxxxx`
 
`< style name = ”Theme . MaterialComponents . * ” parent = ” ... ” >` `...` `< item name = ”textAppearanceBody1” >` `@ style / TextAppearance . MaterialComponents . Body1` `< /item>` `< style />` 
You might recognize `TextAppearance` styles from AppCompat or the platform and these are discussed in more detail in the Type resources section below. The corresponding attributes are new to MDC and give you the ability to vary typography by theme.
 
link
 
Copy link Link copied
 
## Picking type
 
Figuring out which type styles to use and the values within them may be the responsibility of a designer, or derived from your product’s brand. However, it’s still useful to know about the role of each style and in which scenarios they should be used:
 
`textAppearanceHeadline*` styles are for headings
 
`textAppearanceSubtitle*` styles are for subheadings
 
`textAppearanceBody*` styles are for multiline body text
 
`textAppearanceButton` is for buttons but also maps to parts of other components like tabs and dialog actions
 
`textAppearanceCaption` is for smaller text like text field hints and errors
 
`textAppearanceOverline` is also for smaller text but capitalization and increased letter spacing make it suitable for small titles and labels like date picker headers
 
link
 
Copy link Link copied
 
## Type tool
 
Material Design provides a useful tool for previewing type scales, integrating with [Google Fonts](https://fonts.google.com/) and exporting code. See "Type scale generator" in the [Material Design type scale guidelines](https://material.io/design/typography/the-type-system.html#type-scale) .
 Google Fonts (left) and Type scale generator (right) 
link
 
Copy link Link copied
 
## Type resources
 
Type resources consist of fonts as well as `TextAppearance` styles. Let’s take a look at what’s available on Android and a few things to keep in mind when declaring styles.
 
XML and downloadable fonts
 
Fonts are stored in the res/font directory and referenced with `@font/` notation. You can use either local XML fonts or downloadable fonts. Android Studio offers a built-in wizard to get you started with downloadable fonts including the necessary certificates and manifest metadata. You may also want to check out “ [The Android Developer’s Guide to Better Typography](https://medium.com/google-design/the-android-developers-guide-to-better-typography-97e11bb0e261) ” by Rod Sheeter for a more detailed guide and further optimizations to font preloading.
 
In general we recommend using downloadable fonts as they reduce the size of your app bundle by leveraging the shared font provider cache. However, downloadable fonts currently only work with those available on Google Fonts. If your app requires a purchased or proprietary font, use XML fonts.
 
It’s also worth mentioning that variable fonts are supported on Android from API 26 onwards. Take a look at Rebbeca Franks’ “ [Variable Fonts in Android O 🖍](https://medium.com/over-engineering/variable-fonts-in-android-p-c5c918275646) ” article for more information.
 
link
 
Copy link Link copied
 
## TextAppearance styles
 
`TextAppearance` styles can be seen as the Android equivalent of Material Design type styles. For custom styles, we recommend two approaches to help separate concerns and create a single source of truth for type theming values in your app:
 
Store all `TextAppearance` styles in a single res/values/type.xml file
 
Use the MDC `TextAppearance` styles as parents and adhere to the same naming convention
 
Attributes and values you can use within these styles align with those supported by `TextView` :
 
`fontFamily` is the font family, typically an `@font/` resource referring to an XML or downloadable font
 
`android:textSize` is the size of the text, typically an `sp` dimension
 
`android:textColor` is the color of text
 
`android:letterSpacing` is the spacing between characters
 
`android:textAllCaps` is a boolean to toggle text capitalization
 
`android:textFontWeight` is the weight of the font, used to select the closest match from a font family, but is only available on API 28 and above. `android:textStyle` can also be used to apply transformations such as `bold` and `italic` .
 `xxxxxxxxxx`
 
`<!-- In res/values/type.xml -->` `< style name = "TextAppearance.App.Headline6" parent = "TextAppearance.MaterialComponents.Headline6" >` `< item name = "fontFamily" >@ font / roboto_mono < /item>` `...` `< /style>` `< style name = "TextAppearance.App.Body2" parent = "TextAppearance.MaterialComponents.Body2" >` `< item name = "fontFamily" >@ font / roboto_mono < /item>` `< item name = "android:textSize" > 14 sp < /item>` `...` `< /style>` `< style name = "TextAppearance.App.Button" parent = "TextAppearance.MaterialComponents.Button" >` `< item name = "fontFamily" >@ font / roboto_mono < /item>` `< item name = "android:textAllCaps" > false < /item>` `...` `< /style>` 
link
 
Copy link Link copied
 
## Calculating letterSpacing
 
Letter spacing values on Android tend to use a different unit of measurement (em) to those used in design tools like Sketch (tracking). The [Material Design typography guidelines](https://material.io/design/typography/the-type-system.html#type-scale) provide a relatively simple equation for determining suitable em values from tracking values:
 
(Tracking from Sketch / font size in sp) = letter spacing
 `xxxxxxxxxx`
 
`<!-- (0.25 tracking / 14sp font size) = 0.0178571429 em -->` `< style name = "TextAppearance.App.Body2" parent = "TextAppearance.MaterialComponents.Body2" >` `< item name = "fontFamily" >@ font / roboto_mono < /item>` `< item name = "android:textSize" > 14 sp < /item>` `+ < item name = "android:letterSpacing" > 0.0178571429 < /item>` `...` `< /style>` 
link
 
Copy link Link copied
 
## MaterialTextView and lineHeight
 
The platform `TextView` added support for the `android:lineHeight` attribute in API 28. MDC provides backported support for this via the `MaterialTextView` class. You don’t need to use this class directly in layouts as `<TextView>` s will get auto-inflated as `MaterialTextView` s by `MaterialComponentsViewInflater` .
 
You can use `lineHeight` in various scenarios:
 
Included as an item in `TextAppearance` styles (applied with `android:textAppearance="..."` )
 
Included as an item in widget styles with parent `Widget.MaterialComponents.TextView` (applied with `style=”...”` )
 
Applied directly to `<Texview>` s in layouts
 Different lineHeight values 
link
 
Copy link Link copied
 
## Things to consider
 
You don’t have to override all type styles. However, bear in mind that default MDC styles use the system font (typically Roboto). Be sure to check which type styles your widgets and `TextView` s are using.
 
While `TextAppearance` does support `android:textColor` , MDC tends to separate concerns by specifying this separately in the main widget styles:
 `xxxxxxxxxx`
 
`< style name = ”Widget . MaterialComponents . * ” parent = ” ... ” >` `...` `< item name = ”android : textColor” >? attr / colorOnSurface < /item>` `< item name = ”android : textAppearance” >? attr / textAppearanceBody1 < /item>` `< /style>` 
link
 
Copy link Link copied
 
## Additional type styles
 
Your design system may call for additional type styles outside of the 13 that Material Theming specifies. Thankfully this is relatively easy to do on Android by declaring a type attr:
 ​ x
 
`<!-- In res/values/attrs.xml -->` `< attr name = "textAppearanceCustom" format = "reference" />` `​` `<!-- In res/values/type.xml -->` `< style name = "TextAppearance.App.Custom" parent = "TextAppearance.MaterialComponents.*" >` `...` `< /style>` `​` `<!-- In res/values/themes.xml -->` `< style name = "Theme.App" parent = "Theme.MaterialComponents.*" >` `...` `< item name = "textAppearanceCustom" >@ style / TextAppearance . App . Custom < /item>` `< /style>` 
link
 
Copy link Link copied
 
## Overriding type styles in an app theme
 
Let’s take a look at how you can add your chosen type styles to your app theme by overriding relevant attributes.
 
First, we recommend setting up your theme(s) to gracefully handle light and dark color palettes while reducing repetition with base themes. For more on this topic, take a look at Chris Banes’ article on [dark theme](https://medium.com/androiddevelopers/dark-theme-with-mdc-4c6fc357d956) as well as the " [Developing Themes with Style](https://chris.banes.dev/talks/2019/developing-themes-with-style-berlin/) " talk given by him and Nick Butcher.
 
Once set up, override the type attributes you wish to change in your base theme:
 `xxxxxxxxxx`
 
`<!-- In res/values/themes.xml -->` `< style name = "Theme.App.Base" parent = "Theme.MaterialComponents.*" >` `...` `< item name = "textAppearanceHeadline6" >` `@ style / TextAppearance . App . Headline6` `< /item>` `< item name = "textAppearanceBody2" >` `@ style / TextAppearance . App . Body2` `< /item>` `< item name = "textAppearanceButton" >` `@ style / TextAppearance . App . Button` `< /item>` `<!-- Using default values for textAppearanceSubtitle1, textAppearanceCaption, etc. --><p></style></p>` `​` 
Material Components will respond to theme-level type overrides:
 Material Design components responding to theme-level type overrides 
link
 
Copy link Link copied
 
## Type in MDC widgets
 
Earlier we said that MDC widgets respond to overrides of theme level type attributes. But how would you know, for example, that a button uses `textAppearanceButton` as the style for its text label? Let’s take a look at a few options.
 
link
 
Copy link Link copied
 
## MDC developer docs
 
The MDC developer docs have recently been refreshed. As part of this we’ve included attribute tables which include design terminology and default values used in the library. For example, check out the “Anatomy and key properties” sections of the updated [buttons doc](https://material.io/develop/android/components/buttons/#contained-button) .
 MDC button dev doc attribute table with default type values 
link
 
Copy link Link copied
 
## Source code
 
Inspecting the MDC source code is arguably the most reliable approach. MDC uses default styles to achieve Material Theming so it’s a good idea to look at these as well as any styleable attrs and the java file(s). For example, check out the [styles](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/res/values/styles.xml) , [attrs](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/res/values/attrs.xml) and [java file](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/MaterialButton.java) for `MaterialButton` .
 MDC button default style with type values 
link
 
Copy link Link copied
 
## Type in custom views
 
Your app may include custom widgets you’ve built or gotten from an existing library. Making these views responsive to Material Theming is useful when using them alongside standard MDC widgets. Let’s take a look at what to keep in mind when supporting type theming for custom widgets.
 
link
 
Copy link Link copied
 
## Use MDC attrs declare-styleables and default styles
 
Allowing your custom views to be styled involves using a `<declare-styleable>` . Reusing attr names from MDC can be useful for consistency. Default styles that use `<declare-styleable>` s  can also reference MDC theme type attrs for their values:
 `xxxxxxxxxx`
 
`<!-- In res/values/attrs.xml -->` `< declare - styleable name = "AppCustomView" >` `< attr name = "titleTextAppearance" />` `< attr name = "subtitleTextAppearance" />` `...` `< /declare-styleable>` `​` `<!-- In res/values/styles.xml -->` `< style name = "Widget.App.CustomView" parent = "android:Widget" >` `< item name = "titleTextAppearance" >? attr / textAppearanceHeadline6 < /item>` `< item name = "subtitleTextAppearance" >? attr / textAppearanceBody2 < /item>` `...` `< /style>` 
link
 
Copy link Link copied
 
## OK Google, what’s next?
 
We’ve been through the process of implementing color theming in your Android app using MDC. Be sure to check out our other posts in this series on [why we recommend using MDC](https://medium.com/androiddevelopers/we-recommend-material-design-components-81e6d165c2dd) , [color theming](https://material.io/blog/android-material-theme-color) , [shape theming](https://material.io/blog/android-material-theme-shape) , [dark theme](https://medium.com/androiddevelopers/dark-theme-with-mdc-4c6fc357d956) , and Material's [motion system](https://material.io/blog/android-material-motion) .
 
As always, we encourage you to file [bug reports](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BComponent+name%5D+Short+description+of+issue) and [feature requests](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=feature+request&template=feature_request.md&title=%5BComponent+name%5D+Short+description+of+request) on GitHub. Also be sure to check out our [Android companion example apps](https://github.com/material-components/material-components-android-examples) .
 
If you’ve successfully implemented type theming or if you’re having trouble doing so, reach out to us on Twitter [@MaterialDesign](https://twitter.com/materialdesign) .
