# Changelog

## :package: [2.1.1](https://pypi.org/project/django-apiblueprint-view/2.1.1/) - 2019-10-17

* Tested on python 3.8
* Adopt poetry for packaging

## :package: [2.1.0](https://pypi.org/project/django-apiblueprint-view/2.1.0/) - 2019-05-31

* Fixes to whitespace in rendered output
* Pin `draughtsman` to 0.1.0
* Add support for django 2.2
* Drop support for django 2.0

## :package: [2.0.1](https://pypi.org/project/django-apiblueprint-view/2.0.1/) - 2019-05-13

Strip redundant whitespace in output

## :package: [2.0.0](https://pypi.org/project/django-apiblueprint-view/2.0.0/) - 2018-11-04

* Add support for python 3.7, django 2.1
* Require python >=3.5, django >=1.11
* Drop dependency on `typing`
* Fix `ResourceWarnings`

## :package: [1.1.2](https://pypi.org/project/django-apiblueprint-view/1.1.2/) - 2017-12-03

Add support for python 3.6, django 2.0

## :package: [1.1.1](https://pypi.org/project/django-apiblueprint-view/1.1.1/) - 2017-10-26

Distribute via PyPI

## :package: 1.1.0 - 2017-10-03

Allow include directive to be used more safely [#10](https://github.com/chris48s/django-apiblueprint-view/pull/1):
  * Allow user to turn off processing includes
  * Use `safe_join` to ensure included files are inside project dir
  * Implement file extension whitelist for includes

## :package: 1.0.0 - 2017-08-20

First Release
