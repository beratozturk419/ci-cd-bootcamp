# 📁 Vaka 10 — Son Kilit

```
Zorluk: ⭐⭐⭐⭐ (Çok Zor)
Tür:    Meta-bulmaca (önceki cevapları birleştirir)
```

---

## 📋 Olay

Ada'nın bilgisayarında son bir kilit daha var. Bu kilidi açmak için
**önceki 9 vakanın cevaplarına** ihtiyacın var.

Ada bir tablo bırakmış. Bu tablo, önceki cevaplardan belirli harfleri
seçerek son şifreyi oluşturuyor.

## 🔎 Kanıt

### Ada'nın Son Notu:

> *"Her cevabın içinde bir harf gizli. Doğru harfleri doğru sırayla*
> *seçersen, benim gerçek kimliğimi bulursun."*

### Şifre Tablosu:

```
╔═══════════╦═══════════════════════╦══════════════════╗
║  SIRA     ║  HANGİ VAKANIN        ║  KAÇINCI          ║
║  NO       ║  CEVABINDAN?          ║  HARFİ?           ║
╠═══════════╬═══════════════════════╬══════════════════╣
║   1.      ║  Vaka 1'in cevabı     ║  1. harf          ║
║   2.      ║  Vaka 6'nın cevabı    ║  2. harf          ║
║   3.      ║  Vaka 9'un cevabı     ║  1. harf          ║
║   4.      ║  Vaka 5'in cevabı     ║  2. harf          ║
║   5.      ║  Vaka 4'ün cevabı     ║  5. harf          ║
║   6.      ║  Vaka 2'nin cevabı    ║  2. harf          ║
║   7.      ║  Vaka 3'ün cevabı     ║  2. harf          ║
║   8.      ║  Vaka 8'in cevabı     ║  1. harf          ║
╚═══════════╩═══════════════════════╩══════════════════╝
```

## 📝 Görev

1. Önceki 9 vakanın cevaplarını bir yere yaz
2. Tablodaki her satır için ilgili cevabın ilgili harfini bul
3. 8 harfi sırayla birleştirerek son şifreyi oluştur

> **Örnek:** "Vaka 1'in cevabının 1. harfi" demek, Vaka 1'e yazdığın
> cevabın ilk harfini almak demektir.

> **⚠️ Dikkat:** Bu bulmacayı çözmek için önce diğer 9 vakayı
> çözmüş olmalısın!

## ✏️ Cevabını Yaz

`cevaplar.py` dosyasını aç ve `vaka10` satırına 8 harflik son şifreyi yaz.

Tüm cevaplar doğruysa pipeline yeşile dönecek ve siten deploy olacak! 🚀
