# Material Design 3 for Compose 1.2

> Source: https://m3.material.io/blog/material-3-compose-1-2

Posted by
 James Williams , Material Developer Advocate
 The 1.2 release of Compose Material 3 is here, and with it comes new components, some component changes and an expansion of the Material3 color system.
 
link
 
Copy link Link copied
 
## Component Changes, Demotions and Promotions
 
`Segmented Button` is a new experimental component. There are single select and multiple selection variants.
 
`BottomAppBar` has a `BottomAppBarScrollBehavior` to auto-hide itself when content is scrolled.
 
`SwipeToDismiss` has been refactored into `SwipeDismissBox` and remains in experimental status.
 
`Badge` and `BadgedBox` have been promoted to stable.
 
The `Chip` APIs have been promoted to stable.
 
link
 
Copy link Link copied
 
## Color Changes
 
Material3 Compose 1.2 has an expanded color set giving you more ways to personalize your apps. Notable additions are more surface options to represent emphasis of information in your UIs. Components have been updated to make fuller use of the new surface values.
 
A small implementation note is that the ColorScheme object is now immutable allowing Jetpack Compose to skip it and possibly optimize successive compositions when the object hasn’t changed.
 
If your code currently modifies the colors in [ColorScheme](https://developer.android.com/reference/kotlin/androidx/compose/material3/ColorScheme) directly, you will need to make use of the [copy](https://developer.android.com/reference/kotlin/androidx/compose/material3/ColorScheme#copy(androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color)) method now to change colors.
 
#### Surfaces
 
Previously in Material, we provided a single surface value and calculated interpolated variants of it at runtime by blending with the primary color. This was frustrating for developers and designers when it came to implementing UIs because they were unable to assign those colors directly.
 
Color roles simulating different elevation levels have been added to theming. There are now three surface color options and five surface container options.
 
`Surface Bright` is guaranteed to be the lightest surface color. It is not currently in use by any of our provided components.
 
`Surface` was the former backing color for many components. It has been replaced largely by the five surface container in 1.2. It is still in the spec so your components using it will not break.
 
`Surface Dim` is guaranteed to be the darkest surface color. Like Surface Bright, they are not in use in any existing components.
 
`Surface Container Lowest` , `Low` , `High` and `Highest` are additional color roles that can provide more or less emphasis in contrast to Surface Container.
 
The new color roles are already available in [Material Theme Builder](https://material-foundation.github.io/material-theme-builder/) .
 
link
 
Copy link Link copied
 
## Where can I find more information about Material Compose ?
 
The components or features we highlight in these posts are only a fraction of the work that lands in each release. Check out the [release notes](https://developer.android.com/jetpack/androidx/releases/compose-material3) for a full listing.
 
You can file [bug reports](https://b.corp.google.com/issues/new?component=742043&template=1346811) and follow [open issues](https://b.corp.google.com/issues?q=componentid:742043%20status:open) on Buganizer. You can also follow the progress of new versions on [cs.android.com](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/;bpv=1;bpt=0) . Check out the [catalog app](https://play.google.com/store/apps/details?id=androidx.compose.material.catalog) to see the components in action.
