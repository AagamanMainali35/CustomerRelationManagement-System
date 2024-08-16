from django.db import models
from django.contrib.auth.models import User
class product(models.Model):
    prdctname=models.CharField(max_length=50,null=False,blank=False,verbose_name='Enter product name Name here')
    price=models.IntegerField(null=True,blank=False,verbose_name='Enter product Price')
    def __str__(self):
        return self.prdctname   

class customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    c_name=models.CharField(max_length=50,null=True,blank=False,verbose_name='Customer Name ')
    Date=models.DateField(null=True,blank=False)
    profilepic = models.ImageField(
        upload_to='CoreImages/',
        default='CoreImages/Default.jpg',
        null=True,
        blank=True
    )     
    Purchase_product=models.CharField(max_length=50,null=True,blank=False,verbose_name='Produst name here')
    def __str__(self):
        return (f"Account Name : {self.c_name}") 
    
class account(models.Model):
    username=models.CharField(max_length=50,null=True,blank=False,verbose_name="username")
    password=models.CharField(max_length=50,null=True,blank=False,verbose_name="Password")

    def __str__(self):
        return self.username