from django.db import models

# Create your models here.
class occo_details(models.Model):
    occo_noi = models.PositiveIntegerField()
    system_line = models.CharField(max_length =50)
    occo_date = models.DateTimeField(auto_now=False)
