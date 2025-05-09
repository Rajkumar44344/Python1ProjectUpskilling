from django.db import models

class Student(models.Model):
   name = models.CharField(max_length=200)
   college = models.CharField(max_length=200)
   age = models.IntegerField()
   is_active = models.BooleanField(default=False)
   city=models.CharField(max_length=200, default="Unknown City")


class Course(models.Model):
   cname=models.CharField(max_length=200)
   cdescription=models.CharField(max_length=200)
   cdurition=models.CharField(max_length=200)
   cid=models.IntegerField(max_length=20)