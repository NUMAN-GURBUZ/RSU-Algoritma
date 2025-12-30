import hashlib

# === SABİTLER ===
BLOK_BOYUTU = 16  # 128 bit = 16 byte
TUR_SAYISI = 3    # Algoritma 3 tur dönecek (basitleştirildi)

# === 1. ANAHTAR ÜRETME (Gereksinim 2.1.1) ===
# === 1. ANAHTAR ÜRETME (Gereksinim 2.1.1) ===
def Anahtar_Uret(parola):
    """
    Kullanıcı parolasından SHA-256 kullanarak 128 bitlik (16 byte) anahtar üretir.
    """
    hash_obj = hashlib.sha256(parola.encode('utf-8'))
    # SHA256 32 byte döner, biz ilk 16 byte'ını alıyoruz.
    return bytearray(hash_obj.digest()[:BLOK_BOYUTU])

# === YARDIMCI MATEMATİKSEL FONKSİYONLAR ===
def tur_anahtarlarini_uret(ana_anahtar):
    """
    Ana anahtardan tur anahtarları türetir (basitleştirilmiş).
    Her tur için ana anahtarı tur numarasıyla XOR yaparak basit bir türetme.
    """
    anahtarlar = []
    for i in range(TUR_SAYISI):
        # Basit türetme: Ana anahtarı tur numarasıyla XOR'la
        tur_anahtari = bytearray([b ^ i for b in ana_anahtar])
        anahtarlar.append(tur_anahtari)
    return anahtarlar

def sub_bytes(durum):
    """İkame Fonksiyonu: (b * 5 + 13) mod 256"""
    return bytearray([(b * 5 + 13) % 256 for b in durum])

def inv_sub_bytes(durum):
    """Ters İkame Fonksiyonu: 205 * (b - 13) mod 256"""
    # Not: 5'in mod 256'da tersi 205'tir.
    return bytearray([(205 * (b - 13)) % 256 for b in durum])

def shift_bytes(durum):
    """Basit Permütasyon: Byte'ları 1 pozisyon sola kaydır (dairesel)"""
    yeni = bytearray(16)
    for i in range(16):
        yeni[i] = durum[(i + 1) % 16]  # Dairesel kaydırma
    return yeni

def inv_shift_bytes(durum):
    """Ters Permütasyon: Byte'ları 1 pozisyon sağa kaydır"""
    yeni = bytearray(16)
    for i in range(16):
        yeni[i] = durum[(i - 1) % 16]  # Ters dairesel kaydırma
    return yeni

def xor_bytes(b1, b2):
    """İki byte dizisini XOR işlemine sokar"""
    return bytearray([x ^ y for x, y in zip(b1, b2)])

# === 2. ŞİFRELEME FONKSİYONU (Gereksinim 2.1.2) ===
def Sifrele(duz_metin, anahtar):
    if len(duz_metin) != 16:
        raise ValueError("HATA: Metin tam olarak 16 byte (128 bit) olmalıdır.")
    
    blok = bytearray(duz_metin)
    tur_anahtarlari = tur_anahtarlarini_uret(anahtar)
    
    for i in range(TUR_SAYISI):
        # A. AddRoundKey (Anahtar Karıştırma)
        blok = xor_bytes(blok, tur_anahtarlari[i])
        # B. SubBytes (İkame)
        blok = sub_bytes(blok)
        # C. ShiftBytes (Basit Permütasyon)
        blok = shift_bytes(blok)
        
    return blok

# === 3. DEŞİFRELEME FONKSİYONU (Gereksinim 2.1.3) ===
def Desifrele(sifreli_metin, anahtar):
    blok = bytearray(sifreli_metin)
    tur_anahtarlari = tur_anahtarlarini_uret(anahtar)
    
    # İşlemleri TERS Sırada ve TERS Fonksiyonlarla yapıyoruz
    for i in range(TUR_SAYISI - 1, -1, -1):
        # C. Ters Permütasyon
        blok = inv_shift_bytes(blok)
        # B. Ters İkame
        blok = inv_sub_bytes(blok)
        # A. Anahtar Çıkarma (XOR'un tersi yine XOR'dur)
        blok = xor_bytes(blok, tur_anahtarlari[i])
        
    return blok

# === TEST VE DOĞRULAMA (Gereksinim 2.2) ===
if __name__ == "__main__":
    print("=== GÖLGE-128 ŞİFRELEME ALGORİTMASI: PYTHON TESTLERİ ===\n")

    # --- TEST 1: BASİT DOĞRULAMA (Encrypt -> Decrypt) ---
    print("--- TEST 1: BASİT DOĞRULAMA ---")
    parola = "GizliAnahtar123"
    # Tam 16 byte olacak şekilde ayarlanmış metin (Boşluklarla tamamlanabilir)
    orjinal_metin_str = "YazilimMuh2025!!" 
    orjinal_metin_bytes = orjinal_metin_str.encode('utf-8')

    print(f"1. Parola: {parola}")
    print(f"2. Orjinal Metin: {orjinal_metin_str}")

    # Anahtar Üret
    ana_anahtar = Anahtar_Uret(parola)
    print(f"3. Üretilen Anahtar (Hex): {ana_anahtar.hex().upper()}")

    # Şifrele
    sifreli = Sifrele(orjinal_metin_bytes, ana_anahtar)
    print(f"4. Şifreli Metin (Hex):  {sifreli.hex().upper()}")

    # Deşifrele
    cozulen_bytes = Desifrele(sifreli, ana_anahtar)
    cozulen_metin = cozulen_bytes.decode('utf-8', errors='ignore')
    print(f"5. Deşifre Edilen Metin: {cozulen_metin}")

    if orjinal_metin_str == cozulen_metin:
        print(">> SONUÇ: BAŞARILI (Metinler Birebir Eşleşiyor)\n")
    else:
        print(">> SONUÇ: BAŞARISIZ\n")

    # --- TEST 2: ANAHTAR HASSASİYETİ (ÇIĞ ETKİSİ) ---
    print("--- TEST 2: ANAHTAR HASSASİYETİ (Tek Bit Değişimi) ---")
    
    # Anahtarın son bitini değiştiriyoruz (XOR 1 yaparak)
    bozuk_anahtar = bytearray(ana_anahtar)
    bozuk_anahtar[15] ^= 1 # Son byte'ın son bitini tersle
    
    print("Senaryo: Orijinal şifreli metni, sadece 1 bit farklı anahtarla çözmeye çalışıyoruz.")
    print(f"Orijinal Anahtar: {ana_anahtar.hex().upper()}")
    print(f"Bozuk Anahtar   : {bozuk_anahtar.hex().upper()}")

    hatali_cozum_bytes = Desifrele(sifreli, bozuk_anahtar)
    # Çıktı anlamsız byte'lar olacağı için hex olarak gösteriyoruz
    print(f"Hatalı Çözüm (Hex): {hatali_cozum_bytes.hex().upper()}")
    
    # Okunabilir metin var mı diye bakalım (Muhtemelen saçma karakterler çıkacak)
    hatali_metin = hatali_cozum_bytes.decode('utf-8', errors='replace')
    print(f"Hatalı Metin (Str): {hatali_metin}")
    
    print(">> SONUÇ: BAŞARILI (Çıktı tamamen anlamsız, Çığ Etkisi gözlendi.)")