import os
import re

def rename_files(folder_path, renaming_list):
    # Iterate over all folders in the directory
    for folder_name in os.listdir(folder_path):
        folder_dir = os.path.join(folder_path, folder_name)

        # Check if the item is a directory
        if os.path.isdir(folder_dir):
            # Print log message for switching to a new folder
            print(f"Switching to folder: {folder_name}")

            # Scan all files in the folder
            files = os.listdir(folder_dir)

            for file_name in files:
                # Get the full path of the file
                file_path = os.path.join(folder_dir, file_name)

                # Check if the file is a regular file
                if os.path.isfile(file_path):
                    # Flag to check if the file is found in the renaming list
                    found = False

                    # Iterate over the renaming list
                    for original_prefix, new_name in renaming_list.items():
                        # Check if the original prefix matches the file name
                        if file_name.startswith(original_prefix):
                            # Create the new file name
                            new_file_name = new_name

                            # Get the full path of the new file
                            new_file_path = os.path.join(folder_dir, new_file_name)

                            if not os.path.exists(new_file_path):
                                # Rename the file
                                os.rename(file_path, new_file_path)
                                print(f"Renamed '{file_name}' to '{new_file_name}'")

                            found = True
                            break

                    # Log error if file is not found in the renaming list
                    if not found:
                        print(f"\tFile '{file_name}' not found in the renaming list. Skipping...")
                else:
                    print(f"'{file_name}' is not a regular file. Skipping...")

    # Log files in the renaming list that have not been renamed
    for original_prefix, new_name in renaming_list.items():
        if original_prefix not in [file_name[:len(original_prefix)] for file_name in files]:
            print(f"\tFile with prefix '{original_prefix}' not found in the folder. Skipping...")

def rename_folders(folder_path, folders_to_rename):
    for partial_old_name, new_name in folders_to_rename:
        pattern = re.compile(r"\b" + re.escape(partial_old_name) + r"\b", re.IGNORECASE)
        for folder_name in os.listdir(folder_path):
            folder_dir = os.path.join(folder_path, folder_name)

            if os.path.isdir(folder_dir):
                if pattern.search(folder_name.lower()):
                    # Print log message for switching to a new folder
                    print(f"Switching to folder: {new_name}")

                    old_name = folder_dir
                    new_folder_name = os.path.join(folder_path, new_name)
                    change_folder_name(old_name, new_folder_name)

