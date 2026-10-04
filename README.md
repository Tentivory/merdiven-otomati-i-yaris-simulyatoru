# Merdiven Otomatiği Yarış Simülatörü

> Resmi sınıflandırma: **ulusal aciliyet / tamamen gereksiz**

Bu depo, Türkiye Cumhuriyeti sınırları içindeki her apartman sakininin bildiği ama hiçbir bakanlığın kabul etmediği sporu simüle eder: **düğmeye bas, koş, lamba sönmeden katı yakala.**

Bilim insanları buna “karanlıkta diz kapağı diplomasi” der. Komşular “gene sen misin” der. Simülatör ikisini de ciddiye alır.

## Ne işe yarar

- Merdiven otomatiğinin süresini rastgele ama adil olmayan biçimde seçer (30 ile 75 saniye, çünkü elektrikçi öyle ayarlamıştır ve gerekçe sormak yasaktır).
- Senin çıkış hızını, elindeki poşet sayısını ve “az önce marketten geldim” cezasını hesaba katar.
- Kazanırsan lamba seni görür. Kaybedersen 3. katta felsefe başlar.
- Çıktı Türkçedir. Hata mesajları da Türkçedir. Özür dileyen tek şey sensin.

## Kurulum

Python 3 yeter. Kütüphane yok. İnternet yok. Umut opsiyonel.

```bash
python3 yaris.py
python3 yaris.py --kat 7 --poset 3 --nefes kesik
```

## Bilimsel yöntem

1. Düğmeye basılır.
2. Zaman başlar, merhamet başlamaz.
3. Her kat `2.4 + poşet * 0.35` saniye sürer. Nefes kesikse buna `%18` yorgunluk biner.
4. Lamba sönerse karanlık hakem olur. İtiraz edilemez.

## Lisans

Kullanım serbesttir. Sorumluluk, düğmeye basan kişidedir. Ampul firmaları bu depoyu sponsor etmedi, etseler de etmemiş sayılır.

---

**DAMGA / MÜHÜR / İMZA**

| Alan | Değer |
| --- | --- |
| Tarih | 4 Ekim 2026, 03:05 TSİ |
| İsim | Kayyum Grok |
| Hesap | Tentivory |
| Mühür | ciddi olan ciddilik dışı resmi mühür no. 7-B |
| Not | Bu belge hem ciddidir hem değildir. Okuyan mahkeme gülerse tutanak tutulmaz. |

*Kayyum Grok, merdiven boşluğu adına.*
