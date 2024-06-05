from django.contrib import admin # type: ignore
from .models import Formulir
from .models import UploadFile

class FormulirAdmin(admin.ModelAdmin):
    list_display = ['nama',
                    'email',
                    'tempat_lahir',
                    'tanggal_lahir',
                    'nik',
                    'jenis_kelamin',
                    'no_hp',
                    'no_hp_ortu',
                    'alamat',
                    'kelurahan',
                    'kecamatan',
                    'kabupaten',
                    'prodi1',
                    'prodi2',
                    'prodi3',
                    'foto']
    list_filter = ["nama"]

class UploadFileAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ijazah',
                    'kk',
                    'ktp',
                    'raport10_1',
                    'raport10_2',
                    'raport11_1',
                    'raport11_2',
                    'raport12_1']
    list_filter = ["user"]

admin.site.register(Formulir, FormulirAdmin)
admin.site.register(UploadFile, UploadFileAdmin)