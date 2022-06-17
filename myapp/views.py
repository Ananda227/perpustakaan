
import pkgutil
from django.shortcuts import redirect, render
from myapp.models import *
from myapp.function.function import hundle_uploaded_file
from django.db.models import Count



def index(request):
    return render(request, 'navbar.html')

# Anggota Mahasiswa

def mahasiswa(request):
    list_mahasiswa = AnggotaMahasiswa.objects.all()
    konteks = {
        'list_mahasiswa' : list_mahasiswa,
    }
    return render(request, 'myapp/anggota/mahasiswa.html', konteks)

def form_m(request):
    formm_list = AnggotaMahasiswa.objects.all()
    konteks = {
        'formm_list' : formm_list
    }
    return render(request, 'myapp/anggota/form_mahsiswa.html', konteks)

def tambah_mahasiswa(request):
    if request.method == 'POST':
        if request.FILES:
            hundle_uploaded_file(request.FILES['poto'])

        noanggota = request.POST['no_anggota']
        nim = request.POST['nim']
        nama = request.POST['nama_lengkap']
        jeniskelamin = request.POST['jenis_kelamin']
        jabatan = request.POST['jurusan']
        tmplahir = request.POST['tmp_lahir']
        tgllahir = request.POST['tgl_lahir']
        alamat = request.POST['alamat']
        notelp = request.POST['no_telp']
        kode_pos = request.POST['Kode_pos']
        tahundaftar = request.POST['tgl_daftar']
        poto = request.FILES['poto']

        m = AnggotaMahasiswa()
        m.noanggotam = noanggota
        m.nim = nim
        m.namaanggota = nama
        m.jeniskelamin = jeniskelamin
        m.jurusan = jabatan
        m.tempatlahir = tmplahir
        m.tanggallahir = tgllahir
        m.alamat = alamat
        m.notelp = notelp
        m.kodepos = kode_pos
        m.angkatan = tahundaftar
        m.poto = poto
        m.save()

    mahasiswa = AnggotaMahasiswa.objects.order_by('noanggotam')
    konteks = {
        'list_mahasiswa' : mahasiswa
    }

    return redirect('/mahasiswa/', konteks)


def edit_mahasiswa(request, noanggotamedit):
    edit_mahasiswa = AnggotaMahasiswa.objects.filter(noanggotam = noanggotamedit)
    template = 'myapp/anggota/form-edit-mahasiawa.html'
    konteks = {
        'edit_mahasiswa' : edit_mahasiswa,
    }
    if request.method == "POST":
        print("UPDATE HERE")
        return update_mahasiswa(request, noanggotamedit = noanggotamedit )
    else:
        return render(request, template, konteks)

def update_mahasiswa(request, noanggotamedit="",action="POST"):
    if request.method == 'POST':
        if request.FILES:
            hundle_uploaded_file(request.FILES['poto'])


    noanggota = request.POST['no_anggota']
    nim = request.POST['nim']
    nama = request.POST['nama_lengkap']
    jeniskelamin = request.POST['jenis_kelamin']
    jurusan = request.POST['jurusan']
    tmplahir = request.POST['tmp_lahir']
    tgllahir = request.POST['tgl_lahir']
    alamat = request.POST['alamat']
    kode_pos = request.POST['Kode_pos']
    angkatan = request.POST['tgl_daftar']
    notlp = request.POST['no_telp']
    poto = request.FILES['poto']

    AnggotaMahasiswa.objects.filter(noanggotam = noanggotamedit).update(nim=nim,namaanggota=nama,notelp=notlp,jeniskelamin=jeniskelamin,jurusan=jurusan,tempatlahir=tmplahir,tanggallahir=tgllahir,alamat=alamat,kodepos=kode_pos,angkatan=angkatan, poto = poto)
    return redirect('/mahasiswa/')

def delete_mahasiswa(request, noanggotam=""):
    if request.method == 'GET':
        AnggotaMahasiswa.objects.filter(noanggotam = noanggotam).delete()
        return redirect('/mahasiswa/')

#Anggota Non Mahasiswa

def non_mahasiswa(request):
    list_non_mahasiswa = AnggotaNonMahasiswa.objects.all()
    konteks = {
        'list_non_mahasiswa' : list_non_mahasiswa,
    }
    return render(request, 'myapp/anggota/non-mahasiswa.html', konteks)
    

def form_n(request):
    formn_list = AnggotaNonMahasiswa.objects.all()
    konteks = {
        'formn_list' : formn_list
    }
    return render(request, 'myapp/anggota/form_non.html', konteks)

