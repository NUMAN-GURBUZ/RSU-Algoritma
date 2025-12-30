# GÖLGE-128: Kriptografik Algoritma Geliştirme Projesi

Bu proje, **Bilgi Sistemleri Güvenliği (BSG)** dersi kapsamında verilen "Kriptografik Algoritma Geliştirme ve Analizi" deney föyü doğrultusunda hazırlanmıştır.

## Proje Amacı
Temel kriptografik prensipleri (ikame, permütasyon, yayılma, karıştırma) kullanarak basit ama özgün bir şifreleme algoritması tasarlamak, kodlamak ve analiz etmektir.

## Süreç ve Aşamalar
Proje 3 haftalık (3 aşamalı) bir süreci kapsamaktadır:

### Aşama 1: Algoritma Tasarımı
*   **Tarih:** 12.12.25
*   **İçerik:** SPN mimarisine dayalı **GÖLGE-128** algoritmasının kağıt üzerinde tasarlanması.
*   **Teslim:** [BSG-Proje-Raporu.md](BSG-Proje-Raporu.md) içerisinde Algoritma Adı, Felsefesi, Akış Şeması ve Matematiksel Modeli sunulmuştur.

### Aşama 2: Kodlama
*   **Tarih:** 19.12.25
*   **İçerik:** Tasarlanan algoritmanın Python dilinde kodlanması.
*   **Dosya:** `Golge128_Sifreleme.py`
*   **Gereksinimler:**
    *   `Anahtar_Uret(parola)`
    *   `Sifrele(duz_metin, anahtar)`
    *   `Desifrele(sifreli_metin, anahtar)`

### Aşama 3: Analiz ve Kırılma (Planlanan)
*   Algoritmanın zayıf yönlerinin akranlar tarafından analiz edilmesi aşamasıdır.

## Kurulum ve Çalıştırma

1. Python 3.8+ yüklü olduğundan emin olun.
2. Aşağıdaki komutu çalıştırarak testleri başlatın:

```bash
python Golge128_Sifreleme.py
```

## Test Sonuçları
Program çalıştırıldığında iki temel test senaryosunu doğrular:
1. **Basit Doğrulama:** Metnin şifrelenip tekrar açıldığında bozulmadığını kanıtlar.
2. **Anahtar Hassasiyeti (Çığ Etkisi):** Anahtarın tek bir biti değiştiğinde sonucun tamamen değiştiğini kanıtlar.
