from django.db import models


class CustomUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"
    
    
class Resume(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    userimg=models.ImageField(upload_to="images/",default='')
    username=models.CharField(max_length=100)
    usernumber=models.IntegerField(unique=True)
    useremail=models.EmailField(unique=True)
    useraddress=models.CharField(max_length=500)
    userhobbies=models.CharField(max_length=500)
    userlang=models.CharField(max_length=500)
    userprofile=models.CharField(max_length=500)
    userquali=models.CharField(max_length=500)
    userachieve=models.CharField(max_length=500)
    userproject=models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
   
    
    def __str__(self):
        return f"{self.username}"