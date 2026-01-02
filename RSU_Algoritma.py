"""
RSÜ (Rastgele Sayı Üreteci) Algoritması
Basit matematiksel işlemlerle rastgele sayı üretimi

Yazar: Numan Gürbüz
Tarih: 2 Ocak 2026
"""

import hashlib


class RSU:
    """Basit RSÜ algoritması - LCG + XOR karıştırma"""
    
    def __init__(self, parola):
        """RSÜ başlatıcı"""
        # LCG parametreleri
        self.a = 1103515245
        self.c = 12345
        self.m = 2**32
        
        # Paroladan seed oluştur
        self.seed = self._seed_olustur(parola)
    
    def _seed_olustur(self, parola):
        """Paroladan seed oluştur"""
        hash_obj = hashlib.sha256(parola.encode('utf-8'))
        hash_hex = hash_obj.hexdigest()
        return int(hash_hex[:8], 16)
    
    def _lcg_adim(self):
        """LCG adımı: seed = (a × seed + c) mod m"""
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed
    
    def _karistir(self, sayi):
        """XOR karıştırma"""
        sayi ^= (sayi >> 11)
        sayi ^= (sayi << 7) & 0x9D2C5680
        sayi ^= (sayi << 15) & 0xEFC60000
        sayi ^= (sayi >> 18)
        return sayi
    
    def rastgele_sayi_uret(self):
        """0-1 arası rastgele sayı üret"""
        ham = self._lcg_adim()
        karisik = self._karistir(ham)
        return karisik / self.m
    
    def rastgele_bit_uret(self):
        """Rastgele bit üret (0 veya 1)"""
        return 1 if self.rastgele_sayi_uret() >= 0.5 else 0
    
    def rastgele_bit_dizisi_uret(self, n):
        """n bitlik rastgele dizi üret"""
        return [self.rastgele_bit_uret() for _ in range(n)]


# Test kodu
if __name__ == "__main__":
    print("=" * 60)
    print("RSÜ ALGORİTMASI - TEST ÇIKTILARI")
    print("=" * 60)
    
    # RSÜ oluştur
    rsu = RSU("test_parola")
    
    # Test 1: Rastgele sayılar
    print("\n[1] Rastgele Sayılar (0.0 - 1.0):")
    for i in range(5):
        print(f"  {i+1}. {rsu.rastgele_sayi_uret():.6f}")
    
    # Test 2: Rastgele bitler
    print("\n[2] Rastgele Bit Dizisi (20 bit):")
    bitler = rsu.rastgele_bit_dizisi_uret(20)
    print(f"  Bitler: {bitler}")
    print(f"  0 sayısı: {bitler.count(0)}, 1 sayısı: {bitler.count(1)}")
    
    # Test 3: Büyük dizi istatistikleri
    print("\n[3] Büyük Bit Dizisi (10,000 bit):")
    buyuk_dizi = rsu.rastgele_bit_dizisi_uret(10000)
    sifir = buyuk_dizi.count(0)
    bir = buyuk_dizi.count(1)
    print(f"  0 sayısı: {sifir} ({sifir/100:.1f}%)")
    print(f"  1 sayısı: {bir} ({bir/100:.1f}%)")
    
    print("\n" + "=" * 60)
    print("TESTLER TAMAMLANDI")
    print("=" * 60)
