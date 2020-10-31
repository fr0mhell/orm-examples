from django.contrib import admin
from . import models


@admin.register(models.Spaceship)
class SpaceshipAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'ship_class',
        'pilot',
        'hp',
    )


@admin.register(models.Pilot)
class PilotAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Race)
class RaceAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Fraction)
class FractionAdmin(admin.ModelAdmin):
    ...


@admin.register(models.PilotFraction)
class PilotFractionAdmin(admin.ModelAdmin):
    ...
