import random
#Öğrenci ve öğretmen otomasyon sistemi
#Öğretmen şifresi : 123456
class Okul:
    def __init__(self,isim):
        self.isim = isim
    
    class Ogrenci:
        def __init__(self,isim,soyisim,no,sinif,disiplin_puani,ders = {"Turkce":0,"Matematik":0 }):
            self.isim = isim
            self.soyisim = soyisim
            self.no = no
            self.sinif = sinif
            self.disiplin_puani = disiplin_puani
            self.ders = ders 
            
        def disiplin(self):
            disiplin = input("Ogrenci disipline gitti mi? (e-evet h-hayir) : ")
            
            if (disiplin == 'e'):
                self.disiplin_puani-= 10
                
                if (self.disiplin_puani <= 0):
                    print("Ogrencinin kaydi silindi...")
                    self.isim = None
                    self.soyisim = None
                    self.no = None
                    self.sinif = None
                    self.disiplin_puani = None
                
                else:
                    print("Ogrencinin puani 10 puan düşürüldü! Yeni puan :",self.disiplin_puani)
            
            elif(disiplin != 'e'):
                print("Mesgul etme...")
                
        def goruntule(self):
            print("""
                  İsim = {}
                  Soyisim = {}
                  No = {}
                  Sinif = {}
                  Disiplin_puani = {}
                                   
                  """.format(self.isim,self.soyisim,self.no,self.sinif,self.disiplin_puani))
            
        def puan_degistir(self):
            girdi = input("Lutfen puan degistirmek istediginiz dersi giriniz('Turkce' ya da 'Matematik' :")
            
            if girdi == "Turkce":
                self.ders["Turkce"] = int(input("Lutfen puan giriniz: "))
                
                if 0 <= self.ders["Turkce"] <= 100:
                    print("Basarili bir sekilde puan degistirildi. Turkce puaniniz :",self.ders["Turkce"])
                    
                else : 
                    print("Puaniniz degismedi!")
                    self.ders["Turkce"] = 0
            elif girdi == "Matematik":               
                self.ders["Matematik"] = int(input("Lutfen puan giriniz: "))
                
                if 0 <= self.ders["Matematik"] <= 100:
                    print("Basarili bir sekilde puan degistirildi. Matematik puaniniz :",self.ders["Matematik"])
                    
                else : 
                    print("Puaniniz degismedi!")
                    self.ders["Matematik"] = 0
            
            else:
                print("Boyle bir ders yok...")
                
        def puan_goruntule(self):
            print("""
                  Turkce notunuz : {}
                  Matematik notunuz : {}                  
                  """.format(self.ders["Turkce"], self.ders["Matematik"]))
            
        def hoca_yakaladi(self):
            sayi = random.randint(1,2)
            
            if sayi == 1 :
                print("Hoca yakaladi...")
                self.disiplin_puani -= 5
            
            elif sayi == 2:
                print("Yanlis alarm!")
    
    class Ogretmen:
        def __init__(self,isim,soyisim,sifre):
            self.isim = isim
            self.soyisim = soyisim
            self.sifre = sifre  
            
        def ogretmen_bilgi(self):
            print("""
                  İsim : {}
                  Soyisim : {}               
                  """.format(self.isim,self.soyisim))


ogrenci1 = Okul.Ogrenci("Dorukan","Aydin",1,"12-A",50)
ogretmen1 = Okul.Ogretmen("Ali","Yilmaz",123456)
okul1 = Okul("Mustafa Kemal Atatürk Okulu")

while True :
    print("""\nSevgili {} sakinleri,okulumuza hosgeldiniz.
          """.format(okul1.isim))
    
    islem = int(input("Ogrenci islemleri icin 1'e , Ogretmen islemleri icin 2'ye , Cıkmak icin 3'e basiniz : "))
    
    match islem :
        case 1:
            print("Ogrenci sistemine girdiniz.\n")
            islem2 = int(input("Puan goruntulemek icin 1'e , Ogrenci bilgilerinizi goruntulemek icin 2'ye basiniz : "))
            
            if islem2 == 1:
                if ogrenci1.disiplin_puani == None:
                    pass
                
                else:
                    ogrenci1.puan_goruntule()
            
            elif islem2 == 2:
                ogrenci1.goruntule()
                
            else:
                print("Yanlis deger girdiniz. Sistemi mesgul ettiginiz icin görevli ogretmene bilgi verildi...")
                ogrenci1.hoca_yakaladi()
        
        case 2:
            print("Ogretmen bilgi sistemindesiniz.")
            islem3 = int(input("""
                           Disiplin icin '1',
                           Ders notu icin '2',
                           Ogretmen bilgisi icin '3' tusuna basiniz :  """))
            if islem3 == 1:
                sifre = int(input("Lutfen sifrenizi giriniz :"))
                
                if sifre == ogretmen1.sifre:
                    ogrenci1.disiplin()
                
                elif sifre != ogretmen1.sifre:
                    print("Yanlis sifre girdiniz! Gorevli ogretmene bilgi verildi...")
                    ogrenci1.hoca_yakaladi()
                    
            if islem3 == 2:
                sifre = int(input("Lutfen sifrenizi giriniz :"))
                
                if sifre == ogretmen1.sifre:
                    if ogrenci1.disiplin_puani == None:
                        pass
                    
                    else:
                        ogrenci1.puan_degistir()
                
                elif sifre != ogretmen1.sifre:
                    print("Yanlis sifre girdiniz! Gorevli ogretmene bilgi verildi...")
                    ogrenci1.hoca_yakaladi()
            
            if islem3 == 3:
                ogretmen1.ogretmen_bilgi()
                
        case 3:
            break
                    

