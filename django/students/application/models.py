   from django.db import models

# Create your models here.

class Datas(models.Model):
    Student_Name= models.CharField(max_length=25)
    First_Name= models.CharField(max_length=25)
    Middle_Name= models.CharField(max_length=25)
    Last_Name= models.CharField(max_length=25)
    Date_of_Birth= models.DateField()
    Mobile_Number= models.IntegerField()
    Email_Address= models.EmailField(max_length=50)
    Address= models.CharField(max_length=60)  
    

