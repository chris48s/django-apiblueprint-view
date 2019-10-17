from django.test import TestCase, RequestFactory
from apiblueprint_view.views import ApiBlueprintView


class ApibpTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def get_response(self, fixture):
        view = ApiBlueprintView.as_view(blueprint=fixture)
        response = view(self.factory.get("/foo/bar"))
        response.render()
        return response

    def get_html(self, response):
        return response.content.decode("utf-8")
