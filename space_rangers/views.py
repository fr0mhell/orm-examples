from django.views.generic import TemplateView
from django.conf import settings


class IndexTemplateView(TemplateView):
    """Main page."""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'env': settings.PROJECT_ENV})
        return context
