from django.shortcuts import render
from Flight.models import Flight
from django.http import HttpResponse, HttpResponseRedirect



def flight_home(request):
    return render(request, 'flight_home.html')


