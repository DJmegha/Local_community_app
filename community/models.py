from sqlite3 import Timestamp
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Services(models.Model):
    Service=models.CharField(max_length=200)
    
    def __str__(self):
        return self.Service


class Categories(models.Model):
    Service=models.ForeignKey( Services,on_delete=models.CASCADE)
    Category=models.CharField(max_length=200)
    
    def __str__(self):
         return self.Category

class ServiceProviders(models.Model):
    Service=models.ForeignKey(Services,on_delete=models.CASCADE,null=True)
    Category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    Service_provider=models.CharField(max_length=200)
    Price=models.DecimalField(max_digits=10,decimal_places=2)
    Contact_no=models.CharField(max_length=15)
    Cover_img=models.ImageField(upload_to='images/',null=True)
    
    def __str__(self):
        return self.Service_provider


# class QueryAnswer(models.Model):
#     Service_provide=models.ForeignKey(ServiceProviders,null=True,on_delete=models.CASCADE)
#     Query=models.TextField()
#     QueriesAnswer=models.TextField()
    

#     def __str__(self):
#         return self. Query

class Comment(models.Model):
    Sno=models.AutoField(primary_key=True)
    Comment=models.TextField()
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    Service_provider=models.ForeignKey(ServiceProviders,related_name="comments",on_delete=models.CASCADE)
    Reply=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    Timestamp=models.DateTimeField(default=timezone.now())
    
    
    def __str__(self):
        return '%s - %s' % (self.Service_provider,self.User)