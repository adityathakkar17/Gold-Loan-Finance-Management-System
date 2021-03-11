from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
# Create your models here.

class Customer(models.Model):
    username=models.CharField(max_length=100,default='',unique=True)
    password=models.CharField(max_length=25,default='')
    customerName=models.CharField(max_length=100)
    customerId=models.AutoField(primary_key=True)
    aadhaarId=models.DecimalField(unique=True,max_digits=12,decimal_places=0)
    nomineeName=models.CharField(max_length=100)
    income=models.PositiveIntegerField()
    address=models.CharField(max_length=100)
    mobile=models.DecimalField(max_digits=10,decimal_places=0)
    applicationDate=models.DateField(default=date.today,null=False)
    dob=models.DateField()
    def __str__(self) -> str:
        return self.customerName