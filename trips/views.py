# Create your views here.
from django.http import HttpResponse
from trips.models import Trip
from django.shortcuts import render
def index(request):
    	latest_trip_list = Trip.objects.all();
    	context = {'latest_trip_list': latest_trip_list}
    	return render(request,'trips/index.html',context)
