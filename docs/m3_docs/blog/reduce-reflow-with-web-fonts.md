# How to reduce layout reflow when using web fonts

> Source: https://m3.material.io/blog/reduce-reflow-with-web-fonts

Posted by
 Dave Crossland , Fonts Programmes & Operations Manager
 Font loading times are becoming more important than ever as they can influence your Google Search page ranking. These loading times are important to visitors because fonts play a part in how often a visitor experiences unexpected layout shifts as pages load. Cumulative Layout Shift (CLS) is a [metric for web page quality](http://web.dev/cls) that quantifies this experience.
 
When a web font is loaded a little slower than the time it takes to start rendering the page, browsers will either render the text using a fall back font (unstyled) or with a blank area (invisible) until the font has loaded.
 
This is known as the “flash of unstyled text” (FOUT) or “flash of invisible text” (FOIT) and these flashes of text repainting will reduce a CLS score. There are a few different optimization techniques, [described on web.dev](https://web.dev/optimize-cls) . One technique can prevent flashes of text from happening at all, but this is a significant trade-off because many users simply won't see the web fonts at all.
 
When using Google Fonts there are three key optimizations you should use, and ensure are present in any previous integrations. Here’s an example of what to do if you’re using Google Fonts—you can use this HTML to integrate the Google Fonts API.
 `<!-- 1: links at top of head -->` `< head >` `< meta charset = "utf-8" >` `<!-- 2: preconnect -->` `< link rel = "preconnect" href = "https://fonts.googleapis.com" >` `< link rel = "preconnect" href = "https://fonts.gstatic.com" crossorigin >` `<!-- 3: use font-display -->` `< link href = "https://fonts.googleapis.com/css2?family=Roboto&display=optional" rel = "stylesheet" >` 
The benefits of the three optimizations shown above are:
 
#### 1. All GF `<link>` elements are at the top of `<head>`
 
By placing the font link elements immediately after the head element and the mandatory first meta element to define the page’s encoding, the browser can start the web font loading process as early as possible.
 
#### 2. Preconnect to fonts.googleapis.com and fonts.gstatic.com
 `xxxxxxxxxx`
 
`< link rel = "preconnect" href = "https://fonts.googleapis.com" >` `< link rel = "preconnect" href = "https://fonts.gstatic.com" crossorigin >` 
These links instruct the browser to open a HTTP connection to the Google Fonts API domains, so that assets loaded from these domains can start downloading faster. You can also use the [Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link) http header, which is processed even earlier. [Learn more on web.dev](https://web.dev/preconnect-and-dns-prefetch) .
 
#### 3. Use font-display
 `xxxxxxxxxx`
 
`< link href = "https://fonts.googleapis.com/css2?family=Roboto&display=optional" rel = "stylesheet" >` 
This API option requests that the CSS returned by the Google Fonts API will include a `font-display` property. We advise use of one of the following options, depending on what trade-offs you prefer:
 
optional - best CLS score, worse typography. Many users will not see the web font at all, since it will only be shown after it is downloaded.
 
swap - worse CLS score, better typography. Most users will see the font, but they will experience layout shift if the font arrives late.
 
fallback - a middle ground. If the font arrives a little after content is drawn in a fallback font, there is some layout shift, and a worse CLS score.
 
These trade-offs are broad guidelines. Depending on what other content your page loads, the font may consistently be ready in time because other parts of the page take even longer to load. Or, if the font is the only external resource, it may almost never be ready in time. For example, the AMP team [has found](https://bugs.chromium.org/p/chromium/issues/detail?id=1231827) that using “optional” stops the font being used on the page. AMP pages only allow inline stylesheets, meaning the page is ready to render before the fonts have a chance to download. Therefore setting the API’s Display feature to “swap” may be better in this case.
 
[Learn more on web.dev](https://web.dev/preload-optional-fonts/) and [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display) to determine what option is right for your use-case. Tools like [webpagetest.org](https://www.webpagetest.org/) can help review the loading characteristics of your page under varied conditions.
 
link
 
Copy link Link copied
 
## Other Considerations
 
The CSS Font Loading API allows you to take direct control over loading and applying fonts. [Learn more on MDN](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Font_Loading_API) .
 
There’s also an advanced technique emerging, to use fallbacks with some new CSS properties for scaling and shifting them, so that when they are replaced by web fonts the resulting layout shift is reduced. This is slightly tricky because not all operating systems have the same set of fonts to fallback to. [Learn more on Smashing Magazine](https://www.smashingmagazine.com/2021/05/reduce-font-loading-impact-css-descriptors/) .
 
link
 
Copy link Link copied
 
## Conclusion
 
These recommendations are relatively new compared to the lifetime of Google Fonts, so there are many older integrations that don’t use these techniques yet. If you haven’t updated your Google Fonts code this year, take a look and tune up your site to enhance your users’ experience today!
