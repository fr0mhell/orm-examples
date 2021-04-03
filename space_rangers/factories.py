from random import randint

from django.contrib.auth.models import User
from django.utils.text import slugify

import factory
from factory import django, fuzzy

from . import models


class UserFactory(django.DjangoModelFactory):
    username = factory.Sequence(lambda n: "User %03d" % n)

    @factory.lazy_attribute
    def email(self):
        slug_name = slugify(self.username)
        return f'{slug_name}@example.com'

    @factory.post_generation
    def set_pwd(self, create, extracted, **kwargs):
        slug_name = slugify(self.username)
        self.set_password(slug_name)
        self.save()

    class Meta:
        model = User


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
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = models.Pilot
