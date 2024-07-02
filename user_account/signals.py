


# myapp/signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(pre_save, sender=User)
def test_signal(sender, instance, **kwargs):
    print("User instance is about to be saved!")
    # Your logic here
