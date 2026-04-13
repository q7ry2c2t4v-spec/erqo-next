# registry-item.json

> Source: https://ui.shadcn.com/docs/registry/registry-item-json

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

# registry-item.json

Copy Page

[Previous](/docs/registry/registry-json)

Specification for registry items.

The `registry-item.json` schema is used to define your custom registry items.

registry-item.json
    
    
    Copy{
      "$schema": "https://ui.shadcn.com/schema/registry-item.json",
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
      "devDependencies": ["tw-animate-css"],
      "files": [
        {
          "path": "registry/new-york/hello-world/hello-world.tsx",
          "type": "registry:component"
        },
        {
          "path": "registry/new-york/hello-world/use-hello-world.ts",
          "type": "registry:hook"
        }
      ],
      "cssVars": {
        "theme": {
          "font-heading": "Poppins, sans-serif"
        },
        "light": {
          "brand": "oklch(0.205 0.015 18)"
        },
        "dark": {
          "brand": "oklch(0.205 0.015 18)"
        }
      }
    }

[See more examples](/docs/registry/examples)

## Definitions

You can see the JSON Schema for `registry-item.json` [here](https://ui.shadcn.com/schema/registry-item.json).

### $schema

The `$schema` property is used to specify the schema for the `registry-item.json` file.

registry-item.json
    
    
    Copy{
      "$schema": "https://ui.shadcn.com/schema/registry-item.json"
    }

### name

The name of the item. This is used to identify the item in the registry. It should be unique for your registry.

registry-item.json
    
    
    Copy{
      "name": "hello-world"
    }

### title

A human-readable title for your registry item. Keep it short and descriptive.

registry-item.json
    
    
    Copy{
      "title": "Hello World"
    }

### description

A description of your registry item. This can be longer and more detailed than the `title`.

registry-item.json
    
    
    Copy{
      "description": "A simple hello world component."
    }

### type

The `type` property is used to specify the type of your registry item. This is used to determine the type and target path of the item when resolved for a project.

registry-item.json
    
    
    Copy{
      "type": "registry:block"
    }

The following types are supported:

Type| Description  
---|---  
`registry:base`| Use for entire design systems.  
`registry:block`| Use for complex components with multiple files.  
`registry:component`| Use for simple components.  
`registry:font`| Use for fonts.  
`registry:lib`| Use for lib and utils.  
`registry:hook`| Use for hooks.  
`registry:ui`| Use for UI components and single-file primitives.  
`registry:page`| Use for page or file-based routes.  
`registry:file`| Use for miscellaneous files.  
`registry:style`| Use for registry styles. eg. `new-york`.  
`registry:theme`| Use for themes.  
`registry:item`| Use for universal registry items.  
  
### author

The `author` property is used to specify the author of the registry item.

It can be unique to the registry item or the same as the author of the registry.

registry-item.json
    
    
    Copy{
      "author": "John Doe <john@doe.com>"
    }

### dependencies

The `dependencies` property is used to specify the dependencies of your registry item. This is for `npm` packages.

Use `@version` to specify the version of your registry item.

registry-item.json
    
    
    Copy{
      "dependencies": [
        "@radix-ui/react-accordion",
        "zod",
        "lucide-react",
        "name@1.0.2"
      ]
    }

### devDependencies

The `devDependencies` property is used to specify the dev dependencies of your registry item. These are `npm` packages that are only needed during development.

Use `@version` to specify the version of the package.

registry-item.json
    
    
    Copy{
      "devDependencies": ["tw-animate-css", "name@1.2.0"]
    }

### registryDependencies

Used for registry dependencies. Can be names, namespaced or URLs.

  * For `shadcn/ui` registry items such as `button`, `input`, `select`, etc use the name eg. `['button', 'input', 'select']`.
  * For namespaced registry items such as `@acme` use the name eg. `['@acme/input-form']`.
  * For custom registry items use the URL of the registry item eg. `['https://example.com/r/hello-world.json']`.

registry-item.json
    
    
    Copy{
      "registryDependencies": [
        "button",
        "@acme/input-form",
        "https://example.com/r/editor.json"
      ]
    }

Note: The CLI will automatically resolve remote registry dependencies.

### files

The `files` property is used to specify the files of your registry item. Each file has a `path`, `type` and `target` (optional) property.

**The`target` property is required for `registry:page` and `registry:file` types.**

registry-item.json
    
    
    Copy{
      "files": [
        {
          "path": "registry/new-york/hello-world/page.tsx",
          "type": "registry:page",
          "target": "app/hello/page.tsx"
        },
        {
          "path": "registry/new-york/hello-world/hello-world.tsx",
          "type": "registry:component"
        },
        {
          "path": "registry/new-york/hello-world/use-hello-world.ts",
          "type": "registry:hook"
        },
        {
          "path": "registry/new-york/hello-world/.env",
          "type": "registry:file",
          "target": "~/.env"
        }
      ]
    }

#### path

The `path` property is used to specify the path to the file in your registry. This path is used by the build script to parse, transform and build the registry JSON payload.

#### type

The `type` property is used to specify the type of the file. See the type section for more information.

#### target

The `target` property is used to indicate where the file should be placed in a project. This is optional and only required for `registry:page` and `registry:file` types.

By default, the `shadcn` cli will read a project's `components.json` file to determine the target path. For some files, such as routes or config you can specify the target path manually.

Use `~` to refer to the root of the project e.g `~/foo.config.js`.

### tailwind

**DEPRECATED:** Use `cssVars.theme` instead for Tailwind v4 projects.

The `tailwind` property is used for tailwind configuration such as `theme`, `plugins` and `content`.

You can use the `tailwind.config` property to add colors, animations and plugins to your registry item.

registry-item.json
    
    
    Copy{
      "tailwind": {
        "config": {
          "theme": {
            "extend": {
              "colors": {
                "brand": "hsl(var(--brand))"
              },
              "keyframes": {
                "wiggle": {
                  "0%, 100%": { "transform": "rotate(-3deg)" },
                  "50%": { "transform": "rotate(3deg)" }
                }
              },
              "animation": {
                "wiggle": "wiggle 1s ease-in-out infinite"
              }
            }
          }
        }
      }
    }

### cssVars

Use to define CSS variables for your registry item.

registry-item.json
    
    
    Copy{
      "cssVars": {
        "theme": {
          "font-heading": "Poppins, sans-serif"
        },
        "light": {
          "brand": "20 14.3% 4.1%",
          "radius": "0.5rem"
        },
        "dark": {
          "brand": "20 14.3% 4.1%"
        }
      }
    }

### css

Use `css` to add new rules to the project's CSS file eg. `@layer base`, `@layer components`, `@utility`, `@keyframes`, `@plugin`, etc.

registry-item.json
    
    
    Copy{
      "css": {
        "@plugin @tailwindcss/typography": {},
        "@plugin foo": {},
        "@layer base": {
          "body": {
            "font-size": "var(--text-base)",
            "line-height": "1.5"
          }
        },
        "@layer components": {
          "button": {
            "background-color": "var(--color-primary)",
            "color": "var(--color-white)"
          }
        },
        "@utility text-magic": {
          "font-size": "var(--text-base)",
          "line-height": "1.5"
        },
        "@keyframes wiggle": {
          "0%, 100%": {
            "transform": "rotate(-3deg)"
          },
          "50%": {
            "transform": "rotate(3deg)"
          }
        }
      }
    }

### envVars

Use `envVars` to add environment variables to your registry item.

registry-item.json
    
    
    Copy{
      "envVars": {
        "NEXT_PUBLIC_APP_URL": "http://localhost:4000",
        "DATABASE_URL": "postgresql://postgres:postgres@localhost:5432/postgres",
        "OPENAI_API_KEY": ""
      }
    }

Environment variables are added to the `.env.local` or `.env` file. Existing variables are not overwritten.

**IMPORTANT:** Use `envVars` to add development or example variables. Do NOT use it to add production variables.

### docs

Use `docs` to show custom documentation or message when installing your registry item via the CLI.

registry-item.json
    
    
    Copy{
      "docs": "To get an OPENAI_API_KEY, sign up for an account at https://platform.openai.com."
    }

### categories

Use `categories` to organize your registry item.

registry-item.json
    
    
    Copy{
      "categories": ["sidebar", "dashboard"]
    }

### meta

Use `meta` to add additional metadata to your registry item. You can add any key/value pair that you want to be available to the registry item.

registry-item.json
    
    
    Copy{
      "meta": { "foo": "bar" }
    }

[ registry.json](/docs/registry/registry-json)

On This Page

Definitions$schemanametitledescriptiontypeauthordependenciesdevDependenciesregistryDependenciesfilespathtypetargettailwindcssVarscssenvVarsdocscategoriesmeta

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Adobe, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)
