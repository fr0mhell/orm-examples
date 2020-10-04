from uuid import uuid4
from django.db import models


def get_uid():
    return str(uuid4())


class PilotQuerySet(models.QuerySet):
    """"""


class PilotManager(models.Manager):
    """"""


class Spaceship(models.Model):
    """Model representing Spaceship."""
    class SpaceshipClassChoices(models.TextChoices):
        WARRIOR = 'W', 'Warrior'
        PIRATE = 'P', 'Pirate'
        MERCHANT = 'M', 'Merchant'
        DIPLOMAT = 'D', 'Diplomat'

    name = models.CharField(
        max_length=128,
        verbose_name='Name',
    )
    uid = models.CharField(
        max_length=128,
        primary_key=True,
        unique=True,
        default=get_uid,
    )
    ship_class = models.CharField(
        max_length=1,
        choices=SpaceshipClassChoices.choices,
        default=SpaceshipClassChoices.WARRIOR,
        verbose_name='Spaceship class',
    )
    speed = models.IntegerField(
        default=100,
        verbose_name='Speed',
        help_text='Spaceship speed',
    )
    hp = models.IntegerField(
        default=0,
        verbose_name='Hit Points',
        help_text='Spaceship Hit Points',
    )
    max_distance = models.IntegerField(
        default=0,
        verbose_name='Max Distance',
        help_text='Spaceship Max Distance for Hyper-jump',
    )

    pilot = models.OneToOneField(
        to='space_rangers.Pilot',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='space_ship',
    )

    class Meta:
        ordering = ['-name', ]
        db_table = 'spaceships'
        unique_together = (
            'name', 'ship_class',
        )

    def __str__(self):
        return self.name


class Pilot(models.Model):
    """"""
    name = models.CharField(
        max_length=128,
        verbose_name='Name',
    )
    race = models.ForeignKey(
        to='space_rangers.Race',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='pilots',
    )
    fractions = models.ManyToManyField(
        through='space_rangers.PilotFraction',
        related_name='pilots',
        to='space_rangers.Fraction',
        related_query_name='all_pilots',
    )


class Race(models.Model):
    """"""
    name = models.CharField(
        max_length=128,
        verbose_name='Name',
    )


class Fraction(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Name',
    )


class PilotFraction(models.Model):
    pilot = models.ForeignKey(
        to=Pilot,
        on_delete=models.CASCADE,
    )
    fraction = models.ForeignKey(
        to=Fraction,
        on_delete=models.CASCADE,
    )
