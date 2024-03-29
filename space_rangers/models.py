from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import Signal, receiver

healed = Signal()


def validate_speed(value):
    if 49 < value < 501:
        raise ValidationError(
            f'Wrong value for `speed` param. '
            f'Your value {value} is not in the range [50, ... 500]'
        )


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
        validators=(
            validate_speed,
        )
    )
    current_hp = models.IntegerField(
        default=0,
        verbose_name='Current Hit Points',
        validators=(
            MinValueValidator(limit_value=0),
        )
    )
    max_hp = models.IntegerField(
        default=1,
        verbose_name='Maximum Hit Points',
        validators=(
            MaxValueValidator(limit_value=1000),
        )
    )
    max_distance = models.IntegerField(
        default=1,
        verbose_name='Max Distance',
        help_text='Spaceship Max Distance for Hyper-jump',
    )
    pilot = models.ForeignKey(
        to='space_rangers.Pilot',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='spaceships',
    )

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name

    @property
    def hp(self):
        return f'{self.current_hp} / {self.max_hp}'

    def heal(self):
        """Heal the spaceship."""
        self.current_hp = self.max_hp
        self.save()

    def kill(self):
        """Kill the spaceship."""
        self.current_hp = 0
        self.save()

    def full_clean(self, exclude=None, validate_unique=True):
        return super().full_clean(exclude, validate_unique)

    def clean_fields(self, exclude=None):
        return super().clean_fields(exclude)

    def clean(self):
        if self.current_hp > self.max_hp:
            raise ValidationError({
                'current_hp': '`current_hp` must be less of equal to `max_hp`'
            })

    def validate_unique(self, exclude=None):
        return super().validate_unique(exclude)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Pilot(models.Model):
    """Pilot model."""
    name = models.CharField(
        max_length=128,
        verbose_name='Name',
    )
    race = models.ForeignKey(
        to='space_rangers.Race',
        on_delete=models.CASCADE,
        related_name='pilots',
    )
    fractions = models.ManyToManyField(
        through='space_rangers.PilotFraction',
        related_name='pilots',
        to='space_rangers.Fraction',
        related_query_name='all_spaceships',
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return f'{self.name} ({self.race})'

    def save(self, *args, **kwargs):
        print('before Saving!')
        super().save(*args, **kwargs)
        print('after Saving!')

    def heal_all(self):
        """Heal all ships."""
        ships = self.spaceships.all()
        for ship in ships:
            ship.heal()

        healed.send(sender=Pilot, instance=self, abc=1)

    def kill_all(self):
        """Kill all ships."""
        ships = self.spaceships.all()
        for ship in ships:
            ship.kill()


@receiver(pre_save, sender=Pilot)
def pre_handler(sender, instance, **kwargs):
    print(f'Pre-save for Pilot {instance.name}!')


@receiver(post_save, sender=Pilot)
def my_handler(sender, instance, **kwargs):
    print(f'Post-save for Pilot {instance.name}!')


class Race(models.Model):
    """Model representing Pilot's race."""
    name = models.CharField(
        max_length=128,
        verbose_name='Name',
    )

    def __str__(self):
        return self.name


class Fraction(models.Model):
    """Model representing Pilot's fraction."""
    name = models.CharField(
        max_length=128,
        verbose_name='Name',
    )

    def __str__(self):
        return self.name


class PilotFraction(models.Model):
    """Model representing Pilot's fraction."""
    pilot = models.ForeignKey(
        to=Pilot,
        on_delete=models.CASCADE,
    )
    fraction = models.ForeignKey(
        to=Fraction,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.fraction.name

    class Meta:
        unique_together = (
            'pilot', 'fraction',
        )
