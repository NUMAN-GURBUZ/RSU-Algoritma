"""
RSÜ Algoritması İstatistiksel Testler
Ki-kare, Runs ve Frekans testleri

Yazar: Numan Gürbüz
Tarih: 2 Ocak 2026
"""

import math
from RSU_Algoritma import RSU


class RSUTestler:
    """RSÜ için istatistiksel testler"""
    
    def __init__(self, rsu, test_bit_sayisi=100000):
        self.rsu = rsu
        self.test_bit_sayisi = test_bit_sayisi
        self.bitler = None
    
    def bit_uret(self):
        """Test için bit dizisi üret"""
        print(f"\n{self.test_bit_sayisi:,} bit üretiliyor...")
        self.bitler = self.rsu.rastgele_bit_dizisi_uret(self.test_bit_sayisi)
    
    def frekans_testi(self):
        """Frekans Testi - 0 ve 1 dengesi"""
        print("\n" + "=" * 60)
        print("FREKANS TESTİ")
        print("=" * 60)
        
        if not self.bitler:
            self.bit_uret()
        
        sifir = self.bitler.count(0)
        bir = self.bitler.count(1)
        fark = abs(sifir - bir)
        fark_orani = fark / self.test_bit_sayisi
        
        basarili = fark_orani < 0.02
        
        print(f"\n0 sayısı: {sifir:,} ({sifir/self.test_bit_sayisi*100:.2f}%)")
        print(f"1 sayısı: {bir:,} ({bir/self.test_bit_sayisi*100:.2f}%)")
        print(f"Fark: {fark:,} ({fark_orani*100:.2f}%)")
        print(f"\nSonuç: {'✓ BAŞARILI' if basarili else '✗ BAŞARISIZ'}")
        
        return basarili
    
    def runs_testi(self):
        """Runs Testi - Ardışık bitlerin rastgeleliği"""
        print("\n" + "=" * 60)
        print("RUNS TESTİ")
        print("=" * 60)
        
        if not self.bitler:
            self.bit_uret()
        
        # Runs sayısını hesapla
        runs = 1
        for i in range(1, len(self.bitler)):
            if self.bitler[i] != self.bitler[i-1]:
                runs += 1
        
        # Beklenen runs
        n = self.test_bit_sayisi
        sifir = self.bitler.count(0)
        bir = self.bitler.count(1)
        beklenen = ((2 * sifir * bir) / n) + 1
        
        # Test istatistiği
        pay = 2 * sifir * bir * (2 * sifir * bir - n)
        payda = (n ** 2) * (n - 1)
        std = math.sqrt(pay / payda)
        z = abs(runs - beklenen) / std
        
        # p-değeri (basitleştirilmiş)
        p = 2 * (1 - self._normal_cdf(abs(z)))
        basarili = p > 0.05
        
        print(f"\nGözlenen Runs: {runs:,}")
        print(f"Beklenen Runs: {beklenen:.2f}")
        print(f"p-değeri: {p:.4f}")
        print(f"\nSonuç: {'✓ BAŞARILI' if basarili else '✗ BAŞARISIZ'}")
        
        return basarili
    
    def kikare_testi(self):
        """Ki-Kare Testi - Bit çiftlerinin dağılımı"""
        print("\n" + "=" * 60)
        print("Kİ-KARE TESTİ")
        print("=" * 60)
        
        if not self.bitler:
            self.bit_uret()
        
        # Bit çiftlerini say
        ciftler = {'00': 0, '01': 0, '10': 0, '11': 0}
        for i in range(0, len(self.bitler) - 1, 2):
            cift = str(self.bitler[i]) + str(self.bitler[i+1])
            ciftler[cift] += 1
        
        toplam = sum(ciftler.values())
        beklenen = toplam / 4
        
        # Ki-kare hesapla
        kikare = sum(((g - beklenen) ** 2) / beklenen for g in ciftler.values())
        kritik = 7.815  # α=0.05, df=3
        
        basarili = kikare < kritik
        
        print(f"\nBeklenen: {beklenen:.2f}")
        print("Gözlenen:")
        for k, v in sorted(ciftler.items()):
            print(f"  {k}: {v:,} ({v/toplam*100:.2f}%)")
        print(f"\nKi-Kare: {kikare:.4f}")
        print(f"Kritik Değer: {kritik}")
        print(f"\nSonuç: {'✓ BAŞARILI' if basarili else '✗ BAŞARISIZ'}")
        
        return basarili
    
    def _normal_cdf(self, x):
        """Normal dağılım CDF"""
        return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0
    
    def tum_testler(self):
        """Tüm testleri çalıştır"""
        print("\n" + "=" * 60)
        print("RSÜ İSTATİSTİKSEL TESTLER")
        print("=" * 60)
        print(f"Test Bit Sayısı: {self.test_bit_sayisi:,}")
        
        self.bit_uret()
        
        sonuclar = []
        sonuclar.append(('Frekans Testi', self.frekans_testi()))
        sonuclar.append(('Runs Testi', self.runs_testi()))
        sonuclar.append(('Ki-Kare Testi', self.kikare_testi()))
        
        # Özet
        print("\n" + "=" * 60)
        print("TEST SONUÇLARI")
        print("=" * 60)
        for test, basarili in sonuclar:
            print(f"{test}: {'✓ BAŞARILI' if basarili else '✗ BAŞARISIZ'}")
        
        basarili_sayi = sum(1 for _, b in sonuclar if b)
        print(f"\nGeçen: {basarili_sayi}/{len(sonuclar)}")
        
        if basarili_sayi == len(sonuclar):
            print("\n🎉 TÜM TESTLER BAŞARILI!")
        
        print("=" * 60)


if __name__ == "__main__":
    rsu = RSU("test_parola_2026")
    testler = RSUTestler(rsu, test_bit_sayisi=100000)
    testler.tum_testler()