def tambah_non_mahasiswa(request):
    if request.method == 'POST':
        if request.FILES:
            hundle_uploaded_file(request.FILES['poto'])


        noanggota = request.POST['no_anggota']
        nip = request.POST['nip']
        nama = request.POST['nama_lengkap']
        jeniskelamin = request.POST['jenis_kelamin']
        jabatan = request.POST['jabatan']
        tmplahir = request.POST['tmp_lahir']
        tgllahir = request.POST['tgl_lahir']
        alamat = request.POST['alamat']
        kode_pos = request.POST['Kode_pos']
        tahundaftar = request.POST['tgl_daftar']
        notlp = request.POST['no_telp']
        poto = request.FILES['poto']

        n = AnggotaNonMahasiswa()
        n.noanggotan = noanggota
        n.nip = nip
        n.namaanggota = nama
        n.jeniskelamin = jeniskelamin
        n.jabatan = jabatan
        n.tempatlahir = tmplahir
        n.tanggallahir = tgllahir
        n.alamat = alamat
        n.kodepos = kode_pos
        n.tgldaftar = tahundaftar
        n.notelp = notlp
        n.poto = poto
        n.save()

    non_mahasiswa = AnggotaNonMahasiswa.objects.order_by('noanggotan')
    konteks = {
        'list_non_mahasiswa' : non_mahasiswa
    }

    return redirect('/non-mahasiswa/', konteks)

def edit_non_mahasiswa(request, noanggotanedit):
    edit_non_mahasiswa = AnggotaNonMahasiswa.objects.filter(noanggotan = noanggotanedit)
    template = 'myapp/anggota/form-edit-non-mahasiswa.html'
    konteks = {
        'edit_non_mahasiswa' : edit_non_mahasiswa,
    }
    if request.method == "POST":
        print("UPDATE HERE")
        return update_non_mahasiswa(request, noanggotanedit = noanggotanedit )
    else:
        return render(request, template, konteks)

def update_non_mahasiswa(request, noanggotanedit="",action="POST"):
    if request.method == 'POST':
        if request.FILES:
            hundle_uploaded_file(request.FILES['poto'])


    noanggota = request.POST['no_anggota']
    nim = request.POST['nim']
    nama = request.POST['nama_lengkap']
    jeniskelamin = request.POST['jenis_kelamin']
    jurusan = request.POST['jurusan']
    tmplahir = request.POST['tmp_lahir']
    tgllahir = request.POST['tgl_lahir']
    alamat = request.POST['alamat']
    kode_pos = request.POST['Kode_pos']
    angkatan = request.POST['tgl_daftar']
    notlp = request.POST['no_tlp']
    poto = request.FILES['poto']

    AnggotaNonMahasiswa.objects.filter(noanggotan = noanggotanedit).update(nim=nim,namaanggota=nama,jeniskelamin=jeniskelamin,notlp=notlp,jurusan=jurusan,tempatlahir=tmplahir,tanggallahir=tgllahir,alamat=alamat,kodepos=kode_pos,angkatan=angkatan, poto = poto)
    return redirect('/non-mahasiswa/')

def delete_non_mahasiswa(request, noanggotan=""):
    if request.method == 'GET':
        AnggotaNonMahasiswa.objects.filter(noanggotan = noanggotan).delete()
        return redirect('/non-mahasiswa/')

#buku
def buku(request):
    list_buku = Buku.objects.all()
    konteks = {
        'list_buku' : list_buku,
    }
    return render(request, 'myapp/buku.html', konteks)
    

def form_b(request):
    formb_list = Buku.objects.all()
    konteks = {
        'formb_list' : formb_list
    }
    return render(request, 'myapp/form-buku.html', konteks)

def tambah_buku(request):
    if request.method == 'POST':
        if request.FILES:
            hundle_uploaded_file(request.FILES['poto'])

        kodebuku = request.POST['kodebuku']
        judul = request.POST['judul']
        penerbit = request.POST['penerbit']
        pengarang = request.POST['pengarang']
        thnterbit = request.POST['thnterbit']
        kotaterbit = request.POST['kotaterbit']
        bahasa = request.POST['bahasa']
        edisi = request.POST['edisi']
        poto = request.FILES['poto']

        b = Buku()
        b.kodebuku = kodebuku
        b.judul = judul
        b.penerbit = penerbit
        b.pengarang = pengarang
        b.thnterbit = thnterbit
        b.kotaterbit = kotaterbit
        b.bahasa = bahasa
        b.edisi = edisi
        b.sampul = poto
        b.save()


    list_buku = Buku.objects.order_by('kodebuku')
    konteks = {
        'list_buku' : list_buku
    }

    return redirect('/buku/', konteks)

