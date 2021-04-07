import hashlib
import os
os.system("figlet HANEDAN-I ROOT | lolcat && echo @nethunterROM | lolcat -p 0.4 -a -d 200 -s 150")
print ("HÂNEDAN-I ROOT ŞİFRELEYİCİ")
print ("MD5 ŞİFRELEME İÇİN= 1")
print ("SHA256 ŞİFRELEME İÇİN= 2")
while True:
    a=int(input("Seçiminizi yapınız:"))
    if a==1:
                print("MD5 ŞİFRELEME")
                m=input('Lütfen şifrenizi giriniz:')
                md5=hashlib.md5(m.encode('utf8')).hexdigest()
                print("MD5 ŞİFRENİZ:", md5)
                exit()
    if a==2:
        print("SHA256 ŞİFRELEME")
        s=input("Lütfen şifrenizi giriniz:")
        sha256=hashlib.sha256(s.encode('utf-8')).hexdigest()
        print("SHA256 ŞİFRENİZ:", sha256)
        exit()

    else:
        print("Lütfen HÂNEDAN-I ROOT'a yakışır bir seçim yapınız.")
#@nethunterROM
#Tüm hakları m12345'e aittir.
