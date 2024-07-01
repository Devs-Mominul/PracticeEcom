from django.urls import path
from Accounts.views import *
urlpatterns = [
    path('reg_login/', reg_login, name='reg_login'),
    path('login/', Login_view, name='login_view'),
]