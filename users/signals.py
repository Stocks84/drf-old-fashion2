from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile 

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Create a Profile for new users
    if created:
        Profile.objects.create(user=instance)
    else:
        # Save Profile for existing users
        instance.profile.save()
