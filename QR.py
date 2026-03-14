import qrcode
print("Select QR Type:")
print("1.wifi QR")
print("2.UPI payment QR")
print("3.watsaap qr")
choice=input("enter choice (1/2/3)")
if choice=="1":
    ssid=input("enter teh wifi name(SSID):")
    password=input("enter the password:")
    security=input("security type (WPA/WEP/none):").upper()
    if security=="NONE":
        security=""
    data=f"WIFI:{security};S:{ssid};P:{password};;"
elif choice=="2":
    upi_id =input("enter the upi id:")
    name=input("enter your name:")
    amount= input("enter the maount(optional,press enter to coninue):")
    note=input("enter note(optional):")
    data=f"upi://pay?pa={upi_id}&pn={name}"
    if amount:
        data+=f"&am={amount}"
    if note:
        data+=f"&tn={note}"
elif choice=="3":
    phone=input("enter phone number with country code(e.g. 1998999997):")
    data=f"https://wa.me/{phone}"
else:
    print("invalid choice")
    exit()
qr=qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4
    )
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="darkgreen",back_color="white").convert("RGB")
img.save("smart_qr.png")
print("QR cod egenerated saved as smart_qr.png")
