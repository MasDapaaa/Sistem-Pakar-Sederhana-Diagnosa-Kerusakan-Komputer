# 🧠 Sistem Pakar Diagnosa Kerusakan Komputer
Metode **Forward Chaining** berbasis Python & Streamlit

## 📌 Deskripsi Proyek
Proyek ini merupakan **Sistem Pakar** yang digunakan untuk membantu mendiagnosa kerusakan pada komputer berdasarkan **gejala-gejala** yang dialami pengguna.

Sistem bekerja menggunakan metode **Forward Chaining**, yaitu penalaran yang dimulai dari **fakta (gejala)** menuju **kesimpulan (diagnosa kerusakan)** berdasarkan aturan (rule) yang telah ditentukan.

Aplikasi ini dibuat berbasis **web** menggunakan **Streamlit**, sehingga mudah dijalankan dan digunakan.

---

## 🧠 Metode yang Digunakan
### Forward Chaining
Forward Chaining adalah metode inferensi yang:
- Memulai penalaran dari **fakta-fakta awal (gejala)**
- Mencocokkan fakta dengan **rule**
- Menghasilkan **diagnosis utama** dan **indikasi kerusakan lainnya**

Pada sistem ini:
- **Rule utama** → diagnosis utama (menggunakan lebih dari satu gejala)
- **Rule tunggal** → indikasi awal (jika tidak termasuk rule utama)

---

pip install streamlit

streamlit run frontend.py
