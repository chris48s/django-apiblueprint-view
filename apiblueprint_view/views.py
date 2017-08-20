from django.views.generic import TemplateView
from .parser import ApibpParser


BASE_STYLES = {
    'action': {'class': 'api-action'},
    'action_body': {'class': 'api-action-body'},
    'action_example': {'class': 'api-action-example'},
    'action_headers': {'class': 'api-action-headers'},
    'action_request': {'class': 'api-action-request'},
    'action_response': {'class': 'api-action-response'},
    'action_schema': {'class': 'api-action-schema'},
    'action_transaction': {'class': 'api-action-transaction'},
    'description': {'class': 'api-description'},
    'method': {'class': 'api-method'},
    'method_CONNECT': {'class': 'api-method-CONNECT'},
    'method_DELETE': {'class': 'api-method-DELETE'},
    'method_GET': {'class': 'api-method-GET'},
    'method_HEAD': {'class': 'api-method-HEAD'},
    'method_OPTIONS': {'class': 'api-method-OPTIONS'},
    'method_PATCH': {'class': 'api-method-PATCH'},
    'method_POST': {'class': 'api-method-POST'},
    'method_PUT': {'class': 'api-method-PUT'},
    'method_TRACE': {'class': 'api-method-TRACE'},
    'parameters': {'class': 'api-parameters'},
    'resource': {'class': 'api-resource'},
    'resource_group': {'class': 'api-resource-group'},
}


class ApiBlueprintView(TemplateView):

    blueprint = None
    template_name = "api_docs/default_base.html"
    styles = None

    def make_styles(self):
        styles = BASE_STYLES
        if not isinstance(self.styles, dict):
            return styles
        for style in styles:
            if style in self.styles and 'class' in self.styles[style] and\
                isinstance(self.styles[style]['class'], str):
                styles[style]['class'] += ' ' + self.styles[style]['class']
        return styles

    def get_context_data(self, **context):
        parser = ApibpParser(self.blueprint)
        api = parser.parse()

        context['root'] = api.content[0]
        context['styles'] = self.make_styles()

        return context
