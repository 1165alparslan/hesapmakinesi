### Hesap Makinesi

sayi1= int(input("İllk değeri giriniz."))
sayi2= int(input("İkinci değeri giriniz."))
islem= input("Toplama için 1, Çıkarma için 2, Çarpma için 3, Bölme için 4 ve Mod alma için 5 tuşuna basın.")

if (islem==1):
    print("Sonuç:", int(sayi1+sayi2))
elif (islem==2):
    print("Sonuç:", int(sayi1-sayi2))
elif (islem==3):
    print("Sonuç:", int(sayi1*sayi2))
elif (islem==4):
    print("Sonuç:", float(sayi1/sayi2))
elif (islem==5):
    if (sayi2>sayi1):
        print("Sonuç:", int(sayi2%sayi1))
    else:
        pass
    