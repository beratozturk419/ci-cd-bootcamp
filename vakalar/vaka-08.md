# 📁 Vaka 8 — Hazine Haritası

```
Zorluk: ⭐⭐⭐ (Zor)
Tür:    Koordinat tablosu
```

---

## 📋 Olay

Ada'nın duvarında bir harf tablosu asılıydı. Yanında da küçük bir
kağıtta koordinatlar yazılıydı. Klasik bir hazine haritası yöntemi:
tablodaki doğru koordinatları takip ederek gizli kelimeyi bul.

## 🔎 Kanıt

### Ada'nın Harf Tablosu:

```
         Sütun
         1    2    3    4    5
       ┌────┬────┬────┬────┬────┐
  A    │ K  │ S  │ M  │ P  │ T  │
       ├────┼────┼────┼────┼────┤
  B    │ Ö  │ İ  │ D  │ R  │ E  │
S      ├────┼────┼────┼────┼────┤
a C    │ A  │ L  │ F  │ N  │ U  │
t      ├────┼────┼────┼────┼────┤
ı D    │ H  │ Y  │ O  │ G  │ Z  │
r      ├────┼────┼────┼────┼────┤
  E    │ V  │ Ç  │ B  │ J  │ W  │
       └────┴────┴────┴────┴────┘
```

### Ada'nın Koordinatları:

```
╔════════════════════════════════════════╗
║                                        ║
║   A2  →  B2  →  C3  →  B4  →  B5      ║
║                                        ║
╚════════════════════════════════════════╝
```

## 📝 Görev

Her koordinat bir harf verir. Satır harfi (A-E) ve sütun numarası
(1-5) kesişimindeki harfi bul.

**Örnek:** A2 → A satırı, 2. sütun → **S**

Tüm koordinatları çöz ve harfleri sırayla birleştir.

## ✏️ Cevabını Yaz

`cevaplar.py` dosyasını aç ve `vaka8` satırına bulduğun kelimeyi yaz.
