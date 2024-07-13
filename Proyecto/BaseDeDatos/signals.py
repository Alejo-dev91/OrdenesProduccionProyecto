from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save,sender=Profile)
def add_user_to_administrative_group(sender,instance,created,**kwargs):
    if created:
        try:
            administrative=Group.objects.get(name='administrativos')
        except Group.DoesNotExist:
            administrative=Group.objects.create(name='administrativos')
        instance.user.groups.add(administrative)
            