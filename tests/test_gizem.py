import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from cevaplar import cevaplar

# ╔══════════════════════════════════════════════════════════╗
# ║  🔍 KAYIP YAZILIMCININ ŞİFRESİ — TEST DOSYASI           ║
# ║                                                           ║
# ║  ⚠️  BU DOSYAYI DEĞİŞTİRMEYİN!                          ║
# ║  📝  Sadece cevaplar.py dosyasını düzenleyin.             ║
# ║                                                           ║
# ║  Her doğru cevap, Ada'nın mesajından bir kelime açar.     ║
# ╚══════════════════════════════════════════════════════════╝


def n(s):
    """Türkçe karakterleri normalize eden yardımcı fonksiyon"""
    return (
        str(s)
        .lower()
        .replace("ş", "s")
        .replace("ç", "c")
        .replace("ğ", "g")
        .replace("ü", "u")
        .replace("ö", "o")
        .replace("ı", "i")
        .replace("İ", "i")
        .replace("Ş", "s")
        .replace("Ç", "c")
        .replace("Ğ", "g")
        .replace("Ü", "u")
        .replace("Ö", "o")
        .strip()
    )


# ─────────────────────────────────────
# 📁 VAKA 1 — Ayna Yazısı
# ─────────────────────────────────────
class TestVaka1AynaYazisi:
    def test_ters_yazi_cozuldu_mu(self):
        assert n(cevaplar["vaka1"]) == "merhaba"
        print('\n    🟢 Vaka 1 ÇÖZÜLDÜ! Ada\'nın mesajından kelime 1: "Kodlamak"\n')


# ─────────────────────────────────────
# 📁 VAKA 2 — Sayı Alfabesi
# ─────────────────────────────────────
class TestVaka2SayiAlfabesi:
    def test_sayi_sifresi_cozuldu_mu(self):
        assert n(cevaplar["vaka2"]) == "ada"
        print('\n    🟢 Vaka 2 ÇÖZÜLDÜ! Ada\'nın mesajından kelime 2: "bir"\n')


# ─────────────────────────────────────
# 📁 VAKA 3 — Sezar'ın Mirası
# ─────────────────────────────────────
class TestVaka3SezarinMirasi:
    def test_sezar_sifresi_cozuldu_mu(self):
        assert n(cevaplar["vaka3"]) == "github"
        print('\n    🟢 Vaka 3 ÇÖZÜLDÜ! Ada\'nın mesajından kelime 3: "süper"\n')


# ─────────────────────────────────────
# 📁 VAKA 4 — Görünmez Dosya
# ─────────────────────────────────────
class TestVaka4GorunmezDosya:
    def test_gizli_dosya_bulundu_mu(self):
        assert n(cevaplar["vaka4"]) == "liman"
        print('\n    🟢 Vaka 4 ÇÖZÜLDÜ! Ada\'nın mesajından kelime 4: "güç"\n')


# ─────────────────────────────────────
# 📁 VAKA 5 — Üç Şüpheli
# ─────────────────────────────────────
class TestVaka5UcSupheli:
    def test_dogru_supheli_bulundu_mu(self):
        assert n(cevaplar["vaka5"]) == "defne"
        print('\n    🟢 Vaka 5 ÇÖZÜLDÜ! Ada\'nın mesajından kelime 5: "değil"\n')


# ─────────────────────────────────────
# 📁 VAKA 6 — Makinelerin Dili
# ─────────────────────────────────────
class TestVaka6MakinelerinDili:
    def test_binary_kod_cozuldu_mu(self):
        assert n(cevaplar["vaka6"]) == "bulut"
        print('\n    🟢 Vaka 6 ÇÖZÜLDÜ! Ada\'nın mesajından kelime 6: "ama"\n')


# ─────────────────────────────────────
# 📁 VAKA 7 — Şiirin Sırrı
# ─────────────────────────────────────
class TestVaka7SiirinSirri:
    def test_akrostis_cozuldu_mu(self):
        assert n(cevaplar["vaka7"]) == "yazilim"
        print('\n    🟢 Vaka 7 ÇÖZÜLDÜ! Ada\'nın mesajından kelime 7: "en"\n')


# ─────────────────────────────────────
# 📁 VAKA 8 — Hazine Haritası
# ─────────────────────────────────────
class TestVaka8HazineHaritasi:
    def test_koordinatlar_cozuldu_mu(self):
        assert n(cevaplar["vaka8"]) == "sifre"
        print('\n    🟢 Vaka 8 ÇÖZÜLDÜ! Ada\'nın mesajından kelime 8: "yakın"\n')


# ─────────────────────────────────────
# 📁 VAKA 9 — Bip Bip Biiiip
# ─────────────────────────────────────
class TestVaka9BipBipBiiiip:
    def test_mors_kodu_cozuldu_mu(self):
        assert n(cevaplar["vaka9"]) == "hazir"
        print('\n    🟢 Vaka 9 ÇÖZÜLDÜ! Ada\'nın mesajından kelime 9: "şey"\n')


# ─────────────────────────────────────
# 📁 VAKA 10 — Son Kilit
# ─────────────────────────────────────
class TestVaka10SonKilit:
    def test_son_sifre_cozuldu_mu(self):
        assert n(cevaplar["vaka10"]) == "muhendis"

        print("\n")
        print("    ╔═══════════════════════════════════════════════════════╗")
        print("    ║                                                       ║")
        print("    ║   🎉 TEBRİKLER! TÜM VAKALARI ÇÖZDÜN!                ║")
        print("    ║                                                       ║")
        print('    ║   Ada\'nın Gizli Mesajı:                               ║')
        print('    ║   "Kodlamak bir süper güç değil,                      ║')
        print('    ║    ama en yakın şey odur."                            ║')
        print("    ║                                                       ║")
        print("    ║   Ada'nın Gerçek Kimliği: MÜHENDİS                   ║")
        print("    ║                                                       ║")
        print("    ║   🚀 Pipeline yeşil! Siten deploy ediliyor...         ║")
        print("    ╚═══════════════════════════════════════════════════════╝")
        print("\n")
