import wfdb
import os
import glob
import numpy as np

folder = r"E:\MIMIC4\MIMIC4\physionet.org\files\mimic4wdb\0.1.0\waves\p100\p10014354\81739927"
print("Folder:", folder)
print("Folder exists:", os.path.exists(folder))

print("\nFiles/folders inside:")
for item in os.listdir(folder):
    print(item)
hea_files = glob.glob(os.path.join(folder, "*.hea"))

print("Number of header files:", len(hea_files))

for hea_file in hea_files:

    record_path = os.path.splitext(hea_file)[0]

    try:
        record = wfdb.rdrecord(record_path)

        if "II" in record.sig_name:

            ecg_index = record.sig_name.index("II")

            ecg = record.p_signal[:, ecg_index]

            std = np.std(ecg)

            print(
                os.path.basename(record_path),
                "| samples:", len(ecg),
                "| ECG std:", std
            )

    except Exception as e:
        print("Error:", record_path, e)