# Example usage:
folder_path = './'
folders_to_rename = [
    ("Ahli Teknik Bangunan Gedung","SI011001"),
    ("Ahli Muda Perencana Beton Pracetak Untuk Struktur Bangunan Gedung","SI011002"),
    ("Ahli Rekayasa Konstruksi Bangunan Gedung","SI011007"),
    ("Ahli Perawatan Bangunan Gedung","SI011011"),
    ("Ahli Penilai Kelaikan Bangunan Gedung (Aspek Arsitektur dan Tata Ruang Luar)","SI011012"),
    ("Manajer pengelolaan Bangunan Gedung","SI011013"),
    ("Ahli Pemeriksa Kelaikan Fungsi Struktur Bangunan Gedung","SI011015"),
    ("Ahli Penilai Bangunan Hijau","SI011016"),
    ("Manajer Lapangan Pelaksanaan Pekerjaan Gedung","SI012001"),
    ("Pengawas Pekerjaan Struktur Bangunan Gedung","SI012002"),
    ("Kepala Pengelola Lingkungan Bangunan Gedung","SI012003"),
    ("Perencana Struktur Bangunan RISHA","SI012018"),
    ("Pembuat Panel Struktur RISHA","SI012019"),
    ("Juru Gambar Bangunan Gedung","SI012022"),
    ("Tukang Cat Bangunan Gedung","SI013001"),
    ("Tukang Plester Bangunan Gedung","SI013002"),
    ("Tukang Pasang Ubin","SI013003"),
    ("Tukang Pasang Bata","SI013013"),
    ("Tukang Kayu","SI013015"),
    ("Tukang Kayu Konstruksi","SI013016"),
    ("Tukang Besi Beton","SI013017"),
    ("Mandor Tukang Pasang Beton Precast","SI013020"),
    ("Pemasang Perancah Dan Acuan/Cetakan Beton","SI013023"),
    ("Tukang Bangunan Gedung","SI013026"),
    ("Tukang Pasang Rangka Atap Baja Ringan","SI013027"),
    ("Tukang Pasang/Aplikator/Instalatur Baja Ringan","SI013028"),
    ("Tukang Pasang Water Proofing","SI013029"),
    ("Mandor Pemasangan (Installer) Rangka Atap Baja Ringan","SI013030"),
    ("Mandor Pemasangan Rangka Dinding dan Lantai Baja Ringan","SI013039"),
    ("Ahli Material Jalan","SI021002"),
    ("Manajer Produksi Campuran Aspal Panas (Asphalt Mixing Plant Manager)","SI022001"),
    ("Teknisi Laboratorium Beton Aspal","SI022003"),
    ("Pelaksana Produksi Campuran Aspal Panas","SI023001"),
    ("Manajer Pelaksanaan Pekerjaan Jalan/ Jembatan","SI031006"),
    ("Ahli Keselamatan Jalan","SI031010"),
    ("Ahli Pemeliharaan Jalan Dan Jembatan","SI031012"),
    ("Juru Gambar Pekerjaan Jalan dan Jembatan","SI032002"),
    ("Pelaksana Lapangan Pekerjaan Jalan","SI032004"),
    ("Pelaksana Lapangan Perkerasan Jalan Beton","SI032006"),
    ("Mandor Perkerasan Jalan","SI033001"),
    ("Ahli Perencanaan Jembatan Rangka Baja","SI041003"),
    ("Ahli Rehabilitasi Jembatan","SI041010"),
    ("Pelaksana Lapangan Pekerjaan Pemasangan Jembatan Rangka Baja Standar","SI042002"),
    ("Teknisi Jembatan Rangka Baja","SI042003"),
    ("Pelaksana Pemeliharaan Jembatan","SI042005"),
    ("Ahli Perencanaan Terowongan Jalan","SI061001"),
    ("Ahli Teknik Bendungan Besar","SI071002"),
    ("Ahli Operasi dan Pemeliharaan Bendungan Tipe Urukan","SI071004"),
    ("Ahli Madya Pengawas Pelaksanaan Konstruksi Bangunan Sipil Pembangkit Listrik Tenaga Mini Hidro","SI071005"),
    ("Inspektur Bendungan Urukan","SI072001"),
    ("Pelaksana Operasi dan Pemeliharaan Bendungan Tipe Urukan","SI072004"),
    ("Mandor Pekerjaan Timbunan Tubuh Bendungan Tipe Urugan","SI073001"),
    ("Ahli Muda Perencana Irigasi","SI081003"),
    ("Ahli Teknik Perencanaan Irigasi Rawa","SI081004"),
    ("Ahli Perencanaan Operasi dan Pemeliharaan Jaringan Irigasi","SI081007"),
    ("Ahli Teknik Rawa","SI081008"),
    ("Pelaksana Lapangan Pekerjaan Saluran Irigasi","SI082003"),
    ("Pelaksana Pemasangan Pintu Air","SI082004"),
    ("Pelaksana Pekerjaan Pemeliharaan Jaringan Irigasi","SI082006"),
    ("Ahli Perencanaan Pengamanan Pantai","SI091001"),
    ("Ahli Teknik Pantai","SI091002"),
    ("Ahli Perencanaan Operasi dan Pemeliharaan Prasarana Sungai Serta Pemeliharaan Sungai","SI091004"),
    ("Pelaksana Lapangan Pekerjaan Bronjong","SI092001"),
    ("Pelaksana Lapangan Pekerjaan Bangunan Pengaman Pantai","SI092002"),
    ("Pelaksana Pekerjaan Pemeliharaan Sungai","SI093001"),
    ("Ahli Muda Hidrologi","SI101001"),
    ("Ahli Madya Hidrologi","SI101002"),
    ("Ahli Utama Hidrologi","SI101003"),
    ("Ahli Hidrolika","SI101007"),
    ("Pelaksana Konstruksi Bangunan Unit Produksi SPAM","SI111001"),
    ("Manajer Pelaksana Konstruksi Sistem Produksi Air Minum (SPAM)","SI112001"),
    ("Pelaksana Konstruksi Bangunan Unit Distribusi SPAM","SI112002"),
    ("Pelaksana Lapangan Pekerjaan Bangunan Air Limbah Permukiman (setempat dan terpusat)","SI122001"),
    ("Pelaksana Lapangan Pekerjaan Pemasangan Pipa Leachate (Lindi) dan Pipa Gas/Ventilasi Di TPA","SI132001"),
    ("Pelaksana Lapangan Pekerjaan Pemasangan Lapisan Kedap Air di Tempat Pemrosesan Akhir","SI132002"),
    ("Ahli Perencanaan Jaringan Drainase","SI141001"),
    ("Pelaksana Lapangan Pekerjaan Drainase Perkotaan","SI142001"),
    ("Pengawas Lapangan Pekerjaan Drainase Perkotaan","SI142002"),
    ("Ahli Geoteknik","SI151001"),
    ("Ahli Geologi Pekerjaan Konstruksi","SI151002"),
    ("Ahli Muda Perencana Pondasi","SI151005"),
    ("Ahli Madya Perencana Pondasi","SI151006"),
    ("Ahli Utama Perencana Pondasi","SI151007"),
    ("Teknisi Geoteknik","SI152001"),
    ("Ahli Geodesi Dan Bangunan Gedung","SI161001"),
    ("Ahli Geodesi Untuk Perencanaan Teknis Jalan dan Jembatan","SI161002"),
    ("Ahli Muda Pengukuran Jalan","SI161003"),
    ("Juru Ukur (Surveyor)","SI163001"),
    ("Ahli Madya Perencana Struktur Jalan Rel","SI171001"),
    ("Manajer Teknik Pembangunan Jalan Rel","SI171003"),
    ("Pelaksana Lapangan Pekerjaan Pembangunan Jalan Rel","SI172001"),
    ("Ahli Teknik Dermaga","SI191001"),
    ("Ahli Pelaksanaan Pembongkaran Bangunan","SI221001"),
    ("Teknisi Grouting Senior","SI232001"),
    ("Operator Grouting Bendungan Besar","SI233001"),
    ("Ahli Muda Teknik Bangunan Gedung","SI011017"),
    ("Ahli Madya Teknik Bangunan Gedung","SI011018"),
    ("Ahli Madya Rekayasa Konstruksi Bangunan Gedung","SI011019"),
    ("Ahli Muda Perawatan Bangunan Gedung","SI011020"),
    ("Ahli Madya Perawatan Bangunan Gedung","SI011021"),
    ("Perakit Struktur Bangunan RISHA","SI012023"),
    ("Juru Gambar Bangunan Gedung Level 3","SI013040"),
    ("Juru Gambar Bangunan Gedung Level 2","SI013041"),
    ("Ahli Muda Keselamatan Jalan","SI031013"),
    ("Ahli Madya Keselamatan Jalan","SI031014"),
    ("Ahli Muda Pemeliharaan Jalan Dan Jembatan","SI031015"),
    ("Ahli Madya Pemeliharaan Jalan Dan Jembatan","SI031016"),
    ("Pelaksana Lapangan Pekerjaan Jalan Level 3","SI033006"),
    ("Pelaksana Lapangan Pekerjaan Jalan Level 2","SI033007"),
    ("Juru Gambar Pekerjaan Jalan dan Jembatan Level 3","SI033008"),
    ("Juru Gambar Pekerjaan Jalan dan Jembatan Level 2","SI033009"),
    ("Ahli Muda Teknik Bendungan Besar","SI071006"),
    ("Ahli Madya Teknik Bendungan Besar","SI071007"),
    ("Ahli Madya Operasi dan Pemeliharaan Bendungan Tipe Urukan","SI071008"),
    ("Ahli Madya Teknik Perencanaan Irigasi Rawa","SI081009"),
    ("Ahli Muda Perencanaan Operasi dan Pemeliharaan Jaringan Irigasi","SI081010"),
    ("Ahli Madya Perencanaan Operasi dan Pemeliharaan Jaringan Irigasi","SI081011"),
    ("Ahli Muda Teknik Rawa","SI081012"),
    ("Ahli Madya Teknik Rawa","SI081013"),
    ("Pelaksana Lapangan Pekerjaan Saluran Irigasi Level 3","SI083001"),
    ("Pelaksana Lapangan Pekerjaan Saluran Irigasi Level 2","SI083002"),
    ("Ahli Madya Perencanaan Pengamanan Pantai","SI091006"),
    ("Ahli Muda Teknik Pantai","SI091007"),
    ("Ahli Madya Teknik Pantai","SI091008"),
    ("Ahli Muda Perencanaan Operasi dan Pemeliharaan Prasarana Sungai Serta Pemeliharaan Sungai","SI091009"),
    ("Ahli Madya Perencanaan Operasi dan Pemeliharaan Prasarana Sungai Serta Pemeliharaan Sungai","SI091010"),
    ("Ahli Muda Hidrolika","SI101011"),
    ("Ahli Madya Hidrolika","SI101012"),
    ("Ahli Muda Perencanaan Jaringan Drainase","SI141002"),
    ("Ahli Madya Perencanaan Jaringan Drainase","SI141003"),
    ("Ahli Muda Geoteknik","SI151008"),
    ("Ahli Madya Geoteknik","SI151009"),
    ("Ahli Madya Geologi Pekerjaan Konstruksi","SI151010"),
    ("Ahli Muda Survei Terestris","SI161004"),
    ("Ahli Madya Survei Terestris","SI161005"),
    ("Ahli Utama Survei Terestris","SI161006"),
    ("Juru Ukur (Surveyor) Level 2","SI163005"),
    ("Ahli Muda Teknik Dermaga","SI191002"),
    ("Ahli Madya Teknik Dermaga","SI191003"),
    ("Ahli Muda Pelaksanaan Pembongkaran Bangunan","SI221002"),
    ("Ahli Madya Pelaksanaan Pembongkaran Bangunan","SI221003"),
    ("Pengelola Teknis Pembangunan Bangunan Gedung Negara","SI011022"),
    ("Ahli Penilai Kegagalan Bangunan Gedung","SI011023"),
    ("Pelaksana Lapangan Pekerjaan Gedung Madya","SI012024"),
    ("Pengawas Pekerjaan Struktur Bangunan Gedung Madya","SI012025"),
    ("Pengawas Pekerjaan Struktur Bangunan Gedung Utama","SI012026"),
    ("Mandor Pemasangan (Installer) Rangka Atap Baja Ringan Level 2","SI013044"),
    ("Mandor Pemasangan Rangka Dinding dan Lantai Baja Ringan Level 2","SI013045"),
    ("Mandor Tukang Pasang Beton Precast Level 2","SI013046"),
    ("Tukang Plester Bangunan Gedung Level 2","SI013047"),
    ("Tukang Pasang Ubin Level 2","SI013048"),
    ("Tukang Bangunan Gedung Level 1","SI013049"),
    ("Tukang Cat Bangunan Gedung Level 2","SI013050"),
    ("Tukang Pasang Bata Level 2","SI013051"),
    ("Tukang Besi Beton Level 2","SI013052"),
    ("Tukang Pasang Water Proofing Level 1","SI013053"),
    ("Tukang Kayu Konstruksi Level 1","SI013054"),
    ("Ahli Madya Material Jalan","SI021005"),
    ("Ahli Muda Material Jalan","SI021006"),
    ("Teknisi Laboratorium Beton Aspal Madya","SI022012"),
    ("Teknisi Laboratorium Beton Aspal Utama","SI022013"),
    ("Pelaksana Produksi Campuran Aspal Panas Muda","SI022014"),
    ("Pengawasan Teknis Jalan","SI031017"),
    ("Pelaksana Pemeliharaan Jalan Muda","SI032014"),
    ("Pelaksana Pemeliharaan Jalan Madya","SI032015"),
    ("Pelaksana Lapangan Perkerasan Jalan Beton Muda","SI032016"),
    ("Pelaksana Lapangan Perkerasan Jalan Beton Madya","SI032017"),
    ("Pelaksana Lapangan Pekerjaan Jalan Madya","SI032019"),
    ("Mandor Perkerasan Jalan Level 2","SI033015"),
    ("Ahli Muda Perencanaan Jembatan Rangka Baja","SI041011"),
    ("Ahli Madya Perencanaan Jembatan Rangka Baja","SI041012"),
    ("Pengendali Pelaksanaan Pekerjaan Jembatan","SI041013"),
    ("Ahli Muda Rehabilitasi Jembatan","SI041014"),
    ("Ahli Madya Rehabilitasi Jembatan","SI041015"),
    ("Ahli Penilai Kegagalan Bangunan Jalan Layang dan Jembatan","SI041016"),
    ("Pelaksana Pemeliharaan Jembatan Muda","SI042007"),
    ("Pelaksana Pemeliharaan Jembatan Madya","SI042008"),
    ("Pelaksana Lapangan Pekerjaan Pemasangan Jembatan Rangka Baja Standar Madya","SI042009"),
    ("Teknisi Jembatan Rangka Baja Madya","SI042010"),
    ("Teknisi Jembatan Rangka Baja Utama","SI042011"),
    ("Ahli Madya Perencanaan Terowongan Jalan","SI061008"),
    ("Inspektur Bendungan Urukan Madya","SI072005"),
    ("Pelaksana Operasi dan Pemeliharaan Bendungan Tipe Urukan Utama","SI072006"),
    ("Pelaksana Pemasangan Pintu Air Madya","SI082008"),
    ("Pelaksana Lapangan Pekerjaan Saluran Irigasi Madya","SI082009"),
    ("Pelaksana Pekerjaan Operasi dan Pemeliharaan Jaringan Irigasi","SI082010"),
    ("Pelaksana Pekerjaan Pemeliharaan Jaringan Irigasi Level 3","SI082011"),
    ("Pelaksana Lapangan Pekerjaan Bangunan Pengaman Pantai Madya","SI092003"),
    ("Pelaksana Pekerjaan Pemeliharaan Sungai Muda","SI092004"),
    ("Pelaksana Lapangan Pekerjaan Bronjong Level 3","SI093002"),
    ("Pelaksana Konstruksi Bangunan Unit Distribusi SPAM Level 3","SI113001"),
    ("Pelaksana Lapangan Pekerjaan Bangunan Air Limbah Permukiman (Setempat dan Terpusat) Madya","SI123001"),
    ("PELAKSANA LAPANGAN PEKERJAAN PEMASANGAN PIPA LEACHATE (LINDI) DAN PIPA GAS/VENTILASI DI TPA MADYA","SI132004"),
    ("Pelaksana Lapangan Pekerjaan Lapisan Kedap Air di Tempat Pemrosesan Akhir (TPA) Madya","SI132005"),
    ("Pengawas Lapangan Pekerjaan Drainase Perkotaan Madya","SI142003"),
    ("Teknisi Geoteknik Madya","SI152004"),
    ("Ahli Muda Hidrografi Pesisir","SI161007"),
    ("Ahli Muda Survei Pemetaan Udara","SI161008"),
    ("Manager Proyek Survei dan Pemetaan Wilayah","SI161009"),
    ("Spesialis SIG","SI161010"),
    ("Ahli Madya Hidrografi Lepas Pantai","SI161011"),
    ("Ahli Madya Kewilayahan","SI161012"),
    ("Ahli Madya Sistem Informasi Geografis","SI161013"),
    ("Ahli Utama Kewilayahan","SI161014"),
    ("Operator Utama Survei Terestris","SI162003"),
    ("Teknisi Survei Terestris","SI162004"),
    ("Surveyor Rekayasa","SI162005"),
    ("Surveyor Terestris","SI162006"),
    ("Operator Muda Survei Terestris","SI163006"),
    ("Operator Madya Survei Terestris","SI163007"),
    ("Pelaksana Lapangan Pekerjaan Pembangunan Jalan Rel Madya","SI172002"),
    ("Operator Grouting Bendungan Besar Level 3","SI233002"),
    ("Ahli Muda Teknik Jalan","SI031018"),
    ("Ahli Madya Teknik Jalan","SI031019"),
    ("Ahli Utama Teknik Jalan","SI031020"),
    ("Ahli Muda Teknik Jembatan","SI041017"),
    ("Ahli Madya Teknik Jembatan","SI041018"),
    ("Ahli Utama Teknik Jembatan","SI041019"),
    ("Pelaksana Lapangan Pekerjaan Gedung","SI012027"),
    ("Pelaksana Lapangan Pekerjaan Gedung Level 2","SI013055"),
    ("Pelaksana Lapangan Pekerjaan Gedung Level 3","SI013056"),
    ("Pelaksana Pemeliharaan Jalan","SI032018"),
    ("Ahli Muda Bidang Keahlian Teknik Sumber Daya Air","SI101013"),
    ("Ahli Madya Bidang Keahlian Teknik Sumber Daya Air","SI101014"),
    ("Ahli Utama Bidang Keahlian Teknik Sumber Daya Air","SI101015"),
    ("Ahli Muda Penilai Bangunan Hijau","SI011024"),
    ("Ahli Madya Penilai Bangunan Hijau","SI011025"),
    ("Ahli Teknik Perencana Bendungan","SI071009"),
    ("Ahli Penilai Kegagalan Bangunan Sumber Daya Air (SDA)","SI101016")
    # Add more folder name pairs here
]

