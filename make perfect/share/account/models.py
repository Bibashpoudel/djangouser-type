from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_sponsor = models.BooleanField(default=False)
    is_ideapeacher = models.BooleanField(default=False)



class Sponsor(models.Model):
	user =  models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Ideapeacher(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)



class Idea(models.Model):
    owner = models.ForeignKey(Ideapeacher, on_delete=models.CASCADE, related_name='ideas')
    title  = models.CharField(max_length=50)