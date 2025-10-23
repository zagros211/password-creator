import random
import string

def sifre_olustur():
    """
    Kullanıcının tercihlerine göre güvenli şifre oluşturur.
    """
    print("=" * 50)
    print("GELİŞMİŞ ŞİFRE OLUŞTURUCU")
    print("=" * 50)
    
    # Karakter havuzlarını tanımla
    kucuk_harfler = string.ascii_lowercase
    buyuk_harfler = string.ascii_uppercase
    sayilar = string.digits
    ozel_karakterler = string.punctuation
    
    # Kullanıcıdan şifre uzunluğunu al
    try:
        uzunluk = int(input("\nŞifre kaç karakter olsun? (minimum 6, maximum 16): "))
        if uzunluk < 6:
            print("Hata: Şifre en az 6 karakter olmalıdır!")
            return None
        if uzunluk > 16:
            print("Hata: Şifre en fazla 16 karakter olabilir!")
            return None
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin!")
        return None
    
    # Kaç tane şifre oluşturulacak
    MAX_SIFRE_SAYISI = 50
    try:
        sifre_sayisi = int(input(f"Kaç tane şifre oluşturmak istersiniz? (maximum {MAX_SIFRE_SAYISI}): "))
        if sifre_sayisi < 1:
            print("Hata: En az 1 şifre oluşturmalısınız!")
            return None
        if sifre_sayisi > MAX_SIFRE_SAYISI:
            print(f"Hata: En fazla {MAX_SIFRE_SAYISI} şifre oluşturabilirsiniz!")
            return None
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin!")
        return None
    
    # Hangi karakterleri kullanacağız?
    print("\n--- KARAKTER TİPLERİ ---")
    karakter_havuzu = ""
    
    kucuk_kullan = input("Küçük harfler (a-z) kullanılsın mı? (e/h): ").lower() == 'e'
    if kucuk_kullan:
        karakter_havuzu += kucuk_harfler
    
    buyuk_kullan = input("Büyük harfler (A-Z) kullanılsın mı? (e/h): ").lower() == 'e'
    if buyuk_kullan:
        karakter_havuzu += buyuk_harfler
    
    sayi_kullan = input("Sayılar (0-9) kullanılsın mı? (e/h): ").lower() == 'e'
    if sayi_kullan:
        karakter_havuzu += sayilar
    
    ozel_kullan = input("Özel karakterler (!@#$%...) kullanılsın mı? (e/h): ").lower() == 'e'
    if ozel_kullan:
        karakter_havuzu += ozel_karakterler
    
    if not karakter_havuzu:
        print("\nHata: En az bir karakter tipi seçmelisiniz!")
        return None
    
    print("\n--- BAŞLANGIÇ VE BİTİŞ KARAKTERİ ---")
    print(f"Kullanılabilir karakterler: {karakter_havuzu[:50]}...")
    
    baslangic = input("\nŞifre hangi karakterle BAŞLASIN? (boş bırak = rastgele): ").strip()
    
    if baslangic:
        if len(baslangic) > 1:
            print("Uyarı: Sadece ilk karakter kullanılacak.")
            baslangic = baslangic[0]
        
        if baslangic not in karakter_havuzu:
            print(f"Hata: '{baslangic}' seçili karakter tiplerinde yok!")
            print("Lütfen seçtiğiniz karakter tiplerinden birini kullanın.")
            return None
    
    bitis = input("Şifre hangi karakterle BİTSİN? (boş bırak = rastgele): ").strip()
    
    if bitis:
        if len(bitis) > 1:
            print("Uyarı: Sadece ilk karakter kullanılacak.")
            bitis = bitis[0]
        
        if bitis not in karakter_havuzu:
            print(f"Hata: '{bitis}' seçili karakter tiplerinde yok!")
            print("Lütfen seçtiğiniz karakter tiplerinden birini kullanın.")
            return None
    
    min_uzunluk = (1 if baslangic else 0) + (1 if bitis else 0)
    if uzunluk < min_uzunluk:
        print(f"\nHata: Başlangıç ve bitiş karakteri için şifre en az {min_uzunluk} karakter olmalıdır!")
        return None
    
    sifreler = []
    for i in range(sifre_sayisi):
        sifre = []
        
        temp_uzunluk = uzunluk
        if baslangic:
            sifre.append(baslangic)
            temp_uzunluk -= 1
        
        if bitis:
            temp_uzunluk -= 1
        
        for _ in range(temp_uzunluk):
            sifre.append(random.choice(karakter_havuzu))
        
        if bitis:
            sifre.append(bitis)
        
        sifre_son = ''.join(sifre)
        sifreler.append(sifre_son)
    
    print("\n" + "=" * 50)
    print(f"✓ OLUŞTURULAN {len(sifreler)} ŞİFRE:")
    print("=" * 50)
    
    for idx, sifre in enumerate(sifreler, 1):
        print(f"{idx:2d}. {sifre}")
    
    print("\n" + "=" * 50)
    print(f"Şifre Uzunluğu: {len(sifreler[0])} karakter")
    
    if baslangic and bitis:
        print(f"Başlangıç: '{baslangic}' | Bitiş: '{bitis}'")
    elif baslangic:
        print(f"Başlangıç: '{baslangic}' | Bitiş: Rastgele")
    elif bitis:
        print(f"Başlangıç: Rastgele | Bitiş: '{bitis}'")
    else:
        print("Başlangıç ve Bitiş: Rastgele")
    
    guc_skoru = 0
    if kucuk_kullan: guc_skoru += 1
    if buyuk_kullan: guc_skoru += 1
    if sayi_kullan: guc_skoru += 1
    if ozel_kullan: guc_skoru += 1
    
    print("\n--- GÜVENLİK ANALİZİ ---")
    if len(sifre_son) >= 12 and guc_skoru >= 3:
        print("Şifre Gücü: ⭐⭐⭐ ÇOK GÜÇLÜ ✓")
    elif len(sifre_son) >= 8 and guc_skoru >= 2:
        print("Şifre Gücü: ⭐⭐ GÜÇLÜ")
    else:
        print("Şifre Gücü: ⭐ ZAYIF (Daha uzun ve karışık şifre önerilir)")
    
    print("=" * 50)


def coklu_sifre_olustur():
    """
    Birden fazla şifre oluşturur.
    """
    while True:
        sifre_olustur()
        
        devam = input("\nBaşka bir şifre oluşturmak ister misiniz? (e/h): ").lower()
        if devam != 'e':
            print("\n" + "=" * 50)
            print("Program sonlandırılıyor. Güvenli günler! 🔐")
            print("=" * 50)
            break
        print("\n")


# Programı çalıştır
if __name__ == "__main__":
    coklu_sifre_olustur()