# Nama file: app.py (Versi 4.8 - Final Tanpa Redirect untuk Stabilitas Session)

from flask import Flask, render_template, request, session, redirect, url_for
from engine import DiagnosisEngine
import webbrowser
from threading import Timer
import os

app = Flask(__name__)
# Menggunakan kunci yang lebih kuat dan acak, ini praktik yang baik
app.config['SECRET_KEY'] = 'b1d8f2a7e9c3a0d4e5f6g7h8i9j0k1l2'

# knowledge_map tidak perlu diubah
knowledge_map = {
    'tanya_tipe_motor': {'pertanyaan': 'Pertama, apa tipe umum motor Anda?', 'pilihan': { 'matic': 'Matic (CVT)', 'manual': 'Manual (Gigi / Rantai)' }},
    'tanya_sistem_bb': {'pertanyaan': 'Apa sistem bahan bakar yang digunakan motor Anda?', 'pilihan': { 'karburator': 'Karburator', 'injeksi': 'Injeksi (FI)' }},
    'gejala_utama': {
        'pertanyaan': 'Baik, sekarang apa gejala utama yang paling Anda rasakan?',
        'pilihan': {
            'motor_tidak_menyala': 'Motor tidak mau menyala sama sekali.',
            'motor_brebet': 'Performa motor menurun (brebet/tersendat).',
            'masalah_penggerak': 'Masalah pada area penggerak roda (CVT/Rantai).', 
            'suara_mesin_kasar': 'Terdengar suara mesin yang tidak normal/kasar.',
            'asap_knalpot_aneh': 'Knalpot mengeluarkan asap yang tidak wajar.'
        }
    },
    'kondisi_lampu': { 'pertanyaan': 'Saat kunci kontak di-ON-kan, bagaimana kondisi lampu indikator?', 'pilihan': {'lampu_mati_total': 'Mati total', 'lampu_normal': 'Menyala normal'} },
    'reaksi_starter': { 'pertanyaan': 'Saat tombol starter ditekan, apa reaksinya?', 'pilihan': {'bunyi_cetek': "Hanya bunyi 'cetek'", 'dinamo_lemah': 'Dinamo berputar lemah', 'tidak_ada_respon': 'Tidak ada respon'} },
    'sudah_jumper_aki': { 'pertanyaan': "Untuk memastikan, apakah Anda sudah mencoba melakukan jumper dari aki motor lain yang sehat?", 'pilihan': {'sudah_dan_sama': "Sudah, tapi hasilnya tetap sama (hanya bunyi 'cetek').", 'belum_coba': "Belum, saya belum mencoba jumper."}},
    'kapan_brebet_karbu': { 'pertanyaan': 'Kapan brebet paling terasa (untuk Karburator)?', 'pilihan': {'rpm_bawah': 'Saat RPM rendah', 'rpm_atas': 'Saat RPM tinggi'} },
    'kondisi_mil': { 'pertanyaan': 'Apakah lampu indikator mesin/MIL (Malfunction Indicator Lamp) menyala atau berkedip (untuk Injeksi)?', 'pilihan': {'mil_menyala': 'Ya, menyala/berkedip', 'mil_tidak_menyala': 'Tidak, lampu MIL normal'} },
    'gejala_cvt': { 'pertanyaan': 'Apa gejala yang Anda rasakan pada area CVT (untuk Matic)?', 'pilihan': {'gredek': 'Getar/Gredek saat tarikan awal.', 'tarikan_selip': 'Tarikan terasa berat dan seperti selip.'}},
    'gejala_rantai': { 'pertanyaan': 'Apa gejala yang Anda rasakan pada Rantai & Gigi (untuk Manual)?', 'pilihan': {'rantai_berisik': 'Rantai sangat berisik.', 'gigi_keras': 'Perpindahan gigi terasa keras atau kopling selip.'}},
    'jenis_suara_kasar': { 'pertanyaan': 'Seperti apa suara kasar yang terdengar?', 'pilihan': {'kletek_di_head': "Bunyi 'kletek-kletek' di bagian atas mesin (head).", 'kemrosok_di_mesin_tengah': "Bunyi 'kemrosok' dari bagian tengah/bawah mesin."}},
    'warna_asap': { 'pertanyaan': 'Apa warna asap yang keluar dari knalpot?', 'pilihan': {'putih_tipis_pagi_hari': 'Putih tipis saat mesin dingin & lalu hilang.', 'putih_tebal_terus': 'Putih tebal terus-menerus.', 'hitam_pekat': 'Hitam pekat dan berbau bensin.'}}
}


