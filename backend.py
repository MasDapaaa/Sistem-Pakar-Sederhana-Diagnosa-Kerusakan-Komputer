# backend.py
from data import rules

def forward_chaining(fakta):
    hasil_utama = []
    indikasi = []

    gejala_dipakai_utama = set()

    # =========================
    # 1. Cari RULE UTAMA
    # =========================
    for rule in rules:
        if len(rule["if"]) > 1:
            if all(g in fakta for g in rule["if"]):
                hasil_utama.append({
                    "kerusakan": rule["then"],
                    "gejala": rule["if"]
                })
                gejala_dipakai_utama.update(rule["if"])

    # =========================
    # 2. Cari INDIKASI PER GEJALA
    # =========================
    for g in fakta:
        # kalau gejala ini SUDAH dipakai rule utama → skip
        if g in gejala_dipakai_utama:
            continue

        # cari rule tunggal yang cocok dengan gejala ini
        for rule in rules:
            if len(rule["if"]) == 1 and rule["if"][0] == g:
                indikasi.append({
                    "kerusakan": rule["then"],
                    "gejala": g
                })

    return hasil_utama, indikasi
