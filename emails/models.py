from space_rangers.models import healed, Pilot
from django.dispatch import Signal, receiver


@receiver(healed, sender=Pilot)
def hey(sender, instance, abc, **kwargs):
    """"""
    print(instance)
