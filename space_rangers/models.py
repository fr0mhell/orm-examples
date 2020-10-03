from django.db import models


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

    def __str__(self):
        return f''
