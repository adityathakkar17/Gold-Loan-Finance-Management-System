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

class GoldAsset(models.Model):
    COIN='C'
    BISCUIT='B'
    ORNAMENT='O'
    GoldType=[(BISCUIT,'Biscuit'),(ORNAMENT,'Ornament'),(COIN,'Coin')]
    assetID=models.AutoField(primary_key=True)
    weight=models.DecimalField(max_digits=5,decimal_places=2)
    goldtype=models.CharField(max_length=1,choices=GoldType)
    customerId=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)

class LoanApplication(models.Model):
    APPROVED='APP'
    REJECTED='REJ'
    FILE_UNDER_PROCESS='FUP'
    ApplicationStatus=[(APPROVED,'Approved'),(REJECTED,'Rejected'),(FILE_UNDER_PROCESS,'Under process')]
    loanId=models.AutoField(primary_key=True)
    principalAmount=models.DecimalField(max_digits=20,decimal_places=2,default=0)
    totalLoanAmount = models.DecimalField(max_digits=20,decimal_places=2)
    paid = models.DecimalField(max_digits=20,decimal_places=2,default=0)
    emipaid = models.PositiveIntegerField(default=0)
    lentRateOfInterest=models.DecimalField(max_digits=5,decimal_places=2)
    lentGoldValue=models.DecimalField(max_digits=8,decimal_places=2)
    lentLoanTenure=models.PositiveSmallIntegerField()
    emi = models.DecimalField(max_digits=20,decimal_places=2)
    loanApplicationStatus=models.CharField(max_length=3,choices=ApplicationStatus,default=FILE_UNDER_PROCESS)
    lentltvRatio=models.DecimalField(max_digits=5,decimal_places=2)
    customerId=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    assetId=models.ForeignKey(GoldAsset,null=True,on_delete=models.CASCADE)
   

class Payment(models.Model):
    cardtype = models.CharField(max_length=50)
    cardnumber= models.PositiveIntegerField()
    cvc= models.PositiveIntegerField()
    expmonth = models.CharField(max_length=50)
    expyear = models.PositiveIntegerField()
    customerId=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)

class LoanRates(models.Model):
    goldValue = 50000
    interest = 9.5
    ltv_ratio = 0.75
    GoldValue=models.DecimalField(max_digits=8,decimal_places=2,default=goldValue)
    RateOfInterest=models.DecimalField(max_digits=5,decimal_places=2,default=interest)
    ltvRatio=models.DecimalField(max_digits=5,decimal_places=2,default=ltv_ratio)
    Date=models.DateField(default=date.today,null=False)

