import os
import glob
import wfdb
import numpy as np


waves_folder = r"E:\MIMIC4\MIMIC4\physionet.org\files\mimic4wdb\0.1.0\waves"


hea_files = glob.glob(
    os.path.join(waves_folder, "p*", "p*", "*", "*_*.hea")
)


print("Checking ECG + PPG records...\n")


found = 0


for hea_file in hea_files:

    try:

        record_path = os.path.splitext(hea_file)[0]

        header = wfdb.rdheader(record_path)

        # We need ECG Lead II and PPG
        if "II" not in header.sig_name:
            continue

        if "Pleth" not in header.sig_name:
            continue

        # Only inspect first 30 seconds
        samples = min(
            int(30 * header.fs),
            header.sig_len
        )

        record = wfdb.rdrecord(
            record_path,
            sampfrom=0,
            sampto=samples
        )

        # Extract ECG
        ecg_index = record.sig_name.index("II")
        ecg = record.p_signal[:, ecg_index]

        # Extract PPG
        ppg_index = record.sig_name.index("Pleth")
        ppg = record.p_signal[:, ppg_index]

        # Check for NaN / infinite values
        ecg_finite = np.isfinite(ecg).all()
        ppg_finite = np.isfinite(ppg).all()

        if not ecg_finite or not ppg_finite:
            continue

        # Check variation
        ecg_std = np.std(ecg)
        ppg_std = np.std(ppg)

        # Reject almost-flat signals
        if ecg_std < 0.001:
            continue

        if ppg_std < 0.001:
            continue

        print(
            os.path.basename(record_path),
            "| ECG std:", round(ecg_std, 4),
            "| PPG std:", round(ppg_std, 4),
            "| samples:", samples,
            "| fs:", header.fs
        )

        found += 1

        # Stop after finding 10 usable records
        if found >= 10:
            break

    except Exception:
        continue


print("\nUsable records found:", found)
