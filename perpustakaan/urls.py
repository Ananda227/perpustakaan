"""perpustakaan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index),
    # mahasiswa
    path('mahasiswa/', mahasiswa, name="mahasiswa"),
    path('mahasiswa/form', form_m, name="form_mahasiswa"),
    path('mahasiswa/create', tambah_mahasiswa, name="tambah_mahasiswa"),
    path('mahasiswa/edit/<int:noanggotamedit>/', edit_mahasiswa, name="edit_mahasiswa"),
    path('mahasiswa/delete/<int:noanggotam>/', delete_mahasiswa, name="delete_mahasiswa"),
    # path('kembali-mahasiswa/', kembaliM, name="kembali_mahasiswa"),
    #non mahasiswa
    path('non-mahasiswa/', non_mahasiswa, name="non_mahasiswa"),
    path('non-mahasiswa/form', form_n, name="form_non_mahasiswa"),
    path('non-mahasiswa/create', tambah_non_mahasiswa, name="tambah_non_mahasiswa"),
    path('non-mahasiswa/edit/<int:noanggotanedit>/', edit_non_mahasiswa, name="edit_non_mahasiswa"),
    path('non-mahasiswa/delete/<int:noanggotan>/', delete_non_mahasiswa, name="delete_non_mahasiswa"),
    
    #Buku
    path('buku/', buku, name="buku"),
    path('buku/form', form_b, name="form_buku"),
    path('buku/create', tambah_buku, name="tambah_buku"),
    path('buku/edit/<str:kodebukuedit>/', edit_buku, name="edit_buku"),
    path('buku/delete/<str:kodebuku>/', delete_buku, name="delete_buku"),
    
    #menu 
    path('', dashboard, name="dashboard"),
    path('database/', database, name="database"),
    path('registrasi/', registrasi, name="registrasi"),
    path('laporan/', laporan, name="laporan"),
    path('transaksi/', transaksi, name="transaksi"),
    path('peminjaman/', peminjaman, name="peminjaman"),
    path('pengembalian/', pengembalian, name="pengembalian"),



]
