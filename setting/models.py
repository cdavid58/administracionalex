from django.db import models

class Percentage(models.Model):
	porcentaje_x_persona = models.FloatField(default = 0.2)
	porcentaje_subtotal_reservacion = models.FloatField(default = 0.03)

class History_Transaccion(models.Model):
	amount_total = models.FloatField()
	amount_me = models.FloatField()
	amount_property = models.FloatField()
	date_register = models.DateField(auto_now_add = True)
	date_payment = models.DateField(auto_now_add = True)
	