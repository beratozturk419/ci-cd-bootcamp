import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.puzzle import (
    topla,
    tersten_yaz,
    bas_harf_buyut,
    tek_sayilari_filtrele,
    en_buyuk_bul,
    palindrom_mu,
    kelime_say,
    asal_mi,
    sezar_coz,
    gizli_mesaj,
)

# ╔═══════════════════════════════════════════════════════════╗
# ║  🔍 KAYIP YAZILIMCININ ŞİFRESİ — TEST DOSYASI           ║
# ║                                                           ║
# ║  ⚠️  BU DOSYAYI DEĞİŞTİRMEYİN!                          ║
# ║  📝  Sadece src/puzzle.py dosyasını düzenleyin.            ║
# ║                                                           ║
# ║  Her geçen test bir ipucu kelimesi ortaya çıkarır.         ║
# ║  Tüm testler geçtiğinde Ada'nın mesajı açığa çıkar!       ║
# ╚═══════════════════════════════════════════════════════════╝

IPUCLARI = {}


# ─────────────────────────────────────
# 📌 İPUCU 1/10 — Toplama
# ─────────────────────────────────────
class TestIpucu1Toplama:
    def test_iki_pozitif_sayiyi_toplar(self):
        assert topla(3, 5) == 8

    def test_negatif_sayilarla_calisir(self):
        assert topla(-3, -7) == -10

    def test_sifir_ile_calisir(self):
        assert topla(0, 42) == 42

    def test_ipucu_kelimesi_ortaya_cikti(self):
        assert topla(100, 200) == 300
        IPUCLARI[1] = "KODLAMAK"
        print('\n    🟢 İpucu 1/10: "KODLAMAK"\n')


# ─────────────────────────────────────
# 📌 İPUCU 2/10 — Tersine Çevirme
# ─────────────────────────────────────
class TestIpucu2TersineCevirme:
    def test_basit_metni_cevirir(self):
        assert tersten_yaz("merhaba") == "abahrem"

    def test_tek_karakteri_dondurur(self):
        assert tersten_yaz("a") == "a"

    def test_ipucu_kelimesi_ortaya_cikti(self):
        assert tersten_yaz("rib") == "bir"
        IPUCLARI[2] = "BIR"
        print('\n    🟢 İpucu 2/10: "BİR"\n')


# ─────────────────────────────────────
# 📌 İPUCU 3/10 — Baş Harf Büyütme
# ─────────────────────────────────────
class TestIpucu3BasHarfBuyutme:
    def test_tek_kelimeyi_buyutur(self):
        assert bas_harf_buyut("merhaba") == "Merhaba"

    def test_birden_fazla_kelimeyi_buyutur(self):
        assert bas_harf_buyut("merhaba dünya") == "Merhaba Dünya"

    def test_zaten_buyuk_harfleri_korur(self):
        assert bas_harf_buyut("javaScript dili") == "JavaScript Dili"

    def test_ipucu_kelimesi_ortaya_cikti(self):
        assert bas_harf_buyut("süper güç") == "Süper Güç"
        IPUCLARI[3] = "SUPER"
        print('\n    🟢 İpucu 3/10: "SÜPER"\n')


# ─────────────────────────────────────
# 📌 İPUCU 4/10 — Tek Sayı Filtreleme
# ─────────────────────────────────────
class TestIpucu4TekSayiFiltrele:
    def test_karisik_diziden_tek_sayilari_secer(self):
        assert tek_sayilari_filtrele([1, 2, 3, 4, 5]) == [1, 3, 5]

    def test_tum_cift_dizide_bos_doner(self):
        assert tek_sayilari_filtrele([2, 4, 6]) == []

    def test_negatif_tek_sayilari_da_bulur(self):
        assert tek_sayilari_filtrele([-3, -2, -1, 0]) == [-3, -1]

    def test_ipucu_kelimesi_ortaya_cikti(self):
        sonuc = tek_sayilari_filtrele([10, 21, 32, 43, 54])
        assert sonuc == [21, 43]
        IPUCLARI[4] = "GUC"
        print('\n    🟢 İpucu 4/10: "GÜÇ"\n')


# ─────────────────────────────────────
# 📌 İPUCU 5/10 — En Büyük Eleman
# ─────────────────────────────────────
class TestIpucu5EnBuyukEleman:
    def test_pozitif_sayilardan_en_buyugunu_bulur(self):
        assert en_buyuk_bul([3, 7, 2, 9, 1]) == 9

    def test_negatif_sayilarla_calisir(self):
        assert en_buyuk_bul([-5, -1, -10]) == -1

    def test_tek_elemanli_dizi(self):
        assert en_buyuk_bul([42]) == 42

    def test_ipucu_kelimesi_ortaya_cikti(self):
        assert en_buyuk_bul([88, 12, 55, 3, 99, 44]) == 99
        IPUCLARI[5] = "DEGIL"
        print('\n    🟢 İpucu 5/10: "DEĞİL"\n')


