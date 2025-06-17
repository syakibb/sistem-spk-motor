# Nama file: engine.py (Versi 3.0 - Aturan Lebih Mendalam)

class DiagnosisEngine:
    def run(self, gejala_list):
        if not gejala_list:
            return {'tanya': 'gejala_utama'}

        gejala_utama = gejala_list[0]

        # --- ALUR 1: MASALAH STARTER (DIPERDALAM) ---
        if gejala_utama == 'motor_tidak_menyala':
            if len(gejala_list) == 1:
                return {'tanya': 'kondisi_lampu'}
            
            kondisi_lampu = gejala_list[1]
            if kondisi_lampu == 'lampu_mati_total':
                return {'diagnosis': "Masalah pada sumber daya utama.", 'solusi': "Periksa tegangan Aki (bisa jadi soak atau habis). Periksa juga Sekring (fuse) utama di dekat aki, mungkin putus."}
            elif kondisi_lampu == 'lampu_normal':
                if len(gejala_list) == 2:
                    return {'tanya': 'reaksi_starter'}
                
                reaksi_starter = gejala_list[2]
                if reaksi_starter == 'bunyi_cetek':
                    # Pertanyaan lanjutan untuk memastikan masalah relay
                    if len(gejala_list) == 3:
                        return {'tanya': 'sudah_jumper_aki'}
                    
                    sudah_jumper = gejala_list[3]
                    if sudah_jumper == 'sudah_dan_sama':
                        return {'diagnosis': "100% Relay Starter (Bendik) rusak.", 'solusi': "Ganti Relay Starter dengan yang baru. Masalah bukan pada aki Anda."}
                    elif sudah_jumper == 'belum_coba':
                        return {'diagnosis': "Kemungkinan besar Relay Starter, tapi bisa juga Aki lemah.", 'solusi': "Lakukan jumper dari aki motor lain. Jika menyala, ganti aki Anda. Jika tetap sama, ganti Relay Starter."}

                elif reaksi_starter == 'dinamo_lemah':
                    return {'diagnosis': "Aki soak / tegangan kurang.", 'solusi': "Aki tidak memiliki cukup daya untuk memutar dinamo dengan kuat. Segera isi ulang (charge) atau ganti Aki dengan yang baru."}
                elif reaksi_starter == 'tidak_ada_respon':
                    return {'diagnosis': "Masalah pada jalur tombol starter.", 'solusi': "Periksa saklar/tombol starter di stang, kemungkinan kotor atau rusak. Periksa juga koneksi kabel yang menuju ke relay starter."}

        # --- ALUR 2: MASALAH PERFORMA (DIPERDALAM) ---
        elif gejala_utama == 'motor_brebet':
            if len(gejala_list) == 1:
                return {'tanya': 'kapan_brebet'}
            
            kapan_brebet = gejala_list[1]
            if kapan_brebet == 'rpm_bawah':
                return {'diagnosis': "Filter udara kotor atau setelan langsam/pilot jet tidak pas.", 'solusi': "Bersihkan atau ganti filter udara. Jika masih brebet, bawa ke bengkel untuk menyetel ulang karburator/injeksi."}
            elif kapan_brebet == 'rpm_atas':
                # Pertanyaan lanjutan untuk memastikan masalah pembakaran
                if len(gejala_list) == 2:
                    return {'tanya': 'warna_busi'}
                
                warna_busi = gejala_list[2]
                if warna_busi == 'hitam_kering':
                    return {'diagnosis': "Pembakaran terlalu boros (kebanyakan bensin).", 'solusi': "Setelan main jet pada karburator terlalu besar atau ada masalah pada sensor injeksi. Perlu disetel ulang oleh mekanik."}
                elif warna_busi == 'putih_pucat':
                    return {'diagnosis': "Pembakaran terlalu irit (kekurangan bensin).", 'solusi': "Setelan main jet terlalu kecil atau tekanan bensin kurang. Bisa menyebabkan mesin overheat. Segera periksakan."}
                elif warna_busi == 'merah_bata':
                    return {'diagnosis': "Pembakaran normal, masalah mungkin bukan di suplai bensin.", 'solusi': "Jika pembakaran sempurna tapi masih brebet di RPM atas, kemungkinan masalah ada pada sistem pengapian (CDI/ECU) yang limiternya tercapai terlalu cepat."}

        # --- ALUR 3: MASALAH SUARA MESIN (TETAP SAMA, SUDAH CUKUP DALAM) ---
        elif gejala_utama == 'suara_mesin_kasar':
            # ... (logika ini sama seperti versi 2.0) ...
            if len(gejala_list) == 1:
                return {'tanya': 'jenis_suara_kasar'}
            jenis_suara = gejala_list[1]
            if jenis_suara == 'kletek_di_head':
                return {'diagnosis': "Setelan klep (valve) terlalu renggang.", 'solusi': "Motor perlu penyetelan klep (setel shim/tappet). Ini pekerjaan yang sebaiknya dilakukan oleh mekanik."}
            elif jenis_suara == 'kemrosok_di_mesin_tengah':
                return {'diagnosis': "Kerusakan pada laher (bearing) kruk as atau stang seher.", 'solusi': "Ini adalah kerusakan serius. Segera bawa motor ke bengkel untuk diperiksa lebih lanjut dan kemungkinan turun mesin."}
        
        # --- ALUR 4: KATEGORI BARU - ASAP KNALPOT ---
        elif gejala_utama == 'asap_knalpot_aneh':
            if len(gejala_list) == 1:
                return {'tanya': 'warna_asap'}
            
            warna_asap = gejala_list[1]
            if warna_asap == 'putih_tipis_pagi_hari':
                return {'diagnosis': "Normal, itu hanya uap air (kondensasi).", 'solusi': "Tidak perlu tindakan apa-apa. Asap akan hilang setelah mesin panas."}
            elif warna_asap == 'putih_tebal_terus':
                return {'diagnosis': "Oli mesin masuk ke ruang bakar.", 'solusi': "Ini masalah serius. Kemungkinan besar disebabkan oleh seal klep yang sudah getas/bocor atau ring piston yang sudah lemah. Segera bawa ke bengkel."}
            elif warna_asap == 'hitam_pekat':
                return {'diagnosis': "Pembakaran terlalu boros (kebanyakan bensin).", 'solusi': "Sama seperti kasus busi hitam. Setelan karburator/injeksi terlalu basah. Perlu disetel ulang."}

        return None