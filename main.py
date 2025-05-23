from pysondb import db
import os

inventaris_db = db.getDb("./semester 3/LabManagement/database/inventaris_lab.json")
penggunaan_db = db.getDb("./semester 3/LabManagement/database/penggunaan_lab.json")
pengguna_db = db.getDb("./semester 3/LabManagement/database/pengguna_lab.json")

# Inventaris
class Inventaris:
    def __init__(self, nama, kategori, jumlah, kondisi):
        self.nama = nama
        self.kategori = kategori
        self.jumlah = jumlah
        self.kondisi = kondisi

    def simpan_ke_db(self):
        inventaris_db.add({
            "nama": self.nama,
            "kategori": self.kategori,
            "jumlah": self.jumlah,
            "kondisi": self.kondisi
        })
        print(f"Inventaris '{self.nama}' berhasil disimpan ke database.")

        pilihan = input("Tambah lagi (y/n) : ")
        if pilihan == "y":
            tambah_inventaris()
        else:
            menu_inventaris()

        

    @staticmethod
    def tampilkan_inventaris():
        os.system('cls')
        data = inventaris_db.getAll()
        if data:
            print("\nData Inventaris Lab:")
            for item in data:
                print(f"ID: {item['id']}, Nama: {item['nama']}, Kategori: {item['kategori']}, Jumlah: {item['jumlah']}, Kondisi: {item['kondisi']}")
        else:
            print("\nBelum ada data inventaris yang tersimpan.")
            
    @staticmethod
    def hapus_inventaris():
        Inventaris.tampilkan_inventaris()
        id_hapus = input("Masukkan ID inventaris yang akan dihapus: ")
        inventaris_db.deleteById(id_hapus)
        print(f"Inventaris dengan ID '{id_hapus}' berhasil dihapus.")
        pilihan = input("Hapus lagi (y/n) : ")
        if pilihan == "y":
            Inventaris.hapus_inventaris()
        else:
            menu_inventaris()

    @staticmethod
    def update_inventaris():
        Inventaris.tampilkan_inventaris()
        id_update = input("Masukkan ID inventaris yang akan diupdate: ")
        nama = input("Nama peralatan baru: ")
        kategori = input("Kategori baru: ")
        jumlah = int(input("Jumlah baru: "))
        kondisi = input("Kondisi baru: ")
        inventaris_db.updateById(id_update, {
            "nama": nama,
            "kategori": kategori,
            "jumlah": jumlah,
            "kondisi": kondisi
        })
        print(f"Inventaris dengan ID '{id_update}' berhasil diupdate.")

        pilihan = input("Edit lagi (y/n) : ")
        if pilihan == "y":
            Inventaris.update_inventaris()
        else:
            menu_inventaris()


