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
    list_filter = (
        'ship_class',
    )
    ordering = (
        'name',
        'ship_class',
        'pilot',
    )


@admin.register(models.Race)
class RaceAdmin(admin.ModelAdmin):
    """Admin class for `Race` model."""
    search_fields = (
        'name',
    )


@admin.register(models.Fraction)
class FractionAdmin(admin.ModelAdmin):
    """Admin class for `Fraction` model."""
    search_fields = (
        'name',
    )


class SpaceshipInline(admin.TabularInline):
    """Inline class for `Spaceship` model."""
    model = models.Spaceship
    extra = 1


class PilotFractionInline(admin.StackedInline):
    """Inline class for `PilotFraction` model."""
    model = models.PilotFraction
    extra = 1
    autocomplete_fields = (
        'fraction',
    )


@admin.register(models.Pilot)
class PilotAdmin(admin.ModelAdmin):
    """Admin class for `Pilot` model."""
    list_display = (
        'id',
        'name',
        'race',
    )
    inlines = (
        SpaceshipInline,
        PilotFractionInline,
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
