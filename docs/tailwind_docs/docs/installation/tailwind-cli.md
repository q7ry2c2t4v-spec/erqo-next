# Tailwind CLI

> Source: https://tailwindcss.com/docs/installation/tailwind-cli

[](/)v4.2

`⌘K``Ctrl K`[Docs](/docs)[Blog](/blog)[Showcase](/showcase)[Sponsor](/sponsor)[Plus](/plus?ref=top)[](https://github.com/tailwindlabs/tailwindcss)

  1. Getting Started
  2. Tailwind CLI

Installation

# Get started with Tailwind CSS

Tailwind CSS works by scanning all of your HTML files, JavaScript components, and any other templates for class names, generating the corresponding styles and then writing them to a static CSS file.

It's fast, flexible, and reliable — with zero-runtime.

## Installation

  * ## [Using Vite](/docs/installation/using-vite)

  * ## [Using PostCSS](/docs/installation/using-postcss)

  * ## [Tailwind CLI](/docs/installation/tailwind-cli)

  * ## [Framework Guides](/docs/installation/framework-guides)

  * ## [Play CDN](/docs/installation/play-cdn)

### Installing Tailwind CLI

The simplest and fastest way to get up and running with Tailwind CSS from scratch is with the Tailwind CLI tool. The CLI is also available as a [standalone executable](https://github.com/tailwindlabs/tailwindcss/releases/latest) if you want to use it without installing Node.js.

01

#### Install Tailwind CSS

Install `tailwindcss` and `@tailwindcss/cli` via npm.

Terminal
    
    
    npm install tailwindcss @tailwindcss/cli

02

#### Import Tailwind in your CSS

Add the `@import "tailwindcss";` import to your main CSS file.

src/input.css
    
    
    @import "tailwindcss";

03

#### Start the Tailwind CLI build process

Run the CLI tool to scan your source files for classes and build your CSS.

Terminal
    
    
    npx @tailwindcss/cli -i ./src/input.css -o ./src/output.css --watch

04

#### Start using Tailwind in your HTML

Add your compiled CSS file to the `<head>` and start using Tailwind’s utility classes to style your content.

src/index.html
    
    
    <!doctype html><html><head>  <meta charset="UTF-8">  <meta name="viewport" content="width=device-width, initial-scale=1.0">  <link href="./output.css" rel="stylesheet"></head><body>  <h1 class="text-3xl font-bold underline">    Hello world!  </h1></body></html>

Copyright © 2026 Tailwind Labs Inc.·[Trademark Policy](/brand)
