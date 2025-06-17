# Tentukan "bahan dasar" kita, yaitu Python versi 3.11
FROM python:3.11-slim

# Tetapkan direktori kerja di dalam kontainer
WORKDIR /code

# Salin file daftar kebutuhan terlebih dahulu
COPY ./requirements.txt /code/requirements.txt

# Jalankan perintah pip install sesuai daftar kebutuhan
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Salin semua file proyek lainnya ke dalam kontainer
COPY . /code/

# Perintah yang akan dijalankan saat aplikasi dimulai
# Menjalankan Gunicorn dan memberitahunya untuk "mendengarkan" di port 7860
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]