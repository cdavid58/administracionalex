from django.db import models

class Percentage(models.Model):
	porcentaje_x_persona = models.FloatField(default = 0.2)
	porcentaje_subtotal_reservacion = models.FloatField(default = 0.03)