# MDC-Android Stable release 1.7.0

> Source: https://m3.material.io/blog/android-stable-release-1-7-0

Posted by
 James Williams , Material Developer Advocate
 The latest releases of Material Design Components (MDC) - 1.7.0 brings updates to Material You styling, accessibility and size coherence and new minimum version requirements
 
MDC 1.7.0 has new minimum version requirements:
 
Java 8 (1.8), previously Java 7 (1.7)
 
Android Gradle Plugin (AGP) 7.3.3, previously 4.0.0
 
Android Studio Chipmunk, version 2021.2.1
 
This is a fairly large jump in terms of the Gradle plugin version, so make sure to secure changes in your build files first before moving on to UI code. As always, our release notes contain the full details of what has been updated. There are a couple standout updates we’d like to highlight.
 
link
 
Copy link Link copied
 
## MaterialSwitch component
 
The Switch component has undergone a visual refresh that increases contrast and accessibility. The `MaterialSwitch` class replaces the previous `SwitchMaterial` class.
 
It now differentiates between the on and off states more by making the “on” thumb larger and able to contain an icon in addition to an on state color. The “off” state has a smaller thumb with less contrast.
 
Much of the new component’s core API aligns with the obsolete `SwitchMaterial` class so to get started, you can simply replace the class references.
 
For more information on how the obsolete component stacks against the new implementation, [check the documentation on GitHub](https://github.com/material-components/material-components-android/blob/master/docs/components/Switch.md) .
 
link
 
Copy link Link copied
 
## Shape Theming
 
A component’s shape is one way to express your brand. In addition to providing a custom [MaterialShapeDrawable](https://developer.android.com/reference/com/google/android/material/shape/MaterialShapeDrawable) , there is also a means to more simply customize shape theming using rounded or cut corners.
 
Material 3 components have been updated to apply one of the seven styles ranging from None to Full. A component’s shape is defined by two properties: its Shape family, either rounded or cut, and its value, usually described in dp. Where a “none” style always results in a rectangular shape, the resulting shape for full depends on the shape family. Rounded returns a rectangle with fully rounded edges, while Cut returns a hexagonal shape.
 
You are able to set the shape family and value individually and arbitrarily on each edge but there are set intervals and baseline values.
 
Shape Style Value None 0dp Extra Small 4dp Small 8dp Medium 12dp Large 16dp Extra Large 28dp Full N/A
 
Default theming will apply the same shape family and value on all four edges. You can apply shape family and shape style (or alternatively a custom value) independently on each corner.
 
The Shape Theming card in the Catalog app allows you to see how different values affect rounded or cut corners.
 
link
 
Copy link Link copied
 
## What’s next for MDC ?
 
We’re fast at work on the next major version of MDC. You can follow the progress, file [bug reports](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BComponent+name%5D+Short+description+of+issue) and [feature requests](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=feature+request&template=feature_request.md&title=%5BComponent+name%5D+Short+description+of+request) on GitHub. Also feel free to reach out to us on [Twitter](https://twitter.com/materialdesign) .
