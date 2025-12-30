# BSG Proje Raporu — Aşama 1: Algoritma Tasarımı

## 1. Algoritmanın Adı
**GÖLGE-128 (Shadow-128)**
*İsimlendirme Mantığı:* Şifreli metnin, açık metnin bir "gölgesi" gibi takip etmesi ancak asıl sureti gizlemesi metaforuna dayanır.

## 2. Gerekçe ve Felsefe
Bu algoritma, **Hız ve Güvenlik Dengesi** gözetilerek **SPN (Substitution-Permutation Network)** mimarisi üzerine kurgulanmıştır.

*   **Neden Blok Şifre?** Akış şifrelerine kıyasla senkronizasyon kaybı durumunda daha dayanıklı olması ve modern işlemcilerde 128-bit blok işlemlerinin optimize edilebilmesi nedeniyle tercih edilmiştir.
*   **Tasarım Kararları:**
    *   *İkame (Confusion):* Doğrusal olmayan bir yapı (modüler aritmetik tabanlı S-Box benzeri işlem) kullanılarak frekans analizi zorlaştırılmıştır.
    *   *Permütasyon (Diffusion):* Bit/Byte kaydırma işlemleriyle tek bir bit değişiminin tüm bloğu etkilemesi (Çığ Etkisi) hedeflenmiştir.
    *   *Anahtar Karıştırma:* Her turda anahtar ile XOR işlemi yapılarak tersine mühendislik zorlaştırılmıştır.
*   **Hedeflenen Dayanıklılık:** 128-bit anahtar uzayı (Brute-force direnci) ve çok turlu yapı (Diferansiyel kriptanaliz direnci).

## 3. Detaylı Şema (Flowchart)

Aşağıdaki şema, GÖLGE-128 algoritmasının bir turundaki şifreleme sürecini göstermektedir:

```mermaid
graph TD
    Start([Başlat: 128-bit Blok & Ana Anahtar]) --> KeyGen[Anahtar Üretimi & Tur Anahtarları]
    KeyGen --> RoundLoop{Tur Döngüsü (N kez)}
    
    RoundLoop -- Tur Başı --> AddKey[Adım 1: AddRoundKey (XOR)]
    AddKey --> SubBytes[Adım 2: SubBytes (İkame)]
    SubBytes --> ShiftRows[Adım 3: ShiftRows (Permütasyon)]
    ShiftRows --> RoundLoop
    
    RoundLoop -- Döngü Bitti --> End([Bitiş: Şifreli Metin])

    subgraph "Bir Turun İçeriği"
    AddKey
    SubBytes
    ShiftRows
    end
```

## 4. Matematiksel Fonksiyonlar
Tüm işlemler 128-bit (16 byte) bloklar üzerinde tanımlanmıştır.

### Tanımlar
*   $P$: Açık Metin (Plaintext)
*   $C$: Şifreli Metin (Ciphertext)
*   $K$: Ana Anahtar
*   $K_i$: $i$. Tur Anahtarı
*   $\oplus$: XOR İşlemi

### 4.1 Anahtar Genişletme
Her tur anahtarı, ana anahtarın tura bağlı bir varyasyonu olarak üretilir:
$$ K_i = K \oplus i $$
*(Not: Basitleştirilmiş gösterimdir, gerçek kodda byte-byte XOR uygulanır.)*

### 4.2 İkame (SubBytes)
Her byte ($b$) için aşağıdaki doğrusal olmayan dönüşüm uygulanır:
$$ S(b) = (5 \cdot b + 13) \pmod{256} $$
Bu işlem Shannon'un **Karıştırma (Confusion)** ilkesini sağlar.

### 4.3 Permütasyon (ShiftRows)
16 byte'lık blok üzerinde dairesel kaydırma işlemi yapılır:
$$ P(Block) = (Block \ll 1 \text{ byte}) $$
Bu işlem Shannon'un **Yayılma (Diffusion)** ilkesini sağlar.

### 4.4 Tur Denklemi
Her turda aşağıdaki işlem sırası izlenir:
$$ M_{i+1} = \text{Permütasyon}( \text{İkame}( M_i \oplus K_i ) ) $$
