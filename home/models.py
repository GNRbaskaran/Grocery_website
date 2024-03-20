from django.db import models

# Create your models here.
class UserModel(models.Model):
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.email
    
class Product(models.Model):
    pname=models.CharField(max_length=200)
    pdesc=models.CharField(max_length=500)
    stock=models.PositiveIntegerField(default=0)
    img=models.ImageField(upload_to='uploads')

class Product1(models.Model):
    pname=models.CharField(max_length=200)
    pdesc=models.CharField(max_length=500)
    stock=models.PositiveIntegerField(default=0)
    price=models.IntegerField()
    img=models.ImageField(upload_to='uploads')

    def __str__(self):
        return self.pname

class Cart(models.Model):
    product=models.ForeignKey(Product1,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.pname

class Payment(models.Model):
    name=models.CharField(max_length=100)
    cnum=models.IntegerField()
    total=models.IntegerField()
    
    def __str__(self):
        return self.name