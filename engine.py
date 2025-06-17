# Nama file: engine.py (Versi 4.2 - Melengkapi Semua Aturan)

class DiagnosisEngine:
    def run(self, gejala_list, konteks_motor):
        if not gejala_list:
            return {'tanya': 'gejala_utama'}

        gejala_utama = gejala_list[0]
        tipe_motor = konteks_motor.get('tipe')
        sistem_bb = konteks_motor.get('sistem_bb')

        # --- ALUR 1: MASALAH STARTER ---
        if gejala_utama == 'motor_tidak_menyala':
            if len(gejala_list) == 1: return {'tanya': 'kondisi_lampu'}
            kondisi_lampu = gejala_list[1]
            if kondisi_lampu == 'lampu_mati_total':
                return {'diagnosis': "Masalah pada sumber daya utama (Aki atau Sekring).", 'solusi': "Periksa tegangan Aki. Jika di bawah 12V, coba charge atau ganti. Periksa juga Sekring (fuse) utama.", 'estimasi_biaya': "Rp 25.000 (sekring) - Rp 350.000 (aki baru)", 'kesulitan': "Bisa dikerjakan sendiri"}
            elif kondisi_lampu == 'lampu_normal':
                if len(gejala_list) == 2: return {'tanya': 'reaksi_starter'}
                reaksi_starter = gejala_list[2]
                if reaksi_starter == 'bunyi_cetek':
                    if len(gejala_list) == 3: return {'tanya': 'sudah_jumper_aki'}
                    sudah_jumper = gejala_list[3]
                    if sudah_jumper == 'sudah_dan_sama':
                        return {'diagnosis': "100% Relay Starter (Bendik) rusak.", 'solusi': "Ganti Relay Starter dengan yang baru. Masalah bukan pada aki Anda.", 'estimasi_biaya': "Rp 50.000 - Rp 125.000", 'kesulitan': "Mekanik dianjurkan"}
                    elif sudah_jumper == 'belum_coba':
                        return {'diagnosis': "Kemungkinan besar Relay Starter, tapi bisa juga Aki lemah.", 'solusi': "Lakukan jumper dari aki motor lain. Jika menyala, ganti aki Anda. Jika tetap sama, ganti Relay Starter.", 'estimasi_biaya': "Rp 50.000 (relay) - Rp 350.000 (aki)", 'kesulitan': "Bisa dikerjakan sendiri"}
                elif reaksi_starter == 'dinamo_lemah':
                    return {'diagnosis': "Aki soak / tegangan kurang.", 'solusi': "Aki tidak memiliki cukup daya untuk memutar dinamo dengan kuat. Segera isi ulang (charge) atau ganti Aki.", 'estimasi_biaya': "Rp 150.000 - Rp 350.000", 'kesulitan': "Bisa dikerjakan sendiri"}
                elif reaksi_starter == 'tidak_ada_respon':
                    return {'diagnosis': "Masalah pada jalur tombol starter.", 'solusi': "Periksa saklar/tombol starter di stang, kemungkinan kotor atau rusak. Periksa juga koneksi kabel yang menuju ke relay starter.", 'estimasi_biaya': "Rp 30.000 - Rp 75.000", 'kesulitan': "Mekanik dianjurkan"}

        # --- ALUR 2: MASALAH PERFORMA (BREBET) ---
        elif gejala_utama == 'motor_brebet':
            if sistem_bb == 'karburator':
                if len(gejala_list) == 1: return {'tanya': 'kapan_brebet_karbu'}
                kapan_brebet = gejala_list[1]
                if kapan_brebet == 'rpm_bawah': return {'diagnosis': "Filter udara kotor atau setelan langsam/pilot jet tidak pas.", 'solusi': "Bersihkan filter udara. Jika masih, perlu servis karburator untuk membersihkan dan menyetel pilot jet.", 'estimasi_biaya': "Rp 40.000 - Rp 75.000 (servis karbu)", 'kesulitan': "Bisa dikerjakan sendiri (filter), Mekanik (setel karbu)"}
                elif kapan_brebet == 'rpm_atas': return {'diagnosis': "Busi lemah atau main jet tersumbat/tidak pas.", 'solusi': "Ganti busi. Jika masih, perlu servis karburator untuk membersihkan main jet.", 'estimasi_biaya': "Rp 25.000 (busi) - Rp 75.000 (servis karbu)", 'kesulitan': "Bisa dikerjakan sendiri (busi), Mekanik (servis karbu)"}
            elif sistem_bb == 'injeksi':
                if len(gejala_list) == 1: return {'tanya': 'kondisi_mil'}
                kondisi_mil = gejala_list[1]
                if kondisi_mil == 'mil_menyala': return {'diagnosis': "ECU mendeteksi kerusakan pada sensor injeksi.", 'solusi': "Segera bawa ke bengkel resmi atau bengkel spesialis injeksi untuk dilakukan pemindaian (scan) menggunakan alat diagnostik.", 'estimasi_biaya': "Rp 50.000 - Rp 150.000 (biaya scan), harga sensor bervariasi.", 'kesulitan': "Wajib dibawa ke mekanik"}
                elif kondisi_mil == 'mil_tidak_menyala': return {'diagnosis': "Filter bensin atau injektor kotor.", 'solusi': "Motor memerlukan servis injeksi, yaitu pembersihan throttle body dan injektor menggunakan cairan pembersih khusus (infus/ultrasonic).", 'estimasi_biaya': "Rp 75.000 - Rp 200.000", 'kesulitan': "Wajib dibawa ke mekanik"}

        # --- ALUR 3: MASALAH PENGGERAK (DIPERDALAM) ---
        elif gejala_utama == 'masalah_penggerak':
            if tipe_motor == 'matic':
                if len(gejala_list) == 1: return {'tanya': 'gejala_cvt'}
                gejala_cvt = gejala_list[1]
                if gejala_cvt == 'gredek':
                    return {'diagnosis': "Kotoran menumpuk di area CVT (kampas/mangkok ganda).", 'solusi': "Area CVT perlu dibersihkan secara menyeluruh. Jika gredek parah, mungkin kampas ganda sudah aus dan perlu diganti.", 'estimasi_biaya': "Rp 50.000 - Rp 100.000 (servis CVT)", 'kesulitan': "Mekanik dianjurkan"}
                elif gejala_cvt == 'tarikan_selip': # ATURAN BARU
                    return {'diagnosis': "V-belt sudah aus/retak atau Roller menjadi peyang.", 'solusi': "Perlu penggantian V-belt dan/atau roller. Sebaiknya dilakukan bersamaan saat servis CVT.", 'estimasi_biaya': "Rp 150.000 - Rp 400.000 (tergantung tipe motor)", 'kesulitan': "Wajib dibawa ke mekanik"}
            elif tipe_motor == 'manual':
                if len(gejala_list) == 1: return {'tanya': 'gejala_rantai'}
                gejala_rantai = gejala_list[1]
                if gejala_rantai == 'rantai_berisik':
                    return {'diagnosis': "Rantai kering, kotor, atau terlalu kencang/kendor.", 'solusi': "Bersihkan rantai dengan cairan pembersih, lalu lumasi dengan chain lube. Setel ulang ketegangan rantai.", 'estimasi_biaya': "Rp 15.000 - Rp 30.000 (jika dilakukan di bengkel)", 'kesulitan': "Bisa dikerjakan sendiri"}
                elif gejala_rantai == 'gigi_keras': # ATURAN BARU
                    return {'diagnosis': "Kampas kopling sudah aus atau setelan tuas kopling tidak pas.", 'solusi': "Coba setel ulang jarak main bebas tuas kopling. Jika masih keras, kemungkinan kampas kopling sudah waktunya diganti.", 'estimasi_biaya': "Rp 150.000 - Rp 300.000 (ganti kampas kopling)", 'kesulitan': "Wajib dibawa ke mekanik"}

        # --- ALUR 4: SUARA MESIN KASAR (ATURAN BARU DITAMBAHKAN) ---
        elif gejala_utama == 'suara_mesin_kasar':
            if len(gejala_list) == 1: return {'tanya': 'jenis_suara_kasar'}
            jenis_suara = gejala_list[1]
            if jenis_suara == 'kletek_di_head':
                return {'diagnosis': "Setelan klep (valve) terlalu renggang.", 'solusi': "Motor perlu penyetelan klep (setel shim/tappet). Ini pekerjaan yang sebaiknya dilakukan oleh mekanik.", 'estimasi_biaya': "Rp 50.000 - Rp 100.000", 'kesulitan': "Wajib dibawa ke mekanik"}
            elif jenis_suara == 'kemrosok_di_mesin_tengah':
                return {'diagnosis': "Kerusakan pada laher (bearing) kruk as atau stang seher.", 'solusi': "Ini adalah kerusakan serius. Segera bawa motor ke bengkel untuk diperiksa lebih lanjut dan kemungkinan turun mesin.", 'estimasi_biaya': "Rp 750.000 - Rp 2.000.000+", 'kesulitan': "Wajib dibawa ke mekanik (Turun Mesin)"}

        # --- ALUR 5: ASAP KNALPOT ANEH (ATURAN BARU DITAMBAHKAN) ---
        elif gejala_utama == 'asap_knalpot_aneh':
            if len(gejala_list) == 1: return {'tanya': 'warna_asap'}
            warna_asap = gejala_list[1]
            if warna_asap == 'putih_tipis_pagi_hari':
                return {'diagnosis': "Normal, itu hanya uap air (kondensasi).", 'solusi': "Tidak perlu tindakan apa-apa. Asap akan hilang setelah mesin panas.", 'estimasi_biaya': "Rp 0", 'kesulitan': "Tidak ada masalah"}
            elif warna_asap == 'putih_tebal_terus':
                return {'diagnosis': "Oli mesin masuk ke ruang bakar.", 'solusi': "Ini masalah serius. Kemungkinan besar disebabkan oleh seal klep yang sudah getas/bocor atau ring piston yang sudah lemah. Segera bawa ke bengkel.", 'estimasi_biaya': "Rp 150.000 - Rp 500.000 (tergantung tingkat kerusakan)", 'kesulitan': "Wajib dibawa ke mekanik"}
            elif warna_asap == 'hitam_pekat':
                return {'diagnosis': "Pembakaran terlalu boros (kebanyakan bensin).", 'solusi': "Sama seperti kasus busi hitam. Setelan karburator/injeksi terlalu basah. Perlu disetel ulang.", 'estimasi_biaya': "Rp 40.000 - Rp 75.000 (servis)", 'kesulitan': "Mekanik dianjurkan"}

        return None