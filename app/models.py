from django.db import models
from django.db.models.fields import CharField

class Offers(models.Model):
    name = models.CharField(blank=False, max_length= 50, verbose_name= 'Name')
    discription = models.TextField(blank=False, verbose_name= 'Description')
    image = models.ImageField(upload_to = 'img', verbose_name= 'Foto')
    price = models.DecimalField(blank=False, max_digits= 5, decimal_places= 2, verbose_name='Prices')

    def __str__(self):
        return self.name

class PotencialClient(models.Model):
    first_name = models.CharField(blank=False, max_length=50, verbose_name= 'First Name')
    last_name = models.CharField(blank=False, max_length=50, verbose_name= 'Last Name')
    email = models.EmailField(max_length=100, verbose_name= 'Email')
    phone_number = models.CharField(blank=False, max_length=50, verbose_name= 'Phone number')
    date = models.DateField(verbose_name= 'Date')
    message = models.TextField(blank=False, max_length=500, verbose_name= 'Message')

    def __str__(self):
        return self.last_name