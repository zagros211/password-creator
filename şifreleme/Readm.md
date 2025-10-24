
# Şifre Oluşturucu (password_creator.py)

Bu küçük Python betiği, kullanıcı tercihleri doğrultusunda güvenli ve rastgele şifreler oluşturur. Terminal üzerinden etkileşimli çalışır ve üretilen şifreleri ekrana yazdırır.

## Özellikler

- Şifre uzunluğu seçimi (6–16 karakter arası)
- Birden fazla şifre oluşturma (1–50 arası)
- Karakter tipi seçenekleri: küçük harf, büyük harf, rakam, özel karakter
- İsteğe bağlı başlangıç ve bitiş karakterleri
- Basit bir şifre güç analizi (zayıf/güçlü/çok güçlü)
- Döngüsel kullanım: "Başka bir şifre oluşturmak ister misiniz?" sorusuyla tekrar çalıştırma

## Gereksinimler

- Python 3.6 veya daha yeni bir sürüm (3.10/3.11 tavsiye edilir)
- Harici kütüphane gerektirmez; yalnızca standart kütüphaneler (`random`, `string`) kullanılır

## Nasıl çalıştırılır (Windows PowerShell)

1. PowerShell'i açın ve dosyanın bulunduğu klasöre gidin:

2. Betiği çalıştırın:
3. Program sizden etkileşimli olarak girdiler isteyecek. Sırasıyla:

- Şifre uzunluğu (6–16)
- Kaç adet şifre oluşturulacağı (1–50)
- Küçük/büyük harf, rakam ve özel karakter kullanılacak mı? (e/h)
- Opsiyonel: Şifrenin hangi karakterle başlamasını / bitmesini isteğiniz

Program, girdilerinize göre şifreleri oluşturup ekrana yazdırır.

## Örnek kullanım akışı

- Şifre kaç karakter olsun? 12
- Kaç tane şifre oluşturmak istersiniz? 5
- Küçük harfler (a-z) kullanılsın mı? e
- Büyük harfler (A-Z) kullanılsın mı? e
- Sayılar (0-9) kullanılsın mı? e
- Özel karakterler (!@#$%...) kullanılsın mı? h
- Şifre hangi karakterle BAŞLASIN? (boş bırak = rastgele): a
- Şifre hangi karakterle BİTSİN? (boş bırak = rastgele):

Çıktı: 5 adet, 12 karakter uzunluğunda, 'a' ile başlayan şifreler listelenecektir ve program size bir güç değerlendirmesi gösterecektir.

## Dikkat Edilmesi Gerekenler

- Minimum/maximum sınırlar betikte sabit olarak belirlenmiştir (uzunluk: 6–16, adet: 1–50).
- Başlangıç veya bitiş için girilen karakter, seçtiğiniz karakter tipleri arasında olmalıdır; değilse betik hata verip işlemi iptal eder.
- Hiçbir karakter tipi seçilmezse betik hata verir.

## Güvenlik Önerileri ve Geliştirme Fikirleri

- Mevcut sürüm `random.choice` kullanır; daha güçlü kriptografik rastgelelik için `secrets` modülünün (`secrets.choice`) kullanılması tavsiye edilir.
- Oluşturulan şifreleri dosyaya kaydetme veya panoya kopyalama özellikleri eklenebilir; bu tür özellikler eklenirken gizliliğe dikkat edin.
- Şifrelerin en az bir büyük/küçük/sayı/özel karakter içermesini zorunlu kılacak doğrulamalar eklenebilir.

## Sorun Giderme

- "Lütfen geçerli bir sayı girin!" hatası: sayı girişi beklenen yere harf/boş/uygun olmayan değer girmişsiniz. Geçerli bir tam sayı girin.
- "Hata: ... seçili karakter tiplerinde yok!" hatası: başlangıç/bitiş için seçtiğiniz karakter, etkin karakter havuzunda yok. Karakter tiplerinizi kontrol edin.
- "python: command not found" veya benzeri hatalar: Python sistem PATH'ine eklenmemiş olabilir; tam python yolunu kullanarak çalıştırın veya PATH'e ekleyin.
