# 🎓 Eğitmen Rehberi — CI/CD Bootcamp (Gizem Çözme Edisyonu)

## Konsept Özeti

Bu bootcamp, CI/CD kavramlarını **sıfır kodlama gerektiren** bir dedektiflik
oyunuyla öğretir. Katılımcılar 10 farklı bulmacayı (ters yazı, şifre çözme,
mantık, binary, morse vb.) çözer ve cevaplarını basit bir dosyaya yazar.
Her `git push` otomatik testleri tetikler. Tüm cevaplar doğru olduğunda
site otomatik deploy olur.

**Neden bu format?**
- Kod yazmak bilmeyenler de katılabilir (sadece bulmaca çöz + cevap yaz)
- Yapay zekaya yapıştırarak çözmek zor (gizli dosya, repo keşfi, görsel bulmacalar)
- CI/CD döngüsünü gerçekten deneyimliyorlar (push → test → deploy)
- Hikaye ve rekabet motivasyonu yüksek tutuyor

## Cevap Anahtarı (Sadece Eğitmen İçin!)

```
Vaka 1  — MERHABA    (ABAHREM'i tersten oku)
Vaka 2  — ADA        (1=A, 4=D, 1=A)
Vaka 3  — GITHUB     (JLWKXE, her harfi 3 geri kaydır)
Vaka 4  — LIMAN      (vakalar/.ada-gizli-not.txt dosyasında)
Vaka 5  — DEFNE      (erkek değil → Kerem elenir,
                       5 harf → ikisi de uyar,
                       sistem yönetimi → DevOps → Defne)
Vaka 6  — BULUT      (01000010=B, 01010101=U, 01001100=L,
                       01010101=U, 01010100=T)
Vaka 7  — YAZILIM    (şiirin satır başları: Y-A-Z-I-L-İ-M)
Vaka 8  — SİFRE      (A2=S, B2=İ, C3=F, B4=R, B5=E)
Vaka 9  — HAZIR      (.... = H, .- = A, --.. = Z, .. = I, .-. = R)
Vaka 10 — MÜHENDİS  (Vaka1[1]=M, Vaka6[2]=U, Vaka9[1]=H,
                       Vaka5[2]=E, Vaka4[5]=N, Vaka2[2]=D,
                       Vaka3[2]=I, Vaka8[1]=S)
```

### Ada'nın Gizli Mesajı
Her doğru cevap bir kelime açar:
```
Vaka  1 → "Kodlamak"     Vaka  6 → "ama"
Vaka  2 → "bir"          Vaka  7 → "en"
Vaka  3 → "süper"        Vaka  8 → "yakın"
Vaka  4 → "güç"          Vaka  9 → "şey"
Vaka  5 → "değil"        Vaka 10 → "odur"

→ "Kodlamak bir süper güç değil, ama en yakın şey odur."
```

## Ön Hazırlık (1 gün önce)

### Template Repo
1. GitHub'da `kayip-yazilimcinin-sifresi` adlı public repo oluşturun
2. ZIP'teki dosyaları yükleyin
3. **Settings → Actions → General** → "Allow all actions" etkin olmalı
4. Kendiniz fork edip tüm akışı test edin

### Katılımcılara Gönderin
- GitHub hesabı açsınlar
- Git kurulumu: https://git-scm.com
- Python 3.12+: https://python.org
- VS Code (veya herhangi bir editör)
- **GitHub Desktop** (terminal kullanmak istemeyenler için alternatif)

## 3 Saatlik Bootcamp Planı

### 🕐 1. Saat — Giriş + Kurulum (60 dk)

| Süre | Aktivite |
|------|----------|
| 00-15 | **CI/CD Nedir?** Günlük hayattan benzetme: "Yemek tarifi yazdın, her değişiklikte otomatik tadım yapılıyor. Lezzetliyse otomatik servise çıkıyor." |
| 15-25 | **Canlı Demo:** Template repo'yu göster, bilerek yanlış cevap yaz, push et, pipeline'ın KIRMIZI olduğunu göster. Sonra doğru cevabı yaz, YEŞİL pipeline + deploy |
| 25-40 | **Herkes Fork Etsin:** Adım adım ekranı paylaşarak fork → clone → pip install -r requirements.txt |
| 40-55 | **İlk Vaka Birlikte:** Vaka 1'i birlikte açın, çözün, `cevaplar.py`'ye yazın, birlikte push edin |
| 55-60 | **Actions Sekmesi:** Herkes kendi Actions sekmesini açsın, 1 testin yeşil olduğunu görsün |

**İpuçları:**
- "Actions sekmesi sizin otomatik sınav kağıdınız" benzetmesini kullanın
- İlk yeşil tiki gördüklerinde alkış / kutlama yapın
- Terminal kullanmak istemeyenler için GitHub Desktop veya web editörü gösterin

### 🕐 2. Saat — Bulmaca Çözme (60 dk)

| Süre | Aktivite |
|------|----------|
| 00-05 | **Kurallar:** Her vaka bağımsız, istediğinden başla. Her push'ta Actions'ı kontrol et |
| 05-50 | **Serbest Çalışma:** Katılımcılar kendi hızlarında çözer |
| 50-60 | **Durum Kontrolü:** Kim kaçıncı vakada? Scoreboard güncelleme |

