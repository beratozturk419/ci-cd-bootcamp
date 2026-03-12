# 📁 Vaka 3 — Sezar'ın Mirası

```
Zorluk: ⭐⭐ (Orta)
Tür:    Sezar şifresi
```

---

## 📋 Olay

Ada'nın tarayıcı geçmişinde Jül Sezar hakkında araştırmalar bulundu.
Sezar, düşmanlarının okuyamaması için mesajlarındaki her harfi
alfabede **belirli bir sayı kadar ileri** kaydırırmış.

Ada da aynı yöntemi kullanmış — ama kaç harf kaydırdığını bulmak
sana kalmış.

## 🔎 Kanıt

### Sezar Şifresi Nasıl Çalışır?

Eğer kaydırma = 3 ise:

```
Düz:     A  B  C  D  E  F  G  H  I  J  K  L  M
Şifreli: D  E  F  G  H  I  J  K  L  M  N  O  P

Düz:     N  O  P  Q  R  S  T  U  V  W  X  Y  Z
Şifreli: Q  R  S  T  U  V  W  X  Y  Z  A  B  C
```

Yani "ADA" → 3 ileri → "DGD"

### Ada'nın Şifreli Notu:

```
╔════════════════════════════════════════╗
║                                        ║
║  Kaydırma miktarı: 3                   ║
║                                        ║
║  Şifreli mesaj:  J  L  W  K  X  E      ║
║                                        ║
╚════════════════════════════════════════╝
```

## 📝 Görev

Her harfi **3 geri** kaydırarak orijinal kelimeyi bul.

> **İpucu:** J'den 3 geri git → ? , L'den 3 geri git → ? ...
> Harf harf çöz! Sonuç tanıdık bir platform ismi.

## ✏️ Cevabını Yaz

`cevaplar.py` dosyasını aç ve `vaka3` satırına cevabını yaz.
