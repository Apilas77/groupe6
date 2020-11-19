from django.core.management import call_command
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import ApplicationForm
from .models import Application


class IndexView(TemplateView):
    template_name = "home/index.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Application, pk=self.kwargs["pk"])


class AddView(FormView):
    template_name = "home/add-form.html"
    form_class = ApplicationForm
    success_url = "//"

    def form_valid(self, form):
        call_command('startapp', form.nom)

        return super().form_valid(form)
