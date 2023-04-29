from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


# Create your models here.


class User(AbstractUser):
    email=models.EmailField(max_length=45)
    phone=models.CharField(max_length=15)
    d_o_b=models.DateField(null=True)
    address=models.TextField(max_length=600)
    dist=models.CharField(max_length=45)
    state=models.CharField(max_length=45)
    cr_dist1=models.CharField(max_length=45,null=True)
    cr_dist2=models.CharField(max_length=45,null=True)
    id_proof=models.CharField(max_length=40)
    dr_name=models.CharField(max_length=40,null=True)
    mh=models.IntegerField(null=True)
    allot_status=models.IntegerField(null=True)
    salary=models.FloatField(null=True)
    usertype=models.IntegerField(null=True)
    resume=models.FileField(null=True)
    cr_status=models.IntegerField(null=True)
    p_id=models.IntegerField(null=True)
    cr_id=models.IntegerField(null=True)
    s_id=models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args,**kwargs)

class Support(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField(max_length=500)
