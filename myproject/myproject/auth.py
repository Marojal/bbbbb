from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group

def akun_login(request):
    if request.user.is_authenticated:
         return redirect('/form-pendaftaran')

    template_name = "login/login.html"
    pesan = ''
    if request.method == "POST":
         username = request.POST.get("username")
         password = request.POST.get("password")

         user = authenticate(request, username=username, password=password)
         if user:
              login(request, user)
              return redirect('/form-pendaftaran')
         else:
              pesan = "Gagal Login"
    context = {
         'pesan': pesan
    }
    return render(request, template_name, context)

def akun_registrasi(request):
     # jika user sudah login maka tidak boleh akses fungsi ini lagi
     if request.user.is_authenticated:
          return redirect('/')
     
     pesan = ''
     template_name = "register.html"
     if request.method == "POST":
          username = request.POST.get("username")
          email = request.POST.get("email")
          password = request.POST.get("password")

          print(username, password, email)
          
          check_user = User.objects.filter(username=username)
          if check_user.count() == 0:
               User_simpan = User.objects.create(
                    username = username,
                    email = email,
                    is_active = True
               )
               User_simpan.set_password(password)
               User_simpan.save()

               return redirect('/login')
          else:
               pesan = "username sudah digunakan"

     context = {
          'pesan':pesan
     }
     return render(request, template_name, context)

def akun_logout(request):
     logout(request)
     return redirect('/')