**Eğitmen Stratejisi:**
- Sınıfta dolaşın, tıkananlara ipucu verin (çözümü DEĞİL!)
- 15. dakikada: "Vaka 4'te gizli dosyayı `ls -a` ile bulabilirsiniz" diye genel ipucu
- 30. dakikada: Sezar şifresi için tahtaya örnek çözüm adımı yazın
- Hızlı çözenleri yavaş olanlara eşleyin (pair çalışma)
- **Canlı scoreboard** tutun (aşağıdaki şablona bakın)

**Beklenen İlerleme:**
- Vaka 1-2: Herkes 5-10 dk'da çözer
- Vaka 3-5: 15-20 dk, bazıları yardım ister
- Vaka 6-9: 20-30 dk, binary ve morse zorlar
- Vaka 10: Diğer 9'u çözmüş olanlar 5-10 dk'da çözer

### 🕐 3. Saat — Deploy + Kapanış (60 dk)

| Süre | Aktivite |
|------|----------|
| 00-10 | **GitHub Pages Kurulumu:** Birlikte Settings → Pages → GitHub Actions |
| 10-20 | **İlk Deploy!** Tüm vakaları çözmüş birinin sitesini canlı gösterin |
| 20-40 | **Kalan Bulmacalar:** Tamamlayamamış olanlar devam eder, çözmüşler yardım eder |
| 40-50 | **CI/CD Gerçek Dünyada:** Branch protection, staging, production, Docker, cloud deploy |
| 50-60 | **Kapanış:** Deploy URL'lerini paylaşın, sonraki adımlar, kaynaklar |

## Olası Sorunlar

| Sorun | Çözüm |
|-------|-------|
| Fork edemiyor | Email doğrulaması gerekli olabilir |
| `pip install` hata veriyor | `python --version` kontrol (3.12+ olmalı) |
| Push yapamıyor | GitHub credential/token ayarı gerekli |
| Actions çalışmıyor | Settings → Actions → "Allow all" kontrol |
| Pages deploy olmuyor | Settings → Pages → Source: "GitHub Actions" seçili mi? |
| Vaka 4: Gizli dosyayı bulamıyor | `ls -a vakalar/` veya GitHub'da klasöre tıkla |
| Türkçe karakter sorunu | Test normalizer var, büyük/küçük + Türkçe fark etmez |
| "pytest: command not found" | Python veya pytest yüklü değil |

## Canlı Scoreboard Şablonu

Tahtaya veya Google Sheet'e:

```
╔═══════════════╦══╦══╦══╦══╦══╦══╦══╦══╦══╦═══╦════════╗
║ Katılımcı     ║1 ║2 ║3 ║4 ║5 ║6 ║7 ║8 ║9 ║10 ║Deploy? ║
╠═══════════════╬══╬══╬══╬══╬══╬══╬══╬══╬══╬═══╬════════╣
║ Grup Alfa     ║✅║✅║✅║✅║✅║⬜║⬜║⬜║⬜║ ⬜ ║  ❌    ║
║ Grup Beta     ║✅║✅║✅║✅║✅║✅║✅║⬜║⬜║ ⬜ ║  ❌    ║
║ Grup Gamma    ║✅║✅║✅║✅║✅║✅║✅║✅║✅║ ✅ ║  ✅ 🎉 ║
╚═══════════════╩══╩══╩══╩══╩══╩══╩══╩══╩══╩═══╩════════╝
```

> 💡 45 kişiyi 3-4 kişilik gruplara ayırmanızı öneriyoruz.
> Bu hem iş birliğini artırır hem de git çakışmalarını (conflict)
> deneyimlemeleri için fırsat yaratır!

## YZ İle Kopya Çekme Önlemleri

Bu format, yapay zekaya yapıştırarak çözmeyi zorlaştırır çünkü:

1. **Vaka 4** repo içinde fiziksel dosya aramayı gerektirir
2. **Vaka 10** diğer 9 cevabı bilmeyi gerektirir (tek seferde çözülemez)
3. Bulmacalar bağlam gerektirir (tablolar, görseller, dosya yapısı)

Ek önlem olarak:
- Zaman sınırı koyun (ilk bitiren gruba ödül)
- Ekranlarda dolaşarak süreci gözlemleyin
- "Nasıl çözdün?" diye sorun, süreci anlatamayan kopya çekmiştir

## Sunum Slaytları İçin Başlıklar

1. CI/CD nedir? (Sürekli Entegrasyon / Sürekli Dağıtım)
2. Neden önemli? (Manuel hata riski, zaman kaybı, ekip koordinasyonu)
3. GitHub Actions nasıl çalışır? (YAML, trigger, job, step)
4. Demo: Pipeline kırmızı → yeşil
5. Hands-on başlasın!

## Bootcamp Sonrası Kaynaklar

Katılımcılara paylaşmak için:
- GitHub Actions Docs: https://docs.github.com/en/actions
- GitHub Skills: https://skills.github.com
- CI/CD Nedir?: https://www.redhat.com/en/topics/devops/what-is-ci-cd
