# Material Design Components for Android 1.5.0

> Source: https://m3.material.io/blog/android-stable-release-1-5

Posted by
 James Williams , Material Developer Advocate
 Back in October, at [Android Dev Summit](https://developer.android.com/events/dev-summit) , we released a preview of Material Design 3 for Material Design Components (MDC).
 
Now we’re ready to announce the stable release of MDC 1.5.0 with more Material Design 3 support, component fixes and more color utilities. You can check out the release notes [here](https://github.com/material-components/material-components-android/releases/tag/1.5.0) .
 
If you held off on migrating last year, now is a great time to explore the new design system. Beyond the resources listed above, some areas you should focus your attention on are the Material 3 Catalog App and extended color utilities.
 
link
 
Copy link Link copied
 
## Material 3 Catalog App
 
Our engineering team uses the Material Catalog app to verify and show example implementations of new components and features relating to Material Design. It’s a great source for discovering the new system.
 
If you haven’t yet migrated to Material 3 and dynamic color, the catalog app offers a settings area allowing you to see how a default light, dark, or user-generated theme will look throughout the app.
 
You can download the apk file [here](https://github.com/material-components/material-components-android/releases/download/1.5.0/catalog-debug.apk) . For each screen, there’s also source code to [check out](https://github.com/material-components/material-components-android/tree/master/catalog/java/io/material/catalog) , organized by component.
 
link
 
Copy link Link copied
 
## Extended Color Utilities
 
Also at Android Dev Summit, we launched the Material Theme Builder for [Figma](https://www.figma.com/community/plugin/1034969338659738588/Material-Theme-Builder) and [the web](https://material-foundation.github.io/material-theme-builder/) . It provides designers and developers a means to experiment with dynamic color and Material 3 themes with the option to export as code.
 
We've been pleasantly surprised by the community adoption of Material Theme Builder. We've also heard from you that you want to incorporate color roles from more than the standard key colors. At present, we only export the seed color for each extended (non-key) color, despite showing a visualization of them.
 
In anticipation of more color features coming in the library, MDC 1.5.0 has a function in the MaterialColors class named `getColorRoles` that will return:
 
`accent`
 
`onAccentColor`
 
`accentContainer`
 
`onAccentContainer`
 
The full signature is as follows:
 `ColorRoles getColorRoles ( @ ColorInt int color ,` `boolean isLightTheme );` 
With this ColorRoles object, you could retheme a component at runtime. In the following snippet, we change the colorContainer and onColorContainer values for a button. Always remember to reassess the onColorContainer(text) tone when altering the colorContainer tone to ensure text has proper contrast and readability.
 ​ x
 
`val button = view . findViewById < Button > ( R . id . button_first )` `val green = resources . getColor ( R . color . green , null )` `// or Color.parseColor("#FF1BA132")` `val roles = MaterialColors . getColorRoles ( green , true )` `​` `button . setBackgroundColor ( roles . accentContainer )` `button . setTextColor ( roles . onAccentContainer )` 
link
 
Copy link Link copied
 
## What’s next for MDC?
 
We’re fast at work on the next major version of MDC. You can follow the progress, file [bug reports](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BComponent+name%5D+Short+description+of+issue) and [feature requests](https://github.com/material-components/material-components-android/issues/new?assignees=&labels=feature+request&template=feature_request.md&title=%5BComponent+name%5D+Short+description+of+request) on GitHub. Also feel free to reach out to us on Twitter [@materialdesign](https://twitter.com/materialdesign) .
