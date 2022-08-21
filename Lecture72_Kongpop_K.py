
menulist =[]

def showbill():
    sumprice = 0
    print("----my food----")
    for number in range(len(menulist)):
        print(menulist[number])
        sumprice =(int(menulist[number][1]))+sumprice
    print("ราคารวม" ,sumprice, "THBBB")

while True:
    Menuname = input("กรุณาใส่ชื่ออาหาร : ")
    if(Menuname.lower() == "exit"):
        break
    else:
        Menuprice = int(input("ราคา : "))
        menulist.append([Menuname,Menuprice])
showbill()


