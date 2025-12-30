# 3.3 Analiz Raporu

**Tarih:** 26.12.2025
**Analiz Eden:** [Adınız Soyadınız]

### Hedef Algoritma
**Adı:** Kale-128 (Castle-128)
**Tasarımı:** 128-bit blok ve anahtar boyutuna sahip, 10 turlu SPN (Substitution-Permutation Network) mimarisi. Şifreleme süreci Anahtar Karıştırma, İkame (Matematiksel S-Box) ve Permütasyon (ShiftRows) katmanlarından oluşmaktadır.

### Saldırı Yöntemi
**Yöntem:** Brute Force (Kaba Kuvvet / Sözlük Saldırısı).
**Seçilme Nedeni:** Algoritma matematiksel olarak karmaşık olsa da, uygulamanın kullandığı anahtar uzayının (parola politikasının) "4 haneli sayısal PIN" (0000-9999) olduğu tespit edilmiştir. 10.000 gibi çok küçük bir ihtimal havuzu olduğu için en garanti yöntem olan tüm ihtimalleri deneme yolu seçilmiştir.

### Adım Adım Analiz
1.  **Hazırlık:** Şifrelenmiş hedef veri (meydan okuma mesajı) ele geçirildi.
2.  **Araç Geliştirme:** Python dilinde `Kale128_Saldiri.py` adında bir script yazıldı.
3.  **Saldırı Süreci:** Script, `0000`'dan `9999`'a kadar olan tüm sayıları sırayla denedi.
4.  **Kontrol:** Her denemede üretilen anahtarla şifreli metin çözüldü ve sonucun anlamlı bir metin olup olmadığı ("Tebrikler" kelimesi içeriyor mu?) kontrol edildi.

### Sonuç ve Zafiyetler
*   **Durum:** **KIRILDI.**
*   **Sonuç:** Yaklaşık 0.18 saniye içinde doğru anahtar **"2024"** olarak bulundu ve şifreli metin **"TebriklerKirdin!"** olarak çözüldü.
*   **Temel Zafiyet:** Algoritmanın şifreleme mantığında (matematiksel işlemlerinde) değil, **anahtar yönetimi politikasında** zafiyet vardır. Kullanıcının sadece 4 rakamdan oluşan bir şifre belirlemesine izin verilmesi, anahtar uzayını güvensiz seviyede küçültmüş ve sistemin saniyeler içinde kırılmasına neden olmuştur.
