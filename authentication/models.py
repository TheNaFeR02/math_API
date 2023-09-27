from django.db import models

# Create your models here.
# create a user model that extends from the default django user model
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class OperationLevel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, primary_key=True)
    level = models.IntegerField()
    
    def __str__(self):
        return self.name


    # add = models.ForeignKey(OperationLevel, editable=False)
    # subtract = models.IntegerField(OperationLevel, editable=False)
    # multiply = models.IntegerField(OperationLevel, editable=False)
    # divide = models.IntegerField(OperationLevel, editable=False)
    
