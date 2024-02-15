from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    TYPE_CHOICES = [
        ('perishable', 'Perishable'),
        ('non_perishable', 'Non-Perishable')
    ]
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=100)
    base_distance_in_km = models.FloatField()
    km_price = models.FloatField()
    fix_price = models.FloatField()
