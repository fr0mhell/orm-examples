from django.dispatch import Signal, receiver

from space_rangers.models import Pilot, healed


@receiver(healed, sender=Pilot)
def hey(sender, instance, abc, **kwargs):
    """"""
    print(instance)
