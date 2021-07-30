# latihan konversi satuan temprature

## program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukkan suhu dalam celcius : "))
print("suhu adalah",celcius,"Celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur,"Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah",fahrenheit,"Fahrenheit")

# kelvin
kelvin = celcius + 273.15
print("suhu dalam kelvin adalah",kelvin,"Kelvin")

## PR KAWAN

fahrenheit = float(input("Masukkan suhu dalam fahrenheit : "))
print("suhu adalah",fahrenheit,"Fahrenheit")

kelvin = ((fahrenheit - 32) * (5/9)) + 273.15
print("suhu dalam kelvin adalah",kelvin,"Kelvin")

kelvin = float(input("Masukkan suhu dalam kelvin : "))
print("suhu adalah",kelvin,"Kelvin")

fahrenheit = ((kelvin - 273.15) * (9/5)) + 32
print("suhu dalam fahrenheit adalah",fahrenheit,"Fahrenheit")

