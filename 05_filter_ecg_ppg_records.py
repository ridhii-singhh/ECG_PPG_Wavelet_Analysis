import os
import glob
import wfdb

waves_folder = r"E:\MIMIC4\MIMIC4\physionet.org\files\mimic4wdb\0.1.0\waves"

hea_files = glob.glob(
    os.path.join(waves_folder, "p*", "p*", "*", "*_*.hea")
)

print("Searching records...\n")

for hea_file in hea_files:

    try:
        record_path = os.path.splitext(hea_file)[0]
        header = wfdb.rdheader(record_path)

        if "II" in header.sig_name and "Pleth" in header.sig_name:

            duration = header.sig_len / header.fs

            # Keep records between 30 seconds and 10 minutes
            if 30 <= duration <= 600:

                print(
                    os.path.basename(record_path),
                    "| samples:", header.sig_len,
                    "| duration:", round(duration, 2), "sec",
                    "| fs:", header.fs
                )

    except Exception:
        pass
    