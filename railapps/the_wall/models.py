from django.db import models

# Create your models here.
class Occupation(models.Model):
    occupation_noi = models.PositiveIntegerField()
    system_line = models.CharField(max_length = 100, help_text='Enter the System Line e.g. Sunbury to Bendigo.')
    occupation_start_date = models.DateTimeField()
    occupation_end_date = models.DateTimeField()
    occupation_type = models.CharField(max_length = 50, help_text='Enter the Occupation Type e.g. BLU')

    AREA_CHOICE = (('w', 'Western Region'),('n', 'North/North-East Region'),('c', 'Central & Eastern Region'))


    rail_area = models.CharField(max_length = 50,choices=AREA_CHOICE, help_text='Enter the Rail Area Type e.g. North/North-East')

    def __str__(self):
        return self.system_line

    def get_absolute_url(self):
        # Returns the url to access a detail record for this occo.
        return reverse('Occupation-detail', args=[str(self.id)])

    class Meta:
        ordering = ['occupation_start_date']

class Work(models.Model):
    start_chainage = models.DecimalField(max_digits = 6, decimal_places = 3)
    end_chainage = models.DecimalField(max_digits = 6, decimal_places = 3)

    DISCIPLINE_CHOICE = (('c', 'Civil'),('t', 'Track'),('f', 'Facilities'),('s', 'Signals'),)

    discipline = models.CharField(max_length = 100, choices=DISCIPLINE_CHOICE, help_text='Enter the discipline e.g. Civil')
    work_information = models.CharField(max_length = 255)
    additional_details = models.CharField(max_length = 255, blank=True)
    occupation_details = models.ForeignKey('Occupation', on_delete = models.CASCADE)

    def __str__(self):
        return self.work_information

    def get_absolute_url(self):
        # Returns the url to access a detail record for the works.
        return reverse('Works-detail', args=[str(self.id)])

    class Meta:
        ordering = ['start_chainage']
