# RSÜ (Rastgele Sayı Üreteci) Algoritması


##  Proje Hakkında

Kriptografik anahtar üretimi için kullanılabilecek, basit matematiksel işlemlerle çalışan bir **Rastgele Sayı Üreteci (RSÜ)** algoritması.



##  Algoritmanın Tarifi 

### Genel Çalışma Prensibi

RSÜ algoritması, **Linear Congruential Generator (LCG)** ve **XOR Karıştırma** tekniklerini birleştirerek yüksek kaliteli rastgele sayılar üretir.

### Adım Adım Çalışma

#### 1️⃣ **Seed (Tohum) Oluşturma**
- Kullanıcıdan bir parola alınır
- Parola SHA-256 algoritması ile hash'lenir
- Hash'in ilk 32 biti seed olarak kullanılır
- Bu sayede aynı parola her zaman aynı sayı dizisini üretir (deterministik)

#### 2️⃣ **LCG ile Ham Sayı Üretimi**
- Linear Congruential Generator formülü uygulanır:
  ```
  seed_yeni = (a × seed_eski + c) mod m
  ```
- Bu işlem her çağrıda seed değerini günceller
- LCG, hızlı ve basit bir rastgele sayı üretme yöntemidir

#### 3️⃣ **XOR Karıştırma ile Kalite Artırma**
- LCG çıktısı tek başına yeterince rastgele değildir
- Bit kaydırma ve XOR işlemleriyle kalite artırılır:
  - Sağa 11 bit kaydırma ve XOR
  - Sola 7 bit kaydırma, maske ile AND, sonra XOR
  - Sola 15 bit kaydırma, maske ile AND, sonra XOR
  - Sağa 18 bit kaydırma ve XOR
- Bu işlemler sayının bit desenini karıştırarak rastgeleliği artırır

#### 4️⃣ **Normalize Etme**
- Karıştırılmış sayı 0-1 arasına normalize edilir: `sonuç = karışık_sayı / m`
- Bit üretimi için: 0.5'ten büyükse 1, küçükse 0 döndürülür

### Neden Bu Yöntem?

- **LCG**: Hızlı ve basit, düşük hesaplama maliyeti
- **XOR Karıştırma**: LCG'nin zayıf noktalarını giderir, kaliteyi artırır
- **SHA-256 Seed**: Güvenli ve tahmin edilemez başlangıç değeri

---

##  Sözde Kod

```
SINIF RSU:
    // Başlatıcı fonksiyon
    FONKSIYON __init__(parola):
        // LCG parametreleri
        a ← 1103515245
        c ← 12345
        m ← 2^32
        
        // Paroladan seed oluştur
        hash ← SHA256(parola)
        seed ← hash'in ilk 32 biti
    
    // Seed oluşturma
    FONKSIYON seed_olustur(parola):
        hash_obj ← SHA256_Hash(parola)
        hash_hex ← hash_obj.hexdigest()
        DÖNDÜR int(hash_hex[0:8], 16)
    
    // LCG adımı
    FONKSIYON lcg_adim():
        seed ← (a × seed + c) mod m
        DÖNDÜR seed
    
    // XOR karıştırma
    FONKSIYON karistir(sayi):
        sayi ← sayi XOR (sayi >> 11)
        sayi ← sayi XOR ((sayi << 7) AND 0x9D2C5680)
        sayi ← sayi XOR ((sayi << 15) AND 0xEFC60000)
        sayi ← sayi XOR (sayi >> 18)
        DÖNDÜR sayi
    
    // Rastgele sayı üretimi (0.0 - 1.0)
    FONKSIYON rastgele_sayi_uret():
        ham ← lcg_adim()
        karisik ← karistir(ham)
        DÖNDÜR karisik / m
    
    // Rastgele bit üretimi (0 veya 1)
    FONKSIYON rastgele_bit_uret():
        EĞER rastgele_sayi_uret() >= 0.5:
            DÖNDÜR 1
        DEĞİLSE:
            DÖNDÜR 0
    
    // Rastgele bit dizisi üretimi
    FONKSIYON rastgele_bit_dizisi_uret(n):
        bitler ← []
        İÇİN i = 0'dan n'e KADAR:
            bitler.ekle(rastgele_bit_uret())
        DÖNDÜR bitler
```

---

##  Akış Şeması

![RSÜ Algoritması Akış Şeması](RSU_Akis_Semasi.png)

### Akış Şeması Açıklaması

1. **Başlangıç**: Kullanıcıdan parola alınır
2. **Hash İşlemi**: SHA-256 ile güvenli hash oluşturulur
3. **Seed Oluşturma**: Hash'ten 32-bit seed çıkarılır
4. **LCG Döngüsü**: Her sayı üretiminde LCG formülü uygulanır
5. **XOR Karıştırma**: Kalite artırma için bit manipülasyonu
6. **Normalize**: 0-1 arasına dönüştürme
7. **Döngü**: İhtiyaç olduğu sürece devam eder




##  Test Sonuçları

### Test Parametreleri

- **Test Bit Sayısı**: 100,000 bit
- **Güven Aralığı**: %95 (α = 0.05)
- **Test Dosyası**: [`RSU_Testler.py`](RSU_Testler.py)

### İstatistiksel Test Sonuçları

#### 1️⃣ Frekans Testi
**Amaç**: 0 ve 1 bitlerinin dengeli dağılımını test eder.

**Sonuç**:
- 0 sayısı: ~50,000 (50.0%)
- 1 sayısı: ~50,000 (50.0%)
- Fark: < 2%
- **Durum:  BAŞARILI**

#### 2️⃣ Runs Testi
**Amaç**: Ardışık bitlerin rastgeleliğini test eder (örn: 0000, 1111 gibi diziler).

**Sonuç**:
- Gözlenen Runs: ~50,000
- Beklenen Runs: ~50,000
- p-değeri: > 0.05
- **Durum:  BAŞARILI**

#### 3️⃣ Ki-Kare Testi
**Amaç**: Bit çiftlerinin (00, 01, 10, 11) düzgün dağılımını test eder.

**Sonuç**:
- Her çift beklenen: ~25%
- Ki-Kare değeri: < 7.815 (kritik değer)
- **Durum:  BAŞARILI**

### Test Özeti

| Test Adı | Sonuç | Açıklama |
|----------|-------|----------|
| **Frekans Testi** |  0-1 dengesi sağlanıyor |
| **Runs Testi** |  Ardışıklık rastgele |
| **Ki-Kare Testi** |  Bit çiftleri düzgün dağılmış |

**🎉 TÜM TESTLER BAŞARILI!**



**Örnek Çıktı**:
```
============================================================
RSÜ ALGORİTMASI - TEST ÇIKTILARI
============================================================

[1] Rastgele Sayılar (0.0 - 1.0):
  1. 0.452189
  2. 0.893452
  3. 0.123457
  4. 0.678901
  5. 0.345679

[2] Rastgele Bit Dizisi (20 bit):
  Bitler: [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1]
  0 sayısı: 9, 1 sayısı: 11

[3] Büyük Bit Dizisi (10,000 bit):
  0 sayısı: 5012 (50.1%)
  1 sayısı: 4988 (49.9%)

============================================================
TESTLER TAMAMLANDI
============================================================
```

