from .. import models
from rest_framework.serializers import ModelSerializer


class SpaceshipSerializer(ModelSerializer):

    class Meta:
        model = models.Spaceship
        fields = (
            'id',
            'name',
            'ship_class',
            'speed',
            'max_distance',
            'pilot',
            'hp',
        )


class FractionSerializer(ModelSerializer):

    class Meta:
        model = models.Fraction
        fields = (
            'id',
            'name',
        )


class RaceSerializer(ModelSerializer):

    class Meta:
        model = models.Race
        fields = (
            'id',
            'name',
        )


class PilotSerializer(ModelSerializer):
    race = RaceSerializer()
    spaceships = SpaceshipSerializer(many=True)
    fractions = FractionSerializer(many=True)

    class Meta:
        model = models.Pilot
        fields = (
            'id',
            'name',
            'race',
            'user',
            'spaceships',
        )
