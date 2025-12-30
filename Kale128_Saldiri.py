import Kale128_Sifreleme as Cipher
import time

print("--- [KALE-128] BRUTE FORCE SALDIRISI BAŞLATILIYOR ---")
print("Hedef: 4 haneli sayısal bir parola (PIN) ile şifrelenmiş metni kırmak.")

# 1. ADIM: Hedef Şifreli Metni Ele Geçirme (Simülasyon)
# Normalde bu networkten veya dosyadan okunur.
# Burada 'Bilinmeyen' şifrenin "2024" olduğunu biliyoruz ama script bilmiyormuş gibi davranacak.
gercek_parola = "2024"
gercek_anahtar = Cipher.anahtar_uret(gercek_parola)
hedef_mesaj = b"TebriklerKirdin!"
sifreli_metin = Cipher.sifrele(hedef_mesaj, gercek_anahtar)

print(f"\n[1] Hedef Şifreli Metin (Hex): {sifreli_metin.hex().upper()}")
print("[2] Saldırı Başlıyor... (Anahtar Uzayı: 0000-9999)")

baslangic_zamani = time.time()
bulunan_parola = None

# Brute Force Döngüsü
for i in range(10000):
    deneme_parola = f"{i:04d}" # 0000, 0001, ... 2024 ... 9999
    deneme_anahtar = Cipher.anahtar_uret(deneme_parola)
    
    try:
        cozulen_bytes = Cipher.desifrele(sifreli_metin, deneme_anahtar)
        
        # Anlamsız verileri elemek için kontrol:
        try:
            cozulen_metin = cozulen_bytes.decode('utf-8')
            # Basit bir heuristik: UTF-8 ile çözülebiliyor ve ASCII karakterler içeriyorsa muhtemel adaydır.
            # Kesinlik için bilinen bir kelimeyi (Known-Plaintext) de arayabiliriz ama burada
            # sadece okunabilir olmasına bakacağız.
            if cozulen_metin.isprintable():
                # Bulunan adayları ekrana yazdırabiliriz ama burada tam eşleşmeyi arıyoruz
                # Simülasyon olduğu için 'Tebrikler' kelimesini arayalım
                if "Tebrikler" in cozulen_metin:
                    print(f"\n>> PAROLA BULUNDU: {deneme_parola}")
                    print(f">> ÇÖZÜLEN METİN: {cozulen_metin}")
                    bulunan_parola = deneme_parola
                    break
        except UnicodeDecodeError:
            continue # Geçersiz metin
            
    except Exception as e:
        continue

gecen_sure = time.time() - baslangic_zamani
print(f"\n[SONUÇ] Saldırı Tamamlandı.")
print(f"Süre: {gecen_sure:.4f} saniye")
if bulunan_parola:
    print("DURUM: BAŞARILI (KIRILDI)")
else:
    print("DURUM: BAŞARISIZ")
