from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2, max_digits=20)
    image=models.ImageField(upload_to='products', blank=True)


    def __str__(self):
        return f'{self.title}'
