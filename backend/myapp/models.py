from django.db import models

# Create your models here.


# Investment Fund Model
class InvestmentFund (models.Model):
    name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    description = models.TextField()
    net_asset_value = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateField()
    performance = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name[0:50]
    
    
