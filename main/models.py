from django.db import models

# Create your models here.
class Wleta(models.Model):
  added_date = models.DateTimeField()
  full_name = models.CharField(max_length=30)
  wleta_list = models.CharField(max_length=50)