from . import models
import factory
from factory import fuzzy, django
from random import randint


class SpaceshipFactory(django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Spaceship %04d" % n)
    ship_class = fuzzy.FuzzyChoice(
        models.Spaceship.SpaceshipClassChoices.choices,
        getter=lambda c: c[0],
    )
    speed = fuzzy.FuzzyInteger(100, 1000)
    max_hp = fuzzy.FuzzyInteger(100, 1000)
    max_distance = fuzzy.FuzzyInteger(10, 100)

    @factory.lazy_attribute
    def current_hp(self):
        return randint(0, self.max_hp)

    class Meta:
        model = models.Spaceship


class RaceFactory(django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Race %04d" % n)

    class Meta:
        model = models.Race


class FractionFactory(django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Fraction %04d" % n)

    class Meta:
        model = models.Fraction


class PilotFactory(django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Pilot %04d" % n)
    race = factory.SubFactory(RaceFactory)

    class Meta:
        model = models.Pilot
