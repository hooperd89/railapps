from django.db import models
from datetime import date
from django.urls import reverse, reverse_lazy

# Create your models here.
class Occupation(models.Model):
    occupation_noi = models.PositiveIntegerField()
    system_line = models.CharField(max_length = 100, help_text='Enter the System Line e.g. Sunbury to Bendigo.')
    occupation_start_date = models.DateTimeField(help_text='Format is YYYY-MM-DD HH-MM-SS')
    occupation_end_date = models.DateTimeField(help_text='Format is YYYY-MM-DD HH-MM-SS')
    occupation_type = models.CharField(max_length = 50, help_text='Enter the Occupation Type e.g. BLU')
    AREA_CHOICE = (('Western Region', 'Western Region'),('North/North-East Region', 'North/North-East Region'),('Central & Eastern Region', 'Central & Eastern Region'))
    rail_area = models.CharField(max_length = 50,choices=AREA_CHOICE, help_text='Enter the Rail Area Type e.g. North/North-East')

    def __str__(self):
        return self.system_line

    def get_absolute_url(self):
        # Returns the url to access a detail record for this occo.
        return reverse('the_wall:occupation_detail', args=[str(self.id)])

    class Meta:
        ordering = ['occupation_start_date']



class Work(models.Model):
    start_chainage = models.DecimalField(max_digits = 6, decimal_places = 3)
    end_chainage = models.DecimalField(max_digits = 6, decimal_places = 3)
    DISCIPLINE_CHOICE = (('Civil', 'Civil'),('Track', 'Track'),('Facilities', 'Facilities'),('Signals', 'Signals'),)
    discipline = models.CharField(max_length = 100, choices=DISCIPLINE_CHOICE, help_text='Enter the discipline e.g. Civil')
    work_information = models.CharField(max_length = 255)
    additional_details = models.CharField(max_length = 255, blank=True)
    occupation_details = models.ForeignKey('Occupation', on_delete = models.CASCADE)
    works_start_date = models.DateField(help_text='Format is YYYY-MM-DD')
    works_end_date = models.DateField(help_text='Format is YYYY-MM-DD')


    def __str__(self):
        return self.work_information

    def get_absolute_url(self):
        # Returns the url to access a detail record for the work.
        return reverse('the_wall:work_detail', args=[str(self.id)])

    class Meta:
        ordering = ['start_chainage']
