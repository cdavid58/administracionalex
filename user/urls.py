from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$',Login,name="Login"),
	url(r'^Index/$',Index,name="Index"),
	url(r'^Register/$',Register,name="Register"),
	url(r'^Activate_Account/(\d+)/$',Activate_Account,name="Activate_Account"),
]