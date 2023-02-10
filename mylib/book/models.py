from django.db import models

# Create your models here.
class Book(models.Model):
    id=models.AutoField(name='ID',primary_key=True)
    name=models.CharField(max_length=100)
    publisher=models.CharField(max_length=50 ,null=True)
    catagory=models.ForeignKey(to='catagory.Catagory',on_delete=models.CASCADE)