# --- RUTE UTAMA YANG DIROMBAK TOTAL UNTUK MENGHINDARI REDIRECT ---
@app.route('/', methods=['GET', 'POST'])
def diagnose():
    # Selalu cek dan inisialisasi sesi di awal jika belum ada
    if 'konteks_motor' not in session:
        session['konteks_motor'] = {}
        session['gejala_list'] = []

    # Jika ada parameter 'reset', bersihkan sesi dan mulai dari awal
    if request.args.get('reset'):
        session.clear()
        session['konteks_motor'] = {}
        session['gejala_list'] = []

    # Proses jawaban HANYA jika metode adalah POST
    if request.method == 'POST':
        jawaban_user = request.form.get('jawaban')
        if jawaban_user:
            if 'tipe' not in session['konteks_motor']:
                session['konteks_motor']['tipe'] = jawaban_user
            elif 'sistem_bb' not in session['konteks_motor']:
                session['konteks_motor']['sistem_bb'] = jawaban_user
            else:
                session['gejala_list'].append(jawaban_user)
            session.modified = True
    
    # Bagian ini akan berjalan untuk GET dan SETELAH data POST diproses
    jawaban_sebelumnya = session.get('pilihan_sebelumnya')
    riwayat_gabungan = list(session.get('konteks_motor', {}).values()) + session.get('gejala_list', [])

    def render_pertanyaan(key):
        data_pertanyaan = knowledge_map[key].copy()
        data_pertanyaan['jawaban_sebelumnya'] = jawaban_sebelumnya
        if 'pilihan_sebelumnya' in session:
            session.pop('pilihan_sebelumnya')
        return render_template('pertanyaan.html', data=data_pertanyaan, riwayat_jawaban=riwayat_gabungan)

    # Logika untuk menentukan pertanyaan apa yang akan ditampilkan
    if 'tipe' not in session.get('konteks_motor', {}):
        return render_pertanyaan('tanya_tipe_motor')
    if 'sistem_bb' not in session.get('konteks_motor', {}):
        return render_pertanyaan('tanya_sistem_bb')

    if not session.get('gejala_list', []):
        data_pertanyaan = knowledge_map['gejala_utama'].copy()
        tipe_motor = session['konteks_motor'].get('tipe')
        if tipe_motor == 'matic':
            data_pertanyaan['pilihan']['masalah_penggerak'] = 'Masalah pada area penggerak roda (CVT).'
        elif tipe_motor == 'manual':
            data_pertanyaan['pilihan']['masalah_penggerak'] = 'Masalah pada area penggerak roda (Rantai & Gigi).'
        data_pertanyaan['jawaban_sebelumnya'] = jawaban_sebelumnya
        return render_pertanyaan('gejala_utama')
    
    # Jika semua konteks sudah ada, jalankan engine diagnosis
    engine = DiagnosisEngine()
    result = engine.run(session['gejala_list'], session['konteks_motor'])

    if result:
        if 'diagnosis' in result:
            return render_template('hasil.html', hasil=result)
        elif 'tanya' in result and result['tanya'] in knowledge_map:
            return render_pertanyaan(result['tanya'])
            
    return render_template('hasil.html', hasil={'diagnosis': 'Alur Diagnosis Selesai.', 'solusi': 'Sistem tidak memiliki cukup informasi untuk menyimpulkan.'})


@app.route('/kembali')
def kembali():
    jawaban_terakhir = None
    if session.get('gejala_list'):
        jawaban_terakhir = session['gejala_list'].pop()
    elif session.get('konteks_motor', {}).get('sistem_bb'):
        jawaban_terakhir = session['konteks_motor'].pop('sistem_bb', None)
    elif session.get('konteks_motor', {}).get('tipe'):
        jawaban_terakhir = session['konteks_motor'].pop('tipe', None)
    
    if jawaban_terakhir:
        session['pilihan_sebelumnya'] = jawaban_terakhir
    session.modified = True
    return redirect(url_for('diagnose'))


@app.route('/tentang')
def tentang():
    return render_template('tentang.html')


def buka_browser():
      webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        Timer(1, buka_browser).start()
    app.run(debug=True)