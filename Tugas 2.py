class Mahasiswa:
# kita definisikan kelas dengan nama Mahasiswa
    def __init__(self, Nama, NIM, Jurusan):
    # kode di atas merupakan inisialisasi untuk kelas Mahasiswa dengan 
    # menerima argumen "Nama", "NIM", dan "Jurusan" sebagai parameter
        self.nama = Nama
        # Parameter "Nama" disimpan pada atribut "nama" dari objek Mahasiswa yang dibuat
        self.nim = NIM
        # Parameter "NIM" disimpan pada atribut "nim" dari objek Mahasiswa yang dibuat
        self.jurusan = Jurusan
        # Parameter "Jurusan" disimpan pada atribut "jurusan" dari objek Mahasiswa yang dibuat

    def tampilkan_info(self):
    # Kode di atas merupakan metode untuk menampilkan informasi mahasiswa
        print("\n- Nama Mahasiswa:", self.nama)
        # Menampilkan pesan nama mahasiswa dan memanggil atribut "nama"
        print("- NIM:", self.nim)
        # Menampilkan pesan NIM dan memanggil atribut "nim"
        print("- Jurusan:", self.jurusan.NamaJurusan)
        # Menampilkan pesan Jurusan dan memanggil atribut "NamaJurusan"


class Jurusan:
# Mendefinisikan sebuah kelas bernama "Jurusan
    def __init__(self, nama_jurusan):
    # Kode di atas merupakan metode inisialisasi (constructor) untuk kelas Jurusan
    # dengan menerima argumen "nama_jurusan" sebagai parameter
        self.NamaJurusan = nama_jurusan
        # Menyimpan nilai parameter "nama_jurusan" ke atribut "NamaJurusan" dari objek Jurusan yang sedang dibuat
        self.DaftarMahasiswa = []
        # Membuat sebuah daftar kosong untuk menyimpan objek Mahasiswa

    def tambah_mahasiswa(self, mahasiswa):
    # Metode untuk menambahkan objek Mahasiswa ke dalam daftar mahasiswa
        self.DaftarMahasiswa.append(mahasiswa)
        # Menambahkan objek Mahasiswa ke dalam daftar mahasiswa pada objek Jurusan 

    def tampilkan_daftar_mahasiswa(self):
    # Kode di atas merupakan metode untuk menampilkan daftar mahasiswa dalam jurusan
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        # Menampilkan pesan sebagai judul daftar mahasiswa dan memanggil atribut NamaJurusan
        for mahasiswa in self.DaftarMahasiswa:
        # Melakukan perulangan untuk setiap objek Mahasiswa dalam daftar mahasiswa pada objek Jurusan 
            print("- Nama:", mahasiswa.nama)
            # Menampilkan pesan "Nama" dan memanggil atribut nama dari parameter mahasiswa
            print("- NIM:", mahasiswa.nim)
            # Menampilkan pesan "NIM" dan memanggil atribut nim dari parameter mahasiswa

class Universitas:
# Mendefinisikan sebuah kelas bernama "Universitas"
    def __init__(self, nama_universitas):
    # Metode inisialisasi (constructor) untuk kelas Universitas. Menerima argumen "nama_universitas" sebagai parameter
        self.NamaUniversitas = nama_universitas
        # Menyimpan nilai parameter "nama_universitas" ke atribut "NamaUniversitas" dari objek Universitas 
        self.DaftarJurusan = []
        # membuat sebuah variabel bernama DaftarJurusan yang merupakan sebuah daftar kosong

    def tambah_jurusan(self, jurusan):
    # Mendefinisikan sebuah metode bernama tambah_jurusan yang menerima parameter jurusan
        self.DaftarJurusan.append(jurusan)
        # Kode di atas digunakan untuk menambahkan objek jurusan ke dalam daftar DaftarJurusan

    def tampilkan_daftar_jurusan(self):
    # Mendefinisikan sebuah metode bernama tampilkan_daftar_jurusan
        print("\nDaftar Jurusan di Universitas", self.NamaUniversitas)
        # Kode omo dogunakan untuk menampilkan nama jurusan di universitas
        for jurusan in self.DaftarJurusan:
        # Kondisi for digunakan untuk memanggil semua jurusan yang ada DaftarJurusan
            print("Nama Jurusan:", jurusan.NamaJurusan)


