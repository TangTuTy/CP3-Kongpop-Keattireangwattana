pricelist = []
menulist =[]

def showbill():
    sumprice = 0
    print("----my food----")
    for number in range(len(menulist)):
        print(menulist[number],pricelist[number])
        sumprice =int(pricelist[number])+sumprice
    print("ราคารวม" ,sumprice, "THB")

while True:
    Menuname = input("กรุณาใส่ชื่ออาหาร : ")
    if(Menuname.lower() == "exit"):
        break
    else:
        Menuprice = int(input("ราคา : "))
        menulist.append(Menuname)
        pricelist.append(Menuprice)


showbill()

