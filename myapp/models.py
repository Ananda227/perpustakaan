# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnggotaMahasiswa(models.Model):
    noanggotam = models.CharField(db_column='NoAnggotaM', primary_key=True, max_length=20)  # Field name made lowercase.
    nim = models.CharField(db_column='NIM', max_length=15)  # Field name made lowercase.
    namaanggota = models.CharField(db_column='NamaAnggota', max_length=50)  # Field name made lowercase.
    jurusan = models.CharField(db_column='Jurusan', max_length=20)  # Field name made lowercase.
    tanggallahir = models.DateField(db_column='TanggalLahir')  # Field name made lowercase.
    alamat = models.CharField(db_column='Alamat', max_length=50)  # Field name made lowercase.
    kodepos = models.CharField(db_column='KodePos', max_length=20)  # Field name made lowercase.
    notelp = models.CharField(db_column='NoTelp', max_length=20)  # Field name made lowercase.
    hp = models.CharField(db_column='HP', max_length=20)  # Field name made lowercase.
    angkatan = models.IntegerField(db_column='Angkatan')  # Field name made lowercase.
    namaortu = models.CharField(db_column='NamaOrtu', max_length=50, null=True)  # Field name made lowercase.
    alamatortu = models.CharField(db_column='AlamatOrtu', max_length=50, null=True )  # Field name made lowercase.
    notelportu = models.CharField(db_column='NoTelpOrtu', max_length=20, null=True)  # Field name made lowercase.
    jeniskelamin = models.CharField(db_column='JenisKelamin', max_length=20)  # Field name made lowercase.
    tempatlahir = models.CharField(db_column='TempatLahir', max_length=20)  # Field name made lowercase.
    poto = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anggota_mahasiswa'


