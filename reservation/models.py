from django.db import models
from property.models import Property
from user.models import User

class Reservation(models.Model):
	date_enter = models.CharField(max_length = 12)
	date_exit = models.CharField(max_length = 12)
	user_email = models.EmailField()
	propertys = models.ForeignKey(Property, on_delete = models.CASCADE)
	propietrio = models.ForeignKey(User, on_delete = models.CASCADE,null = True, blank = True)
	boys = models.IntegerField()
	adult = models.IntegerField()
	price = models.IntegerField()
	hour_input = models.CharField(max_length = 20)
	note = models.TextField()
	days = models.IntegerField(default = 1)
	status = models.CharField(max_length = 45, default="En espera")
	limpieza = models.IntegerField(default = 0,null=True,blank=True)
	money_returned = models.IntegerField(default = 0)