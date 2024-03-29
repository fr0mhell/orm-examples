from django.contrib import admin, messages

from . import forms, models


@admin.register(models.Spaceship)
class SpaceshipAdmin(admin.ModelAdmin):
    """Admin class for `Spaceship` model."""
    form = forms.SpaceshipForm
    list_display = (
        'id',
        'name',
        'ship_class',
        'pilot',
        'hp',
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

    actions = (
        'heal_selected',
        'kill_selected',
    )

    def heal_selected(self, request, queryset):
        for obj in queryset:
            obj.heal()

        messages.success(request, 'All selected spaceships healed!')

    def kill_selected(self, request, queryset):
        for obj in queryset:
            obj.kill()


@admin.register(models.Race)
class RaceAdmin(admin.ModelAdmin):
    """Admin class for `Race` model."""
    search_fields = (
        'name',
    )


class PilotFractionInline(admin.StackedInline):
    """Inline class for `PilotFraction` model."""
    model = models.PilotFraction
    extra = 1
    autocomplete_fields = (
        'fraction',
    )


@admin.register(models.Fraction)
class FractionAdmin(admin.ModelAdmin):
    """Admin class for `Fraction` model."""
    search_fields = (
        'name',
    )
    inlines = (
        PilotFractionInline,
    )


class SpaceshipInline(admin.TabularInline):
    """Inline class for `Spaceship` model."""
    model = models.Spaceship
    extra = 1


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
