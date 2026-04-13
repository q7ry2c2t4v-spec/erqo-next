# Android Stable Release from Material.io - Version 1.8.0

> Source: https://m3.material.io/blog/android-stable-release-1-8-0

Posted by
 James Williams , Material Developer Advocate
 The new year brings with it two new components that can redefine how users navigate in and interact with your applications: search and side sheets.
 
link
 
Copy link Link copied
 
## SearchBar
 
The SearchBar component allows you to bring a well-understood navigation pattern to your apps that your users will have seen many times before across Google apps.
 
SearchBar provides a floating search field that extends Toolbar. That means you can use navigation icons, menu items, or any other APIs you’ve already been using with Toolbars. When using SearchBar within a CoordinatorLayout parent, you can set SearchBar’s scrolling behavior to control how it responds to scrolling.
 
link
 
Copy link Link copied
 
## SearchView
 
SearchView offers a full-screen search view. When used with SearchBar, SearchView provides an immersive search experience, with seamless transitions between the smaller SearchBar and the full-screen SearchView.
 
SearchView's header is similar to SearchBar; it supports navigation, text entry/hinting, and actions. Below the header, SearchView also holds search results, previous search queries, and suggestions/helper text.
 For more information on integrating the new Material Search components into your app, check out the full [developer documentation](https://github.com/material-components/material-components-android/blob/master/docs/components/Search.md) . 
link
 
Copy link Link copied
 
## Side Sheets
 
Side sheets are surfaces that contain supplementary content related to a screen anchored to the side. [Design guidance](https://m2.material.io/components/sheets-side) has existed for a while, but this release provides a working implementation (see [Material 3 guidance](https://m3.material.io/components/side-sheets/overview) ). Similar to bottom sheets, there is no explicit SideSheet tag. A `CoordinatorLayout` child view with a SideSheetBehavior, either in layout XML or programmatically in code, will be recognized as a side sheet.
 
Your application’s needs and screen real estate will determine which side sheet option will work best.
 
link
 
Copy link Link copied
 
## Types of Side Sheets
 
#### Standard Side Sheets
 
Standard side sheets allow the user to view and interact with the side sheet and the visible portion of the main content at the same time. These are well suited to large screens or foldables in tablet mode and are not recommended for smaller screens; opt for modal side sheets on narrower screens.
 
#### Modal Side Sheets
 
Modal side sheets are more useful on smaller screens. They appear above the main content and block interaction with content outside their bounds. User actions outside the side sheet will dismiss the modal sheet.
 
#### Coplanar Side Sheets
 
Coplanar side sheets are a more responsive version of standard sheets; coplanar sheets squash the main content as they expand, resizing the container's dimensions during the sheet's expansion animation. The main content remains fully visible and open for interaction while the sheet is expanded. When the sheet is dismissed, the main content container automatically resizes to its former dimensions alongside the sheet's dismiss animation.
 
Like standard sheets, coplanar sheets are recommended for large screens and foldable devices, and are not recommended for smaller screens.
 
For more information on integrating the new Material Side Sheet components into your app, check out the full [developer documentation](https://github.com/material-components/material-components-android/blob/master/docs/components/SideSheet.md) .
 
link
 
Copy link Link copied
 
## What’s next for MDC?
 
We’re hard at work on the 1.9.0 release featuring [a Carousel component powered by RecyclerView](https://github.com/material-components/material-components-android/releases/tag/1.9.0-alpha01) . The components or features we highlight in these posts are only a fraction of the work that lands in each release. Check out the [1.8.0 release notes](https://github.com/material-components/material-components-android/releases/tag/1.8.0) for a full listing.
 
You can follow the progress of new versions, file [bug reports](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BComponent+name%5D+Short+description+of+issue) and submit [feature requests](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=feature+request&template=feature_request.md&title=%5BComponent+name%5D+Short+description+of+request) on GitHub. Check out the [catalog app](https://github.com/material-components/material-components-android/releases/download/1.8.0/catalog-debug.apk) to see the components in action. Also feel free to reach out to us on Twitter [@materialdesign](https://twitter.com/materialdesign) .