class AnggotaNonMahasiswa(models.Model):
    noanggotan = models.CharField(db_column='NoAnggotaN', primary_key=True, max_length=10)  # Field name made lowercase.
    nip = models.CharField(db_column='NIP', max_length=15)  # Field name made lowercase.
    namaanggota = models.CharField(db_column='NamaAnggota', max_length=50)  # Field name made lowercase.
    jabatan = models.CharField(db_column='Jabatan', max_length=20)  # Field name made lowercase.
    tanggallahir = models.DateField(db_column='TanggalLahir')  # Field name made lowercase.
    alamat = models.CharField(db_column='Alamat', max_length=50)  # Field name made lowercase.
    kodepos = models.CharField(db_column='KodePos', max_length=20)  # Field name made lowercase.
    notelp = models.CharField(db_column='NoTelp', max_length=20)  # Field name made lowercase.
    hp = models.CharField(db_column='HP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tgldaftar = models.IntegerField(db_column='TglDaftar')  # Field name made lowercase.
    jeniskelamin = models.CharField(db_column='JenisKelamin', max_length=20)  # Field name made lowercase.
    tempatlahir = models.CharField(db_column='TempatLahir', max_length=20)  # Field name made lowercase.
    poto = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anggota_non_mahasiswa'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Buku(models.Model):
    kodebuku = models.CharField(db_column='KodeBuku', primary_key=True, max_length=10)  # Field name made lowercase.
    noudc = models.CharField(db_column='NoUDC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    noreg = models.CharField(db_column='NoReg', max_length=20)  # Field name made lowercase.
    judul = models.CharField(db_column='Judul', max_length=50)  # Field name made lowercase.
    penerbit = models.CharField(db_column='Penerbit', max_length=50)  # Field name made lowercase.
    pengarang = models.CharField(db_column='Pengarang', max_length=50)  # Field name made lowercase.
    thnterbit = models.CharField(db_column='ThnTerbit', max_length=5)  # Field name made lowercase.
    kotaterbit = models.CharField(db_column='KotaTerbit', max_length=20)  # Field name made lowercase.
    bahasa = models.CharField(db_column='Bahasa', max_length=20)  # Field name made lowercase.
    edisi = models.CharField(db_column='Edisi', max_length=20)  # Field name made lowercase.
    deskripsi = models.CharField(db_column='Deskripsi', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='Isbn', max_length=20, blank=True, null=True)  # Field name made lowercase.
    jumekslempar = models.IntegerField(db_column='JumEkslempar', blank=True, null=True)  # Field name made lowercase.
    subyekutama = models.CharField(db_column='SubyekUtama', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subyektambahan = models.CharField(db_column='SubyekTambahan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sampul = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buku'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class KembaliMahasiswa(models.Model):
    nokembalim = models.CharField(db_column='NoKembaliM', primary_key=True, max_length=10)  # Field name made lowercase.
    nopinjamm = models.CharField(db_column='NoPinjamM', max_length=10)  # Field name made lowercase.
    tglkembali = models.DateField(db_column='TglKembali')  # Field name made lowercase.
    kodepetugas = models.CharField(db_column='KodePetugas', max_length=10)  # Field name made lowercase.
    denda = models.CharField(db_column='Denda', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kembali_mahasiswa'


class KembaliNonMahasiswa(models.Model):
    nokembalin = models.CharField(db_column='NoKembaliN', primary_key=True, max_length=10)  # Field name made lowercase.
    nopinjamn = models.CharField(db_column='NoPinjamN', max_length=10)  # Field name made lowercase.
    tglkembali = models.DateField(db_column='TglKembali')  # Field name made lowercase.
    kodepetugas = models.CharField(db_column='KodePetugas', max_length=10)  # Field name made lowercase.
    denda = models.CharField(db_column='Denda', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kembali_non_mahasiswa'


class Petugas(models.Model):
    kodepetugas = models.CharField(db_column='KodePetugas', primary_key=True, max_length=10)  # Field name made lowercase.
    nama = models.CharField(db_column='Nama', max_length=50)  # Field name made lowercase.
    jabatan = models.CharField(db_column='Jabatan', max_length=20)  # Field name made lowercase.
    hakakses = models.CharField(db_column='HakAkses', max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'petugas'


class PinjamMahasiswa(models.Model):
    nopinjamm = models.CharField(db_column='NoPinjamM', max_length=10)  # Field name made lowercase.
    kodebuku = models.CharField(db_column='KodeBuku', max_length=10)  # Field name made lowercase.
    judul = models.CharField(db_column='Judul', max_length=50)  # Field name made lowercase.
    penerbit = models.CharField(db_column='Penerbit', max_length=50)  # Field name made lowercase.
    thnterbit = models.CharField(db_column='ThnTerbit', max_length=5)  # Field name made lowercase.
    jml = models.IntegerField(db_column='Jml')  # Field name made lowercase.
    noanggotam = models.CharField(db_column='NoAnggotaM', max_length=10)  # Field name made lowercase.
    tglpinjam = models.DateField(db_column='TglPinjam')  # Field name made lowercase.
    tglkembali = models.DateField(db_column='TglKembali')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pinjam_mahasiswa'


class PinjamNonMahasiswa(models.Model):
    nopinjamn = models.CharField(db_column='NoPinjamN', max_length=10)  # Field name made lowercase.
    kodebuku = models.CharField(db_column='KodeBuku', max_length=10)  # Field name made lowercase.
    judul = models.CharField(db_column='Judul', max_length=50)  # Field name made lowercase.
    penerbit = models.CharField(db_column='Penerbit', max_length=50)  # Field name made lowercase.
    thnterbit = models.CharField(db_column='ThnTerbit', max_length=5)  # Field name made lowercase.
    jml = models.IntegerField(db_column='Jml')  # Field name made lowercase.
    noanggotan = models.CharField(db_column='NoAnggotaN', max_length=10)  # Field name made lowercase.
    tglpinjam = models.DateField(db_column='TglPinjam')  # Field name made lowercase.
    tglkembali = models.DateField(db_column='TglKembali')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pinjam_non_mahasiswa'
