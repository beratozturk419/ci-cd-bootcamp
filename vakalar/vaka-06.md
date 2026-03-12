# 📁 Vaka 6 — Makinelerin Dili

```
Zorluk: ⭐⭐⭐ (Zor)
Tür:    İkili (binary) kod çözme
```

---

## 📋 Olay

Ada'nın monitöründe garip bir sayı dizisi bulundu. Sadece 0 ve 1'lerden
oluşuyor. Bu, bilgisayarların konuştuğu dil: **ikili (binary) sistem**.

## 🔎 Kanıt

### Binary Nasıl Çalışır?

Bilgisayarlar her harfi 8 basamaklı bir 0-1 dizisi (byte) olarak saklar.

```
Harf → Sayı (ASCII) → Binary
──────────────────────────────
 A   →   65         → 01000001
 B   →   66         → 01000010
 C   →   67         → 01000011
 ...
```

### Çeviri Tablosu (lazım olacak harfler):

```
01000010 = B          01001111 = O
01000011 = C          01010000 = P
01000100 = D          01010010 = R
01000101 = E          01010011 = S
01001000 = H          01010100 = T
01001001 = I          01010101 = U
01001011 = K          01010110 = V
01001100 = L          01011001 = Y
01001101 = M          01011010 = Z
01001110 = N
```

### Ada'nın Binary Mesajı:

```
╔══════════════════════════════════════════════════╗
║                                                  ║
║  01000010  01010101  01001100  01010101  01010100 ║
║                                                  ║
╚══════════════════════════════════════════════════╝
```

## 📝 Görev

Her 8'li binary grubu tabloda bul ve karşılık gelen harfi yaz.
5 harfi birleştirdiğinde cevabı bulacaksın.

> **İpucu:** İlk grup 01000010 — tabloda bul, hangi harf?
> İkinci grup 01010101 — bu hangi harf? Devam et...

## ✏️ Cevabını Yaz

`cevaplar.py` dosyasını aç ve `vaka6` satırına çözdüğün kelimeyi yaz.
