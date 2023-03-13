from django.shortcuts import render
from .models import Reservation

def List_Reservations(request):
	list_reservation = Reservation.objects.all()
	return render(request,'reservation/list_reservations.html',{'list':list_reservation})
