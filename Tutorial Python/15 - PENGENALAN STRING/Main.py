data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# Membuat tanda ' menjadi string
print('mari sholat jum\'at')
print('g\'day, isn\'t it?')

# backlash 
print("C:\\user\\Suheb") # \ tambah 1 biar \ menjadi string

# tab
print("ucup\t\t\totong, jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.") # LF --> line feed --> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR --> carriage return --> comodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") #CRLF --> line feed carriage return --> dipakai oleh windows

# 3. String literal atau raw

# hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Suheb
Kelas : 1 SD
""")

# multiline literal string dan RAW
print(r"""
Nama : Suheb
Kelas : 0 SD\new normal
Website : www.suheb.com/newID
""")