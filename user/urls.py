from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$',Login,name="Login"),
	url(r'^Index/$',Index,name="Index"),
	url(r'^Register/$',Register,name="Register"),
	url(r'^Owners_List/$',Owners_List,name="Owners_List"),
	url(r'^Activate_Account/(\d+)/$',Activate_Account,name="Activate_Account"),
	url(r'^Profile/(\d+)/$',Profile,name="Profile"),
]