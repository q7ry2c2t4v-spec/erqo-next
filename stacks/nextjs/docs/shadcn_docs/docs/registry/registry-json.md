# registry.json

> Source: https://ui.shadcn.com/docs/registry/registry-json

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

# registry.json

Copy Page

[Previous](/docs/registry/open-in-v0)[Next](/docs/registry/registry-item-json)

Schema for running your own component registry.

The `registry.json` schema is used to define your custom component registry.

registry.json
    
    
    Copy{
      "$schema": "https://ui.shadcn.com/schema/registry.json",
      "name": "shadcn",
      "homepage": "https://ui.shadcn.com",
      "items": [
        {
          "name": "hello-world",
          "type": "registry:block",
          "title": "Hello World",
          "description": "A simple hello world component.",
          "registryDependencies": [
            "button",
            "@acme/input-form",
            "https://example.com/r/foo"
          ],
          "dependencies": ["is-even@3.0.0", "motion"],
          "files": [
            {
              "path": "registry/new-york/hello-world/hello-world.tsx",
              "type": "registry:component"
            }
          ]
        }
      ]
    }

## Definitions

You can see the JSON Schema for `registry.json` [here](https://ui.shadcn.com/schema/registry.json).

### $schema

The `$schema` property is used to specify the schema for the `registry.json` file.

registry.json
    
    
    Copy{
      "$schema": "https://ui.shadcn.com/schema/registry.json"
    }

### name

The `name` property is used to specify the name of your registry. This is used for data attributes and other metadata.

registry.json
    
    
    Copy{
      "name": "acme"
    }

### homepage

The homepage of your registry. This is used for data attributes and other metadata.

registry.json
    
    
    Copy{
      "homepage": "https://acme.com"
    }

### items

The `items` in your registry. Each item must implement the [registry-item schema specification](https://ui.shadcn.com/schema/registry-item.json).

registry.json
    
    
    Copy{
      "items": [
        {
          "name": "hello-world",
          "type": "registry:block",
          "title": "Hello World",
          "description": "A simple hello world component.",
          "registryDependencies": [
            "button",
            "@acme/input-form",
            "https://example.com/r/foo"
          ],
          "dependencies": ["is-even@3.0.0", "motion"],
          "files": [
            {
              "path": "registry/new-york/hello-world/hello-world.tsx",
              "type": "registry:component"
            }
          ]
        }
      ]
    }

See the [registry-item schema documentation](/docs/registry/registry-item-json) for more information.

[ Open in v0](/docs/registry/open-in-v0)[registry-item.json ](/docs/registry/registry-item-json)

On This Page

Definitions$schemanamehomepageitems

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Adobe, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
