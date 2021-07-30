from django.views import generic # CreateView, UpdateView, DetailView, DeleteView, ListView, TemplateView, RedirectView
from . import models


class SpaceshipCreateView(generic.CreateView):
    """"""
    queryset = models.Spaceship.objects.all()


class SpaceshipUpdateView(generic.UpdateView):
    """"""
    queryset = models.Spaceship.objects.all()


class SpaceshipDetailView(generic.DetailView):
    """"""
    queryset = models.Spaceship.objects.all()
