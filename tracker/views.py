from django.shortcuts import render

from tracker.models import Country

from django.http import HttpResponse

def all_countries(request):
	countries = Country.objects.all()
	countries_string = ", ".join([country.name for country in countries])
	#return HttpResponse(countries_string)
	return render(request, "all_countries.html", {'countries': countries})