# ─────────────────────────────────────
# 📌 İPUCU 6/10 — Palindrom Kontrolü
# ─────────────────────────────────────
class TestIpucu6PalindromKontrolu:
    def test_palindromu_tanir(self):
        assert palindrom_mu("aba") is True

    def test_palindrom_olmayani_reddeder(self):
        assert palindrom_mu("merhaba") is False

    def test_buyuk_kucuk_harf_farkini_yok_sayar(self):
        assert palindrom_mu("Ana") is True

    def test_bosluklari_yok_sayar(self):
        assert palindrom_mu("a man a plan a canal panama") is True

    def test_ipucu_kelimesi_ortaya_cikti(self):
        assert palindrom_mu("kayak") is True
        assert palindrom_mu("javascript") is False
        IPUCLARI[6] = "AMA"
        print('\n    🟢 İpucu 6/10: "AMA"\n')


# ─────────────────────────────────────
# 📌 İPUCU 7/10 — Kelime Sayacı
# ─────────────────────────────────────
class TestIpucu7KelimeSayaci:
    def test_basit_cumledeki_kelimeleri_sayar(self):
        assert kelime_say("merhaba dünya") == 2

    def test_fazla_bosluklari_yok_sayar(self):
        assert kelime_say("  bir   iki   üç  ") == 3

    def test_tek_kelime(self):
        assert kelime_say("merhaba") == 1

    def test_bos_string_sifir_doner(self):
        assert kelime_say("") == 0
        assert kelime_say("   ") == 0

    def test_ipucu_kelimesi_ortaya_cikti(self):
        assert kelime_say("CI CD pipeline deploy test") == 5
        IPUCLARI[7] = "EN"
        print('\n    🟢 İpucu 7/10: "EN"\n')


# ─────────────────────────────────────
# 📌 İPUCU 8/10 — Asal Sayı Kontrolü
# ─────────────────────────────────────
class TestIpucu8AsalSayiKontrolu:
    def test_asal_sayilari_tanir(self):
        assert asal_mi(2) is True
        assert asal_mi(7) is True
        assert asal_mi(13) is True

    def test_asal_olmayan_sayilari_reddeder(self):
        assert asal_mi(4) is False
        assert asal_mi(9) is False
        assert asal_mi(15) is False

    def test_ozel_durumlari_dogru_doner(self):
        assert asal_mi(0) is False
        assert asal_mi(1) is False
        assert asal_mi(-5) is False

    def test_ipucu_kelimesi_ortaya_cikti(self):
        assert asal_mi(97) is True
        assert asal_mi(100) is False
        IPUCLARI[8] = "YAKIN"
        print('\n    🟢 İpucu 8/10: "YAKIN"\n')


# ─────────────────────────────────────
# 📌 İPUCU 9/10 — Sezar Şifre Çözücü
# ─────────────────────────────────────
class TestIpucu9SezarSifreCozucu:
    def test_basit_kaydirma_cozer(self):
        assert sezar_coz("CDE", 2) == "ABC"

    def test_z_yi_gecen_kaydirmayi_cozer(self):
        assert sezar_coz("ABC", 3) == "XYZ"

    def test_buyuk_kaydirma_degeri_ile_calisir(self):
        assert sezar_coz("LIPPS", 4) == "HELLO"

    def test_ipucu_kelimesi_ortaya_cikti(self):
        assert sezar_coz("VHB", 5) == "QCW"
        assert sezar_coz("FRGODPDN", 3) == "CODLAMAK"
        IPUCLARI[9] = "SEY"
        print('\n    🟢 İpucu 9/10: "ŞEY"\n')


# ─────────────────────────────────────
# 📌 İPUCU 10/10 — Gizli Mesajı Birleştir
# ─────────────────────────────────────
class TestIpucu10GizliMesajiBirlestir:
    def test_sirali_anahtarlari_birlestirir(self):
        assert gizli_mesaj({1: "hello", 2: "world"}) == "hello world"

    def test_karisik_sirali_anahtarlari_duzgun_birlestirir(self):
        assert gizli_mesaj({3: "!", 1: "CI", 2: "CD"}) == "CI CD !"

    def test_tek_ipucu(self):
        assert gizli_mesaj({1: "merhaba"}) == "merhaba"

    def test_son_ipucu_adanin_mesaji_ortaya_cikiyor(self):
        adanin_mesaji = gizli_mesaj({
            5: "degil",
            2: "bir",
            8: "yakin",
            1: "Kodlamak",
            4: "guc",
            10: "odur",
            6: "ama",
            3: "super",
            9: "sey",
            7: "en",
        })
        assert adanin_mesaji == "Kodlamak bir super guc degil ama en yakin sey odur"
        IPUCLARI[10] = "ODUR"

        print("\n")
        print("    ╔═══════════════════════════════════════════════════╗")
        print("    ║  🎉 TEBRİKLER! TÜM İPUÇLARINI ÇÖZDÜN!          ║")
        print("    ║                                                   ║")
        print('    ║  Ada\'nın Gizli Mesajı:                            ║')
        print('    ║  "Kodlamak bir süper güç değil,                   ║')
        print('    ║   ama en yakın şey odur."                         ║')
        print("    ║                                                   ║")
        print("    ║  🚀 Pipeline yeşil! Deploy başlıyor...            ║")
        print("    ╚═══════════════════════════════════════════════════╝")
        print("\n")