# Kelas Penggunaan Lab
class PenggunaanLab:
    def __init__(self, nama_ruang, tanggal_penggunaan, waktu_mulai, waktu_selesai, pengguna):
        self.nama_ruang = nama_ruang
        self.tanggal_penggunaan = tanggal_penggunaan
        self.waktu_mulai = waktu_mulai
        self.waktu_selesai = waktu_selesai
        self.pengguna = pengguna

    def simpan_ke_db(self):
        penggunaan_db.add({
            "nama_ruang": self.nama_ruang,
            "tanggal_penggunaan": self.tanggal_penggunaan,
            "waktu_mulai": self.waktu_mulai,
            "waktu_selesai": self.waktu_selesai,
            "pengguna": self.pengguna
        })
        print(f"Penggunaan ruang '{self.nama_ruang}' oleh '{self.pengguna}' berhasil disimpan ke database.")

        pilihan = input("Tambah lagi (y/n) : ")
        if pilihan == "y":
            tambah_penggunaan_lab()
        else:
            menu_penggunaan_lab()
        


    @staticmethod
    def tampilkan_penggunaan_lab():
        os.system('cls')
        data = penggunaan_db.getAll()
        if data:
            print("\nData Penggunaan Lab:")
            for item in data:
                print(f"ID: {item['id']}, Ruang: {item['nama_ruang']}, Tanggal: {item['tanggal_penggunaan']}, Waktu: {item['waktu_mulai']} - {item['waktu_selesai']}, Pengguna: {item['pengguna']}")
        else:
            print("\nBelum ada data penggunaan lab yang tersimpan.")

    @staticmethod
    def hapus_penggunaan_lab():
        PenggunaanLab.tampilkan_penggunaan_lab()
        id_hapus = input("Masukkan ID penggunaan lab yang akan dihapus: ")
        penggunaan_db.deleteById(id_hapus)
        print(f"Penggunaan lab dengan ID '{id_hapus}' berhasil dihapus.")
        pilihan = input("Hapus lagi (y/n) : ")
        if pilihan == "y":
            PenggunaanLab.hapus_penggunaan_lab()
        else:
            menu_penggunaan_lab()

    @staticmethod
    def update_penggunaan_lab():
        PenggunaanLab.tampilkan_penggunaan_lab()
        id_update = input("Masukkan ID penggunaan lab yang akan diupdate: ")
        nama_ruang = input("Nama ruang baru: ")
        tanggal_penggunaan = input("Tanggal penggunaan baru (DD-MM-YYYY): ")
        waktu_mulai = input("Waktu mulai baru (HH:MM): ")
        waktu_selesai = input("Waktu selesai baru (HH:MM): ")
        pengguna = input("Nama pengguna baru: ")
        penggunaan_db.updateById(id_update, {
            "nama_ruang": nama_ruang,
            "tanggal_penggunaan": tanggal_penggunaan,
            "waktu_mulai": waktu_mulai,
            "waktu_selesai": waktu_selesai,
            "pengguna": pengguna
        })
        print(f"Penggunaan lab dengan ID '{id_update}' berhasil diupdate.")
        pilihan = input("Edit lagi (y/n) : ")
        if pilihan == "y":
            PenggunaanLab.update_penggunaan_lab()
        else:
            menu_penggunaan_lab()

# Kelas Pengguna Lab
class PenggunaLab:
    def __init__(self, nama, peran, email):
        self.nama = nama
        self.peran = peran
        self.email = email

    def simpan_ke_db(self):
        pengguna_db.add({
            "nama": self.nama,
            "peran": self.peran,
            "email": self.email
        })
        print(f"Pengguna '{self.nama}' berhasil disimpan ke database.")
        
        pilihan = input("Tambah lagi (y/n) : ")
        if pilihan == "y":
            tambah_pengguna_lab()
        else:
            menu_pengguna_lab()

    @staticmethod
    def tampilkan_pengguna_lab():
        os.system('cls')
        data = pengguna_db.getAll()
        if data:
            print("\nData Pengguna Lab:")
            for item in data:
                # Memastikan semua field ada sebelum ditampilkan
                nama = item.get("nama", "Tidak ada nama")
                peran = item.get("peran", "Tidak ada peran")
                email = item.get("email", "Tidak ada email")
                print(f"ID: {item['id']}, Nama: {nama}, Peran: {peran}, Email: {email}")
        else:
            print("\nBelum ada data pengguna lab yang tersimpan.")


    @staticmethod
    def hapus_pengguna_lab():
        PenggunaLab.tampilkan_pengguna_lab()
        id_hapus = input("Masukkan ID pengguna lab yang akan dihapus: ")
        pengguna_db.deleteById(id_hapus)
        print(f"Pengguna lab dengan ID '{id_hapus}' berhasil dihapus.")
        pilihan = input("Hapus lagi (y/n) : ")
        if pilihan == "y":
            PenggunaLab.hapus_pengguna_lab()
        else:
            menu_pengguna_lab()

    @staticmethod
    def update_pengguna_lab():
        PenggunaLab.tampilkan_pengguna_lab()
        id_update = input("Masukkan ID pengguna lab yang akan diupdate: ")
        nama = input("Nama pengguna baru: ")
        peran = input("Peran baru (Mahasiswa, Dosen, Teknisi): ")
        email = input("Email baru: ")
        pengguna_db.updateById(id_update, {
            "nama": nama,
            "peran": peran,
            "email": email
        })
        print(f"Pengguna lab dengan ID '{id_update}' berhasil diupdate.")
        pilihan = input("Edit lagi (y/n) : ")
        if pilihan == "y":
            PenggunaLab.update_pengguna_lab()
        else:
            menu_pengguna_lab()

