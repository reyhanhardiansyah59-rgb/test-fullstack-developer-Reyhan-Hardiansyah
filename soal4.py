def kombinasi(angka , target):
    ditemukan = set()
    hasil = []

    for nilai in angka:
        pasangan_angka = target - nilai

        if pasangan_angka in ditemukan :
            hasil.append([pasangan_angka, nilai])
    
        ditemukan.add(nilai)
    return hasil

angka = [1,2,3,4,5]
target = 6

hasil=kombinasi(angka,target)
print(hasil)