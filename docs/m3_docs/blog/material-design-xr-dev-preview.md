# Material Design for XR (Developer Preview)

> Source: https://m3.material.io/blog/material-design-xr-dev-preview

Posted by
 Yasmine Evjen , Senior Product Manager
 Android is expanding into extended reality, so your app can be viewed in 3D space, whether in virtual reality or blended with the user's surroundings through passthrough.
 
Today, we’re releasing the [Android XR SDK](https://developer.android.com/develop/xr) developer preview, a software development kit to let you build XR apps using familiar Android frameworks and tools. This release also includes [Android XR design guidelines](https://developer.android.com/design/ui/xr) and [developer documentation](https://developer.android.com/develop/xr) to help you create immersive experiences.
 
The [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk) allows you to enhance your existing Android app for XR and see it come to life in the Android XR emulator in [Android Studio](https://developer.android.com/develop/xr/jetpack-xr-sdk/studio-tools) . [Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui) provides an easy onboarding to declaratively build spatial UI layouts, with established concepts such as rows and columns. Material Design for XR provides design guidance and code for spatial adaptations of components and layouts, to help you prepare your apps for this new environment.
 
In addition, we are launching advanced perception capabilities with [ARCore for Jetpack XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore) , as well as [SceneCore](https://developer.android.com/develop/xr/jetpack-xr-sdk#jetpack-scenecore) , our new 3D scene graph library for custom 3D manipulation.
 
link
 
Copy link Link copied
 
## Android apps in XR
 
Android XR is a flexible platform that lets you bring your app into extended reality. [Compatible](https://developer.android.com/develop/xr/get-started#app-manifest) Android mobile and [large-screen apps](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality) will work with no development lift and are automatically available in the Play Store.
 
If you already have a mobile or large screen app on Android, the Jetpack XR SDK can extend your app into a new dimension by spatializing existing layouts and enhancing your experiences with 3D models and immersive environments. Learn how to [bring your Android app into 3D with XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing) .
 
The [Android XR design guidelines](https://developer.android.com/design/ui/xr/) provide a roadmap for creating exceptional XR experiences. Explore key considerations, system foundations, and best practices for designing interactions, spatial UI, 3D content, and immersive environments. Learn how to [develop UI with Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui) .
 
To help you build integrated and boundless experiences, Android XR includes [multimodal inputs](https://developer.android.com/design/ui/xr/guides/foundations#design-multimodal) , and [spatial capabilities](http://developer.android.com/design/ui/xr/guides/spatial-ui) . Users can experience your app in two modes: [Home Space](https://developer.android.com/design/ui/xr/guides/foundations) and [Full Space](https://developer.android.com/design/ui/xr/guides/foundations) . In Home Space, a user is able to multitask with your app running side by side with other apps. In Full Space, your app takes center stage as the focus of the user's experience with full access to the spatial and 3D capabilities of Android XR.
 In Home Space, a user is able to multitask with your app running side by side with other apps. In Full Space, your app takes center stage as the focus of the user's experience with full access to the spatial and 3D capabilities of Android XR. 
link
 
Copy link Link copied
 
## Material Design for XR
 
The Material 3 (or M3) library now includes adaptations to help your app stand out in spatial environments. We've also added design guidance for navigation components and layouts, making it easier to create immersive and user-friendly XR experiences.
 
When designing for XR, you may want to use [spatial UI](http://developer.android.com/design/ui/xr/guides/spatial-ui) to place content in a user’s physical or virtual environment. You can break out your app into spatial panels, orbiters, and add spatial elevation.
 
Spatial panels allow you to take advantage of the infinite canvas that Android XR provides, breaking out your existing UI content into panels that are resizable and moveable by the user. Orbiters are floating UI elements that control the content within spatial panels. They give the app’s main content more space, and users can quickly access features while the content remains visible. Adding spatial elevation to a component raises it above the spatial panel on the Z-axis. This can help get a user's attention, create better visual hierarchy, and improve legibility.
 
Spatial UI behaviors in Material Design components and adaptive layouts will help your app adapt naturally to 3D space.
 Material Design adaptive components and layouts for XR 
link
 
Copy link Link copied
 
## XR adaptations
 
Android XR gives you the flexibility to design a spacious UI that adapts seamlessly to an unlimited display. If you’re building with the latest alpha of Material Design components and [adaptive layouts](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/package-summary) , you may add the `EnableXrComponentOverrides` wrapper to opt into XR changes in your app. This includes placing navigation controls in orbiters—such as the navigation rail and navigation bar—as well as placing panes into spatial panels.
 
### Navigation rail
 
The navigation rail in any Compose layout including [`NavigationSuiteScaffold`](https://developer.android.com/develop/ui/compose/layouts/adaptive/build-adaptive-navigation) will automatically adapt to an XR orbiter. For more information, read [Material Design guidelines](https://m3.material.io/components/navigation-rail/xr) .
 Non-spatialized navigation rail Spatialized (XR-adapted) navigation rail 
### Navigation bar
 
Likewise, the navigation bar in any Compose layout including [`NavigationSuiteScaffold`](https://developer.android.com/develop/ui/compose/layouts/adaptive/build-adaptive-navigation) will automatically adapt to an XR orbiter. For more information, read [Material Design guidelines](https://m3.material.io/components/navigation-bar/xr) .
 Non-spatialized navigation bar Spatialized (XR-adapted) navigation bar 
### List-detail layout for XR
 
[Compose Material 3 Adaptive Layouts](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive) in XR have a 1:1 mapping where each pane becomes an XR spatial panel. Learn more about [`ListDetailPaneScaffold`](https://developer.android.com/develop/ui/compose/layouts/adaptive/list-detail) and [adaptive design guidelines](https://m3.material.io/foundations/adaptive-design) .
 Non-spatialized ListDetailPaneScaffold Spatialized (XR-adapted) ListDetailPaneScaffold 
### Supporting pane layout for XR
 
[Compose Material 3 Adaptive Layouts](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive) in XR also have a 1:1 mapping where each pane becomes an XR spatial panel. Learn more about [`SupportingPaneScaffold`](https://developer.android.com/develop/ui/compose/layouts/adaptive/build-a-supporting-pane-layout) and [adaptive design guidelines](https://m3.material.io/foundations/adaptive-design) .
 Non-spatialized SupportingPaneScaffold Spatialized (XR-adapted) SupportingPaneScaffold 
link
 
Copy link Link copied
 
## Start building with Material Design for XR
 
### Design with the Material 3 Design Kit for Figma
 
In the Figma design kit, you’ll be able to start designing with navigation components as orbiters.
 
Download the [Material 3 Design Kit](https://www.figma.com/community/file/1035203688168086460) to get started
 
### EnableXrComponentOverrides to adapt your existing app
 
All M3 Compose UI inside of the [`EnableXrComponentOverrides`](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/package-summary#EnableXrComponentOverrides(androidx.xr.compose.material3.XrComponentOverrideEnabler,kotlin.Function0)) wrapper will adapt on XR devices. Add the [`EnableXrComponentOverrides`](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/package-summary#EnableXrComponentOverrides(androidx.xr.compose.material3.XrComponentOverrideEnabler,kotlin.Function0)) wrapper to [adapt your app to Material Design for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design) .
 
### Develop spatial UI with Jetpack Compose for XR
 
With Jetpack Compose for XR, you can declaratively build your spatial UI layouts using familiar Compose concepts such as rows and columns, including new components, spatial panels and orbiters. Start building with our [new subspace and spatial components](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui) .
 
link
 
Copy link Link copied
 
## Designing the future together
 
This is our initial developer preview of the Android XR SDK. We’re continuing to extend the design and developer tools you know and love to Android XR. We welcome your feedback, and want to make our developer platform work better for you.
 
[Share your feedback](https://developer.android.com/develop/xr/support)
