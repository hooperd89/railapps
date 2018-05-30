from django.db import models

# Create your models here.
class Occupation(models.Model):
    occo_noi = models.PositiveIntegerField()
    system_line = models.CharField(max_length = 100)
    occo_start_date = models.DateTimeField()
    occo_end_date = models.DateTimeField()
    occo_type = models.CharField(max_length = 50)
    rail_area = models.CharField(max_length = 50)

    def __str__(self):
        return self.system_line


class Work(models.Model):
    start_chainage = models.DecimalField(max_digits = 6, decimal_places = 3)
    end_chainage = models.DecimalField(max_digits = 6, decimal_places = 3)
    dicipline = models.CharField(max_length = 100)
    work_info = models.CharField(max_length = 255)
    additional_details = models.CharField(max_length = 255)
    occo_details = models.ForeignKey('Occupation', on_delete = models.CASCADE)

    def __str__(self):
        return self.work_info
