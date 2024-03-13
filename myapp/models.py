from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    Password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)

class Caregiver(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    pin = models.CharField(max_length=15)
    post = models.CharField(max_length=20)
    Housename = models.CharField(max_length=20)
    gmail = models.CharField(max_length=20)
    phone_no=models.CharField(max_length=20)
    Gender=models.CharField(max_length=10)
    age=models.CharField(max_length=5)
    photo=models.CharField(max_length=260)

class Elderly_person(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    pin = models.CharField(max_length=15)
    post = models.CharField(max_length=20)
    Housename = models.CharField(max_length=20)
    gmail = models.CharField(max_length=20)
    phone_no=models.CharField(max_length=20)
    guardian_details=models.CharField(max_length=20)
    Gender=models.CharField(max_length=10)
    age=models.CharField(max_length=5)
    photo=models.CharField(max_length=260)

class Allocation(models.Model):
    CAREGIVER=models.ForeignKey(Caregiver,on_delete=models.CASCADE)
    ELDERLY_PERSON=models.ForeignKey(Elderly_person,on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()

class Communication(models.Model):
    FROMID=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='log1')
    TOID=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='log2')
    message=models.CharField(max_length=1000)
    date=models.DateField()

class Medication_remainder(models.Model):
    ELDERLYPERSON=models.ForeignKey(Elderly_person,on_delete=models.CASCADE)
    Name_medicine=models.CharField(max_length=50)
    Time=models.TimeField()
    Date=models.DateField()

class VideoLog(models.Model):
    video=models.FileField(upload_to='videos/')
    time=models.TimeField(auto_now_add=True)








