# Get started with Motion Studio

> Source: https://motion.dev/docs/studio

Motion Studio is a suite of AI and visual animation editing tools for VS Code, Cursor, and Windsurf.

  * [**AI Context**](./studio-ai-context)**:** Upgrade your AI with the latest Motion documentation, custom ruleset, and access to over 330 examples and recommended patterns.

  * [**Performance Audit**](./animation-performance-audit)**:** Identify and fix slow animations with this AI skill.

  * [**Transition Editor**](./studio-visual-controls)**:** Real-time editing of Motion and CSS transitions.

  * [**CSS generation**](./studio-generate-css)**:** Generate CSS springs - no animation library needed.

Upgrade to [Motion+](../plus) for AI access to 330+ premium examples, the latest docs, and the full Transition Editor.

### Install Motion Studio 

One-click install for Cursor:

[Add Extension](cursor:extension/motion.motion-vscode-extension)

[Add MCP](https://cursor.com/en-US/install-mcp?name=motion&config=eyJjb21tYW5kIjoibnB4IC15IGh0dHBzOi8vYXBpLm1vdGlvbi5kZXYvcmVnaXN0cnkudGd6P3BhY2thZ2U9bW90aW9uLXN0dWRpby1tY3AmdmVyc2lvbj1sYXRlc3QifQ%3D%3D)

Motion Studio is also compatible with VS Code, Google Antigravity and more. [See full installation guide](./studio-install). 

## Features

### AI Context

LLMs are trained on data that is often out of data, or on low-quality Stack Overflow answers.

Motion Studio lets your LLM query the latest Motion docs, as well as the source code of 330+ premium examples for the best quality both visually and in your codebase.

![](https://framerusercontent.com/images/jWa3w2mxUiXfBvBvynH47y5yadk.png)

[Learn more about improving AI context](./studio-llm-documentation)

### Performance Audit

Use the `/motion-audit` AI skill to run a performance audit on your CSS and Motion code. The report will return a plan that you or your LLM can use to immediately improve performance.

![](https://framerusercontent.com/images/9wvYmyGqcIN79K257arf76ls6I.png)

[Learn more about improving your animation performance](./animation-performance-audit)

### Transition editing

Motion Studio enables real-time editing and preview of CSS and Motion transitions, without having to leave your editor. It currently supports easing curves, delay and duration, with spring support coming soon.

![](https://framerusercontent.com/images/KO5dnHOUSNGb9S73p1J7nLhoFI.gif)

Your favourite transitions can be saved and reused anywhere.

![](https://framerusercontent.com/images/SxtfTFKwCAT1bIFEDY7JybZ30.png)

[Learn more about visual controls](./studio-visual-controls)

### Generate CSS springs

Motion Studio gives your AI editor the ability to generate CSS `linear()` easing curves to create springs or other custom easing curves, using real Motion code.

> Generate a CSS spring that's quite bouncy
    
    
    600ms linear(0, 0.0121 /* ... */)

[Learn more about CSS generation](./studio-generate-css)