# Implementasi Pertanyaan

# 2. Buatlah sebuah objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")
# Membuat objek universitas dengan nama "XYZ University" menggunakan kelas `Universitas`

# 3. Buatlah objek Jurusan dengan nama menerima inputan dan tambahkan objek tersebut ke dalam Universitas XYZ.
nama_jurusan = input("Masukkan nama jurusan: ")
#  Menerima input dari pengguna untuk memasukkan nama jurusan
jurusan_ti = Jurusan(nama_jurusan)
# Membuat objek jurusan dengan menggunakan kelas `Jurusan` dan nama jurusan yang telah dimasukka
universitas_xyz.tambah_jurusan(jurusan_ti)
# Menambahkan objek jurusan ke dalam daftar jurusan di universitas "XYZ University"

# 4. Buatlah objek Mahasiswa dengan nama menerima inputan, NIM menerima inputan juga, dan masukkan ke dalam Jurusan Teknik Informatika di Universitas XYZ.
print("\nMasukkan Data Mahasiswa Pertama")
# Menerima input dari pengguna untuk memasukkan nama mahasiswa
nama_mhs = input("Masukkan nama mahasiswa: ")
# Menerima input dari pengguna untuk memasukkan nama mahasiswa
nim_mhs = input("Masukkan NIM mahasiswa: ")
# Menerima input dari pengguna untuk memasukkan NIM mahasiswa
mahasiswa_baru = Mahasiswa(nama_mhs, nim_mhs, jurusan_ti)
# Membuat objek mahasiswa dengan menggunakan kelas `Mahasiswa` dan data yang telah dimasukkan, serta jurusan "Teknik Informatika"

jurusan_ti.tambah_mahasiswa(mahasiswa_baru)
# Menambahkan objek mahasiswa ke dalam daftar mahasiswa di jurusan "Teknik Informatika"

# 5. Tampilkan daftar jurusan yang ada di Universitas XYZ.
universitas_xyz.tampilkan_daftar_jurusan()

# 6. Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ.
jurusan_ti.tampilkan_daftar_mahasiswa()

# 7. Buatkan juga pilihan "apakah anda ingin menambahkan nama mahasiswa?" Jika ya, maka arahkan ke objek mahasiswa sehingga user dapat memasukkan nama dan NIM nya.
pilihan = input("\nApakah Anda ingin menambahkan nama mahasiswa? (ya/tidak): ")
while pilihan.lower() == "ya":
    nama_mahasiswa = input("\nMasukkan nama mahasiswa: ")
    nim_mahasiswa = input("Masukkan NIM mahasiswa: ")
    mahasiswa_baru = Mahasiswa(nama_mahasiswa, nim_mahasiswa, jurusan_ti)
    jurusan_ti.tambah_mahasiswa(mahasiswa_baru)

    print("Mahasiswa", nama_mahasiswa, "telah ditambahkan.")

    pilihan = input("\nApakah Anda ingin menambahkan nama mahasiswa lagi? (ya/tidak): ")
# Menerima input dari pengguna apakah ingin menambahkan mahasiswa baru. 
# Jika iya, maka data mahasiswa baru dimasukkan dan ditambahkan ke dalam daftar mahasiswa 
# di jurusan "Teknik Informatika". Loop ini akan berlanjut sampai pengguna tidak ingin menambahkan lagi

# 8. Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ setelah penambahan mahasiswa.
jurusan_ti.tampilkan_daftar_mahasiswa()

# 9. Tampilkan daftar mahasiswa yang terdaftar dalam semua jurusan di Universitas XYZ.
universitas_xyz.tampilkan_daftar_jurusan()

# 10. Tampilkan informasi lengkap dari setiap mahasiswa yang terdaftar di Universitas XYZ.
for jurusan in universitas_xyz.DaftarJurusan:
# Kondisi for digunakan untuk memanggil semua jurusan yang ada di universitas_xyz
    for mahasiswa in jurusan.DaftarMahasiswa:
    # Kondisi for digunakan untuk memanggil semua mahasiswa yang ada di DaftarMahasiswa
        mahasiswa.tampilkan_info()
        # Menampilkan informasi lengkap dari setiap mahasiswa yang terdaftar di universitas "XYZ University"
