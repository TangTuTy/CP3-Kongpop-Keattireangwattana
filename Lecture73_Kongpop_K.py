systemmenu = {"ไก่":30,"หมู":40,"หมึก":50,"กุ้ง":45}
menulist =[]

def showbill():
    sumprice = 0
    print("----my food----")
    for number in range(len(menulist)):
        print(menulist[number][0],menulist[number][1])
        sumprice =(int(menulist[number][1]))+sumprice
    print("ราคารวม" ,sumprice, "THB")

while True:
    Menuname = input("กรุณาใส่ชื่ออาหาร : ")
    if(Menuname.lower() == "exit"):
        break
    else:
        menulist.append([Menuname,systemmenu[Menuname]])
showbill()