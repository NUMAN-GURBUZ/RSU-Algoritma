Proje Raporu: Aşama 1 - Algoritma Tasarımı
1. Algoritmanın Adı
İsim: GÖLGE-128 (Shadow-128) (İsimlendirme Mantığı: Şifreli metnin, açık metnin bir "gölgesi" gibi takip etmesi ancak asıl sureti gizlemesi metaforuna dayanır.)
2. Gerekçe ve Felsefe
Bu algoritmayı tasarlarken Hız ve Güvenlik Dengesi (SPN - Substitution Permutation Network) mimarisi temel alınmıştır.
•	Neden Blok Şifre? Akış şifrelerine göre senkronizasyon kaybı durumunda daha dayanıklı olması ve modern işlemcilerde blok bazlı işlemlerin (128-bit) optimize edilebilmesi nedeniyle Blok Şifre tercih edilmiştir.
•	Tasarım Kararları:
o	İkame (Substitution): Frekans analizini engellemek için doğrusal olmayan (non-linear) bir S-Box yapısı kullanıldı. Bu, Shannon'un "Karıştırma" (Confusion) ilkesini sağlar.
o	Permütasyon (Permutation): Bitlerin yerini değiştirerek, tek bir bit değişiminin tüm bloğu etkilemesini (Avalanche Effect) sağlamak hedeflendi. Bu, "Yayılma" (Diffusion) ilkesini sağlar.
o	Anahtar Karıştırma: Her turda verinin anahtarla XOR işlemine girmesi, saldırganın sistemi tersine mühendislikle çözmesini zorlaştırır.
•	Hedeflenen Dayanıklılık: Kaba kuvvet (Brute-force) saldırılarına karşı 128-bit anahtar uzayı ile direnç sağlanmış; diferansiyel kriptanalize karşı ise çok turlu (multi-round) yapı kullanılarak direnç artırılmıştır.







3. Detaylı Şema
 



4. Matematiksel Fonksiyonlar
GÖLGE-128, 128 bitlik (16 byte) veri blokları üzerinde çalışan bir blok şifreleme algoritmasıdır. Tüm işlemler byte ve bit düzeyinde matematiksel fonksiyonlarla tanımlanmıştır.

Tanımlar
•	P: Açık metin
•	C: Şifreli metin
•	K: Ana anahtar
•	Kᵢ: i. tur anahtarı
•	⊕: XOR işlemi
________________________________________
Anahtar Genişletme
Her tur anahtarı bir önceki anahtardan türetilir.
Ki=ROL3(Ki−1)⊕RCiK_i = \text{ROL}_3(K_{i-1}) \oplus RC_iKi=ROL3(Ki−1)⊕RCi 
________________________________________
İkame (SubBytes)
Her byte için aşağıdaki işlem uygulanır:
S(b)=(5b+13) mod 256S(b) = (5b + 13) \bmod 256S(b)=(5b+13)mod256 
________________________________________
Permütasyon (ShiftRows)
16 byte’lık blok 4×4 matris kabul edilir:
•	
1.	satır: kaydırma yok
•	
2.	satır: 1 byte sola
•	
3.	satır: 2 byte sola
•	
4.	satır: 3 byte sola
________________________________________
Tur Denklemi
Her turda yapılan işlem:
Mi+1=P(S(Mi⊕Ki))M_{i+1} = P \big( S ( M_i \oplus K_i ) \big)Mi+1=P(S(Mi⊕Ki)) 
________________________________________
Deşifreleme
İşlemler ters sırada ve ters fonksiyonlarla yapılır:
Mi=S−1(P−1(Mi+1))⊕KiM_i = S^{-1} \big( P^{-1}( M_{i+1} ) \big) \oplus K_iMi=S−1(P−1(Mi+1))⊕Ki






3 – KRİPTANALİZ VE ANALİZ RAPORU 
Algoritma Adı: GÖLGE-128 (Shadow-128)
Blok Boyutu: 128-bit (16 byte)
Tur Sayısı: 10 tur
Anahtar: Kullanıcı parolası UTF-8 ile byte’a çevrilir, 16 byte’a sıfır padding ile tamamlanır (veya kesilir).
## Proje Raporu — Aşama 1: Algoritma Tasarımı

