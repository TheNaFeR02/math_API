from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
 
    def __str__(self):
        return self.username


class OperationLevel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    
    def __str__(self):
        return self.name
    


    

@receiver(post_save, sender=User)
def create_operation_levels(sender, instance, created, **kwargs):
    if created:
        # Create the four OperationLevel instances
        OperationLevel.objects.create(user=instance, name='addition', level=1)
        OperationLevel.objects.create(user=instance, name='subtraction', level=1)
        OperationLevel.objects.create(user=instance, name='multiplication', level=1)
        OperationLevel.objects.create(user=instance, name='division', level=1)