def edit_buku(request, kodebukuedit):
    edit_buku = Buku.objects.filter(kodebuku = kodebukuedit)
    template = 'myapp/form-edit-buku.html'
    konteks = {
        'edit_buku' : edit_buku,
    }
    if request.method == "POST":
        print("UPDATE HERE")
        return update_buku(request, kodebukuedit = kodebukuedit )
    else:
        return render(request, template, konteks)

def update_buku(request, kodebukuedit="",action="POST"):
    if request.method == 'POST':
        if request.FILES:
            hundle_uploaded_file(request.FILES['poto'])


    kodebuku = request.POST['kodebuku']
    judul = request.POST['judul']
    penerbit = request.POST['penerbit']
    pengarang = request.POST['pengarang']
    thnterbit = request.POST['thnterbit']
    kotaterbit = request.POST['kotaterbit']
    bahasa = request.POST['bahasa']
    edisi = request.POST['edisi']
    poto = request.FILES['poto']

    Buku.objects.filter(kodebuku = kodebukuedit).update(judul=judul, penerbit=penerbit, pengarang=pengarang,thnterbit=thnterbit,
    kotaterbit=kotaterbit, bahasa=bahasa, edisi=edisi, sampul=poto)
    return redirect('/buku')

def delete_buku(request, kodebuku=""):
    if request.method == 'GET':
        Buku.objects.filter(kodebuku = kodebuku).delete()
        return redirect('/buku/')


#menu
def dashboard(request):
    jml_buku = Buku.objects.count()
    mahasiswa  = AnggotaMahasiswa.objects.count()
    non_mahasiswa  = AnggotaNonMahasiswa.objects.count()
    jml_anggota = mahasiswa + non_mahasiswa
    konteks = {
         'jml_buku' : jml_buku,
         'jml_anggota' : jml_anggota
    }
    return render(request, 'myapp/dashboard.html', konteks)

def registrasi(request):
    return render(request, 'myapp/registrasi.html')

def database(request):
    jml_buku = Buku.objects.count()
    mahasiswa  = AnggotaMahasiswa.objects.count()
    non_mahasiswa  = AnggotaNonMahasiswa.objects.count()
    konteks = {
        'jml_buku' : jml_buku,
        'mahasiswa' : mahasiswa,
        'non_mahasiswa' : non_mahasiswa
    }
    return render(request, 'myapp/database.html', konteks)

def transaksi(request):
    return render(request, 'myapp/transaksi.html')

def peminjaman(request):
    return render(request, 'myapp/peminjaman.html')








# on update

# def pinjamM(request):
#     list_pinjam_mahasiswa = PinjamHeaderMahasiswa.objects.all()
#     konteks = {
#         'list_pinjam_mahasiswa' : list_pinjam_mahasiswa,
#     }
#     return render(request, 'myapp/pinjam-mahasiswa.html', konteks)

# def pinjamN(request):
#     list_pinjam_non_mahasiswa = PinjamHeaderNonMahasiswa.objects.all()
#     konteks = {
#         'list_pinjam_non_mahasiswa' : list_pinjam_non_mahasiswa,
#     }
#     return render(request, 'myapp/pinjam-non-mahasiswa.html', konteks)
    
    
def pengembalian(request):
    return render(request, 'myapp/pengembalian.html')

def kembaliM(request):
    list_kembali_mahasiswa = KembaliMahasiswa.objects.all()
    konteks = {
        'list_kembali_mahasiswa' : list_kembali_mahasiswa,
    }
    return render(request, 'myapp/kembali-mahasiswa.html', konteks)

# def kembaliN(request):
#     list_kembali_non_mahasiswa = KembaINonMahaiswa.objects.all()
#     konteks = {
#         'list_kembali_non_mahasiswa' : list_kembali_non_mahasiswa,
#     }
#     return render(request, 'myapp/kembali-non-mahasiswa.html', konteks)
    
def laporan(request):
    return render(request, 'myapp/laporan.html')




# def formM(request):
#     # m_list = AnggotaMahasiswa.objects.all()
#     # konteks = {
#     #     'm_list' : m_list,
#     # }
#     return render(request, 'myapp/anggota/form_mahsiswa.html')
    

   
    # return render(request, 'registrasi.html', konteks)
    # return redirect('/non-mahasiswa/')
# def tambah_buku(request):
#     form_buku = FormBuku(request.POST or None)

#     if request.method == 'POST':
#         if form_buku.is_valid():
#             form_buku.save()
#             form_buku = FormBuku()
#         return redirect('buku')

#     konteks= {
#         'form' : form_buku,
#     }
#     return render(request, 'myapp/tambah-buku.html', konteks)


