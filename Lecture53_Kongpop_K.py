def vatcal(ราคาสินค้า):
    result = ราคาสินค้า+(ราคาสินค้า*7/100)
    return result
ราคาสินค้า = int(input("ราคาสินค้า :"))

print(vatcal(ราคาสินค้า))
