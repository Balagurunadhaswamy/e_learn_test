from django.db import models
from django.core.validators import RegexValidator,MaxValueValidator
from django.core.exceptions import ValidationError
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Add custom fields here, if needed

    def __str__(self):
        return self.username
    

class Standard(models.Model):
    CHOICES =[
        ("PKG","PRE_KG"),
        ("LKG","LKG"),
        ("UKG","UKG"),
        ("IST","First"),
        ("2ND","Second"),
        ("3RD","Third"),
        ("4TH","Fourth"),
        ("5TH","Fifth"),
        ("6TH","Sixth"),
        ("7TH","Seventh"),
        ("8TH","Eighth"),
        ("9TH","Nineth"),
        ("10TH","Tenth"),
        ("11TH","Eleventh"),
        ("12TH","Twelth")
    ]
    std_name = models.CharField(primary_key=True,choices=CHOICES,max_length=5)
    roll  = models.IntegerField(default=0,validators=[MaxValueValidator(50)])
    duration  = models.DurationField(default=datetime.timedelta(minutes=30),editable=False)
    def __str__(self):
        return self.std_name


    

class Subject(models.Model):
    sub_code = models.CharField(primary_key=True,max_length=50,unique=True,validators=[RegexValidator(r"^[0-9]{3}[A-Z]{2}")])
    sub_name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.sub_name
    
class Course(models.Model):
    course_code = models.CharField(primary_key=True,max_length=5,blank=False, null=False,validators=[RegexValidator(r"^[0-9]{3}[A-Z]{2}")])
    course_name  = models.CharField(max_length=50,blank = False, null=False)
    subject1 = models.ForeignKey(Subject,on_delete=models.CASCADE, null=False, blank=False,related_name="sub1_courses")
    subject2  = models.ForeignKey(Subject,on_delete=models.CASCADE, null=False, blank=False,related_name="sub2_courses")
    subject3 =  models.ForeignKey(Subject,on_delete=models.CASCADE, null=False, blank=False,related_name="sub3_courses")

    def __str__(self):
        return self.course_code
    
    def clean(self):
        if self.subject1==self.subject2 or self.subject1==self.subject3 or self.subject2 == self.subject3:
            raise ValidationError("The three subjects should be different")

class Student(models.Model):
    student_name = models.CharField(max_length=50, primary_key=True, null=False, blank=False)
    user = models.OneToOneField(CustomUser,blank=False, null=False,on_delete=models.CASCADE,related_name="student")
    standard =models.ForeignKey(Standard,on_delete=models.CASCADE,null=False,blank=False,related_name="student_standard")
    course = models.ForeignKey(Course,blank=False, null= False, on_delete=models.CASCADE,related_name="course")

    def __str__(self):
        return self.user.username
    

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50, primary_key=True, null=False, blank=False)
    user  = models.OneToOneField(CustomUser,blank=False, null= False, on_delete=models.CASCADE,related_name="teacher")
    subject =models.ManyToManyField(Subject)
    #courses =models.ForeignKey(Course,on_delete=models.CASCADE,null=False,blank=False,related_name="teacher_course")

    def __str__(self):
        return self.user.username