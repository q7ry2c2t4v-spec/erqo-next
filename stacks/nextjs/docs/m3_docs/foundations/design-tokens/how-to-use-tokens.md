# Design tokens – Material Design 3

> Source: https://m3.material.io/foundations/design-tokens/how-to-use-tokens

link
 
Copy link Link copied
 
## Download Material baseline tokens
 
link
 
Copy link Link copied
 
Material Design’s baseline theme includes design tokens and default values. [Download the theme](http://github.com/material-foundation/material-tokens) as a Design System Package (DSP) to customize, collaborate on, and use in your own designs and product code. [Learn about the DSP JSON format](https://github.com/AdobeXD/design-system-package-dsp)
 
link
 
Copy link Link copied
 
## Use tokens in Figma
 
link
 
Copy link Link copied
 
To begin, install the [Material Theme Builder](https://goo.gle/material-theme-builder-figma) Figma plugin from the community page.
 
### Generate tokens
 
Open Figma and navigate to: Plugins > Material Theme Builder > Open Plugin
 
Select Get started , this will create material-theme with baseline values by default. Color and text styles will begin populating the right hand design panel. When your tokens are fully generated, your artboard will contain tonal palettes for light and dark color schemes, as well as a default type scale.
 
Your tokens are now represented as [Figma styles](https://help.figma.com/hc/en-us/articles/360039238753-Styles-in-Figma) that can be used throughout your designs
 
### Update token values
 
#### Using the Material Theme Builder Figma plugin (updates colors only)
 
Open Figma and navigate to: Plugins > Material Theme Builder > Open Plugin
 
Choose the colors. Updated color and text styles will begin populating the right hand design panel.
 
Your updated tokens are now represented as [Figma styles](https://help.figma.com/hc/en-us/articles/360039238753-Styles-in-Figma) that can be used throughout your designs
 
#### Using Figma styles
 
In Figma, navigate to the file in which the tokenized style is defined. Shortcut: right click the style in the right hand sidebar and select Go to style definition.
 
In the right hand sidebar, hover over the style you want to update and select the adjust icon when it appears . Or, right click the style in the style picker and select Edit style .
 
Make your changes to the token name, description, properties, etc. using the Edit style panel . Close the panel when finished.
 
### Use tokens in product mock-ups
 
Instead of manually setting the color or typography for elements in a layout, apply the [Figma styles](https://help.figma.com/hc/en-us/articles/360039238753-Styles-in-Figma) representing your design tokens. This helps ensure that developers will correctly understand and apply your design choices.
 
### Use tokens with the Material Design Kit
 
Duplicate the Material Design Kit in Figma
 
Navigate to Plugins > Material Theme Builder > Open plugin
 
With components selected, select swap . This will swap the baseline Material token style values with your own generated token style values.
 
### Export tokens
 
Open Figma and navigate to: Plugins > Material Theme Builder > Open Plugin
 
Navigate to the Export tab . Select the format you want to export for (Android, Jetpack Compose)
 
Name your .zip file and select Save
 
Your tokens are ready to share!
