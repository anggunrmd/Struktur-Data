import pandas as pd

# Baca file Excel, ambil header dari baris pertama
df = pd.read_excel('data.xlsx', engine='openpyxl', header=0)

# Ambil hanya kolom yang diperlukan
data = df[['NIM', 'Nama Mahasiswa', 'Judul Paper', 'Tahun Terbit', 'Nama Penulis', 'Link Paper', 'Abstrak (langusung copas dari paper)']].dropna()
data['Tahun Terbit'] = data['Tahun Terbit'].astype(int)
dataset = data.to_dict(orient='records')

# Linear Search
def linear_search(data, key, value):
    results = []
    value = value.strip().lower()  # Membersihkan input
    for item in data:
        if value in str(item[key]).lower():  # Mencocokkan substring
            results.append(item)
    return results

# Binary Search (harus diurutkan dulu)
def binary_search(data, key, value):
    sorted_data = sorted(data, key=lambda x: x[key])
    low, high = 0, len(sorted_data) - 1
    results = []

    while low <= high:
        mid = (low + high) // 2
        mid_val = sorted_data[mid][key]
        search_val = value

        if mid_val == search_val:
            i = mid
            while i >= 0 and sorted_data[i][key] == search_val:
                results.append(sorted_data[i])
                i -= 1
            i = mid + 1
            while i < len(sorted_data) and sorted_data[i][key] == search_val:
                results.append(sorted_data[i])
                i += 1
            break
        elif search_val < mid_val:
            high = mid - 1
        else:
            low = mid + 1
    return results

# ===== INTERAKTIF DIMULAI =====
print("Pilih metode pencarian:")
print("1. Linear Search")
print("2. Binary Search")
metode = input("Masukkan pilihan (1/2): ")

if metode == '1':
    print("\nPilih pencarian berdasarkan:")
    print("1. Judul Paper")
    print("2. Tahun Terbit")
    print("3. Nama Penulis")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == '1':
        kolom = 'Judul Paper'
    elif pilihan == '2':
        kolom = 'Tahun Terbit'
    elif pilihan == '3':
        kolom = 'Nama Penulis'
    else:
        print("Pilihan tidak valid.")
        exit()

    nilai = input(f"Masukkan {kolom}: ")
    hasil = linear_search(dataset, kolom, nilai)

elif metode == '2':
    kolom = 'Tahun Terbit'
    nilai = int(input("Masukkan Tahun Terbit: "))
    hasil = binary_search(dataset, kolom, nilai)

else:
    print("Metode tidak valid.")
    exit()

# Tampilkan hasil
if hasil:
    print(f"\nDitemukan {len(hasil)} hasil:")
    for item in hasil:
        print(f"NIM\t\t: {item['NIM']}")
        print(f"Nama Mahasiswa\t: {item['Nama Mahasiswa']}")
        print(f"Judul Paper\t: {item['Judul Paper']}")
        print(f"Tahun Terbit\t: {item['Tahun Terbit']}")
        print(f"Nama Penulis\t: {item['Nama Penulis']}")
        print(f"Link Paper\t: {item['Link Paper']}")
        print(f"Abstrak\t\t: {item['Abstrak (langusung copas dari paper)']}")
        print("============================================================")
else:
    print("\nData tidak ditemukan.")