def tambah_inventaris():
    os.system('cls')
    nama = input("Nama peralatan: ")
    kategori = input("Kategori: ")
    jumlah = int(input("Jumlah: "))
    kondisi = input("Kondisi barang: ")
    inventaris = Inventaris(nama, kategori, jumlah, kondisi)
    inventaris.simpan_ke_db()

def tambah_penggunaan_lab():
    os.system('cls')
    nama_ruang = input("Nama ruang: ")
    tanggal_penggunaan = input("Tanggal penggunaan (DD-MM-YYYY): ")
    waktu_mulai = input("Waktu mulai (HH:MM): ")
    waktu_selesai = input("Waktu selesai (HH:MM): ")
    pengguna = input("Nama pengguna: ")
    penggunaan_lab = PenggunaanLab(nama_ruang, tanggal_penggunaan, waktu_mulai, waktu_selesai, pengguna)
    penggunaan_lab.simpan_ke_db()

def tambah_pengguna_lab():
    os.system('cls')    
    nama = input("Nama pengguna: ")
    peran = input("Pengguna sebagai (Mahasiswa, Dosen, Teknisi): ")
    email = input("Email pengguna: ")
    pengguna_lab = PenggunaLab(nama, peran, email)
    pengguna_lab.simpan_ke_db()

def menu_inventaris():
    os.system('cls')
    print("\n===== MENU INVENTARIS LAB =====")
    print("1. Tambah Inventaris Lab")
    print("2. Tampilkan Inventaris Lab")
    print("3. Hapus Inventaris Lab")
    print("4. Update Inventaris Lab")
    print("0. Menu Awal")    
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tambah_inventaris()
    elif pilihan == "2":
        Inventaris.tampilkan_inventaris()

        pilihan = input("Back to menu (y) : ")
        if pilihan == "y":
            menu_inventaris()
    elif pilihan == "3":
        Inventaris.hapus_inventaris()
    elif pilihan == "4":
        Inventaris.update_inventaris()
    elif pilihan == "0":
        tampilkan_menu()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

def menu_penggunaan_lab():
    os.system('cls')
    print("\n===== MENU PENGGUNAAN LAB =====")
    print("1. Tambah Penggunaan Lab")
    print("2. Tampilkan Penggunaan Lab")
    print("3. Hapus Penggunaan Lab")
    print("4. Update Penggunaan Lab")
    print("0. Menu Awal")    
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tambah_penggunaan_lab()
    elif pilihan == "2":
        PenggunaanLab.tampilkan_penggunaan_lab()

        pilihan = input("Back to menu (y) : ")
        if pilihan == "y":
            menu_penggunaan_lab()
    elif pilihan == "3":
        PenggunaanLab.hapus_penggunaan_lab()
    elif pilihan == "4":
        PenggunaanLab.update_penggunaan_lab()
    elif pilihan == "0":
        tampilkan_menu()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

def menu_pengguna_lab():
    os.system('cls')
    print("\n===== MENU PENGGUNA LAB =====")
    print("1. Tambah Pengguna Lab")
    print("2. Tampilkan Pengguna Lab")
    print("3. Hapus Pengguna Lab")
    print("4. Update Pengguna Lab")
    print("0. Menu Awal")    
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tambah_pengguna_lab()
    elif pilihan == "2":
        PenggunaLab.tampilkan_pengguna_lab()

        pilihan = input("Back to menu (y) : ")
        if pilihan == "y":
            menu_pengguna_lab()
    elif pilihan == "3":
        PenggunaLab.hapus_pengguna_lab()
    elif pilihan == "4":
        PenggunaLab.update_pengguna_lab()
    elif pilihan == "0":
        tampilkan_menu()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

def tampilkan_menu():
    os.system('cls')
    print("\n===== MENU MANAJEMEN LAB =====")
    print("1. Inventaris Lab")
    print("2. Penggunaan Lab")
    print("3. Pengguna Lab")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        menu_inventaris()
    elif pilihan == "2":
        menu_penggunaan_lab()
    elif pilihan == "3":
        menu_pengguna_lab()
    elif pilihan == "0":
        print("Keluar dari program.")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        
# Main Program
if __name__ == "__main__":
    tampilkan_menu()
        
