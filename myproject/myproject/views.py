from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    template = "halaman/home/index.html"
    context = {
        'title': 'Home',
    }
    return render(request, template, context)

def akun_login(request):
    template = "halaman/login/login.html"
    context = {
        'title': 'Login',
    }
    return render(request, template, context)

def akun_registrasi(request):
    template = "halaman/login/register.html"
    context = {
        'title': 'Registrasi',
    }
    return render(request, template, context)

# def form_pendaftaran(request):
#     template = "dashboard/snippets/formulir.html"
#     context = {
#         'title': 'Form Pendaftaran',
#     }
#     return render(request, template, context)

def contact(request):
    template = "halaman/home/contact.html"
    context = {
        'title': 'Contact',
    }
    return render(request, template, context)

def dashboard(request):
    template ="dashboard/index.html"
    context ={
        'title':'Halaman Dashboard'
    }
    return render(request,template,context)

@login_required
def some_view(request):
    return render(request, 'login.html', {'user': request.user})