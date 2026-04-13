# Dialogs – Material Design 3

> Source: https://m3.material.io/components/dialogs/xr

link
 
Copy link Link copied
 
star
 
Note:
 
This is a rapidly changing space. Guidelines are primarily intended for designers at this time. Find what’s implemented in code in the [design kit](https://www.figma.com/community/file/1035203688168086460) .
 
link
 
Copy link Link copied
 
Extended reality (XR) introduces spatial capabilities, such as using depth to make dialogs stand out from the background. Currently, spatial dialogs are only available in full space Full space is Android XR’s immersive mode and supports spatial components. [More on full space](https://developer.android.com/design/ui/xr/guides/foundations#modes) . For home space Home space is compatible with mobile and large screen apps, but doesn’t support spatial components. [More on home space](https://developer.android.com/design/ui/xr/guides/foundations#modes) , follow Material’s general [dialog guidance](/m3/pages/dialogs/guidelines#b33988d3-88e6-432c-acb1-4461a84171c9) .
 
link
 
Copy link Link copied
 
## Color & elevation
 
link
 
Copy link Link copied
 
XR uses [color roles](/m3/pages/color-roles/tab-1#89f972b1-e372-494c-aabc-69aea34ed591) to communicate the elevation of UI elements. Dialogs can use two color options: surface container high or surface container highest .
 
link
 
Copy link Link copied
 
star
 
Note:
 
Color and elevation for spatial dialogs can be customized by makers and are not available in Jetpack Compose yet.
 
link
 
Copy link Link copied
 
Surface container high
 
Surface container highest
 
link
 
Copy link Link copied
 
For effective visual hierarchy, a dialog should be the most prominent element. Add a scrim behind a dialog to improve its visibility. Scrims prevent other content from being selected until the dialog action is complete.
 
check Do Make sure a spatial dialog’s color is higher than all other UI elements, and use a scrim
 
link
 
Copy link Link copied
 
The dialog should have the highest elevation in the product.
 
For example, if a dialog is surface container high , don’t use surface container highest for any other elements.
 
close Don’t If a dialog’s color is surface container high , don’t use surface container highest for any other element
 
link
 
Copy link Link copied
 
## Usage
 
link
 
Copy link Link copied
 
[Basic dialogs](/m3/pages/dialogs/guidelines#97ac3858-3932-4084-ae8e-73e42b7cb752) are recommended when designing for XR’s expanded window sizes. This keeps the required action in the person’s [field of view](https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place) . Limit use of [full-screen dialogs](/m3/pages/dialogs/guidelines#007536b9-76b1-474a-a152-2f340caaff6f) to compact window sizes, like mobile devices.
 
link
 
Copy link Link copied
 
check Do A basic dialog elevated above an app in home space
 
link
 
Copy link Link copied
 
close Don’t Avoid using full-screen dialogs in XR. Required actions could appear beyond a person’s field of view.
 
link
 
Copy link Link copied
 
## Spatial dialogs
 
link
 
Copy link Link copied
 
In full space Full space is Android XR’s immersive mode and supports spatial components. [More on full space](https://developer.android.com/design/ui/xr/guides/foundations#modes) , dialogs can be elevated spatially Spatial elevation displays a component above an app on the Z-axis. [More on spatial elevation](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation ) via [overrides](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design#use-enablexrcomponentoverrides) . This helps dialogs stand out from their background in XR.
 
link
 
Copy link Link copied
 
Side view of a basic dialog with spatial elevation in full space
 
link
 
Copy link Link copied
 
## Behavior
 
link
 
Copy link Link copied
 
### Effect
 
The spatial dialog should scale uniformly. It also fades in when appearing, and fades out when disappearing. The dialog's scrim only fades in and out.
 
pause
 Front view of a spatial dialog in motion in full space
 
link
 
Copy link Link copied
 
### Movement
 
When activated, the spatial dialog rises from the app to the highest resting level on the Z-axis.
 
When the action is complete, it returns to a normal resting level.
 
The dialog's scrim stays at the app content level at all times. To prevent motion sickness, use [standard easing](/m3/pages/motion-easing-and-duration/tokens-specs#601d5552-a6e6-4d74-9886-ff8f24b9ec35) and [long duration](/m3/pages/motion-easing-and-duration/tokens-specs#48bf653e-46f9-48f5-87e0-eaf8ea3fe716) motion tokens.
 
pause
 Side view of a spatial dialog in motion in full space
 
link
 
Copy link Link copied
 
## Placement
 
link
 
Copy link Link copied
 
Consider factors like field of view, viewing distance, and possible interactions when deciding where to place dialogs in XR.
 
link
 
Copy link Link copied
 
### Elevation: highest resting level
 
Display spatial dialogs at the highest resting level. When setting the depth value of the highest resting level, make sure the elevated dialog is at a comfortable viewing distance from the person. [More on spatial elevation](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation)
 
link
 
Copy link Link copied
 
pause
 A spatial dialog moves to the highest resting level in full space
 
link
 
Copy link Link copied
 
### Center spatial dialogs in field of view
 
Spatial dialogs should be centered in a person’s [field of view](https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place) . If the dialog can't track head movements, position it in the center of the app’s content.
 
If the dialog can track head movements, configure it with a lazy follow behavior. This keeps the dialog anchored to the center of a person’s field of view until an action is taken.
 
link
 
Copy link Link copied
 
pause
 A dialog in full space stays centered in a person’s field of view
 
link
 
Copy link Link copied
 
## Accessibility considerations
 
link
 
Copy link Link copied
 
[XR accessibility](https://developer.android.com/design/ui/xr/guides/get-started#make-app) guidelines are still evolving. Spatial dialogs should follow applicable Material [dialog accessibility standards](/m3/pages/dialogs/accessibility) .
