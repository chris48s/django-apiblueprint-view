from django.template.defaulttags import register


@register.filter
def get_class(dictionary, key):
    el = dictionary.get('method_' + key, None)
    if el:
        return el['class']
    return ''
