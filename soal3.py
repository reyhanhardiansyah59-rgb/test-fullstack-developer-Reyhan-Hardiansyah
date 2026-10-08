def discount(harga, barang):
    if barang == "gold":
        return harga * 0.8
    elif barang == "silver":
        return harga * 0.9
    else:
        return harga
print(discount(10000, "gold"))
print(discount(9000, "silver"))
print(discount(8000, "anyone"))