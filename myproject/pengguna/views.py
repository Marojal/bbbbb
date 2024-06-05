from django.shortcuts import render,redirect,get_object_or_404 # type: ignore

from pengguna.models import Formulir
from pengguna.forms import FormulirForm
from pengguna.forms import UploadForm

# Create your views here.

def home(request):
    template = "index.html"
    context = {
        'title': 'Home',
    }
    return render(request, template, context)

def formulir_list(request):
    template = "admin.html"
    formulir_list = Formulir.objects.all()
    print(formulir_list)
    context = {
        'title': 'Form Pendaftaran',
        'formulir_list': formulir_list
    }
    return render(request, template, context)

def akun_pengguna(request):
    template = "akun_pengguna.html"
    context = {
        'title': 'Akun Pengguna',
    }
    return render(request, template, context)

    
def formulir_detail(request, pk):
    formulir = get_object_or_404(Formulir, pk=pk)
    context = {
        'formulir': formulir,
        'title': 'Detail Formulir',
    }
    return render(request, 'dashboard/snippets/formulir_detail.html', context)


def create_formulir(request):
    if request.method == "POST":
        form = FormulirForm(request.POST, request.FILES)
        if form.is_valid():
            formulir = form.save()
            return redirect('formulir_detail', pk=formulir.pk)  # Ganti dengan URL halaman sukses Anda
    else:
        form = FormulirForm()

    context={
        'form': form, 
        'title': 'Formulir Pendaftaran'
        }

    return render(request,'dashboard/snippets/formulir.html', context)


def add_file(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            add_form = form.save()
            return redirect('formulir_detail', pk=add_form.pk) 
    else:
        form = UploadForm()

    context = {
        'form': form,  # Mengirimkan form dengan nama 'form'
        'title': 'Upload Berkas'
    }

    return render(request, 'dashboard/snippets/upload-file.html', context)

def formulir_list(request):
    formulirs = Formulir.objects.all()
    context = {
        'formulirs': formulirs,
        'title': 'Daftar Formulir',
    }
    return render(request, 'dashboard/snippets/formulir_list.html', context)
