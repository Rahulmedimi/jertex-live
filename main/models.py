from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
class Serviceprovider(models.Model):
    f_name=models.CharField(max_length=20)
    serviceusername=models.OneToOneField(User, on_delete=models.CASCADE)
    age=models.IntegerField()
    occupation=models.CharField(max_length=50)
    experience=models.IntegerField()

    def __str__(self):
        return self.f_name

class occupations(models.Model):
    work=models.CharField(max_length=50)
    def __str__(self):
        return self.work

class Postmsg(models.Model):
      host=models.ForeignKey(User, on_delete=models.CASCADE)
      workname=models.ForeignKey(occupations, on_delete=models.CASCADE)
      message=models.TextField()
      posted=models.DateTimeField(auto_now=True)
      edited=models.DateTimeField(auto_now_add=True)   

      def __str__(self):
          return self.message[:20]

class Search(models.Model):
    searcheduser=models.ManyToManyField(User)
    serachresults=models.CharField(max_length=20)
    searchdate=models.DateTimeField(auto_now_add=True)



class numberofserviceproviders(models.Model):
    workname=models.CharField(max_length=50)
    count=models.IntegerField()

    def __str__(self):
        return self.workname

# class orderservicedetails(models.Model):
    



      
