from django.shortcuts import render

# Create your views here.
def accounts_view(request):
    return render(request, 'accounts/accounts.html')

def register_view(request):
    return render(request, 'accounts/register.html')

def login_view(request):
    return render(request, 'accounts/login.html')