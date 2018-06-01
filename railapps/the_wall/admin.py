from django.contrib import admin
from the_wall.models import Work, Occupation

# Register your models here.
# admin.site.register(Work)
# admin.site.register(Occupation)
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display =('work_information', 'occupation_details', 'start_chainage', 'end_chainage')

@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display =('system_line', 'occupation_start_date', 'occupation_end_date')
