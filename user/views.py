from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from emails.operations import Send_Emails

def Login(request):
	if request.is_ajax():
		result = False
		try:
			user = User.objects.get(email = request.GET['email'],psswd = request.GET['psswd'],active = True)
			request.session['pk_user'] = user.pk
			result = True
		except User.DoesNotExist:
			result = False
		return HttpResponse(result)
	return render(request,'login.html')

def Index(request):
	return redirect('List_Ads')


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
