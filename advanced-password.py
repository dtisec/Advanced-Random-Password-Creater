import random
Karakterler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
 
sifre_karakter = int(input("Şifre kaç karakterden oluşturulsun : "))
sifre_adet = int(input("Kaç adet şifre oluşturulsun : "))
for x in range(0, sifre_adet):
        password = ""
        for x in range(0, sifre_karakter):
            password_char = random.choice(Karakterler)
            password      = password + password_char
        print("Random Şifreniz : " , password)
 
