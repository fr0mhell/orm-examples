from django import forms

from . import models


class SpaceshipForm(forms.ModelForm):

    class Meta:
        model = models.Spaceship
        fields = (
            'name',
            'ship_class',
            'speed',
            'current_hp',
            'max_hp',
            'max_distance',
            'pilot',
        )

    def full_clean(self):
        return super().full_clean()

    def is_valid(self):
        return super().is_valid()

    def clean_max_distance(self):
        max_distance = self.cleaned_data['max_distance']

        if max_distance < 1:
            return 1
        if max_distance > 100:
            return 100

        return max_distance