### 1. Algoritmanın adı

GÖLGE-128 (Shadow-128)

İsimlendirme mantığı: Şifreli metnin açık metnin bir "gölgesi" gibi takip etmesi, ancak asıl biçimin gizlenmesi metaforuna dayanır.

### 2. Gerekçe ve tasarım felsefesi

Bu algoritma, hız ile güvenlik arasındaki dengeyi sağlamak amacıyla bir SPN (Substitution–Permutation Network) yaklaşımı temel alınarak tasarlanmıştır.

- Neden blok şifre?: Akış şifrelerine kıyasla senkronizasyon kaybına karşı daha dayanıklı olması ve modern işlemcilerde blok işleme optimizasyonunun kolay olması nedeniyle blok şifre tercih edilmiştir.
- Tasarım kararları:
	- İkame (Substitution): Frekans analizini zorlaştırmak için doğrusal olmayan bir S-Box veya affine dönüşüm tercih edilmiştir (Shannon'un "confusion" ilkesi).
	- Permütasyon (Permutation): Tek bir bit değişikliğinin tüm bloğu etkilemesini sağlamak amacıyla permütasyon uygulanmıştır ("diffusion").
	- Anahtar karıştırma: Her turda veriye anahtarın XOR'lanması, tersine mühendislik ile çözmeyi zorlaştırır.
- Hedeflenen dayanıklılık: 128-bit anahtar uzayı ile kaba kuvvet saldırılarına direnç; kriptanalize karşı çok turlu yapı önerisi.

### 3. Matematiksel tanımlar ve gösterimler

- P: Açık metin
- C: Şifreli metin
- K: Ana anahtar
- K_i: i. tur anahtarı
- ⊕: XOR işlemi

Anahtar genişletme (örnek gösterim):

K_i = ROL_3(K_{i-1}) ⊕ RC_i  (örnek ifade)

İkame (SubBytes) örneği:

S(b) = (5·b + 13) mod 256

Permütasyon (ShiftRows):

16 byte'lık blok 4×4 matris olarak kabul edilir ve satırlar sırasıyla 0, 1, 2 ve 3 byte sola kaydırılır.

Tur denklemi (örnek):

M_{i+1} = P( S( M_i ⊕ K_i ) )

Deşifreleme, işlemlerin tersinin ters sırada uygulanması ile elde edilir:

M_i = S^{-1}( P^{-1}( M_{i+1} ) ) ⊕ K_i

### 4. Kriptanaliz — Zayıflıklar ve öneriler

- Zayıf yönler:
	1. Yetersiz tur sayısı (örnek: 3 tur)
	2. Basit anahtar türetme yöntemi
	3. SubBytes'in doğrusal veya affine seçilmesi
	4. Sadece döndürme içeren basit permütasyon

- Olası saldırı yöntemleri:
	- Anahtar türetme zayıflığından yararlanma
	- Doğrusal kriptanaliz
	- Diferansiyel kriptanaliz
	- Meet-in-the-middle

### 5. Uygulamalı örnek: Brute-force/sözlük saldırısı

Senaryo: Challenge anahtarı 4 haneli bir parola olacak şekilde kısıtlanmıştır (örneğin "2024"). Böyle bir anahtar uzayı 10.000 olasılıktan oluşur ve modern bir bilgisayarda kısa sürede taranabilir. Bu nedenle brute-force en verimli yöntemdir.

Adımlar (özet):

1. HEX olarak verilen şifreli metin byte dizisine dönüştürülür.
2. 0000'dan 9999'a kadar tüm parolalar sırayla denenir.
3. Her parola için 16 byte'lık anahtar oluşturulur ve deşifreleme denenir.
4. Çıkan düz metin anlamlılık kriterlerine göre kontrol edilir (ör. içinde "Tebrikler" veya '!' geçmesi).

Kullanılan araçlar ve notlar:

- Python 3.x
- Mevcut `anahtar_uret()` ve `desifrele()` fonksiyonları kullanılmıştır.
- Basit bir brute-force döngüsü uygulanmıştır.

