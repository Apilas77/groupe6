from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "casino/index.html"


class GameView(TemplateView):
    template_name = "casino/start.html"
