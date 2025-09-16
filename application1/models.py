from django.db import models

class Employee(models.Model):
    user_id=models.CharField(max_length=50, unique=True)
    password=models.CharField(max_length=100)


    def __str__(self):
        return self.user_id

class Account(models.Model):
    name=models.CharField(max_length=100)
    account_number=models.CharField(max_length=20,unique=True)
    account_type=models.CharField(max_length=20)
    aadhar_number=models.CharField(max_length=12,unique=True)
    branch=models.CharField(max_length=50)
    ifsc=models.CharField(max_length=15)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    mobile_number=models.CharField(max_length=10,unique=True)
    address=models.TextField()
    town_city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6)
    email=models.EmailField(max_length=100,unique=True)
    account_created_on=models.DateField(auto_now_add=True)
    photo=models.ImageField(upload_to='profile_pics/',null=True,blank=True)
