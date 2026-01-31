# data.py

# GEJALA (G1 - G25)
gejala = {
    "G1": "Tidak ada gambar tampil di monitor",
    "G2": "Terdapat garis horizontal/vertikal di monitor",
    "G3": "Tidak ada tampilan awal BIOS",
    "G4": "Muncul pesan error pada BIOS",
    "G5": "Alarm BIOS berbunyi",
    "G6": "Terdengar suara aneh pada HDD",
    "G7": "Sering hang/crash saat menjalankan aplikasi",
    "G8": "Selalu scandisk ketika booting",
    "G9": "Muncul pesan error saat menjalankan game/aplikasi grafis",
    "G10": "Device driver tidak terdeteksi di device manager",
    "G11": "Tiba-tiba OS restart otomatis",
    "G12": "Muncul blue screen pada OS Windows",
    "G13": "Suara tidak keluar meski driver & setting benar",
    "G14": "Muncul error saat menjalankan aplikasi audio",
    "G15": "Error saat pertama OS di-load dari HDD",
    "G16": "Semua kipas tidak berputar",
    "G17": "Komputer sering mati tiba-tiba",
    "G18": "Windows kekurangan virtual memory",
    "G19": "Aplikasi lambat / respon lambat",
    "G20": "Kinerja grafis sangat berat",
    "G21": "Device tidak terdeteksi di BIOS",
    "G22": "Informasi device salah di BIOS",
    "G23": "Hanya sebagian perangkat yang bekerja",
    "G24": "Sebagian/seluruh input keyboard mati",
    "G25": "Pointer mouse tidak merespon"
}

    # RULE J1 - J17 (RULE UTAMA + RULE TUNGGAL)

rules = [

    # =====================
    # RULE UTAMA (JURNAL)
    # =====================
    {"if": ["G1", "G2"], "then": "Monitor Rusak"},
    {"if": ["G3", "G4", "G5", "G11", "G12"], "then": "Memori Rusak"},
    {"if": ["G6", "G7", "G8", "G10", "G21", "G22"], "then": "HDD Rusak"},
    {"if": ["G1", "G3", "G5", "G9", "G10", "G12", "G13"], "then": "VGA Rusak"},
    {"if": ["G10", "G13", "G14"], "then": "Sound Card Rusak"},
    {"if": ["G11", "G12", "G15"], "then": "OS Bermasalah"},
    {"if": ["G7", "G12"], "then": "Aplikasi Rusak"},
    {"if": ["G16", "G17"], "then": "PSU Rusak"},
    {"if": ["G1", "G3", "G4", "G5"], "then": "Prosesor Rusak"},
    {"if": ["G18", "G19"], "then": "Memory Kurang"},
    {"if": ["G9", "G20"], "then": "Memory VGA Kurang"},
    {"if": ["G9", "G19"], "then": "Clock Prosesor Kurang Tinggi"},
    {"if": ["G21"], "then": "Kabel IDE/SATA Rusak"},
    {"if": ["G5", "G23"], "then": "Kurang Daya pada PSU"},
    {"if": ["G10"], "then": "Perangkat USB Rusak"},
    {"if": ["G10", "G24"], "then": "Keyboard Rusak"},
    {"if": ["G10", "G25"], "then": "Mouse Rusak"},

    # =====================
    # RULE TUNGGAL (INDIKASI AWAL)
    # =====================

    {"if": ["G1"], "then": "Indikasi Monitor / VGA Bermasalah"},
    {"if": ["G2"], "then": "Indikasi Monitor Bermasalah"},
    {"if": ["G3"], "then": "Indikasi Memori / Prosesor Bermasalah"},
    {"if": ["G4"], "then": "Indikasi BIOS / Prosesor Bermasalah"},
    {"if": ["G5"], "then": "Indikasi Memori / PSU Bermasalah"},
    {"if": ["G6"], "then": "Indikasi HDD Bermasalah"},
    {"if": ["G7"], "then": "Indikasi Aplikasi / HDD Bermasalah"},
    {"if": ["G8"], "then": "Indikasi HDD Bermasalah"},
    {"if": ["G9"], "then": "Indikasi VGA Bermasalah"},
    {"if": ["G10"], "then": "Indikasi Driver / USB / Peripheral Bermasalah"},
    {"if": ["G11"], "then": "Indikasi OS / Memori Bermasalah"},
    {"if": ["G12"], "then": "Indikasi Memori / OS Bermasalah"},
    {"if": ["G13"], "then": "Indikasi Sound Card Bermasalah"},
    {"if": ["G14"], "then": "Indikasi Sound Card Bermasalah"},
    {"if": ["G15"], "then": "Indikasi OS Bermasalah"},
    {"if": ["G16"], "then": "Indikasi PSU Bermasalah"},
    {"if": ["G17"], "then": "Indikasi PSU Bermasalah"},
    {"if": ["G18"], "then": "Indikasi Kekurangan Memory"},
    {"if": ["G19"], "then": "Indikasi Kinerja Sistem Rendah"},
    {"if": ["G20"], "then": "Indikasi Memory VGA Kurang"},
    {"if": ["G21"], "then": "Indikasi Kabel / HDD Tidak Terdeteksi"},
    {"if": ["G22"], "then": "Indikasi Konfigurasi BIOS Bermasalah"},
    {"if": ["G23"], "then": "Indikasi Daya PSU Tidak Stabil"},
    {"if": ["G24"], "then": "Indikasi Keyboard Bermasalah"},
    {"if": ["G25"], "then": "Indikasi Mouse Bermasalah"},
]


