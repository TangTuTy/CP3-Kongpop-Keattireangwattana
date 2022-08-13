Username = input("Username :")
Password = input("Password :")
if Username == "kongpop" and Password == "1234":
    print("Product List")
    print("Welcome to RELX Tang Shop !!")
    print("1.เคียวโฮ       : x 130  THB")
    print("2.หลงชา        : x 120  THB")
    print("3.แตงโม        : x 120  THB")
    print("4.Red Wind     : X 150 THB")
    ProductSelected = int(input("กรุณาเลือกสินค้าที่ต้องการ :"))
    if ProductSelected == 1:
        Productname = "เคียวโฮ"
        ProductPrice = "130"
    elif ProductSelected == 2:
        Productname = "หลงชา"
        ProductPrice = "120"
    elif ProductSelected == 3:
        Productname = "แตงโม"
        ProductPrice = "120"
    elif ProductSelected == 4:
        Productname = "Red Wind"
        ProductPrice = "150"

    print("สินค้าที่คุณเลือก",Productname,ProductPrice,"THB")
    Price = int(input("คุณต้องการจำนวนเท่าไหร่"))
    print(Productname,"x",Price,"ราคารวมทั้งสิ้น :", float(Price)*float(ProductPrice), "THB")
else :
    print("PassWord Error !!")
print("THX To RELX Tang Shop")




