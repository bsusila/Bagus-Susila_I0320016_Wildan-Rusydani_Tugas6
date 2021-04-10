# menghitung nilai rata-rata
n = int(input("Jumlah data :"))
nilai = []
angka = 0

for i in range(0,n):
    j = int(input("Masukkan nilai ke-%d:" %(i+1)))
    nilai.append(j)
    angka += nilai[i]
    rata_rata = angka / n
print("Nilai rata-ratanya adalah %0.2f" %rata_rata)