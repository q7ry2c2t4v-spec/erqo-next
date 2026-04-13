# Device Metrics for Any Screen - Material Design 3

> Source: https://m3.material.io/blog/device-metrics

Posted by
 Liam Spradlin , Senior UX Designer, Material Design
 New devices are always coming online, offering new formats, screen sizes, and pixel densities that you’ll want your product to accommodate. If Googling doesn’t give you the numbers you need, or you just want to show off your math skills, here’s a relatively easy way to determine the relevant metrics for your designs.
 
link
 
Copy link Link copied
 
## Do it yourself 🛠
 
There are six pieces of information you’ll want in the end: the screen diagonal measurement, screen dimensions, aspect ratio, pixel resolution, dp (or [density-independent pixel](https://developer.android.com/training/multiscreen/screendensities) , Android’s logical pixel) and the density bucket to which each device belongs. Some of those specifications can be found on each device’s product page, or through other sites that collect information about specific devices.
 
It’s easiest to visualize this information if we have an example. So, to get a feel for the process of finding these values, let’s start with the Pixel 4.
 Screen Diagonal Screen Dimensions Aspect Ratio Pixel Resolution dp Resolution Density Bucket `5.7"` `~` `19:9` `1080×2280` `~` `~` 
The screen diagonal, aspect ratio, and pixel resolution can all be found on the [Pixel 4 product page](https://store.google.com/product/pixel_4_specs) . For devices that don’t have in-depth or easily accessible specification pages, sites like [the GSMArena Phone Finder](https://www.gsmarena.com/search.php3) can be a good resource.
 
link
 
Copy link Link copied
 
## Finding Screen Dimensions 📐
 
After filling in the readily available info, we have three more specs to solve for. The first one is the screen’s dimensions in terms of width and height. The formulas for this — which I learned from an [Omni Calculator page by Hanna Pamula](https://www.omnicalculator.com/other/screen-size) — are fairly easy to use, and only require a diagonal measurement and an aspect ratio (AR).
 
Width = diagonal / √(AR²+1)
 
Height = (AR)×Width
 
So for our example, we know the screen diagonal is 5.7 and the aspect ratio is 19:9 (which we’ll write as 19/9 in the formula).
 
Width = 5.7 / √((19/9)²+1)
 
Width = 2.44”
 
And now that we know Width, we can solve for Height.
 
Height = (19/9)×2.44
 
Height = 5.15”
 
So our screen dimensions are 2.44×5.15”
 
link
 
Copy link Link copied
 
## Finding dp Resolution 📏
 
Density-independent pixels are Android’s logical pixel. Measuring in dp allows designers and developers to ensure that what they create appears at the same physical size across screens, no matter what density those screens happen to be. So knowing the dp resolution of a device can be really helpful in targeting that device with your design. You can easily set up artboards and assets that focus on specific form factors, and reliably reproduce your design across them.
 
For this formula (which you can find in the [Android Developers documentation on pixel density](https://developer.android.com/training/multiscreen/screendensities) ), we need to know the screen’s pixel resolution, the dimensions we calculated before, and the screen’s ppi. The screen’s dpi (written as ppi) should be available at one of the sources mentioned above.
 
px = dp×(dpi/160)
 
In our example, we know the screen’s pixel resolution is 1080×2280px, and its physical dimensions are 2.44×5.15” so we can plug those values into the formula, starting again with width.
 
1080 = dp×(444/160)
 
1080 = dp×2.775
 
dp = 1080/2.775
 
dp = 389
 
Next we’ll do the same calculation for the screen’s height in density-independent pixels.
 
2280 = dp×2.775
 
dp = 2280/2.775
 
dp = 822
 
link
 
Copy link Link copied
 
## Finding the density bucket 🔍
 
The [Android Developers documentation on pixel density](https://developer.android.com/training/multiscreen/screendensities) also outlines the notion of “density qualifiers,” which Android uses to serve bitmap drawable resources in an app. If there are non-vector assets like photos or illustrations in your design, it can be useful to know which density buckets you’re targeting, serving the right asset to each device to speed up loading and to avoid distortion and “out of memory” errors.
 
Finding the density bucket is as easy as looking at the table in the documentation linked above and comparing it to our dpi value. For the Pixel 4’s ~444ppi, we would assign the XXHDPI density qualifier.
 Density Qualifier Denisty Value Scale Description `ldpi` `~120dpi` `0.75x` `Resources for low-density (ldpi) screens.` `mdpi` `~160dpi` `1x` `Resources for medium-density (mdpi) screens. (This is the baseline density.)` `hdpi` `~240dpi` `1.5x` `Resources for high-density (hdpi) screens.` `xhdpi` `~320dpi` `2x` `Resources for extra-high-density (xhdpi) screens.` `xxhdpi` `~480dpi` `3x` `Resources for extra-extra-high-density (xxhdpi) screens.` `xxxhdpi` `~640dpi` `4x` `Resources for extra-extra-extra-high-density (xxxhdpi) uses.` `nodpi` `n/a` `n/a` `Resources for all densities. These are density-independent resources. The system does not scale resources tagged with this qualifier, regardless of the current screen's density.` `tvdpi` `~213dpi` `1.33x` `Resources for screens somewhere between mdpi and hdpi; approximately 213dpi. This is not considered a "primary" density group. It is mostly intended for televisions and most apps shouldn't need it—providing mdpi and hdpi resources is sufficient for most apps and the system will scale them as appropriate. If you find it necessary to provide tvdpi resources, you should size them at a factor of 1.33*mdpi. For example, a 100px x 100px image for mdpi screens should be 133px x 133px for tvdpi.` 
link
 
Copy link Link copied
 
## Putting it all together 🧩
 
Having worked through those calculations, we now have a complete set of device metrics for our example device, the Pixel 4.
 Screen Diagonal Screen Dimensions Aspect Ratio Pixel Resolution dp Resolution Density Bucket `5.7"` `2.44×5.15` `19:9` `1080×2280` `392×822dp` `XXHDPI` 
For further reading on pixel density, layout, and how the two interact, see the [Material Design guidance on Layout](https://material.io/design/layout/understanding-layout.html#usage) .
