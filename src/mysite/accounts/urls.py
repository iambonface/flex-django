from django.urls import path

from . import views as v

urlpatterns = [
    #path('', v.accounts_view, name="accounts"),
    path('register', v.register_view, name="register"),
    path('login', v.login_view, name="login"),
]