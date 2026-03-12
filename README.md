# 🔍 Kayıp Yazılımcının Şifresi — CI/CD Bootcamp

```
╔══════════════════════════════════════════════════════════════╗
║  B Y T E F O R G E   L A B S  —  GİZLİ DAVA DOSYASI #2026  ║
╚══════════════════════════════════════════════════════════════╝
```

ByteForge Labs'ın en yetenekli yazılımcısı **Ada** kayboldu.
Geride **10 şifreli ipucu** bıraktı. Tüm ipuçlarını çöz, Ada'nın
gizli mesajını ortaya çıkar ve siten otomatik olarak yayınlansın!

> **⚠️ Kod yazmana gerek yok!** Sadece bulmacaları çöz ve cevapları yaz.

## 🚀 Nasıl Çalışır?

```
Bulmacayı çöz → Cevabı yaz → git push → Test otomatik çalışır → Tümü doğruysa site deploy olur!
```

## 📋 Hızlı Başlangıç

### 1. Fork Et
Bu sayfanın sağ üstündeki **Fork** butonuna tıkla.

### 2. Klonla
```bash
git clone https://github.com/SENIN-ADIN/kayip-yazilimcinin-sifresi.git
cd kayip-yazilimcinin-sifresi
```

### 3. Bağımlılıkları Yükle
```bash
pip install -r requirements.txt
```

### 4. İlk Vakayı Aç
```bash
# vakalar/vaka-01.md dosyasını oku (veya GitHub'da aç)
```

### 5. Cevabını Yaz
`cevaplar.py` dosyasını aç, ilgili satıra cevabını yaz.

### 6. Test Et ve Push Et
```bash
pytest --verbose -s                             # yerelde kontrol et
git add . && git commit -m "Vaka 1" && git push # gönder!
```

### 7. GitHub Pages'ı Etkinleştir
**Settings → Pages → Source → GitHub Actions** seç.

## 📁 Vakalar

| # | Vaka Adı | Zorluk | Tür |
|---|----------|--------|-----|
| 1 | Ayna Yazısı | ⭐ | Ters okuma |
| 2 | Sayı Alfabesi | ⭐ | Sayı-harf dönüşümü |
| 3 | Sezar'ın Mirası | ⭐⭐ | Sezar şifresi |
| 4 | Görünmez Dosya | ⭐⭐ | Dosya keşfi |
| 5 | Üç Şüpheli | ⭐⭐ | Mantık bulmacası |
| 6 | Makinelerin Dili | ⭐⭐⭐ | Binary kod |
| 7 | Şiirin Sırrı | ⭐⭐⭐ | Akrostiş |
| 8 | Hazine Haritası | ⭐⭐⭐ | Koordinat tablosu |
| 9 | Bip Bip Biiiip | ⭐⭐⭐⭐ | Mors kodu |
| 10 | Son Kilit | ⭐⭐⭐⭐ | Meta-bulmaca |

> Sırayla çözmek zorunda değilsin! (Ama Vaka 10 için diğerlerini çözmüş olmalısın.)

## 🔄 Çalışma Döngüsü

```
1. vakalar/ klasöründen bir vaka seç
2. Bulmacayı oku ve çöz
3. cevaplar.py dosyasına cevabını yaz
4. git add . && git commit -m "Vaka X" && git push
5. GitHub Actions sekmesinden sonucu kontrol et
6. Sonraki vakaya geç!
```

## 🏆 Kazanma Koşulu

**10/10 vaka doğru** olduğunda pipeline otomatik deploy eder:

`https://KULLANICI-ADIN.github.io/kayip-yazilimcinin-sifresi/`

---

CI/CD Bootcamp 2026 — Çöz, push et, deploy et! 🚀
