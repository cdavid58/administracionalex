from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^List_Reservations/$',List_Reservations,name="List_Reservations"),
]