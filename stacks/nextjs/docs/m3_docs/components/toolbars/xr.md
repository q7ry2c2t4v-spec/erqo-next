# Toolbar

> Source: https://m3.material.io/components/toolbars/xr

link
 
Copy link Link copied
 
star
 
Note:
 
This is a rapidly changing space. Guidelines are primarily intended for designers at this time. Find what’s implemented in code in the [design kit](https://www.figma.com/community/file/1035203688168086460) .
 
link
 
Copy link Link copied
 
Extended reality (XR) interfaces have special design requirements, like showing apps in 3D space. Material has an XR-specific toolbar with custom specs and guidance. Read [XR developer documentation](https://developer.android.com/design/ui/xr/guides/foundations) for more details.
 
link
 
Copy link Link copied
 
## Variants
 
There is one toolbar orbiter Orbiters are floating elements that control the content within spatial panels. [More on orbiters](https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters) . It closely aligns with the floating toolbar Floating toolbars float on top of page content and can provide contextual, dynamic actions. [More on toolbars](/m3/pages/toolbars/overview) . It can be configured to be horizontal or vertical.
 
link
 
Copy link Link copied
 
Horizontal floating toolbar
 
Vertical floating toolbar
 
link
 
Copy link Link copied
 
## Anatomy
 
link
 
Copy link Link copied
 
Container
 
Placed components
 
link
 
Copy link Link copied
 
## Color & elevation
 
XR uses color to communicate the elevation of UI elements and orbiters. With [spatial elevation](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-elevation) , the toolbar displays above the spatial panel In Android XR, a spatial panel is a container for UI elements, interactive components, and immersive content. [More on spatial panels](https://developer.android.com/design/ui/xr/guides/spatial-ui#spatial-panels) on the Z-axis. Elevated toolbars can use any of these color options:
 
link
 
Copy link Link copied
 
Surface container
 
Surface container high
 
Surface container highest
 
Tertiary container
 
link
 
Copy link Link copied
 
## Measurements
 
link
 
Copy link Link copied
 
Measurements for toolbar orbiters
 
link
 
Copy link Link copied
 
Padding for toolbar orbiters
 
link
 
Copy link Link copied
 
## Usage
 
A toolbar can appear in an orbiter Orbiters are floating elements that control the content within spatial panels. [More on orbiters](https://developer.android.com/design/ui/xr/guides/spatial-ui#orbiters) for a more immersive experience. Currently, this spatial capability is only available in full space Full space is Android XR’s immersive mode and supports spatial components. [More on full space](https://developer.android.com/design/ui/xr/guides/foundations#modes) . In home space Home space is compatible with mobile and large screen apps, but doesn’t support spatial components. [More on home space](https://developer.android.com/design/ui/xr/guides/foundations#modes) , use a regular toolbar on the same plane as the body content to mimic a 2D experience.
 
link
 
Copy link Link copied
 
pause
 A toolbar’s behavior and placement changes from a 2D to a 3D experience
 
link
 
Copy link Link copied
 
## Behavior
 
link
 
Copy link Link copied
 
### Local context (recommended)
 
When placed in local context, the toolbar orbiter is centered at the bottom of the spatial panel it controls.
 
It repositions in response to layout or content changes.
 
pause
 In most cases, toolbars should be placed in local context. The orbiter is centered and anchored to the bottom of the panel it controls.
 
link
 
Copy link Link copied
 
### Global context
 
When placed in global context, the toolbar orbiter is centered at the bottom of the app.
 
It stays anchored to the app during layout or content changes.
 
pause
 exclamation Caution In global context, toolbar orbiters are centered and anchored to the bottom of the app. This use case is less common, as toolbars usually contain actions that control a specific panel.
 
link
 
Copy link Link copied
 
### Expand & collapse
 
Toolbar orbiters with more than five items can expand and collapse to reveal or hide additional content.
 
When a toolbar orbiter expands, it stays within the bounds of the adjacent spatial panel.
 
Alternatively, more complex toolbars can be split into multiple toolbars.
 
pause
 Toolbar orbiters can expand to reveal additional content, but should stay within the bounds of the adjacent spatial panel
 
link
 
Copy link Link copied
 
### Additional toolbars
 
In some cases, full space apps can have more than one toolbar orbiter, placed in either global or local context.
 
link
 
Copy link Link copied
 
pause
 exclamation Caution Limit the use of multiple toolbars to rare cases when additional spatialization improves usability
 
link
 
Copy link Link copied
 
## Placement
 
link
 
Copy link Link copied
 
### Offset & inset positioning
 
In full space, a toolbar orbiter can be positioned adjacent to or overlap a spatial panel.
 
link
 
Copy link Link copied
 
check Do The recommended toolbar orbiter position from the spatial panel is:
 
Offset by 20dp or
 
Inset by 12dp
 
close Don’t To prevent content obstruction, don’t overlap the toolbar orbiter and spatial panel above a 12dp inset threshold
 
link
 
Copy link Link copied
 
### Horizontal alignment
 
link
 
Copy link Link copied
 
check Do Always align the toolbar orbiter within the horizontal bounds of nearby spatial panels
 
close Don’t The toolbar orbiter shouldn’t exceed the width of adjacent spatial panels
 
link
 
Copy link Link copied
 
### Vertical alignment
 
link
 
Copy link Link copied
 
check Do Always align the toolbar orbiter within the vertical bounds of nearby spatial panels
 
close Don’t The toolbar orbiter shouldn’t exceed the height of adjacent spatial panels
 
link
 
Copy link Link copied
 
### Spatial panel alignment
 
By default, toolbar orbiters are center-aligned to the spatial panel. Their placement can be adjusted to accommodate specific user needs, such as improved ergonomics or [right-to-left (RTL) languages](/m3/pages/understanding-layout/bidirectionality-rtl) .
 
link
 
Copy link Link copied
 
Depending on the configuration (horizontal or vertical) of the toolbar orbiter, it can align to the center, left, right, top, or bottom of a spatial panel
 
link
 
Copy link Link copied
 
Avoid placing a vertical toolbar orbiter between spatial panels. This negatively affects the interface structure and can make it difficult to find.
 
close Don’t Don't place a vertical toolbar orbiter between spatial panels
 
link
 
Copy link Link copied
 
## Accessibility considerations
 
[XR accessibility](https://developer.android.com/design/ui/xr/guides/get-started#make-app) guidelines are still evolving. XR toolbars should follow applicable Material [toolbar accessibility standards](/m3/pages/toolbars/accessibility) .
