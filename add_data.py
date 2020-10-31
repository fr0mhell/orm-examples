import random
from space_rangers import factories, models

SPACESHIPS = 1000
RACES = 5
FRACTIONS = 20
PILOTS = 200


spaceships = factories.SpaceshipFactory.create_batch(SPACESHIPS)
races = factories.RaceFactory.create_batch(RACES)
fractions = factories.FractionFactory.create_batch(FRACTIONS)

# Select random spaceships, 1 per pilot
pilot_ships = random.sample(spaceships, PILOTS)
for i in range(PILOTS):
    # Select spaceship for pilot
    spaceship = pilot_ships[i]
    # Select random race for pilot
    race = random.choice(races)
    # Select 1-5 random fractions for pilot
    pilot_fractions = random.sample(
        fractions,
        random.randint(1, 5)
    )

    pilot = factories.PilotFactory(race=race)
    spaceship.pilot = pilot
    spaceship.save()
    for fraction in pilot_fractions:
        models.PilotFraction.objects.create(
            pilot=pilot,
            fraction=fraction,
        )
