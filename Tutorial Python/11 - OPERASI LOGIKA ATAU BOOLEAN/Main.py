# operasi logika atau boolean

# not, or, and, xor

# NOT (nilai kebalikan)
print("====NOT====")
a = True
c = not a
print("data a =",a)
print("----------NOT")
print("data c =",c)

# OR (jika salah satu True, maka hasilnya akan True)
print("====OR====")
a = False
b = False
c = a or b
print(a,"OR",b,"=",c)
a = False
b = True
c = a or b
print(a,"OR",b," =",c)
a = True
b = False
c = a or b
print(a," OR",b,"=",c)
a = True
b = True
c = a or b
print(a," OR",b," =",c)

# AND (akan True jika keduanya True)
print("====AND====")
a = False
b = False
c = a and b
print(a,"AND",b,"=",c)
a = False
b = True
c = a and b
print(a,"AND",b," =",c)
a = True
b = False
c = a and b
print(a," AND",b,"=",c)
a = True
b = True
c = a and b
print(a," AND",b," =",c)

# XOR (akan True jika salah satu True, sisanya False)
print("====XOR====")
a = False
b = False
c = a ^ b
print(a,"XOR",b,"=",c)
a = False
b = True
c = a ^ b
print(a,"XOR",b," =",c)
a = True
b = False
c = a ^ b
print(a," XOR",b,"=",c)
a = True
b = True
c = a ^ b
print(a," XOR",b," =",c)