from django.db import models

# Create your models here.
class MyUser(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
   myuser=models.ForeignKey(to='MyUser',on_delete=models.CASCADE)

class AddUser(models.Model):
    uid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)