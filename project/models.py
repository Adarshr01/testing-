from django.db import models


class menubaritems(models.Model):
    name = models.TextField(max_length=20)
    status = models.BooleanField(default= False)


class childcell(models.Model):
    name = models.TextField(max_length=20,default='')
    parentcell = models.IntegerField(default=0)


# Create your models here.
