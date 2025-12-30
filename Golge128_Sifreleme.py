import hashlib

# === SABİTLER ===
BLOK_BOYUTU = 16  # 128 bit = 16 byte
TUR_SAYISI = 10   # Algoritma 10 tur dönecek

# === 1. ANAHTAR ÜRETME (Gereksinim 2.1.1) ===
def anahtar_uret(parola):
    """
    Kullanıcı parolasından SHA-256 kullanarak 128 bitlik (16 byte) anahtar üretir.
    """
    hash_obj = hashlib.sha256(parola.encode('utf-8'))
    # SHA256 32 byte döner, biz ilk 16 byte'ını alıyoruz.
    return bytearray(hash_obj.digest()[:BLOK_BOYUTU])

# === YARDIMCI MATEMATİKSEL FONKSİYONLAR ===
def tur_anahtarlarini_uret(ana_anahtar):
    """
    Ana anahtardan 10 adet tur anahtarı türetir.
    Formül: K(i) = (K(i-1) << 3) XOR Tur_Sayisi
    """
    anahtarlar = []
    mevcut = bytearray(ana_anahtar)
    
    for i in range(TUR_SAYISI):
        yeni_anahtar = bytearray(16)
        for j in range(16):
            # Her byte'ı 3 bit sola kaydır (dairesel) ve i ile XOR'la
            val = mevcut[j]
            # Python'da byte sınırlarını korumak için & 0xFF kullanıyoruz
            rotate_val = ((val << 3) | (val >> 5)) & 0xFF
            yeni_anahtar[j] = rotate_val ^ i
        
        anahtarlar.append(yeni_anahtar)
        mevcut = yeni_anahtar # Bir sonraki tur için bunu kullan
    return anahtarlar

def sub_bytes(durum):
    """İkame Fonksiyonu: (b * 5 + 13) mod 256"""
    return bytearray([(b * 5 + 13) % 256 for b in durum])

def inv_sub_bytes(durum):
    """Ters İkame Fonksiyonu: 205 * (b - 13) mod 256"""
    # Not: 5'in mod 256'da tersi 205'tir.
    return bytearray([(205 * (b - 13)) % 256 for b in durum])

def shift_rows(durum):
    """Permütasyon: Satırları sola kaydır"""
    yeni = bytearray(16)
    d = durum # Yazım kolaylığı için
    
    # 1. Satır (0,4,8,12) -> Sabit
    yeni[0], yeni[4], yeni[8], yeni[12] = d[0], d[4], d[8], d[12]
    
    # 2. Satır (1,5,9,13) -> 1 Sola Kaydır
    yeni[1], yeni[5], yeni[9], yeni[13] = d[5], d[9], d[13], d[1]
    
    # 3. Satır (2,6,10,14) -> 2 Sola Kaydır
    yeni[2], yeni[6], yeni[10], yeni[14] = d[10], d[14], d[2], d[6]
    
    # 4. Satır (3,7,11,15) -> 3 Sola Kaydır
    yeni[3], yeni[7], yeni[11], yeni[15] = d[15], d[3], d[7], d[11]
    
    return yeni

def inv_shift_rows(durum):
    """Ters Permütasyon: Satırları sağa kaydır (Şifrelemenin tersi)"""
    yeni = bytearray(16)
    d = durum
    
    # 1. Satır -> Sabit
    yeni[0], yeni[4], yeni[8], yeni[12] = d[0], d[4], d[8], d[12]
    
    # 2. Satır -> 1 Sağa Kaydır (Şifrelemedeki Solun Tersi)
    yeni[5], yeni[9], yeni[13], yeni[1] = d[1], d[5], d[9], d[13]
    
    # 3. Satır -> 2 Sağa Kaydır
    yeni[10], yeni[14], yeni[2], yeni[6] = d[2], d[6], d[10], d[14]
    
    # 4. Satır -> 3 Sağa Kaydır
    yeni[15], yeni[3], yeni[7], yeni[11] = d[3], d[7], d[11], d[15]
    
    return yeni

def xor_bytes(b1, b2):
    """İki byte dizisini XOR işlemine sokar"""
    return bytearray([x ^ y for x, y in zip(b1, b2)])

# === 2. ŞİFRELEME FONKSİYONU (Gereksinim 2.1.2) ===
def sifrele(duz_metin, anahtar):
    if len(duz_metin) != 16:
        raise ValueError("HATA: Metin tam olarak 16 byte (128 bit) olmalıdır.")
    
    blok = bytearray(duz_metin)
    tur_anahtarlari = tur_anahtarlarini_uret(anahtar)
    
    for i in range(TUR_SAYISI):
        # A. AddRoundKey (Anahtar Karıştırma)
        blok = xor_bytes(blok, tur_anahtarlari[i])
        # B. SubBytes (İkame)
        blok = sub_bytes(blok)
        # C. ShiftRows (Permütasyon)
        blok = shift_rows(blok)
        
    return blok

# === 3. DEŞİFRELEME FONKSİYONU (Gereksinim 2.1.3) ===
def desifrele(sifreli_metin, anahtar):
    blok = bytearray(sifreli_metin)
    tur_anahtarlari = tur_anahtarlarini_uret(anahtar)
    
    # İşlemleri TERS Sırada ve TERS Fonksiyonlarla yapıyoruz
    for i in range(TUR_SAYISI - 1, -1, -1):
        # C. Ters Permütasyon
        blok = inv_shift_rows(blok)
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
    ana_anahtar = anahtar_uret(parola)
    print(f"3. Üretilen Anahtar (Hex): {ana_anahtar.hex().upper()}")

    # Şifrele
    sifreli = sifrele(orjinal_metin_bytes, ana_anahtar)
    print(f"4. Şifreli Metin (Hex):  {sifreli.hex().upper()}")

    # Deşifrele
    cozulen_bytes = desifrele(sifreli, ana_anahtar)
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

    hatali_cozum_bytes = desifrele(sifreli, bozuk_anahtar)
    # Çıktı anlamsız byte'lar olacağı için hex olarak gösteriyoruz
    print(f"Hatalı Çözüm (Hex): {hatali_cozum_bytes.hex().upper()}")
    
    # Okunabilir metin var mı diye bakalım (Muhtemelen saçma karakterler çıkacak)
    hatali_metin = hatali_cozum_bytes.decode('utf-8', errors='replace')
    print(f"Hatalı Metin (Str): {hatali_metin}")
    
    print(">> SONUÇ: BAŞARILI (Çıktı tamamen anlamsız, Çığ Etkisi gözlendi.)")