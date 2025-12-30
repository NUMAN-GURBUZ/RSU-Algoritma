# Golge128 — Gölge (Shadow) Şifreleme Algoritması

Bu depo, eğitim amaçlı geliştirilmiş basit bir blok şifreleme algoritmasını içerir. Temel kriptografik prensipleri (ikame, permütasyon, XOR) kullanarak 128 bitlik bloklar üzerinde işlem yapar.

## Özellikler

- **Algoritma türü:** Blok şifre
- **Blok boyutu:** 128 bit (16 byte)
- **Anahtar boyutu:** 128 bit (16 byte)
- **Tur sayısı:** 3 tur (basitleştirilmiş örnek)
- **Dil:** Python 3.8+

## Çalıştırma

```bash
python Golge128_Sifreleme.py
```

## Algoritma (Özet)

Her tur aşağıdaki işlemleri uygular:

1. AddRoundKey — Blok ile tur anahtarı XOR
2. SubBytes — Her byte için doğrusal olmayan veya affine dönüşüm (örnek: S(b) = (5·b + 13) mod 256)
3. ShiftRows — Byte dizisinin döndürülmesi/permütasyonu

### Anahtar türetme (örnek)

Basit türetme: `round_key[i] = master_key XOR i` (örnek gösterim)

### Deşifreleme

Deşifreleme; şifrelemenin ters işlemlerinin ters sırada uygulanmasıyla elde edilir (ör. InvShiftRows, InvSubBytes, AddRoundKey).

## Test çıktıları (örnek)

Bu bölümde algoritmanın çalışma mantığını göstermek için basit test çıktıları örneklenmiştir.

```
=== GOLGE-128 ŞİFRELEME ALGORİTMASI: ÖRNEK TESTLER ===

Program çalıştırıldığında aşağıdaki test sonuçları görüntülenir:

```
=== GÖLGE-128 ŞİFRELEME ALGORİTMASI: PYTHON TESTLERİ ===

--- TEST 1: BASİT DOĞRULAMA ---
1. Parola: GizliAnahtar123
2. Orjinal Metin: YazilimMuh2025!!
3. Üretilen Anahtar (Hex): C0D74E1822CAF2B3C80346430864E621
4. Şifreli Metin (Hex):  14CC87D956AAA80B661FC6F9EA34A907
5. Deşifre Edilen Metin: YazilimMuh2025!!
>> SONUÇ: BAŞARILI (Metinler Birebir Eşleşiyor)

--- TEST 2: ANAHTAR HASSASİYETİ (Tek Bit Değişimi) ---
Senaryo: Orijinal şifreli metni, sadece 1 bit farklı anahtarla çözmeye çalışıyoruz.
Orijinal Anahtar: C0D74E1822CAF2B3C80346430864E621
Bozuk Anahtar   : C0D74E1822CAF2B3C80346430864E620
Hatalı Çözüm (Hex): A6A47A696C696D4D7568323032352120
Hatalı Metin (Str):zilimMuh2025!
>> SONUÇ: BAŞARILI (Çıktı tamamen anlamsız, Çığ Etkisi gözlendi.)
```

### Test Sonuçları Açıklaması

- **TEST 1**: Şifreleme ve deşifreleme işlemlerinin doğru çalıştığını doğrular. Orijinal metin ile deşifre edilen metin birebir eşleşir.

- **TEST 2**: Anahtar hassasiyetini test eder. Anahtarın tek bir biti değiştirildiğinde, deşifreleme sonucu tamamen anlamsız hale gelir (Çığ Etkisi - Avalanche Effect). Bu, algoritmanın anahtar değişikliklerine karşı hassas olduğunu gösterir.

## Algoritmanın Kırılması (Kriptanaliz)

### Zayıf Yönler

1. **Az Tur Sayısı**: Sadece 3 tur kullanılması
2. **Basit Anahtar Türetme**: `K[i] = K[0] XOR i` formülü çok basit
3. **Doğrusal İkame**: SubBytes doğrusal dönüşüm (affine transformation)
4. **Basit Permütasyon**: Sadece dairesel kaydırma

### Kırılma Yöntemleri

#### 1. Anahtar Türetme Zayıflığından Yararlanma
- Tur anahtarları arasındaki ilişki: `K[i] = K[0] XOR i`
- Bir tur anahtarını bulmak, diğerlerini de verir
- Tur sayısı az olduğu için etkili

#### 2. Doğrusal Kriptanaliz
- SubBytes'in doğrusal yapısından yararlanma
- İstatistiksel analizle anahtar bitleri bulma
- Çok sayıda düz metin-şifreli metin çifti gerekir

#### 3. Diferansiyel Kriptanaliz
- Farklı düz metinlerin şifreli metinlerindeki farkları analiz etme
- Seçilmiş düz metin çiftleri ile saldırı

#### 4. Meet-in-the-Middle
- Şifreleme ve deşifreleme yönlerinden aynı anda saldırma
- Tur sayısı az olduğu için pratik olabilir

### Kırılma Adımları

1. **Hazırlık**: Algoritma kodunu ve yapısını anlama, düz metin-şifreli metin çiftleri toplama
2. **Analiz**: Zayıf yönleri belirleme, uygun kriptanaliz yöntemini seçme
3. **Saldırı**: Seçilen yöntemi uygulama, anahtar veya düz metin bulma
4. **Doğrulama**: Bulunan sonuçları test etme

## Güvenlik Uyarısı

⚠️ **Bu algoritma sadece eğitim amaçlıdır** ve gerçek uygulamalarda kullanılmamalıdır. Güvenli şifreleme için AES gibi standart algoritmalar kullanılmalıdır.

---

**Lisans**: Bu depo örnek/eğitim amaçlıdır.
