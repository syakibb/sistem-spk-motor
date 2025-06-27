# Mekanik Virtual - Sistem Pakar Diagnosis Motor 🔧

Ini adalah aplikasi web sistem pakar yang dibuat untuk tugas mata kuliah Kecerdasan Buatan. Aplikasi ini membantu pengguna melakukan diagnosis awal kerusakan motor berdasarkan gejala yang dialami, lengkap dengan solusi dan estimasi biaya perbaikan.

---

## 🚀 Demo Aplikasi

Aplikasi ini sudah di-deploy dan dapat diakses secara publik melalui Hugging Face Spaces.

**[Coba Mekanik Virtual Sekarang!](https://syakib-mekanik-virtual.hf.space/)**

---

## 💻 Cara Menjalankan di Lokal

Jika Anda ingin menjalankan aplikasi ini di komputer Anda sendiri, ikuti langkah-langkah berikut:

1.  **Clone Repositori**
    Buka terminal atau Git Bash, lalu clone repositori ini ke komputer Anda dan masuk ke dalam foldernya.
    ```bash
    git clone [https://github.com/syakibb/sistem-spk-motor.git](https://github.com/syakibb/sistem-spk-motor.git)
    cd sistem-spk-motor
    ```

2.  **Buat dan Aktifkan Virtual Environment** (Sangat Direkomendasikan)
    Ini akan membuat lingkungan terisolasi untuk proyek Anda agar tidak mengganggu instalasi Python utama.
    ```bash
    # Membuat environment
    python -m venv venv

    # Mengaktifkan environment (di Windows)
    .\venv\Scripts\activate

    # Mengaktifkan environment (di macOS/Linux)
    source venv/bin/activate
    ```

3.  **Install Semua Kebutuhan (Dependencies)**
    Install semua library Python yang dibutuhkan proyek ini dari file `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan Aplikasi**
    Setelah semua instalasi selesai, jalankan aplikasi Flask.
    ```bash
    python app.py
    ```
    Aplikasi akan berjalan dan sebuah tab baru di browser Anda akan otomatis terbuka pada alamat `http://127.0.0.1:5000/`. Jika tidak, buka alamat tersebut secara manual.

---

## 💡 Tentang Mekanik Virtual

Mekanik Virtual adalah sebuah aplikasi web berbasis sistem pakar yang dirancang untuk membantu pengguna melakukan diagnosis awal terhadap masalah atau kerusakan yang terjadi pada sepeda motor. Dengan menggunakan metode penalaran berbasis aturan (*rule-based reasoning*), aplikasi ini akan memandu pengguna melalui serangkaian pertanyaan spesifik, layaknya berkonsultasi dengan seorang mekanik berpengalaman.

Tujuan utama dari aplikasi ini adalah untuk memberikan perkiraan awal mengenai sumber masalah, solusi yang mungkin dilakukan, serta estimasi biaya dan tingkat kesulitan perbaikan, sehingga pengguna dapat mengambil keputusan yang lebih baik sebelum membawa kendaraannya ke bengkel.

---

## 🎓 Latar Belakang Proyek

Aplikasi ini dikembangkan untuk memenuhi tugas besar dari mata kuliah **Kecerdasan Buatan** pada program studi Teknik Informatika di Universitas Pamulang.

**Dosen Pengampu:**
HARDIANSYAH S.Kom., M.M., M.Kom.
*NIDN. 0402078601*

---

## 🛠️ Teknologi yang Digunakan

* **Backend:** Python dengan Framework Flask
* **Mesin Inferensi:** Custom Rule-Based System (Logika Pohon Keputusan)
* **Frontend:** HTML, CSS, dan Bootstrap 5

---

## 👥 Tim Pengembang (Kelompok 3)

* **Asita Husna Dewi Fauziah** (*NIM. 221011450476*)
* **Bagus Pandu Pratama** (*NIM. 221011450274*)
* **Hasna Fikriyah Ramadhani** (*NIM. 221011450626*)
* **Syakib Binnur** (*NIM. 221011450394*)
* **Titik Oktaviani** (*NIM. 221011450541*)