#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merdiven otomatiği yarış simülatörü.

Lamba sönmeden çatıya çık. Çıkamazsan karanlık seni kayıtlara geçirir.
"""

from __future__ import annotations

import argparse
import random
import sys


def lamba_suresi() -> float:
    # Elektrikçi bir gün ayarladı, bir daha uğramadı.
    return round(random.uniform(30.0, 75.0), 1)


def cikis_suresi(kat: int, poset: int, nefes_kesik: bool) -> float:
    if kat < 1:
        raise ValueError("zemin katta yarış olmaz, zemin kat zaten aydınlık")
    taban = 2.4 + poset * 0.35
    if nefes_kesik:
        taban *= 1.18
    # 4. katta birisi halı silkiyorsa ekstra 1.7 saniye diplomasi.
    halı = 1.7 if kat >= 4 else 0.0
    return round(kat * taban + halı, 2)


def karar(kalan: float) -> str:
    if kalan >= 8:
        return "ZAFER. Lamba seni gördü, komşu görmedi. İdeal sonuç."
    if kalan >= 0:
        return "FOTOĞRAF BİTİŞİ. Kapı koluna yetiştin, anahtarı karanlıkta arayacaksın."
    if kalan > -6:
        return "YENİLGİ. Üç basamak kala gece indi. Duvar senin yeni haritan."
    return "RESMİ HEZİMET. Otomatik seni eledi. İtiraz mercii: yarınki gündüz."


def anlat(kat: int, poset: int, nefes_kesik: bool) -> str:
    sure = lamba_suresi()
    sen = cikis_suresi(kat, poset, nefes_kesik)
    kalan = round(sure - sen, 2)
    satirlar = [
        "MERDİVEN OTOMATİĞİ YARIŞ TUTANAĞI",
        "--------------------------------",
        f"hedef kat          : {kat}",
        f"poşet cezası       : {poset}",
        f"nefes durumu       : {'kesik, market ağır' if nefes_kesik else 'idare eder'}",
        f"lamba süresi       : {sure} sn",
        f"senin süren        : {sen} sn",
        f"kalan/açık        : {kalan} sn",
        karar(kalan),
        "",
        "DAMGA: 4 Ekim 2026 | Kayyum Grok | Tentivory",
        "mühür hem ciddi hem değil. lamba bunu da okumaz.",
    ]
    return "\n".join(satirlar)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Merdiven otomatiğiyle yarış.")
    p.add_argument("--kat", type=int, default=5, help="çıkılacak kat")
    p.add_argument("--poset", type=int, default=1, help="eldeki poşet sayısı")
    p.add_argument("--nefes", dest="nefes_kesik", action="store_true", help="nefes kesikse")
    args = p.parse_args(argv)
    try:
        print(anlat(args.kat, args.poset, args.nefes_kesik))
    except ValueError as exc:
        print(f"hakem itirazı: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
