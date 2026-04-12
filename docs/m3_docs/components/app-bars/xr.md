# Top app bar – Material Design 3

> Source: https://m3.material.io/components/app-bars/xr

link
 
Copy link Link copied
 
star
 
Note:
 
This is a rapidly changing space. Guidelines are primarily intended for designers at this time. Find what’s implemented in code in the [design kit](https://www.figma.com/community/file/1035203688168086460) .
 
link
 
Copy link Link copied
 
Extended reality (XR) interfaces have special design requirements, like showing apps in 3D space. Material has an XR-specific app bar with custom specs and guidance. See [XR developer documentation](https://developer.android.com/design/ui/xr/guides/foundations) for more details.
 
link
 
Copy link Link copied
 
## Types & configurations
 
link
 
Copy link Link copied
 
There is one app bar orbiter Orbiters are floating elements that control the content within spatial panels. [More on orbiters](https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters) . It closely aligns with the small app bar Small app bars display information and actions in compact layouts. They're often used for scrolled views on subpages that require back navigation and multiple actions. [More on small app bars](/m3/pages/app-bars/overview) . It can be configured to be center-aligned or left-aligned.
 
link
 
Copy link Link copied
 
Center-aligned app bar
 
Left-aligned app bar
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
Container
 
Headline
 
Trailing icons
 
Leading icon
 
link
 
Copy link Link copied
 
## Color & elevation
 
link
 
Copy link Link copied
 
XR uses color to communicate the elevation of UI elements and orbiters. With [spatial elevation](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation) , the app bar displays above the spatial panel In Android XR, a spatial panel is a container for UI elements, interactive components, and immersive content. [More on spatial panels](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels) on the Z-axis. Elevated app bars can use any of these color options:
 
link
 
Copy link Link copied
 
Surface container
 
Surface container high
 
Surface container highest
 
link
 
Copy link Link copied
 
## Measurements
 
link
 
Copy link Link copied
 
Measurements and padding for app bar orbiters
 
link
 
Copy link Link copied
 
## Usage
 
link
 
Copy link Link copied
 
An app bar can appear in an orbiter Orbiters are floating elements that control the content within spatial panels. [More on orbiters](https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters) for a more immersive experience. Currently, this spatial capability is only available in full space Full space is Android XR’s immersive mode and supports spatial components. [More on full space](https://developer.android.com/design/ui/xr/guides/foundations#modes) . In home space Home space is compatible with mobile and large screen apps, but doesn’t support spatial components. [More on home space](https://developer.android.com/design/ui/xr/guides/foundations#modes) , use a regular app bar on the same plane as the body content to mimic a 2D experience.
 
link
 
Copy link Link copied
 
pause
 An app bar’s behavior and placement changes from a 2D to a 3D experience
 
link
 
Copy link Link copied
 
## Behavior
 
link
 
Copy link Link copied
 
### Global context
 
When placed in global context, the orbiter is centered at the top of the app it controls.
 
It stays anchored to the app during layout or content changes.
 
This ensures navigation elements are always easy to find and use.
 
pause
 Global app bar orbiters should be centered and anchored to the top of the app
 
link
 
Copy link Link copied
 
### Local context
 
When placed in local context, the orbiter is centered at the top of the spatial panel it controls.
 
It repositions in response to layout or content changes.
 
pause
 exclamation Caution Local app bar orbiters should be centered and anchored to the top of the panel. However, this is less common, so make sure that it contains actions that only affect its anchored panel.
 
link
 
Copy link Link copied
 
### Additional app bars
 
In most cases, apps should only have one app bar orbiter, placed in global context.
 
pause
 exclamation Caution Limit the use of multiple app bars to rare cases when additional spatialization improves usability
 
link
 
Copy link Link copied
 
## Placement
 
link
 
Copy link Link copied
 
### Offset and inset positioning
 
link
 
Copy link Link copied
 
check Do Include a 20dp margin. This visually separates the app bar orbiter from the spatial panel, and prevents content obstruction.
 
close Don’t Don’t overlap the app bar orbiter and spatial panel
 
link
 
Copy link Link copied
 
### Horizontal alignment
 
link
 
Copy link Link copied
 
check Do Always align the app bar orbiter within the bounds of nearby spatial panels
 
close Don’t The app bar orbiter shouldn’t exceed the width of adjacent spatial panels
 
link
 
Copy link Link copied
 
### Spatial panel alignment
 
By default, app bar orbiters are center-aligned to the spatial panel. Their width and placement can be adjusted to accommodate specific user needs, such as improved ergonomics or right-to-left (RTL) languages.
 
link
 
Copy link Link copied
 
pause
 App bar orbiters can align to the center, left, or right of the spatial panel
 
link
 
Copy link Link copied
 
### Width boundaries
 
An app bar orbiter’s width should adjust to stay in a person’s [field of view](https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place) .
 
This makes crucial navigation elements easy to find.
 
check Do Adjust the width of the app bar orbiter to fit in a person’s field of view
 
link
 
Copy link Link copied
 
It’s not recommended to increase the width of an app bar orbiter beyond a person’s natural [field of view](https://developer.android.com/design/ui/xr/guides/spatial-ui#where-place) .
 
This creates a visual imbalance and makes it difficult to find navigation elements.
 
close Don’t Avoid expanding the app bar orbiter beyond the adjacent panel’s width and a person’s field of view
 
link
 
Copy link Link copied
 
### Adaptable width
 
When placed in a local context, an app bar orbiter can expand to the width of its adjacent spatial panel.
 
Be sure the orbiter stays in a person’s field of view, and test for usability.
 
pause
 exclamation Caution Use caution before expanding the app bar’s width to match its spatial panel. The orbiter may not fit in a person’s primary field of view.
 
link
 
Copy link Link copied
 
## Accessibility considerations
 
link
 
Copy link Link copied
 
[XR accessibility](https://developer.android.com/design/ui/xr/guides/get-started#make-app) guidelines are still evolving. XR app bars should follow applicable Material [app bar accessibility standards](/m3/pages/app-bars/accessibility) .
