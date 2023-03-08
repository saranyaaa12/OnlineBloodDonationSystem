from django.db import models

# Create your models here.
class SignUp(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=10,default='')
    password = models.CharField(max_length=30)
    blood = models.CharField(max_length=5,default='')
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    health = models.CharField(max_length=50)
    zip = models.CharField(max_length=6)


class Contactfom(models.Model):
    firstname = models.CharField(max_length=30,default='')
    lastname = models.CharField(max_length=30,default='')
    mobile = models.CharField(max_length=10,default='')
    email = models.CharField(max_length=100,default='')
    area = models.CharField(max_length=30,default='')
    comment = models.CharField(max_length=500,default='')


class Hospitals(models.Model):
    hospital = models.CharField(max_length=100,default='')
    area = models.CharField(max_length=20,default='')
    contact = models.CharField(max_length=17,default='')
    #links = models.URLField(default='')


class AdminBloodRequest(models.Model):        #For PATIENT, USER is requesting blood
    p_name = models.CharField(max_length=30,default='')
    p_age = models.CharField(max_length=5,default='')
    p_gender = models.CharField(max_length=10,default='')
    p_contact = models.CharField(max_length=15,default='')
    p_blood_needed = models.CharField(max_length=5,default='')
    p_reason = models.CharField(max_length=30,default='')
    p_location = models.CharField(max_length=100,default='')


class AcceptBloodList(models.Model):
    p_name = models.CharField(max_length=30,default='')
    p_age = models.CharField(max_length=5,default='')
    p_gender = models.CharField(max_length=10,default='')
    p_contact = models.CharField(max_length=15,default='')
    p_blood_needed = models.CharField(max_length=5,default='')
    p_reason = models.CharField(max_length=30,default='')
    p_location = models.CharField(max_length=100,default='')


class RejectBloodList(models.Model):
    p_name = models.CharField(max_length=30,default='')
    p_age = models.CharField(max_length=5,default='')
    p_gender = models.CharField(max_length=10,default='')
    p_contact = models.CharField(max_length=15,default='')
    p_blood_needed = models.CharField(max_length=5,default='')
    p_reason = models.CharField(max_length=30,default='')
    p_location = models.CharField(max_length=100,default='')


class UserDonorRequest(models.Model):
    d_name = models.CharField(max_length=30,default='')
    d_age = models.CharField(max_length=5,default='')
    d_gender = models.CharField(max_length=10,default='')
    d_contact = models.CharField(max_length=15,default='')
    d_bloodgroup = models.CharField(max_length=5,default='')
    d_healthissues = models.CharField(max_length=100,default='')
    d_visit = models.CharField(max_length=5,default='')
    d_location = models.CharField(max_length=150,default='')


class AcceptDonorList(models.Model):
    d_name = models.CharField(max_length=30,default='')
    d_age = models.CharField(max_length=5,default='')
    d_gender = models.CharField(max_length=10,default='')
    d_contact = models.CharField(max_length=15,default='')
    d_bloodgroup = models.CharField(max_length=5,default='')
    d_healthissues = models.CharField(max_length=100,default='')
    d_visit = models.CharField(max_length=5,default='')
    d_location = models.CharField(max_length=150,default='')


class RejectDonorList(models.Model):
    d_name = models.CharField(max_length=30,default='')
    d_age = models.CharField(max_length=5,default='')
    d_gender = models.CharField(max_length=10,default='')
    d_contact = models.CharField(max_length=15,default='')
    d_bloodgroup = models.CharField(max_length=5,default='')
    d_healthissues = models.CharField(max_length=100,default='')
    d_visit = models.CharField(max_length=5,default='')
    d_location = models.CharField(max_length=150,default='')

