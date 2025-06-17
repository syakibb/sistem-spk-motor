# Nama file: app.py (Versi 2.0 - Lebih Kompleks)

from flask import Flask, render_template, request, session, redirect, url_for
from engine import DiagnosisEngine
import webbrowser
from threading import Timer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kunci-rahasia-12345'

# 'Peta Pengetahuan' kita sekarang jauh lebih besar
knowledge_map = {
    'gejala_utama': {
        'pertanyaan': 'Apa gejala utama yang paling Anda rasakan pada motor?',
        'pilihan': {
            'motor_tidak_menyala': 'Motor tidak mau menyala sama sekali.',
            'motor_brebet': 'Performa motor menurun (brebet/tersendat).',
            'suara_mesin_kasar': 'Terdengar suara mesin yang tidak normal/kasar.'
        }
    },
    'kondisi_lampu': {
        'pertanyaan': 'Saat kunci kontak di-ON-kan, bagaimana kondisi lampu indikator di speedometer?',
        'pilihan': {
            'lampu_mati_total': 'Lampu mati total, tidak ada tanda kehidupan sama sekali.',
            'lampu_normal': 'Lampu menyala normal dan terang.'
        }
    },
    'reaksi_starter': {
        'pertanyaan': 'Saat tombol starter ditekan, apa reaksi yang terjadi?',
        'pilihan': {
            'bunyi_cetek': "Hanya terdengar bunyi 'cetek-cetek'.",
            'dinamo_lemah': "Dinamo starter berputar, tapi lemah.",
            'tidak_ada_respon': "Tidak ada suara atau reaksi apapun."
        }
    },
    'kapan_brebet': {
        'pertanyaan': 'Kapan gejala brebet paling terasa?',
        'pilihan': {
            'rpm_bawah': 'Saat putaran gas rendah atau saat baru jalan.',
            'rpm_atas': 'Saat putaran gas tinggi atau saat kecepatan tinggi.'
        }
    },
    'jenis_suara_kasar': {
        'pertanyaan': 'Seperti apa suara kasar yang terdengar?',
        'pilihan': {
            'kletek_di_head': "Bunyi 'kletek-kletek' atau 'tik-tik-tik' di bagian atas mesin (head).",
            'kemrosok_di_mesin_tengah': "Bunyi 'kemrosok' atau 'klotok-klotok' dari bagian tengah/bawah mesin."
        }
    }
}

@app.route('/')
def index():
    session.clear()
    session['gejala_list'] = []
    return redirect(url_for('diagnose'))

@app.route('/diagnose', methods=['GET', 'POST'])
def diagnose():
    if 'gejala_list' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        jawaban_user = request.form['jawaban']
        session['gejala_list'].append(jawaban_user)
        session.modified = True

    engine = DiagnosisEngine()
    # Berikan seluruh riwayat jawaban ke engine
    result = engine.run(session['gejala_list'])

    if result:
        if 'diagnosis' in result:
            return render_template('hasil.html', hasil=result)
        elif 'tanya' in result and result['tanya'] in knowledge_map:
            data_pertanyaan = knowledge_map[result['tanya']]
            return render_template('pertanyaan.html', data=data_pertanyaan)
    
    # Jika alur buntu
    return render_template('hasil.html', hasil={'diagnosis': 'Tidak dapat menemukan diagnosis.', 'solusi': 'Sistem tidak memiliki cukup informasi untuk menyimpulkan. Mohon maaf dan silakan konsultasikan dengan mekanik.'})


def buka_browser():
      webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    Timer(1, buka_browser).start()
    app.run(debug=True)