from django.http import HttpResponse
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect
from .models import *
from emails.operations import Send_Emails
from property.models import *
from setting.models import *

def Login(request):
	if request.is_ajax():
		result = False
		try:
			user = User.objects.get(email = request.GET['email'],psswd = request.GET['psswd'],active = True)
			request.session['pk_user'] = user.pk
			request.session['type_user'] = user.type_user
			result = True
		except User.DoesNotExist:
			result = False
		return HttpResponse(result)
	return render(request,'login.html')

def Index(request):
	return redirect('List_Ads')

def LogOut(request):
	for i,j in list(request.session.items()):
		del request.session[i]
	return redirect('/')


def Register(request):
	result = True
	if request.method == 'POST':
		data = request.POST
		try:
			user = User.objects.get(email = data['email'], phone = data['phone'])
		except User.DoesNotExist as e:
			user = None
		if user is None:
			User(
				code = get_random_string(length=9),
				first_name = data['name'],
				email = data['email'],
				phone = data['phone'],
				psswd = data['psswd']
			).save()
			user = User.objects.get(email = data['email'])
			try:
				Multimedia(
					documentI = request.FILES['cc'],
					photo = request.FILES['photo'],
					user = user,
				).save()
				type_email = "https://mail.google.com/mail/u/0/#inbox"
				name_type_email = 'Gmail'
				if 'hotmail' in data['email']:
					type_email = "https://login.live.com/"
					name_type_email = 'Hotmail'
				Send_Emails().Confirm_Email( data['email'], data['name'], user.pk )
				return render(request,'confirm-mail.html',{'email':data['email'],'type_email':type_email,'name_type_email':name_type_email })
			except Exception as e:
				print(e)
				user.delete()
				result = False
	return render(request,'register.html',{'result':result})

def Activate_Account(request,pk):
	try:
		user = User.objects.get(pk = pk)
	except User.DoesNotExist as e:
		user = None

	if user is not None:
		if not user.active:
			user.active = True
			user.save()
			return redirect('/')
		return render(request,'error_confirm_email.html')
	return redirect('/')

def Owners_List(request):
	user = User.objects.all()
	data = [
		{
			'pk':i.pk,
			'code':i.code,
			'property':len(Property.objects.filter(user = i)),
			'name':i.first_name,
			'block':i.active,
			'email':i.email
		}
		for i in user
	]
	print(data)
	return render(request,'users/list_user.html',{'user':data})

def Profile(request,pk):
	user = User.objects.get(pk = pk)
	__property = Property.objects.filter(user = user)
	data_property = [
		{
			'pk':i.pk,
			'cover':Photo.objects.filter(propertys = i)[0].img.url,
			'title':i.title,
			'address':i.city+' - '+i.departament+' - '+i.country
		}
		for i in __property
	]

	data_trans = [
		{
			'title':i.propertys.title,
			'total': i.amount_total,
			'amount_me': i.amount_me,
			'amount_property': i.amount_property,
			'img':Photo.objects.filter(propertys = i.propertys)[0].img.url,
			'date_payment':i.date_payment
		}
		for i in History_Transaccion.objects.filter(user = user)
	]
	return render(request,'users/profile.html',{'user':user,'property':data_property,'history':Movement_History.objects.filter(user = user),
			'data_trans':data_trans
		})