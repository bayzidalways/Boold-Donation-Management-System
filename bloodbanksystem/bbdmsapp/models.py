from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER = {
        (1, 'admin'),
        (2, 'donor'),
        (3, 'requester'),

    }
    user_type = models.CharField(choices=USER, max_length=50, default=1)

    profile_pic = models.ImageField(upload_to='media/profile_pic')


class Bloodgroup(models.Model):
    bloodgroup = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DonorReg(models.Model):
    admin = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=200, default='')
    age = models.IntegerField(default=0)
    mobilenumber = models.CharField(max_length=11)
    bloodgroup = models.ForeignKey(Bloodgroup, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    status = models.CharField(max_length=50, default='0')
    regdate_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or f"Donor #{self.pk}"


class BloodRequest(models.Model):
    donid = models.ForeignKey(DonorReg, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=250)
    mobno = models.CharField(max_length=11)
    email = models.EmailField(max_length=250)
    requirer = models.CharField(max_length=250)
    message = models.TextField(max_length=250)
    regdate_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    fullname = models.CharField(max_length=250)
    mobno = models.CharField(max_length=11)
    email = models.EmailField(max_length=250)
    message = models.TextField(max_length=250)
    status = models.CharField(max_length=50)
    regdate_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
