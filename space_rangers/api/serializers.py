from rest_framework.serializers import ModelSerializer

from .. import models


class RaceSerializer(ModelSerializer):

    class Meta:
        model = models.Race
        fields = (
            'id',
            'name',
        )


class PilotShortInfoSerializer(ModelSerializer):
    race = RaceSerializer()

    class Meta:
        model = models.Pilot
        fields = (
            'id',
            'name',
            'race',
        )


class SpaceshipSerializer(ModelSerializer):
    pilot = PilotShortInfoSerializer()

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


class PilotSerializer(ModelSerializer):
    race = RaceSerializer(read_only=True)
    spaceships = SpaceshipSerializer(many=True, required=False, read_only=True)
    fractions = FractionSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = models.Pilot
        fields = (
            'id',
            'name',
            'race',
            'user',
            'spaceships',
            'fractions',
        )
