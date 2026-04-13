# Install Motion Studio

> Source: https://motion.dev/docs/studio-install

Motion Studio provides visual editing tools via the **Motion Studio extension** , and AI editing tools via the **Motion Studio MCP**. Currently, both must be installed separately.

### Install Motion Studio 

One-click install for Cursor:

[Add Extension](cursor:extension/motion.motion-vscode-extension)

[Add MCP](https://cursor.com/en-US/install-mcp?name=motion&config=eyJjb21tYW5kIjoibnB4IC15IGh0dHBzOi8vYXBpLm1vdGlvbi5kZXYvcmVnaXN0cnkudGd6P3BhY2thZ2U9bW90aW9uLXN0dWRpby1tY3AmdmVyc2lvbj1sYXRlc3QifQ%3D%3D)

Motion Studio is also compatible with VS Code, Google Antigravity and more. Read on for full installation instructions.

## Visual editing

Motion Studio visual editing tools are provided via the official Extension.

[Add to VS Code](vscode:extension/Motion.motion-vscode-extension)

It's also available on the [Open VSX marketplace](https://open-vsx.org/extension/motion/motion-vscode-extension) for other editors.

## MCP

The basic Motion Studio MCP includes AI enhancements like:

  * [AI context](./studio-ai-context): Allow your LLM to improve its animation skills by searching the full Motion docs, source code of 330+ examples, and saved transitions.

  * [CSS spring generation](./studio-generate-css)

To install, add the following to your editor's MCP JSON settings:

{

"mcpServers": {

"motion": {

"command": "npx",

"args": ["-y", "https://api.motion.dev/registry.tgz?package=motion-studio-mcp&version=latest"]

}

}

}

The exact process differs by editor, but here are the MCP docs for popular apps:

  * [VS Code](https://code.visualstudio.com/docs/copilot/customization/mcp-servers) (search "mcp.json")

  * [Windsurf](https://docs.windsurf.com/windsurf/cascade/mcp)

  * [Claude Desktop](https://modelcontextprotocol.io/quickstart/user)

  * [Claude Code](https://scottspence.com/posts/configuring-mcp-tools-in-claude-code)

## Unlock Motion+ features

To enable Motion+ features like the [codex](./studio-codex) and [curve visualisation](./studio-visualise-curves), you have to install with your [personal access token](https://plus.motion.dev/personal-token):
    
    
    {
      "mcpServers": {
        "motion": {
          "command": "npx",
          "args": ["-y", "https://api.motion.dev/registry.tgz?package=motion-studio-mcp&version=latest"],
          "env": {
            "TOKEN": "<YOUR_TOKEN>"
          },
        }
      }
    }
