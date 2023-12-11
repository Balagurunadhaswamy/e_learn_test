from django.db import models

import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Add custom fields here, if needed

    def __str__(self):
        return self.username
        
        
class Student(models.Model):
    user = models.ForeignKey("CustomUser",blank=False, null=False,on_delete=models.CASCADE,related_name="user")
    standard = models.ForeignKey("Standard",blank=False, null= False, on_delete=models.CASCADE,related_name="standard")
    course = models.ForeignKey("Course",blank=False, null= False, on_delete=models.CASCADE,related_name="course")


    ...

class Teacher(models.Model):
    user  = models.ForeignKey("CustomUser",blank=False, null= False, on_delete=models.CASCADE,related_name="user")
    subject =models.OneToOneField("Subject",blank=False, null= False, on_delete=models.CASCADE,related_name="subject")

    ...

class Standard(models.Model):
    CHOICES =[
        ("IST","ENGLISH"),
        ("2ND","URDU"),
        ("3RD","HINDI"),
        ("4TH","MATH"),
        ("5TH","SCIENCE"),
        ("6TH","HISTORY"),
        ("7TH","COMPUTER")
    ]
    std_name = models.TextField(choices=CHOICES,max_length=3)
    duration  = models.DurationField(datetime.timedelta(minutes=30)
)

    ...


class Course(models.Model):
    CHOICES =[
        ("SME","ENGLISH"),
        ("SMU","URDU"),
        ("SMH","HINDI"),
        ("SHE","MATH"),
        ("SHH","SCIENCE"),
        ("CME","HISTORY"),
        ("CMP","COMPUTER")
    ]
    course_name  = models.TextField(choices=CHOICES,max_length=3)
    ...

class Subject(models.Model):

    CHOICES =[
        ("ENG","ENGLISH"),
        ("URD","URDU"),
        ("HND","HINDI"),
        ("MTH","MATH"),
        ("SCE","SCIENCE"),
        ("HIS","HISTORY"),
        ("CMP","COMPUTER")]
    course = models.ForeignKey("Course",blank=False, null= False, on_delete=models.CASCADE,related_name="subject")

    sub_name = models.TextField(choices=CHOICES, max_length=3)

    ...
