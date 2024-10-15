from django.db import models

class Product(models.Model):
    CAT=((1,'Mobile'),(2,'Shoes'),(3,'Clothes'))
    name = models.CharField(max_length=50, verbose_name='Product_name')
    price = models.FloatField(verbose_name='Product_price')
    pdetails = models.CharField(max_length=100,verbose_name='Product_details')
    cat = models.IntegerField(choices=CAT,verbose_name='Category') #verbose dummy name
    is_active = models.BooleanField(default=True,verbose_name='Status')
def __str__(self):
    return self.id    

