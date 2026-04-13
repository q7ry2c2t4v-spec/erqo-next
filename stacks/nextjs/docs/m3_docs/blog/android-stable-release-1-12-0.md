# Material Design Components for Android 1.11.0 and 1.12.0

> Source: https://m3.material.io/blog/android-stable-release-1-12-0

Posted by
 James Williams , Material Developer Advocate
 Material Design Components versions 1.11 and 1.12 come on the eve of our yearly developer conference Google I/O and offer a number of new options for Carousel control, an expansion to color theming, and non-text contrast updates for progress indicators and sliders. The minimum SDK version for MDC Views raises to API 19 in version 1.12, similar to the rest of AndroidX. 1.12 also updates its dependency on androidx.transition (used in SharedElement transitions, Fade, and [Predictive Back animations](https://developer.android.com/guide/navigation/custom-back/support-animations) ) to version 1.5.0 from 1.2.0.
 
link
 
Copy link Link copied
 
## Carousel Updates
 
In the [last post](https://material.io/blog/android-stable-release-1-10-0) we announced a new Carousel strategy, HeroCarouselStrategy, that can be used to showcase large, more immersive content. In MDC 1.11, we’ve added two new strategies - UncontainedCarouselStrategy and FullscreenCarouselStrategy. Additionally, we’ve added the option to center-align any carousel so large, focal items can be placed in the center of the scroll container.
 Start-aligned HeroCarouselStrategy Center-aligned HeroCarouselStrategy 
`UncontainedCarouselStrategy` doesn’t alter the aspect ratio of the carousel items. This is a useful strategy when altering an item’s size could detract from its meaning - for example, a carousel of album covers might benefit from retaining a recognizable 1:1 aspect ratio.
 
`FullScreenCarouselStrategy` allows a single item to take all the available space in a container. This is useful for fully immersive content like video or slideshows where items are interacted with, or viewed, one-at-a-time. We only recommend using this strategy in the vertical orientation.
 
Item Snapping
 
`CarouselSnapHelper` allows your carousels to give focus to the nearest item. They can be used on all strategies but are strongly encouraged on hero carousels and full-screen carousels.
 `val snapHelper = CarouselSnapHelper ()` `snapHelper . attachToRecyclerView ( carouselRecyclerView )` 
link
 
Copy link Link copied
 
## Color Changes
 
API 34 has an [expanded color set](https://github.com/material-components/material-components-android/blob/master/docs/theming/Color.md) giving you more ways to personalize your apps. Some of the additions like the new surface options have been incorporated in components. Fixed and Dim colors on the other hand are developer options but not used by the component set at time of writing.
 
System UI access to named color roles
 
Before API 34, when you used dynamic color, the color was stored as individual tones of the color palettes. MDC would map those colors to [dynamic color properties and then assign those properties to color roles](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/color/res/values-v31/tokens.xml) .
 ​ x
 
`<!-- Primary colors -->` `< color name = "m3_sys_color_dynamic_dark_primary" >@ color / m3_ref_palette_dynamic_primary80 < /color>` `< color name = "m3_sys_color_dynamic_dark_on_primary" >@ color / m3_ref_palette_dynamic_primary20 < /color>` `< color name = "m3_sys_color_dynamic_dark_primary_container" >@ color / m3_ref_palette_dynamic_primary30 < /color>` `< color name = "m3_sys_color_dynamic_dark_on_primary_container" >@ color / m3_ref_palette_dynamic_primary90 < /color>` `​` `<!-- Baseline palette – Primary -->` `< color name = "m3_ref_palette_dynamic_primary100" >@ android : color / system_accent1_0 < /color>` `< color name = "m3_ref_palette_dynamic_primary99" >@ android : color / system_accent1_10 < /color>` `< color name = "m3_ref_palette_dynamic_primary95" >@ android : color / system_accent1_50 < /color>` `< color name = "m3_ref_palette_dynamic_primary90" >@ android : color / system_accent1_100 < /color>` 
As of API 34, the traversal is more direct and compact. Material color roles directly map to color resources from [`@android:color` namespace](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/color/res/values-v34/tokens.xml) .
 `xxxxxxxxxx`
 
`< color name = "m3_sys_color_dynamic_light_primary" >@ android : color / system_primary_light < /color>` `< color name = "m3_sys_color_dynamic_light_on_primary" >@ android : color / system_on_primary_light < /color>` `< color name = "m3_sys_color_dynamic_light_primary_container" >@ android : color / system_primary_container_light < /color>` `< color name = "m3_sys_color_dynamic_light_on_primary_container" >@ android : color / system_on_primary_container_light < /color>` `​` `< color name = "m3_sys_color_dynamic_dark_primary" >@ android : color / system_primary_dark < /color>` `< color name = "m3_sys_color_dynamic_dark_on_primary" >@ android : color / system_on_primary_dark < /color>` `< color name = "m3_sys_color_dynamic_dark_primary_container" >@ android : color / system_primary_container_dark < /color>` `< color name = "m3_sys_color_dynamic_dark_on_primary_container" >@ android : color / system_on_primary_container_dark < /color>` 
Fixed and Fixed Dim
 
Fixed and Fixed Dim color roles are new additions to the color spec. Fixed color roles do not change between light and dark themes. Dim color roles offer a less emphasized option to the associated color role. Neither of these categories of color roles are used in components but are available to further customize your UIs.
 
Surfaces
 
Previously in Material themes, we provided a single surface color value and calculated interpolated variants of it at runtime by blending with the primary color (based on elevation). This was frustrating for developers and designers when it came to implementing UIs because they were unable to assign those colors directly.
 
Color roles simulating different elevation levels have been added to theming. There are now three surface color options and five surface container options.
 
Surface Bright is guaranteed to be the lightest surface color.
 
Surface is largely unchanged from previous versions.
 
Surface Dim is equivalent or darker than its relative Surface color role.
 
Surface Container Lowest, Low, High and Highest are additional color roles that can provide more or less emphasis in contrast to Surface Container.
 
These components use some of the new surface container color roles:
 [Elevated Button](https://m3.material.io/components/buttons/specs)
 
[Bottom App Bar](https://m3.material.io/components/bottom-app-bar/specs)
 
[Navigation Bar](https://m3.material.io/components/navigation-bar/specs)
 
[Bottom Sheet](https://m3.material.io/components/bottom-sheets/specs)
 
[Modal Side Sheet](https://m3.material.io/components/side-sheets/specs)
 
[Elevated Card](https://m3.material.io/components/cards/specs)
 
[Elevated Chips](https://m3.material.io/components/chips/specs)
 
[Datepicker](https://m3.material.io/components/date-pickers/specs)
 
[Dialogs](https://m3.material.io/components/dialogs/specs) [Surface FAB](https://m3.material.io/components/floating-action-button/specs) / [Surface exFAB](https://m3.material.io/components/extended-fab/specs)
 
[Menu](https://m3.material.io/components/menus/specs)
 
[Navigation Drawer](https://m3.material.io/components/navigation-drawer/specs)
 
[Search](https://m3.material.io/components/search/specs)
 
[Switch](https://m3.material.io/components/switch/specs)
 
[Text Fields](https://m3.material.io/components/text-fields/specs)
 
[Timepicker](https://m3.material.io/components/time-pickers/specs)
 
[Top App Bar](https://m3.material.io/components/top-app-bar/specs) 
The new color roles are already available in [Material Theme Builder](https://material-foundation.github.io/material-theme-builder/) .
 
Non-Text Contrast Updates (NTC) for Progress Indicators and Sliders
 
Non-text contrast standards involve first evaluating which parts of controls are essential to demark their state, interactivity options, and legibility and secondly making changes to improve the identified attributes and making sure those portions have a minimum contrast ratio (3:1 in standard contrast at time of writing). Progress Indicators and Sliders have been updated to implement these standards.
 
Progress indicators
 
The NTC changes to progress indicators include a clearly identified gap between the active and inactive tracks for linear progress indicators. In circular progress indicators, the pre-1.12 version does not by default include a track making it more difficult to estimate its value. An inactive track is now drawn to complete the full circle with gaps on both ends where the track meets the active indicator.
 
A number of these options such as the size of the gap size and track attributes are addressable in XML code. You can see the full listing [here](https://github.com/material-components/material-components-android/blob/master/docs/components/ProgressIndicator.md) .
 MDC 1.11 version of Progress Indicators Basic Progress Indicator Options Advanced Progress Indicator Options 
Sliders
 
Sliders have undergone similar changes to progress indicators. There are now gaps between the active and inactive tracks.The default thumb for sliders has also changed from a connected filled circle to a vertical bar with configurable gaps on each side. The shape for formatted labels have also undergone a few tweaks to assist with NTC.
 
As is the case with progress indicators, you can configure these attributes inXML code. You can see the full listing [here](https://github.com/material-components/material-components-android/blob/master/docs/components/Slider.md) .
 MDC 1.11 version of Sliders Basic Slider Options Advanced Slider Options 
link
 
Copy link Link copied
 
## What’s next for MDC?
 
We’re hard at work on the 1.13.0 release. The components or features we highlight in these posts are only a fraction of the work that lands in each release. Check out the [release notes](https://github.com/material-components/material-components-android/releases/tag/1.12.0) for a full listing.
 
You can follow the progress of new versions, file [bug reports](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BComponent+name%5D+Short+description+of+issue) and submit [feature requests](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=feature+request&template=feature_request.md&title=%5BComponent+name%5D+Short+description+of+request) on GitHub. Check out the [catalog app](https://github.com/material-components/material-components-android/releases/download/1.12.0/catalog-debug.apk) to see the components in action. Also feel free to reach out to us on Twitter [@materialdesign](https://twitter.com/materialdesign) .
