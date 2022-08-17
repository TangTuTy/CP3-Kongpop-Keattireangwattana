def Login():
    UsernameInput = input("Username : ")
    PasswordInput = input("Password : ")
    if UsernameInput == "admin" and PasswordInput == "1234":
        return showmenu()
    else:
        print("Try Again")
        return Login()
def showmenu():
    print("----Tang shop----")
    print("1. Vat Calcu")
    print("2. Price Calcu")
    menuselect()
def menuselect():
    Userselcted = int(input("กรุณาเลือก1หรือ2 : "))
    if Userselcted == 1:
       return vatCalculator()
    elif Userselcted == 2:
       return priceCalculator()
    else :
        print("Choose 1 or 2 only")
        menuselect()

def vatCalculator():
    totalPrice = int(input("ใส่ราคาสินค้า : "))
    vat = 7
    result = totalPrice + ((totalPrice * vat) / 100)
    print("ราคาสินค้า + vat = "+str(result),"THB")
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalPrice = price1+price2
    result = totalPrice + ((totalPrice * 7) / 100)
    print(result, "THB")

Login()
print("ขอบคุณง้าบบบ")