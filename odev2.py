#öğrenci ekleme sistemimizin ana konsolunu oluşturuyoruz

def konsol():
    print("Öğrenci kayıt sistemine hoşgeldiniz, lütfen bir işlem seçiniz ")
    print("1 - Öğrenci Ekle")
    print("2 - Birden Fazla Öğrenci Ekle")
    print("3 - Öğrencileri Listele")
    print("4 - Öğrenci Numaralarını gör")
    print("5 - Öğrenci Sil")
    print("6 - Birden Fazla Öğrenci Sil")
    print("7 - Çıkış")
    giris = int(input())

    if giris == 1:
        return 1
    elif giris == 2:
        return 2
    elif giris == 3:
        return 3 
    elif giris == 4:
        return 4 
    elif giris == 5:
        return 5
    elif giris == 6:
        return 6
    elif giris == 7:
        return 7
    
def fazladanEkleme():
    ogrenci = []
    print("Eklemek istediğiniz öğrenci sayısını giriniz:  ")
    sayi = int(input())
    for i in range(sayi):
        print(i + 1,". Öğrenciyi Giriniz")
        ogrenci.append(input())
        i += 1
    return ogrenci

def OgrenciNum():
    print("\n")
    for i in range(len(ogrenci)):
        std = str(ogrenci[i])
        print(f"Öğrenci: {ogrenci[i]} \t Numarası: {ogrenci.index(std)}")
    print("\n")

def fazladanSilme():
    silinen = []
    print("\n")
    i = 0
    while i < len(ogrenci):
        std = str(ogrenci[i])
        print(f"Öğrenci: {ogrenci[i]} \t Numarası: {ogrenci.index(std)}")
        i += 1
    print("Silmek istediğiniz öğrenci sayısını giriniz:")

    silinenDeger = int(input()) 
    i = 0
    while i < silinenDeger:
        print(f"{i + 1}. Silmek istediğiniz öğrencinin ismini giriniz")
         
        silinen = input()
        j = 0
        while j < len(ogrenci):         
            if silinen == ogrenci[j]:
                ogrenci.pop(j)
                break
            elif silinen != ogrenci[j]:
                print("Öğrenci bulunamadı!")
            j += 1        
        i += 1

    
    print("\n")

    
    


ogrenci = []

while True:
    print("Lüfen Yapmak İstediğiniz İşlemi Seçiniz")
    konsolKomut = int(konsol())


    
    #ekleme işlemleri

    if konsolKomut == 1:
        ogrenci.append(input("Lütfen Eklemek İstediğiniz Öğrencinin Adı ve Soyadını Giriniz : "))
        if True:
            print("\nÖğrenci Eklendi\n")
 


    #Fazla sayıda öğrenci eklenme
    elif konsolKomut == 2:
        ogrenci = [fazladanEkleme()]
        for i in range(len(ogrenci)):
            ekleme = ogrenci[i]
            ogrenci.extend(ekleme)
            i += 1
        print(ogrenci)
    
    #Öğrencileri listeleme
    elif konsolKomut == 3:
        print("\n")
        for i in range(len(ogrenci)):
            print(f"{i + 1}. Öğrenci = ",ogrenci[i])
            i += 1
        print("\n")


    #Öğrenci numaraları
    elif konsolKomut == 4:
        OgrenciNum()
    

    #Fazla değer silme
    elif konsolKomut == 5:
        print("Silmek İstediğin Öğrencinin İsim Ve Soyismini Giriniz")
        for i in range(len(ogrenci)):
            print("\t\t", i, ".", ogrenci[i])
            i += 1

        sil = input()
        print("\n")
        for x in range(len(ogrenci)):      
            if sil == ogrenci[x]:
                ogrenci.pop(x)
                print("Silme İşlemi Başarılı\n")
                break
            elif sil != ogrenci:
                print("Lütfen geçerli isim giriniz")
            x += 1

    
    elif konsolKomut == 6:
        fazladanSilme()

    # çıkış
    elif konsolKomut == 7:
        break






