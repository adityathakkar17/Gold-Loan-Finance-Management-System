from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError 
# Create your models here.

class User:
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=25)

class Customer(models.Model):
    customerName=models.CharField(max_length=100)
    customerId=models.CharField(max_length=15,primary_key=True)
    aadhharId=models.CharField(unique=True,max_length=12)
    nomineeName=models.CharField(max_length=100)
    income=models.PositiveIntegerField()
    address=models.CharField(max_length=100)
    mobile=models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(10)])

class Admin(models.Model):
    adminID=models.CharField(max_length=15,primary_key=True)
    adminName=models.CharField(max_length=50)
    
class GuestUser(models.Model):
    guestUserName=models.CharField(max_length=100)
    emailAddress=models.CharField(max_length=50)
    contactNumber=models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(10)])

class LoanApplication(models.Model):
    APPROVED='APP'
    REJECTED='REJ'
    FILE_UNDER_PROCESS='FUP'
    ApplicationStatus=[(APPROVED,'Approved'),(REJECTED,'Rejected'),(FILE_UNDER_PROCESS,'Under process')]
    uniqueLoanId=models.CharField(max_length=20,primary_key=True)
    lentRateOfInterest=models.DecimalField(max_digits=5,decimal_places=2)
    lentGoldValue=models.DecimalField(max_digits=5,decimal_places=2)
    lentLoanTenure=models.PositiveSmallIntegerField()
    loanApplicationStatus=models.CharField(max_length=3,choices=ApplicationStatus)
    ltvRatio=models.DecimalField(max_digits=5,decimal_places=2)

class GoldAsset(models.Model):
    COIN='C'
    BISCUIT='B'
    ORNAMENT='O'
    GoldType=[(BISCUIT,'Biscuit'),(ORNAMENT,'Ornament'),(COIN,'Coin')]
    assetID=models.CharField(max_length=20,primary_key=True)
    weight=models.DecimalField(max_digits=5,decimal_places=2)
    goldType=models.CharField(max_length=1,choices=GoldType)
    purity=models.DecimalField(max_digits=5,decimal_places=2)
    currentGoldValue=models.DecimalField(max_digits=5,decimal_places=2)
    condition=models.CharField(max_length=100)
    remarks=models.CharField(max_length=100)
    count=models.PositiveIntegerField()
