# django-apiblueprint-view

[![Build Status](https://travis-ci.org/chris48s/django-apiblueprint-view.svg?branch=master)](https://travis-ci.org/chris48s/django-apiblueprint-view)
[![Coverage Status](https://coveralls.io/repos/github/chris48s/django-apiblueprint-view/badge.svg?branch=master)](https://coveralls.io/github/chris48s/django-apiblueprint-view?branch=master)
![PyPI Version](https://img.shields.io/pypi/v/django-apiblueprint-view.svg)
![License](https://img.shields.io/pypi/l/django-apiblueprint-view.svg)
![Python Support](https://img.shields.io/pypi/pyversions/django-apiblueprint-view.svg)
![Django Support](https://img.shields.io/pypi/djversions/django-apiblueprint-view.svg)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

Render [API Blueprints](https://apiblueprint.org/) on-the-fly using Django templates

## Installation

1. `pip install django-apiblueprint-view`

2. Add to `INSTALLED_APPS` in django settings:

```python
INSTALLED_APPS = [
    ...
    'apiblueprint_view',
]
```

## Basic Usage

```python
from apiblueprint_view.views import ApiBlueprintView

urlpatterns = [
    url(r'^docs/$', ApiBlueprintView.as_view(blueprint='/path/to/blueprint.apibp')),
]
```

`ApiBlueprintView` has 4 properties which may be passed as params to `.as_view()` as parameters, or defined as class properties:

```py
from apiblueprint_view.views import ApiBlueprintView

class ApiDocsView(ApiBlueprintView):

    blueprint = 'path/to/blueprint.apibp'  # blueprint to render
    drafter_path = 'path/to/libdrafter.so'  # custom drafter library
    template_name = 'base_template.html'  # template to render with
    styles = {  # custom CSS clases
        'resource': {'class': 'card'},
        'resource_group': {'class': 'card'},
    }

urlpatterns = [
    url(r'^docs/$', ApiDocsView.as_view()),
]
```

## Drafter

`django-apiblueprint-view` uses the [Drafter](https://github.com/apiaryio/drafter) C library for API Blueprint parsing. It is compatible with any Drafter >=4.0.0,<6.0.0. By default, a manylinux drafter 4.1.0 shared object is bundled with the package, but it is also possible to use an external drafter library by setting `drafter_path`. This is necessary if you want to use a different version of drafter or use this library on Windows/Mac.

```py
# Use the vendored shared object (drafter 4.1.0/manylinux).
ApiBlueprintView.as_view(blueprint='/path/to/blueprint.apibp')

# Use drafter at this specific path.
ApiBlueprintView.as_view(
    blueprint='/path/to/blueprint.apibp',
    drafter_path='/path/to/libdrafter.dylib'
)

# Search for a global `libdrafter` using `ctypes.util.find_library()`.
ApiBlueprintView.as_view(
    blueprint='/path/to/blueprint.apibp',
    drafter_path=None
)
```

## Styling

### Custom HTML Template

Define a custom base template. It must include the tag

```
{% include 'api_docs/docs_parent.html' %}
```

Set it using `template_name`.

```python
from apiblueprint_view.views import ApiBlueprintView

urlpatterns = [
    url(r'^docs/$', ApiBlueprintView.as_view(
        blueprint='/path/to/blueprint.apibp',
        template_name='my_base_template.html'
    )),
]
```

### Custom CSS

ApiBlueprintView may accept a `styles` dictionary describing custom CSS classes which should be attached to rendered HTML tags.

```python
from apiblueprint_view.views import ApiBlueprintView

urlpatterns = [
    url(r'^docs/$', ApiBlueprintView.as_view(
        blueprint='/path/to/blueprint.apibp',
        template_name='my_base_template.html',
        styles={
            'action': {'class': 'foo bar'},
            'method': {'class': 'baz'}
        }
    )),
]
```

The following keys are valid. All keys are optional:

* `'action'`: Container `<div>` for an API action
* `'action_transaction'`: Container `<div>` for a HTTP transaction (request and response)
* `'action_request'`: Container `<div>` for a HTTP request
* `'action_response'`: Container `<div>` for a HTTP response
* `'action_schema'`: Container `<div>` for a HTTP request or response schema
* `'action_headers'`: Container `<div>` for HTTP request or response headers
* `'action_body'`: Container `<div>` for a HTTP request or response body
* `'action_example'`: Container `<div>` for an API action example URL
* `'description'`: Container `<div>` for some text describing an action, resource, request, response, etc
* `'parameters'`: Container `<div>` for a list of parameters
* `'method'`: Generic `<span>` containing an HTTP method
* `'method_CONNECT'`: `<span>` containing the text `CONNECT`
* `'method_DELETE'`: `<span>` containing the text `DELETE`
* `'method_GET'`: `<span>` containing the text `GET`
* `'method_HEAD'`: `<span>` containing the text `HEAD`
* `'method_OPTIONS'`: `<span>` containing the text `OPTIONS`
* `'method_PATCH'`: `<span>` containing the text `PATCH`
* `'method_POST'`: `<span>` containing the text `POST`
* `'method_PUT'`: `<span>` containing the text `PUT`
* `'method_TRACE'`: `<span>` containing the text `TRACE`
* `'resource'`: Container `<div>` for an API resource
* `'resource_group'`: Container `<div>` for an API resource group

[Highlight.js](https://highlightjs.org/) can be used to add syntax highlighting

### Including Files

You can include other files in your blueprint by using an include directive with a path to the included file relative to the current file's directory. Included files can include other files, so be careful of circular references.

```
<!-- include(filename.md) -->
```

This syntax is not a part of the API Blueprint spec, but is also supported in some other tools e.g: [aglio](https://github.com/danielgtaylor/aglio#including-files).

The include directive has the potential to introduce remote file inclusion or directory traversal vulnerabilities if your application renders user-supplied content. There are a couple of settings to help mitigate this. Set `APIBP_PROCESS_INCLUDES = False` in your django settings to completely ignore include directives (the default is `True`). There is also a whitelist of allowed file types to include. The default whitelist is `['.md', '.apibp', '.json']` but this can be overridden by setting `APIBP_INCLUDE_WHITELIST` to a list of allowed extensions in your django settings.
