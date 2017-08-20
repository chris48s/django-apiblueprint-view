# django-apiblueprint-view

[![Build Status](https://travis-ci.org/chris48s/django-apiblueprint-view.svg?branch=master)](https://travis-ci.org/chris48s/django-apiblueprint-view)
[![Coverage Status](https://coveralls.io/repos/github/chris48s/django-apiblueprint-view/badge.svg?branch=master)](https://coveralls.io/github/chris48s/django-apiblueprint-view?branch=master)

Render API Blueprints on-the-fly using Django templates

## Installation

1. `django-apiblueprint-view` uses the [Drafter](https://github.com/apiaryio/drafter) C library for API Blueprint parsing. Install it using:

```
git clone --recursive git://github.com/apiaryio/drafter.git
cd drafter
./configure --shared
make libdrafter
sudo cp build/out/Release/lib.target/libdrafter.so /usr/lib/libdrafter.so
sudo cp src/drafter.h /usr/include/drafter/drafter.h
```

2. `pip install git+https://github.com/chris48s/django-apiblueprint-view.git`

3. Add to `INSTALLED_APPS` in django settings:

```python
INSTALLED_APPS = [
    ...
    'apiblueprint_view',
]
```

## Platform Support

`django-apiblueprint-view` is tested under:
* Python 3.4 and 3.5
* Django 1.8, 1.9, 1.10 and 1.11

## Usage

```python
from apiblueprint_view.views import ApiBlueprintView

urlpatterns = [
    url(r'^docs/$', ApiBlueprintView.as_view(blueprint='/path/to/blueprint.apibp')),
]
```

## Styling

### Custom HTML Template

Define a custom base template. It must include the tag

```
{% include 'api_docs/docs_parent.html' %}
```

Pass it into `ApiBlueprintView.as_view()` as a parameter.

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

`ApiBlueprintView.as_view()` may accept a `styles` dictionary describing custom CSS classes which should be attached to rendered HTML tags. For example:

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

## Licensing

`django-apiblueprint-view` is made available under the MIT License

## Development

Build and install locally:

```
python setup.py sdist
pip install --upgrade dist/django-apiblueprint-view-x.y.z.tar.gz
```

Run the tests locally:

```
pip install -r testing_requirements.txt
./run_tests.py
```
