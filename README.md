# Golge128 — Gölge (Shadow) Şifreleme

Bu depo, eğitim amaçlı hazırlanmış `Golge128_Sifreleme.py` Python script'ini içerir. Küçük, anlaşılır bir örnek olarak gölge tabanlı şifreleme/simülasyon mantığını gösterir.

**Özeti**
- Dil: Python
- Ana dosya: `Golge128_Sifreleme.py`

**Özellikler**
- Basit ve okunabilir örnek uygulama.
- Çalıştırma çıktısı örneği görseli: `code.jpeg` (README'de gösterilmektedir).

**Gereksinimler**
- Python 3.8 veya üzeri
- (Görsel oluşturma için) `Pillow` kütüphanesi — isteğe bağlı

**Kurulum (kısa)**
1. Ortam oluşturun (isteğe bağlı):

```bash
python -m venv .venv
source .venv/bin/activate   # Windows PowerShell: .\.venv\Scripts\Activate.ps1
```

2. (Görsel oluşturmak isterseniz) bağımlılığı yükleyin:

```bash
pip install pillow
```

**Çalıştırma**

- Sadece script'i çalıştırmak için:

```bash
python Golge128_Sifreleme.py
```

- README'de gösterilen örnek görseli oluşturmak için (`generate_code_image.py` kullanılabilir):

```bash
python generate_code_image.py
```

**Örnek ekran görüntüsü**

![Program çıktısı](code.jpeg)

**Dosya listesi**
- `Golge128_Sifreleme.py` — ana uygulama
- `generate_code_image.py` — README için örnek görsel oluşturucu
- `.gitignore` — yaygın gereksiz dosyalar

---

**Katkıda bulunma**
1. Fork yapın
2. Yeni bir branch oluşturun (`git checkout -b feature-isim`)
3. Değişiklikleri commit edin
4. Pull request gönderin

**Lisans**
- Bu depo örnek/eğitim amaçlıdır; özel lisans yoksa lütfen sahibine danışın veya bir lisans ekleyin.

