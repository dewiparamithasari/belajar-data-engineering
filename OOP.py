#Class
class mahasiswa:
    universitas = "mahasiswa universitas indonesia" #ClassAttributes

    def __init__(self, nama, umur, asal, jenis_kelamin):
        self.nama = nama #InstanceMethod = InstanceAtributes
        self.umur = umur
        self.asal = asal
        self.jenis_kelamin = jenis_kelamin

    def anggota_bem(self):
        print("Mahasiswa", self.nama, "anggota bem")
    
    def bukan_anggota_bem(self):
        print("Mahasiswa", self.nama, "bukan anggota bem")

    def fakultas(self):
        print(self.nama, 'fakultas teknik')

    @classmethod #Classmethod
    def aktif(cls):
        print(cls.universitas, 'status kuliah: aktif')

class Mahasiswa_1(mahasiswa): #Inheritance
    jurusan = "teknik industri" #Overrriding

    def fakultas(self):
        print(self.nama, self.umur, self.jenis_kelamin, 'fakultas teknik S1')
    
    def semester(self, semester=None): #Overloading
        if semester == None:
            print("kosong")
        else:
            print(f"{self.nama} semester {semester}")
   
class Mahasiswa_2(mahasiswa):
    jurusan = "teknik elektro"

    def fakultas(self):
        print(self.nama, self.umur, self.jenis_kelamin, 'fakultas teknik S2')

    def semester(self, semester=None): #Overloading
        if semester == None:
            print("kosong")
        else:
            print(f"{self.nama} semester {semester}")


mahasiswa_1 = Mahasiswa_1('andriani', 19, 'Jakarta', 'perempuan')
mahasiswa_2 = Mahasiswa_2('bimo', 27, 'Malang', 'laki-laki')


print(mahasiswa_1.universitas)
mahasiswa_1.fakultas()
print(mahasiswa_1.jurusan)
mahasiswa_1.aktif()
mahasiswa_1.anggota_bem()
mahasiswa_1.semester()
mahasiswa_1.semester('genap')

print(mahasiswa_2.universitas)
mahasiswa_2.fakultas()
print(mahasiswa_2.jurusan)
mahasiswa_2.aktif()
mahasiswa_2.anggota_bem()
mahasiswa_2.semester('ganjil')