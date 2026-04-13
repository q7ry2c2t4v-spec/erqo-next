# Migrating to Material Components for Android

> Source: https://m3.material.io/blog/migrate-android-material-components

Posted by
 Nick Rout , Material Developer Advocate
 We recently [announced](https://medium.com/google-design/material-design-components-for-android-1-1-0-are-now-available-45e1d576037c) [Material Design Components](https://github.com/material-components/material-components-android) (MDC) `1.0.0` — a library update that brings [Material Theming](https://material.io/design/material-theming/overview.html) , new widgets, dark theme support and other exciting features to your Android app.
 
MDC replaces the Design Support Library. This guide will show you how to migrate your codebase so you can make use of the new attributes, styles, and widgets. If you’re on MDC `1.0.0` this also provides the necessary migration steps to `1.1.0` . Be sure to check out our corresponding [video guide](https://www.youtube.com/watch?v=64OD1PAqELg&feature=youtu.be) as well!
 
link
 
Copy link Link copied
 
## A simplified theming example
 
This guide uses a simplified app to demonstrate the migration process. It uses an AppCompat theme, widgets from the Design Support Library (including a button with a custom background), and various other elements that require migration. We’ll start with an app theme which uses the traditional AppCompat template:
 
`< style name = "Theme.App" parent = "Theme.AppCompat.*" >` `< item name = "colorPrimary" >@ color / navy_700 < /item>` `< item name = "colorPrimaryDark" >@ color / navy_900 < /item>` `< item name = "colorAccent" >@ color / green_300 < /item>` `< /style>`
 
Example app using AppCompat and the Design Support Library
 
link
 
Copy link Link copied
 
## Migrating from the Support Library to Jetpack
 
Before you can use MDC, you need to migrate from the Support Library to [Android Jetpack](https://developer.android.com/jetpack/) . Jetpack uses the new `androidx.*` namespace and splits the previous Support Library packages into separately maintained, semantically versioned libraries, providing feature parity as well as new libraries. MDC is built with AndroidX libraries so migration is mandatory.
 
To migrate to AndroidX, we recommend following the [official developer documentation](https://developer.android.com/jetpack/androidx/migrate) or watching the [“Migrating to AndroidX: The time is right” talk](https://www.youtube.com/watch?v=Hyt7LR5mXLc) from Android Dev Summit ’19. The ‘ Refactor > Migrate to AndroidX ’ tool in Android Studio will refactor your Design Support Library dependency to MDC.
 
Note: Jetpack and MDC artifacts with version `1.0.0` are binary compatible with the Support Library `28.0.0` artifacts. If you’re not on version 28 then we recommend upgrading to this first and then migrating.
 
link
 
Copy link Link copied
 
## Updating to MDC 1.0.0
 
If you used the Android Studio ‘Refactor > Migrate to AndroidX’ tool during Jetpack migration, your Design Support Library dependency should have mapped to MDC `1.0.0` and you can skip this section.
 
If not, you will need to manually update your dependency:
 
`xxxxxxxxxx`
 
`- implementation ‘com . android . support : design : 28.0.0 ’` `+ implementation ‘com . google . android . material : material : 1.0.0 ’`
 
You will also need to change the package namespace of any usages of the Design Support Library classes (in XML layouts and in code) from `android.support.design.*` to `com.google.android.material.*` . To do so, take a look at the [class mapping table](https://developer.android.com/jetpack/androidx/migrate/class-mappings#androidsupportdesign) .
 
link
 
Copy link Link copied
 
## Changing your theme(s)
 
You need to ensure that your app theme inherits from a Material Components theme. The same applies to any additional themes and [theme overlays](https://medium.com/androiddevelopers/android-styling-themes-overlay-1ffd57745207) you may have in your project.
 `xxxxxxxxxx`
 
`-< style name = "Theme.App" parent = "Theme.AppCompat.*" >` `+< style name = "Theme.App" parent = "Theme.MaterialComponents.*" >` `...` `< /style>` 
If you were previously using an `AppCompat` theme variant, the MDC-Android theme variants map one-to-one with these. In most cases, simply swap out the AppCompat portion of the parent with `MaterialComponents` .
 
See the full theme and theme overlay mapping tables below:
 
AppCompat theme MDC-Android theme `Theme.AppCompat` `Theme.MaterialComponents` `Theme.AppCompat.NoActionBar` `Theme.MaterialComponents.NoActionBar` `Theme.AppCompat.Dialog.*` `Theme.MaterialComponents.Dialog.*` `Theme.AppCompat.DialogWhenLarge` `Theme.MaterialComponents.DialogWhenLarge` `Theme.AppCompat.Light` `Theme.MaterialComponents.Light` `Theme.AppCompat.Light.DarkActionBar` `Theme.MaterialComponents.Light.DarkActionBar` `Theme.AppCompat.Light.NoActionBar` `Theme.MaterialComponents.Light.NoActionBar` `Theme.AppCompat.Light.Dialog.*` `Theme.MaterialComponents.Light.Dialog.*` `Theme.AppCompat.Light.DialogWhenLarge` `Theme.MaterialComponents.Light.DialogWhenLarge` `Theme.AppCompat.DayNight` `Theme.MaterialComponents.DayNight` `Theme.AppCompat.DayNight.DarkActionBar` `Theme.MaterialComponents.DayNight.DarkActionBar` `Theme.AppCompat.DayNight.NoActionBar` `Theme.MaterialComponents.DayNight.NoActionBar` `Theme.AppCompat.DayNight.Dialog.*` `Theme.MaterialComponents.DayNight.Dialog.*` `Theme.AppCompat.DayNight.DialogWhenLarge` `Theme.MaterialComponents.DayNight.DialogWhenLarge`
 
AppCompat theme overlay MDC-Android theme overlay `ThemeOverlay.AppCompat` `ThemeOverlay.MaterialComponents` `ThemeOverlay.AppCompat.Light` `ThemeOverlay.MaterialComponents.Light` `ThemeOverlay.AppCompat.Dark` `ThemeOverlay.MaterialComponents.Dark` `ThemeOverlay.AppCompat.*.ActionBar` `ThemeOverlay.MaterialComponents.*.ActionBar.*` `ThemeOverlay.AppCompat.Dialog.*` `ThemeOverlay.MaterialComponents.Dialog.*` N/A `ThemeOverlay.MaterialComponents.*.BottomSheetDialog` N/A `ThemeOverlay.MaterialComponents.MaterialAlertDialog.*` N/A `ThemeOverlay.MaterialComponents.MaterialCalendar.*` N/A `ThemeOverlay.MaterialComponents.Toolbar.*`
 
link
 
Copy link Link copied
 
## Example updates
 Example app using MDC 1.0.0 and Theme.MaterialComponents.* theme 
link
 
Copy link Link copied
 
## Button changes
 
Having changed our dependency to MDC `1.0.0` and our app theme to inherit from `Theme.MaterialComponents.*` , we can observe some unexpected changes to buttons in our example app. We have lost our custom background! They now mostly make use of the green accent color and have wider letter spacing in their text labels.
 Buttons in MDC 1.0.0 
To understand why this has happened, we need to start by taking a look at how we’ve added these buttons in our layout (as framework `<Button>` s ):
 
`xxxxxxxxxx`
 
`< Button` `android : id = "@+id/containedButton"` `android : background = "@drawable/bg_button_gradient"` `android : textColor = "@android:color/white"` `... />` `< Button` `android : id = "@+id/textButton"` `style = ” ? attr / borderlessButtonStyle”` `... />`
 
So, what’s going on? 🤔
 
link
 
Copy link Link copied
 
## MDC widgets and auto-inflation
 
Like AppCompat, MDC will replace some framework widgets with MDC equivalents at inflation time. This makes it possible to ship new features and bugfixes without having to swap all your declarations for a new type. This is done via `[MaterialComponentsViewInflater](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/theme/MaterialComponentsViewInflater.java) ,` an extension of [AppCompatViewInflater](https://developer.android.com/reference/androidx/appcompat/app/AppCompatViewInflater) .
 
See the full widget auto-inflation mapping table below:
 
Framework widget AppCompat widget (replaced by [`AppCompatViewInflater`](https://developer.android.com/reference/androidx/appcompat/app/AppCompatViewInflater) ) MDC-Android widget (replaced by [`MaterialComponentsViewInflater`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/theme/MaterialComponentsViewInflater.java) ) `Button` [`AppCompatButton`](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatButton) [`MaterialButton`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/MaterialButton.java) `CheckBox` [`AppCompatCheckBox`](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatCheckBox) [`MaterialCheckBox`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/checkbox/MaterialCheckBox.java) `RadioButton` [`AppCompatRadioButton`](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatRadioButton) [`MaterialRadioButton`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/radiobutton/MaterialRadioButton.java) `TextView` [`AppCompatTextView`](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatTextView) [`MaterialTextView`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/textview/MaterialTextView.java) `AutoCompleteTextView` [`AppCompatAutoCompleteTextView`](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatAutoCompleteTextView) [`MaterialAutoCompleteTextView`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/textfield/MaterialAutoCompleteTextView.java)
 
Note: In MDC `1.0.0` only Button s were replaced. The other widgets above were added in subsequent versions of the library.
 
Our example app was previously replacing the framework `<Button>` s with `<AppCompatButton>` s because we had a `Theme.AppCompat.*` theme. Having migrated to a `Theme.MaterialComponents.*` theme, this has changed to `<MaterialButton>` s which has an updated default style.
 
Unlike `AppCompatButton` , `MaterialButton` did not support custom backgrounds until [release](https://github.com/material-components/material-components-android/releases/tag/1.2.0-alpha06) [1.2.0-alpha06](https://github.com/material-components/material-components-android/releases/tag/1.2.0-alpha06) [of MDC-Android](https://github.com/material-components/material-components-android/releases/tag/1.2.0-alpha06) . This is covered in more detail, along with a workaround, in the “ Shape ” section below.
 
We will keep this as is for now.
 
link
 
Copy link Link copied
 
## Updating to MDC 1.1.0
 
A lot has [changed](https://github.com/material-components/material-components-android/releases/tag/1.1.0) in MDC between `1.0.0` and `1.1.0` ! The new features include:
 
Full [Material Theming](https://material.io/design/material-theming/overview.html#material-theming) support for color, typography, and shape
 
[Dark theme](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) support
 
Android 10 [gesture navigation](https://developer.android.com/guide/navigation/gesturenav) insets in widgets
 
New widgets like the [extended FAB](https://material.io/develop/android/components/extended-floating-action-button/) , [date picker](https://material.io/develop/android/components/picker/) , [badges](https://material.io/develop/android/components/badging/) , and [toggle buttons](https://material.io/develop/android/components/buttons/#toggle-button)
 
Accessibility improvements, bug fixes, and more
 
We’re now ready to bump our MDC dependency version to `1.1.0` :
 
`xxxxxxxxxx`
 
`- implementation ‘com . google . android . material : material : 1.0.0 ’` `+ implementation ‘com . google . android . material : material : 1.1.0 ’`
 
Note: Some AndroidX dependencies, such as AppCompat, may also need updating at this time. While not strictly required, we recommend updating to the latest [stable versions](https://developer.android.com/jetpack/androidx/versions/stable-channel) if possible.
 
link
 
Copy link Link copied
 
## Some expected changes and common issues
 
MDC `1.1.0` changes some default widget styling to better comply with the Material Design guidelines. After upgrading you may, however, notice some unexpected changes to certain widget colors and other attributes.
 
Example app using MDC 1.1.0
 
In our example above, buttons have changed once again, the colors of text and icons have changed, FABs are now a shade of teal, and the text field looks entirely different. Oh dear! Don’t worry, your theme is likely missing some of the important MDC attributes while also having some AppCompat or framework attributes you no longer need. Let’s understand these issues by going through some common migration scenarios.
 
link
 
Copy link Link copied
 
## Text field changes
 
The default style for text fields has changed in MDC to a new, improved version backed by [user research](https://medium.com/google-design/the-evolution-of-material-designs-text-fields-603688b3fe03) .
 
Text fields in MDC 1.1.0+
 
We recommend sticking with this version for improved usability and configurability. However, we realize that this may not immediately fit with your brand and design system.
 
To revert back to the legacy text field, adjust the style in your layout to use the Design Support Library version:
 
`xxxxxxxxxx`
 
`< com . google . android . material . textfield . TextInputLayout` `...` `+ style = "@style/Widget.Design.TextInputLayout" >` `...` `< /com.google.android.material.textfield.TextInputLayout>`
 
Alternatively, you can make this the default style for all text fields in your theme(s):
 
​ x
 
`< style name = "Theme.App" parent = "Theme.MaterialComponents.*" >` `...` `+ < item name = ”textInputStyle” >@ style / Widget . App . TextInputLayout < /item>` `< /style>` `​` `+< style name = ”Widget . App . TextInputLayout” parent = ”Widget . Design . TextInputLayout” >` `+ <!-- Custom attrs -->` `+< /style>`
 
Legacy Design Support Library text field
 
link
 
Copy link Link copied
 
## Prefer MDC styles and widgets
 
As we’ve seen above, widgets previously in the Design Support Library have since become part of MDC. In most cases there are new `Widget.MaterialComponents.*` styles that replace `Widget.Design.*` styles, along with new attributes that enable additional features. While opting out is possible, we recommend adopting the new MDC styles.
 
For components that were not part of the Design Support Library, in some cases there is now a Material version of the class. We saw this above with `AppCompatButton` and `MaterialButton` . We recommend using MDC classes over AppCompat or framework equivalents, if available. These widgets use updated Material Design design guidelines by default and support the full set of MDC attributes, which enable Material Theming and other features.
 
There are a few scenarios you should consider:
 
Widgets used directly in layouts should change to MDC versions (see the “ MDC widgets and auto-inflation ” section above to see which widgets can be kept as framework tags)
 
Any styles, default styles and default style attributes should change to MDC versions
 
Any widgets used programmatically or as parents for custom classes should change to MDC versions
 
See the full widget and style mapping tables below:
 
MDC-Android widget (moved from Design Support Library) Design Support Library default style MDC-Android default style Default style attr [`AppBarLayout`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/appbar/AppBarLayout.java) `Widget.Design.AppBarLayout` `Widget.MaterialComponents.AppBarLayout.*` `appBarLayoutStyle` [`BottomNavigationView`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/bottomnavigation/BottomNavigationView.java) `Widget.Design.BottomNavigationView` `Widget.MaterialComponents.BottomNavigationView` `bottomNavigationStyle` [`BottomSheetBehavior`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/bottomsheet/BottomSheetBehavior.java) `Widget.Design.BottomSheet.Modal` `Widget.MaterialComponents.BottomSheet.*` `bottomSheetStyle` [`BottomSheetDialog`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/bottomsheet/BottomSheetDialog.java) [`BottomSheetDialogFragment`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/bottomsheet/BottomSheetDialogFragment.java) `Theme.Design.Light.BottomSheetDialog` `Theme.MaterialComponents.*.BottomSheetDialog` `ThemeOverlay.MaterialComponents.*.BottomSheetDialog` `bottomSheetDialogTheme` [`CollapsingToolbarLayout`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/appbar/CollapsingToolbarLayout.java) `Widget.Design.CollapsingToolbar` N/A N/A [`FloatingActionButton`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/floatingactionbutton/FloatingActionButton.java) `Widget.Design.FloatingActionButton` `Widget.MaterialComponents.FloatingActionButton` `floatingActionButtonStyle` [`NavigationView`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/navigation/NavigationView.java) `Widget.Design.NavigationView` `Widget.MaterialComponents.NavigationView` `navigationViewStyle` [`Snackbar`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/snackbar/Snackbar.java) `Widget.Design.Snackbar` `Widget.MaterialComponents.Snackbar` `snackbarStyle` [`TabLayout`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/tabs/TabLayout.java) [`TabItem`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/tabs/TabItem.java) `Widget.Design.TabLayout` `Widget.MaterialComponents.TabLayout` `tabStyle` [`TextInputLayout`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/textfield/TextInputLayout.java) [`TextInputEditText`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/textfield/TextInputEditText.java) `Widget.Design.TextInputLayout` `Widget.MaterialComponents.TextInputLayout.*` `textInputStyle`
 
AppCompat widget AppCompat default style AppCompat default style attr MDC-Android widget MDC-Android default style MDC-Android default style attr [`AlertDialog.Builder`](https://developer.android.com/reference/androidx/appcompat/app/AlertDialog.Builder) `AlertDialog.AppCompat` `ThemeOverlay.AppCompat.Dialog.Alert` `alertDialogStyle` `alertDialogTheme` [`MaterialAlertDialogBuilder`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/dialog/MaterialAlertDialogBuilder.java) `MaterialAlertDialog.MaterialComponents` `ThemeOverlay.MaterialComponents.MaterialAlertDialog` `alertDialogStyle` `materialAlertDialogTheme` [`AppCompatAutoCompleteTextView`](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatAutoCompleteTextView) `Widget.AppCompat.AutoCompleteTextView` `autoCompleteTextViewStyle` [`MaterialAutoCompleteTextView`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/textfield/MaterialAutoCompleteTextView.java) `Widget.MaterialComponents.AutoCompleteTextView.*` `ThemeOverlay.MaterialComponents.AutoCompleteTextView.*` `autoCompleteTextViewStyle` [`AppCompatButton`](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatButton) `Widget.AppCompat.Button` `buttonStyle` [`MaterialButton`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/button/MaterialButton.java) `Widget.MaterialComponents.Button` `materialButtonStyle` [`AppCompatCheckBox`](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatCheckBox) `Widget.AppCompat.CompoundButton.CheckBox` `checkboxStyle` [`MaterialCheckbox`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/checkbox/MaterialCheckBox.java) `Widget.MaterialComponents.CompoundButton.CheckBox` `checkboxStyle` [`AppCompatImageView`](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatImageView) N/A N/A [`ShapeableImageView`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/imageview/ShapeableImageView.java) `Widget.MaterialComponents.ShapeableImageView` N/A [`AppCompatRadioButton`](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatRadioButton) `Widget.AppCompat.CompoundButton.RadioButton` `radioButtonStyle` [`MaterialRadioButton`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/radiobutton/MaterialRadioButton.java) `Widget.MaterialComponents.CompoundButton.RadioButton` `radioButtonStyle` [`AppCompatTextView`](https://developer.android.com/reference/androidx/appcompat/widget/AppCompatTextView) `Widget.AppCompat.TextView` N/A [`MaterialTextView`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/textview/MaterialTextView.java) `Widget.MaterialComponents.TextView` N/A [`CardView`](https://developer.android.com/reference/androidx/cardview/widget/CardView) `CardView` `cardViewStyle` [`MaterialCardView`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/card/MaterialCardView.java) `Widget.MaterialComponents.CardView` `materialCardViewStyle` [`PopupMenu`](https://developer.android.com/reference/androidx/appcompat/widget/PopupMenu) `Widget.AppCompat.PopupMenu.*` `popupMenuStyle` N/A `Widget.MaterialComponents.PopupMenu.*` `popupMenuStyle` [`SwitchCompat`](https://developer.android.com/reference/androidx/appcompat/widget/SwitchCompat) `Widget.AppCompat.CompoundButton.Switch` `switchStyle` [`SwitchMaterial`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/switchmaterial/SwitchMaterial.java) `Widget.MaterialComponents.CompoundButton.Switch` `switchStyle` [`Toolbar`](https://developer.android.com/reference/androidx/appcompat/widget/Toolbar) `Widget.AppCompat.Toolbar` `toolbarStyle` [`MaterialToolbar`](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/appbar/MaterialToolbar.java) `Widget.MaterialComponents.Toolbar` `toolbarStyle`
 
Be sure to also check out the full list of [Android components](https://material.io/develop/android/components) for widgets new to MDC as well as usage documentation.
 
link
 
Copy link Link copied
 
## Example updates
 
Replaces widgets with MDC versions
 
In our example, we need to change some of the widgets in our layout to use MDC versions:
 
`xxxxxxxxxx`
 
`-< androidx . cardview . widget . CardView` `+< com . google . android . material . card . MaterialCardView` `android : id = "@+id/card"` `... >` `...` `-< /androidx.cardview.widget.CardView>` `+< /com.google.android.material.card.MaterialCardView>` `​` `-< androidx . appcompat . widget . SwitchCompat` `+< com . google . android . material . switch . SwitchMaterial` `android : id = "@+id/switch"` `... />`
 
link
 
Copy link Link copied
 
## Color
 
New attributes
 
The MDC color palette draws directly from the [Material Design color system](https://material.io/design/color/) .
 
As a result of the shared history between MDC-Android, AppCompat and the framework, the resulting set of color attributes comprises the following:
 
Existing attributes from the framework that are appropriately named (eg. `android:colorBackground` )
 
Existing attributes from AppCompat that are appropriately named (eg. `colorPrimary` and `colorError` )
 
New attributes introduced by MDC (eg. `colorSurface` , `colorOnPrimary` , etc.)
 MDC color attributes with baseline light theme values MDC color attributes with baseline dark theme values 
These attributes are used by MDC widgets to tint their backgrounds, text, icons and more. Knowing which widgets use which colors requires inspecting the default widget styles in the [source code](https://github.com/material-components/material-components-android) .
 
There are also colors from AppCompat and the framework that still exist but no longer apply to this new system. The `Theme.MaterialComponents.*` themes do their best to backport these old attributes for widgets that still rely on them, eg.
 
`xxxxxxxxxx`
 
`< item name = "colorAccent" >? attr / colorSecondary < /item>`
 
However, you should consider these attributes deprecated; either use a more appropriate MDC attribute or phase them out.
 
See the full color attribute mapping table below:
 
AppCompat / framework color attr MDC-Android color attr `colorPrimary` `colorPrimary` `colorPrimaryDark` `colorPrimaryVariant` (specify `android:statusBarColor` explicitly) N/A `colorOnPrimary` `colorAccent` `colorSecondary` N/A `colorSecondaryVariant` N/A `colorOnSecondary` N/A `colorSurface` N/A `colorOnSurface` `android:colorBackground` `android:colorBackground` N/A `colorOnBackground` `colorError` `colorError` N/A `colorOnError` `android:textColorPrimary` , `android:textColorSecondary` , etc. N/A (prefer MDC "on" attrs or use defaults) `colorControlNormal` , `colorControlHighlight` , `colorControlActivated` N/A (prefer MDC "on" attrs or use defaults) Note: These are still used to tint [`MaterialCheckBox`](https://github.com/material-components/material-components-android/tree/master/lib/java/com/google/android/material/checkbox/MaterialCheckBox.java#L119) , [`MaterialRadioButton`](https://github.com/material-components/material-components-android/tree/master/lib/java/com/google/android/material/radiobutton/MaterialRadioButton.java#L110) , [`SwitchMaterial`](https://github.com/material-components/material-components-android/tree/master/lib/java/com/google/android/material/switchmaterial/SwitchMaterial.java#L148) and [`MaterialToolbar` icons](https://github.com/material-components/material-components-android/tree/master/lib/java/com/google/android/material/appbar/res/values/styles.xml#L78) .
 
link
 
Copy link Link copied
 
## Example updates
 
Update to new color attributes
 
In our example, we need to update our app theme to override the preferred color attributes:
 `xxxxxxxxxx`
 
`< style name = "Theme.App" parent = "Theme.MaterialComponents.*" >` `...` `< item name = "colorPrimary" >@ color / navy_700 < /item>` `- < item name = "colorPrimaryDark" >@ color / navy_900 < /item>` `+ < item name = "colorPrimaryVariant" >@ color / navy_900 < /item>` `- < item name = "colorAccent" >@ color / green_300 < /item>` `+ < item name = "colorSecondary" >@ color / green_300 < /item>` `+ < item name = ”colorSecondaryVariant” >@ color / green_500 < /item>` `+ < item name = "android:statusBarColor" >@ color / navy_900 < /item>` `< /style>` 
Note: We have not overridden all of the color attributes and are relying on the defaults for `colorSurface` , `colorError` , etc, which is perfectly acceptable. We have also not specified a dark theme palette.
 
Use “on” color attributes where appropriate
 
We should also switch from using an `@color` to one of the new “on” color attributes for our contained button text color:
 
`xxxxxxxxxx`
 
`< Button` `- android : textColor = "@android:color/white"` `+ android : textColor = "?attr/colorOnPrimary"` `... />`
 
Example app with updated MDC color attributes (fixed FAB color)
 
link
 
Copy link Link copied
 
## Typography
 
New `TextAppearance` styles/attributes
 
The MDC type scales draw directly from the [Material Design type system](https://material.io/design/typography/) .
 
A new set of `TextAppearance.MaterialComponents.*` styles and corresponding `textAppearance*` theme attributes have been introduced, which replace existing AppCompat / framework styles.
 
MDC type attributes
 
These attributes are used by MDC widgets to style text. Knowing which widgets use which type scales requires inspecting the default widget styles in the [source code](https://github.com/material-components/material-components-android) .
 
See the full type style and attribute mapping table below:
 
AppCompat text style MDC-Android text style MDC-Android text attr `TextAppearance.AppCompat.Display4` `TextAppearance.MaterialComponents.Headline1` `textAppearanceHeadline1` `TextAppearance.AppCompat.Display3` `TextAppearance.MaterialComponents.Headline2` `textAppearanceHeadline2` `TextAppearance.AppCompat.Display2` `TextAppearance.MaterialComponents.Headline3` `textAppearanceHeadline3` `TextAppearance.AppCompat.Display1` `TextAppearance.MaterialComponents.Headline4` `textAppearanceHeadline4` `TextAppearance.AppCompat.Headline` `TextAppearance.MaterialComponents.Headline5` `textAppearanceHeadline5` `TextAppearance.AppCompat.Title` `TextAppearance.AppCompat.Large` `TextAppearance.MaterialComponents.Headline6` `textAppearanceHeadline6` `TextAppearance.AppCompat.Subhead` `TextAppearance.AppCompat.Menu` `TextAppearance.MaterialComponents.Subtitle1` `textAppearanceSubtitle1` `TextAppearance.AppCompat.Small` `TextAppearance.MaterialComponents.Subtitle2` `textAppearanceSubtitle2` `TextAppearance.AppCompat.Body1` `TextAppearance.MaterialComponents.Body1` `textAppearanceBody1` `TextAppearance.AppCompat.Body2` `TextAppearance.MaterialComponents.Body2` `textAppearanceBody2` `TextAppearance.AppCompat.Button` `TextAppearance.MaterialComponents.Button` `textAppearanceButton` `TextAppearance.AppCompat.Caption` `TextAppearance.MaterialComponents.Caption` `textAppearanceCaption` N/A `TextAppearance.MaterialComponents.Overline` `textAppearanceOverline`
 
link
 
Copy link Link copied
 
## Example updates
 
Update to new type attributes
 
In our example, we need to update the `TextView` s within the card in the layout to use the preferred type attributes:
 
`xxxxxxxxxx`
 
`< com . google . android . material . card . MaterialCardView` `... >` `...` `< TextView` `android : id = ” @+ id / headerText”` `- android : textAppearance = "@style/TextAppearance.AppCompat.Title"` `+ android : textAppearance = "?attr/textAppearanceHeadline6"` `... />` `< TextView` `android : id = ” @+ id / subheadText”` `android : textColor = "?android:attr/textColorSecondary"` `- android : textAppearance = "@style/TextAppearance.AppCompat.Body2"` `+ android : textAppearance = "?attr/textAppearanceBody2"` `... />` `< TextView` `android : id = ” @+ id / supportingText”` `android : textColor = "?android:attr/textColorSecondary"` `- android : textAppearance = "@style/TextAppearance.AppCompat.Body2"` `+ android : textAppearance = "?attr/textAppearanceBody2"` `... />` `< /com.google.android.material.card.MaterialCardView>`
 
Customize type scales with font family
 
We can also optionally override type scales in our app theme to use a custom font family, with [XML](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml) or [downloadable](https://developer.android.com/guide/topics/ui/look-and-feel/downloadable-fonts) fonts via Android Studio:
 
`xxxxxxxxxx`
 
`< style name = "Theme.App" parent = "Theme.MaterialComponents.*" >` `...` `+ < item name = "textAppearanceHeadline6" >@ style / TextAppearance . App . Headline6 < /item>` `+ < item name = "textAppearanceBody2" >@ style / TextAppearance . App . Body2 < /item>` `< /style>` `​` `+< style name = "TextAppearance.App.Headline6"` `+ parent = "TextAppearance.MaterialComponents.Headline6" >` `+ < item name = "fontFamily" >@ font / roboto_mono_medium < /item>` `+< /style>` `+< style name = "TextAppearance.App.Body2"` `+ parent = "TextAppearance.MaterialComponents.Body2" >` `+ < item name = "fontFamily" >@ font / roboto_mono_regular < /item>` `+< /style>`
 
Note: For this example, we have only overridden some of the type scales. If you’re using a custom font, we recommend overriding [all of the type scales](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/typography/res/values/attrs.xml) for brand consistency.
 
Example app with updated MDC type attributes (updated font family)
 
link
 
Copy link Link copied
 
## Shape
 
`ShapeAppearance` styles/attributes
 
The [Material Design shape system](https://material.io/design/shape/) is a way to apply treatments to the corners of MDC widgets, split into small, medium and large component categories.
 
This takes the form of Android `ShapeAppearance.*` styles with corresponding theme attributes. They include a `cornerFamily` — `rounded` or `cut` — and `cornerSize*` as a dimension.
 
MDC shape attributes
 
These attributes are used by MDC widgets to style their backgrounds. Knowing which widgets apply to which shape categories requires inspecting the default widget styles in the [source code](https://github.com/material-components/material-components-android) .
 
link
 
Copy link Link copied
 
## Widget backgrounds
 
The class that implements this functionality is `[MaterialShapeDrawable](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/shape/MaterialShapeDrawable.java)` . All MDC widgets use this drawable as their background by default and you can also consider using it for custom views. It handles shape theming, backported shadow rendering, dark theme elevation overlays and more.
 
As a result, we advise against using `android:background` with custom XML drawables on MDC widgets as this will override the `MaterialShapeDrawable` . You may notice that the default styles for most MDC widgets specify
 
`xxxxxxxxxx`
 
`< item name = "android:background" >@ null < /item>`
 
to specifically avoid this. Rather, prefer using `shapeAppearance` / `shapeAppearanceOverlay` and `backgroundTint` attributes to adjust background shape and color.
 
However, there are exceptions:
 
As mentioned above, `MaterialButton` [ignored `android:background`](https://issuetracker.google.com/issues/127420890) until [release](https://github.com/material-components/material-components-android/releases/tag/1.2.0-alpha06) [1.2.0-alpha06](https://github.com/material-components/material-components-android/releases/tag/1.2.0-alpha06) [of MDC-Android](https://github.com/material-components/material-components-android/releases/tag/1.2.0-alpha06) . If you require this functionality while using earlier versions of the library, we advise explicitly using `AppCompatButton` in your layout(s).
 
`MaterialShapeDrawable` [doesn’t support gradients](https://issuetracker.google.com/issues/134526677) . If your brand requires this, using `android:background` with a `GradientDrawable` is your best bet.
 
link
 
Copy link Link copied
 
## Example updates
 
Remove background attrs that do not work with shape theming
 
In our example, we can remove some widget attributes that are now handled by shape theming:
 
`xxxxxxxxxx`
 
`< com . google . android . material . bottomnavigation . BottomNavigationView` `- android : background = "@android:color/white"` `... />` `​` `< com . google . android . material . card . MaterialCardView` `- app : cardCornerRadius = "2dp"` `... >` `...` `< /com.google.android.material.card.MaterialCardView>`
 
Customize shape with corner family and size
 
We can also optionally override shape styles in our app theme to express our brand:
 
`xxxxxxxxxx`
 
`< style name = "Theme.App" parent = "Theme.MaterialComponents.*" >` `...` `+ < item name = "shapeAppearanceSmallComponent" >@ style / ShapeAppearance . App . SmallComponent < /item>` `+ < item name = "shapeAppearanceMediumComponent" >@ style / ShapeAppearance . App . MediumComponent < /item>` `+ < item name = "shapeAppearanceLargeComponent" >@ style / ShapeAppearance . App . LargeComponent < /item>` `< /style>` `​` `+< style name = "ShapeAppearance.App.SmallComponent"` `+ parent = "ShapeAppearance.MaterialComponents.SmallComponent" >` `+ < item name = "cornerFamily" > rounded < /item>` `+ < item name = "cornerSize" > 8 dp < /item>` `+< /style>` `+< style name = "ShapeAppearance.App.MediumComponent"` `+ parent = "ShapeAppearance.MaterialComponents.MediumComponent" >` `+ < item name = "cornerFamily" > rounded < /item>` `+ < item name = "cornerSize" > 12 dp < /item>` `+< /style>` `+< style name = "ShapeAppearance.App.LargeComponent"` `+ parent = "ShapeAppearance.MaterialComponents.LargeComponent" >` `+ < item name = "cornerFamily" > rounded < /item>` `+ < item name = "cornerSize" > 16 dp < /item>` `+< /style>`
 
Example app with updated MDC shape attributes (updated corner radii)
 
Restore button custom gradient background
 
Finally, here’s how to restore our button’s custom gradient background by explicitly using AppCompatButton (along with the new MDC button type theming attribute):
 
`xxxxxxxxxx`
 
`-< Button` `+< androidx . appcompat . widget . AppCompatButton` `android : background = "@drawable/bg_button_gradient"` `+ android : textAppearance = "?attr/textAppearanceButton"` `... />`
 
If you’re using MDC-Android `1.2.0-alpha-06` (or later) then you can rely on `MaterialButton` respecting `android:background` . Keep in mind that you may need to clear the `backgroundTint` (which is set to `colorPrimary` in the `Widget.MaterialComponents.Button` default style):
 
`xxxxxxxxxx`
 
`< Button` `android : background = "@drawable/bg_button_gradient"` `+ app : backgroundTint = "@null"` `... />`
 
Button with restored custom gradient background
 
link
 
Copy link Link copied
 
## What’s next?
 
We’ve successfully gone through the process of migrating from the Design Support Library, to MDC `1.0.0` and finally to MDC `1.1.0` . We’ve migrated our usages of AppCompat and have made use of Material Theming.
 
We encourage you to try out new widgets and features in MDC that were not part of the Design Support Library.
 
The next feature release of MDC — `1.2.0` — is well underway with multiple alpha releases out at the time of writing. Exciting new updates include `[Slider](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/slider/Slider.java)` and `[ShapeableImageView](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/imageview/ShapeableImageView.java)` components along with the first Android release of the [Material motion system](https://material.io/design/motion/the-motion-system.html) !
 
As always, we encourage you to file [bug reports](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BComponent+name%5D+Short+description+of+issue) and [feature requests](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=feature+request&template=feature_request.md&title=%5BComponent+name%5D+Short+description+of+request) on GitHub. Also be sure to check out our Android [companion example apps](https://github.com/material-components/material-components-android-examples) and [Build a Material Theme](https://github.com/material-components/material-components-android-examples/tree/develop/MaterialThemeBuilder) .
 
We highly encourage migrating to MDC `1.1.0` (or later). If you’ve successfully migrated or if you’re having trouble doing so, reach out to us on Twitter [@MaterialDesign](https://twitter.com/materialdesign) and [@AndroidDev](https://twitter.com/AndroidDev) .
