# Episode input user

# data yang dimasukkan pasti string
data = input("Masukkan data: ")

print("data = ", data, ", type = ",type(data))

# jika kita ingin mengambil int, maka
angka = float(input("Masukkan angka: "))
angka = int(input("Masukkan angka: "))

print("data = ", angka, ", type = ",type(angka))

# bagaimana dengan boolean
biner = bool(int(input("Masukkan nilai boolean: "))) # harus ke integer dahulu baru ke boolean
print("data = ", biner, ", type = ",type(biner))