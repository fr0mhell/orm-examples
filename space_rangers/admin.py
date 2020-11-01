from django.contrib import admin
from . import models


@admin.register(models.Spaceship)
class SpaceshipAdmin(admin.ModelAdmin):
    """Admin class for `Spaceship` model."""
    list_display = (
        'id',
        'name',
        'ship_class',
        'pilot',
        'hp',
    )
    readonly_fields = (
        'current_hp',
        'max_hp',
    )
    autocomplete_fields = (
        'pilot',
    )


@admin.register(models.Pilot)
class PilotAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'race',
    )
    list_filter = (
        'race',
    )
    autocomplete_fields = (
        'race',
    )
    search_fields = (
        'name',
    )


@admin.register(models.Race)
class RaceAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )


@admin.register(models.Fraction)
class FractionAdmin(admin.ModelAdmin):
    ...


@admin.register(models.PilotFraction)
class PilotFractionAdmin(admin.ModelAdmin):
    ...
