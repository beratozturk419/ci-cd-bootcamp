# 📁 Vaka 9 — Bip Bip Biiiip

```
Zorluk: ⭐⭐⭐⭐ (Çok Zor)
Tür:    Mors kodu çözme
```

---

## 📋 Olay

Ada'nın masasındaki eski bir telsizin hafızasında bir kayıt bulundu.
Kayıtta kısa ve uzun sinyaller var — bu bir **Mors kodu** mesajı!

## 🔎 Kanıt

### Mors Kodu Tablosu:

```
 A  .-        N  -.
 B  -...      O  ---
 C  -.-.      P  .--.
 D  -..       R  .-.
 E  .         S  ...
 F  ..-.      T  -
 G  --.       U  ..-
 H  ....      V  ...-
 I  ..        Y  -.--
 K  -.-       Z  --..
 L  .-..
 M  --
```

**Okuma kuralları:**
- `.` = kısa sinyal (dit)
- `-` = uzun sinyal (dah)
- Harfler arasında boşluk var
- `/` işareti kelimeler arasındaki boşluğu gösterir

### Ada'nın Telsiz Kaydı:

```
╔══════════════════════════════════════════════╗
║                                              ║
║   ....  .-  --..  ..  .-.                    ║
║                                              ║
╚══════════════════════════════════════════════╝
```

## 📝 Görev

Her sinyal grubunu Mors tablosunda bul ve karşılık gelen harfi yaz.
5 harfi birleştir.

> **Çözüm adımları:**
> 1. `....` → tabloda bul → ?
> 2. `.-` → tabloda bul → ?
> 3. `--..` → tabloda bul → ?
> 4. `..` → tabloda bul → ?
> 5. `.-.` → tabloda bul → ?

## ✏️ Cevabını Yaz

`cevaplar.py` dosyasını aç ve `vaka9` satırına çözdüğün kelimeyi yaz.
