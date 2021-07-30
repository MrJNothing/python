# Latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# +++++++3------------10++++++++++
inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))

# ++++++++3-------------------------
# Memeriksa angka kurang dari 3
isKurangDari = inputUser < 3
print("Kurang dari 3 =", isKurangDari)

# ---------------------10++++++++++++++
# Memeriksa angka lebih dari 10
isLebihDari = inputUser > 10
print("Lebih dari 10 =", isLebihDari)

# +++++++3------------10++++++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan:", isCorrect)

print("\n","="*20,"\n")
# -------3+++++++++++++10---------
# Kasus irisan

inputUser = float(input("Masukkan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

# --------3++++++++++++++++
# Lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 =", isLebihDari)

# +++++++++++10-----------
# Kurang dari 10
isKurangDari = inputUser < 10
print("Kurang dari 10 =", isKurangDari)

# -------3+++++++++++++10---------
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan:", isCorrect)

print("\n","="*20,"\n")
# PR KAWAN

# (SOAL 1) ---------0+++++++++5---------8+++++++++11----------
inputUser = float(input("Masukkan angka yang bernilai\nlebih dari 0 \ndan \nkurang dari 5 \natau \nlebih dari 8 \ndan \nkurang dari 11:"))

# -----------0++++++++++
# Lebih dari 0
isLebihDari = inputUser > 0
print("Lebih dari 0 =", isLebihDari)

# +++++++++++5----------
# Kurang dari 5
isKurangDari = inputUser < 5
print("Kurang dari 5 =", isKurangDari)

# ---------0+++++++++5---------
isCorrect1 = isLebihDari and isKurangDari


# -----------8++++++++++
# Lebih dari 8
isLebihDari = inputUser > 8
print("Lebih dari 8 =", isLebihDari)

# +++++++++++11----------
# Kurang dari 11
isKurangDari = inputUser < 11
print("Kurang dari 11 =", isKurangDari)

# ---------8+++++++++11---------
isCorrect2 = isLebihDari and isKurangDari


isCorrectHasil = isCorrect1 or isCorrect2
print("angka yang anda masukkan:", isCorrectHasil)

print("\n","="*20,"\n")
# (SOAL 2) +++++++++0---------5+++++++++8---------11++++++++++
inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 0 \natau \nlebih dari 5 \ndan \nkurang dari 8 \natau \nlebih dari 11:"))

# +++++++++0---------
# Kurang dari 0
isKurangDari = inputUser < 0
print("Kurang dari 0 =", isKurangDari)
isCorrect1 = isKurangDari

# ---------5+++++++++
# Lebih dari 5
isLebihDari = inputUser > 5
print("Lebih dari 5 =", isLebihDari)

# +++++++++8---------
# Kurang dari 8
isKurangDari = inputUser < 8
print("Kurang dari 8 =", isKurangDari)
isCorrect2 = isLebihDari and isKurangDari

# ---------11++++++++++
# Lebih dari 11
isLebihDari = inputUser > 11
print("Lebih dari 11 =", isLebihDari)
isCorrect3 = isLebihDari

isCorrectHasil = isCorrect1 or isCorrect2 or isCorrect3
print("angka yang anda masukkan:", isCorrectHasil)