renaming_list = {
    '1. ': '1. FR APL 01_1.pdf',
    '2. ': '2. FR APL 02_1.pdf',
    '3. ': '3. FR MAPA 01_1.pdf',
    '5. ': '5. FR MAPA 02.pdf',
    '6. ': '6. FR AK 01.pdf',
    '7': '7. FR AK 04.pdf',
    '8. ': '8. FR-IA 01.pdf',
    '9. ': '9. FR-IA 02.pdf',
    '10. ': '10. FR-IA 03.pdf',
    '11. ': '11. FR.IA.04.pdf',
    '12': '12. FR. IA 05 - IA 05C.pdf',
    '13': '13. FR. IA 06.pdf',
    '14. ': '14. FR. IA 07.pdf',
    '15. ': '15. FR.IA.08.pdf',
    '16. ': '16. FR.IA.09.pdf',
    '17. ': '17. FR.IA.10.pdf',
    '18. ': '18. FR-IA 11.pdf',
    '19. ': '19. FR AK 02.pdf',
    '20. ': '20. FR AK 03.pdf',
    '21. ': '21. FR AK 05.pdf',
    '22. ': '22. FR AK 06.pdf',
    '23. ': '23. FR VA - MKVA.pdf',
    # Add more mappings as needed
}

# Rename folders
rename_folders(folder_path, folders_to_rename)

# Rename files
rename_files(folder_path, renaming_list)

