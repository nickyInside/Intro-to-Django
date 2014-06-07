from django.contrib import admin

# Register your models here

from tracker.models import Country

class CountryAdmin(admin.ModelAdmin):
	list_display = ('name', 'population')
	
admin.site.register(Country, CountryAdmin)
