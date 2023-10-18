from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, primary_key=True)
    first_time_user = models.BooleanField(default=True)
    grade = models.IntegerField(default=0)
    school = models.CharField(max_length=100, default='')
    datebirth = models.CharField(max_length=100, default='')
 
    def __str__(self):
        return self.username


class OperationLevel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.IntegerField()
    new_level = models.IntegerField()
    old_level = models.IntegerField()
    operation = models.CharField(max_length=100)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username + " " + self.operation + " " + str(self.score)
    
    class Meta:
        ordering = ['-date']

@receiver(post_save, sender=User)
def create_operation_levels(sender, instance, created, **kwargs):
    if created:
        # Create the four OperationLevel instances
        OperationLevel.objects.create(user=instance, name='addition', level=1)
        OperationLevel.objects.create(user=instance, name='subtraction', level=1)
        OperationLevel.objects.create(user=instance, name='multiplication', level=1)
        OperationLevel.objects.create(user=instance, name='division', level=1)


