# RTL

> Source: https://ui.shadcn.com/docs/rtl

Sections

  * [Introduction](/docs)
  * [Components](/docs/components)
  * [Installation](/docs/installation)
  * [Theming](/docs/theming)
  * [CLI](/docs/cli)
  * [RTL](/docs/rtl)
  * [Skills](/docs/skills)
  * [MCP Server](/docs/mcp)
  * [Registry](/docs/registry)
  * [Forms](/docs/forms)
  * [Changelog](/docs/changelog)

Components

  * [Accordion](/docs/components/radix/accordion)
  * [Alert](/docs/components/radix/alert)
  * [Alert Dialog](/docs/components/radix/alert-dialog)
  * [Aspect Ratio](/docs/components/radix/aspect-ratio)
  * [Avatar](/docs/components/radix/avatar)
  * [Badge](/docs/components/radix/badge)
  * [Breadcrumb](/docs/components/radix/breadcrumb)
  * [Button](/docs/components/radix/button)
  * [Button Group](/docs/components/radix/button-group)
  * [Calendar](/docs/components/radix/calendar)
  * [Card](/docs/components/radix/card)
  * [Carousel](/docs/components/radix/carousel)
  * [Chart](/docs/components/radix/chart)
  * [Checkbox](/docs/components/radix/checkbox)
  * [Collapsible](/docs/components/radix/collapsible)
  * [Combobox](/docs/components/radix/combobox)
  * [Command](/docs/components/radix/command)
  * [Context Menu](/docs/components/radix/context-menu)
  * [Data Table](/docs/components/radix/data-table)
  * [Date Picker](/docs/components/radix/date-picker)
  * [Dialog](/docs/components/radix/dialog)
  * [Direction](/docs/components/radix/direction)
  * [Drawer](/docs/components/radix/drawer)
  * [Dropdown Menu](/docs/components/radix/dropdown-menu)
  * [Empty](/docs/components/radix/empty)
  * [Field](/docs/components/radix/field)
  * [Hover Card](/docs/components/radix/hover-card)
  * [Input](/docs/components/radix/input)
  * [Input Group](/docs/components/radix/input-group)
  * [Input OTP](/docs/components/radix/input-otp)
  * [Item](/docs/components/radix/item)
  * [Kbd](/docs/components/radix/kbd)
  * [Label](/docs/components/radix/label)
  * [Menubar](/docs/components/radix/menubar)
  * [Native Select](/docs/components/radix/native-select)
  * [Navigation Menu](/docs/components/radix/navigation-menu)
  * [Pagination](/docs/components/radix/pagination)
  * [Popover](/docs/components/radix/popover)
  * [Progress](/docs/components/radix/progress)
  * [Radio Group](/docs/components/radix/radio-group)
  * [Resizable](/docs/components/radix/resizable)
  * [Scroll Area](/docs/components/radix/scroll-area)
  * [Select](/docs/components/radix/select)
  * [Separator](/docs/components/radix/separator)
  * [Sheet](/docs/components/radix/sheet)
  * [Sidebar](/docs/components/radix/sidebar)
  * [Skeleton](/docs/components/radix/skeleton)
  * [Slider](/docs/components/radix/slider)
  * [Sonner](/docs/components/radix/sonner)
  * [Spinner](/docs/components/radix/spinner)
  * [Switch](/docs/components/radix/switch)
  * [Table](/docs/components/radix/table)
  * [Tabs](/docs/components/radix/tabs)
  * [Textarea](/docs/components/radix/textarea)
  * [Toast](/docs/components/radix/toast)
  * [Toggle](/docs/components/radix/toggle)
  * [Toggle Group](/docs/components/radix/toggle-group)
  * [Tooltip](/docs/components/radix/tooltip)
  * [Typography](/docs/components/radix/typography)

Get Started

  * [Installation](/docs/installation)
  * [components.json](/docs/components-json)
  * [Theming](/docs/theming)
  * [Dark Mode](/docs/dark-mode)
  * [CLI](/docs/cli)
  * [Monorepo](/docs/monorepo)
  * [Skills](/docs/skills)
  * [Open in v0](/docs/v0)
  * [JavaScript](/docs/javascript)
  * [Figma](/docs/figma)
  * [llms.txt](/llms.txt)
  * [Legacy Docs](/docs/legacy)

Forms

  * [React Hook Form](/docs/forms/react-hook-form)
  * [TanStack Form](/docs/forms/tanstack-form)

Registry

  * [Introduction](/docs/registry)
  * [Getting Started](/docs/registry/getting-started)
  * [Namespaces](/docs/registry/namespace)
  * [Authentication](/docs/registry/authentication)
  * [Examples](/docs/registry/examples)
  * [MCP Server](/docs/registry/mcp)
  * [Add a Registry](/docs/registry/registry-index)
  * [Open in v0](/docs/registry/open-in-v0)
  * [registry.json](/docs/registry/registry-json)
  * [registry-item.json](/docs/registry/registry-item-json)

