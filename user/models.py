from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=30)
	second_name = models.CharField(max_length=30,null = True, blank=True)
	last_name = models.CharField(max_length=30)
	last_second_name = models.CharField(max_length=30,null = True, blank=True)
	email = models.EmailField()
	psswd = models.CharField(max_length = 20)
	phone = models.CharField(max_length = 15)
	type_user = models.IntegerField(default=2)
	active = models.BooleanField(default = False)

	def __str__(self):
		return self.first_name+' '+self.last_name

class Multimedia(models.Model):
	documentI = models.FileField(upload_to="CC")
	photo = models.FileField(upload_to="DocumentI")
	user = models.ForeignKey(User, on_delete= models.CASCADE)

	def __str__(self):
		return self.user.first_name+' '+self.user.last_name