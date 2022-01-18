from django.db import models


# Create your models here.
class user_details_table(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    number = models.IntegerField(unique=True)
    date_time = models.DateTimeField(unique=True)
    patient_id = models.CharField(max_length=10,default="string")