# RTL

Copy Page

[Previous](/docs/dark-mode)[Next](/docs/cli)

Right-to-left support for shadcn/ui components.

shadcn/ui components have first-class support for right-to-left (RTL) layouts. Text alignment, positioning, and directional styles automatically adapt for languages like Arabic, Hebrew, and Persian.

Arabic (العربية)▼Toggle

تسجيل الدخول إلى حسابك

أدخل بريدك الإلكتروني أدناه لتسجيل الدخول إلى حسابك

إنشاء حساب

البريد الإلكتروني

كلمة المرورنسيت كلمة المرور؟

تسجيل الدخولتسجيل الدخول باستخدام Google

A card component in RTL mode.

When you install components, the CLI automatically transforms physical positioning classes to logical equivalents, so your components work seamlessly in both LTR and RTL contexts.

## Get Started

Select your framework to get started with RTL support.

[Next.jsNext.js](/docs/rtl/next)[ViteVite](/docs/rtl/vite)[TanStack Start](/docs/rtl/start)

## How it works

When you add components with `rtl: true` set in your `components.json`, the shadcn CLI automatically transforms classes and props to be RTL compatible:

  * Physical positioning classes like `left-*` and `right-*` are converted to logical equivalents like `start-*` and `end-*`.
  * Directional props are updated to use logical values.
  * Text alignment and spacing classes are adjusted accordingly.
  * Supported icons are automatically flipped using `rtl:rotate-180`.

## Try it out

Click the link below to open a Next.js project with RTL support in v0.

[![Open in v0](https://v0.app/chat-static/button.svg)](https://v0.app/chat/api/open?url=https://github.com/shadcn-ui/next-template-rtl)

## Supported Styles

Automatic RTL transformation via the CLI is only available for projects created using `shadcn create` with the new styles (`base-nova`, `radix-nova`, etc.).

For other styles, see the Migration Guide.

## Font Recommendations

For the best RTL experience, we recommend using fonts that have proper support for your target language. [Noto](https://fonts.google.com/noto) is a great font family for this and it pairs well with Inter and Geist.

See your framework's RTL guide under Get Started for details on installing and configuring RTL fonts.

## Animations

The CLI also handles animation classes, automatically transforming physical directional animations to their logical equivalents. For example, `slide-in-from-right` becomes `slide-in-from-end`.

This ensures animations like dropdowns, popovers, and tooltips animate in the correct direction based on the document's text direction.

**A note on tw-animate-css:**

There is a [known issue](https://github.com/Wombosvideo/tw-animate-css/issues/67) with the `tw-animate-css` library where the logical slide utilities are not working as expected. For now, make sure you pass in the `dir` prop to portal elements.
    
    
    Copy<Popover>
      <PopoverTrigger>Open</PopoverTrigger>
      <PopoverContent dir="rtl">
        <div>Content</div>
      </PopoverContent>
    </Popover>
    
    
    Copy<Tooltip>
      <TooltipTrigger>Open</TooltipTrigger>
      <TooltipContent dir="rtl">
        <div>Content</div>
      </TooltipContent>
    </Tooltip>

## Migrating existing components

If you have existing components installed before enabling RTL, you can migrate them using the CLI as follows:

### Run the migrate command
    
    
    pnpmnpmyarnbun
    
    
    pnpm dlx shadcn@latest migrate rtl [path]

Copy

`[path]` accepts a path or glob pattern to migrate. If you don't provide a path, it will migrate all the files in the `ui` directory.

### Manual Migration (Optional)

The following components are not automatically migrated by the CLI. Follow the RTL support section for each component to manually migrate them.

  * [Calendar](/docs/components/radix/calendar#rtl-support)
  * [Pagination](/docs/components/radix/pagination#rtl-support)
  * [Sidebar](/docs/components/radix/sidebar#rtl-support)

### Migrate Icons

Some icons like `ArrowRightIcon` or `ChevronLeftIcon` might need the `rtl:rotate-180` class to be flipped correctly. Add the `rtl:rotate-180` class to the icon component to flip it correctly.
    
    
    Copy<ArrowRightIcon className="rtl:rotate-180" />

### Add direction component

Add the direction component to your project.
    
    
    pnpmnpmyarnbun
    
    
    pnpm dlx shadcn@latest add direction

Copy

### Add DirectionProvider

Follow your framework's documentation for details on how to add the `DirectionProvider` component to your project.

See the Get Started section for details on how to add the `DirectionProvider` component to your project.

[ Dark Mode](/docs/dark-mode)[CLI ](/docs/cli)

On This Page

Get StartedHow it worksTry it outSupported StylesFont RecommendationsAnimationsMigrating existing componentsManual Migration (Optional)Migrate IconsAdd direction componentAdd DirectionProvider

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Adobe, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
