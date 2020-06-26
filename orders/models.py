from django.db import models

# Create your models here.

TYPE = (
    ('Regular', 'Regular'),
    ('Sicilian', 'Sicilian')
)

SIZE = (
    ('Small', 'Small'),
    ('Large', 'Large')
)

class pizza(models.Model):
    type = models.CharField(choices=TYPE, max_length=15)
    name = models.CharField(max_length=30)
    size = models.CharField(choices=SIZE, max_length=10)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.type} - {self.name} - {self.size} - ${self.price}"

class topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class sub(models.Model):
    name = models.CharField(max_length=30)
    size = models.CharField(choices=SIZE, max_length=10)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.size} - ${self.price}"

class pasta(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} ${self.price}"

class salad(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} ${self.price}"

class DinnerPlatter(models.Model):
    name = models.CharField(max_length=30)
    size = models.CharField(choices=SIZE, max_length=10)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.size} - ${self.price}"