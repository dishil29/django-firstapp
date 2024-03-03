from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Member(models.Model):
  user_data = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True )
  