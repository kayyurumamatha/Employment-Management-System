#Design
#a Model STAFF_PERSONAL for storing personal details such as staff id, name,
#Age, Mobile no, E-mail id, Department

# Create your models here.
from django.db import models
class staff(models.Model):
    staffid=models.CharField(max_length=10,unique=True)
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    mobno=models.CharField(max_length=10)
    emailid=models.CharField(max_length=40)
    dept=models.CharField(max_length=20)