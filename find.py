import os
import glob
import wfdb

# Main MIMIC-IV waves folder
waves_folder = r"E:\MIMIC4\MIMIC4\physionet.org\files\mimic4wdb\0.1.0\waves"

# Find all segment header files recursively
hea_files = glob.glob(
    os.path.join(waves_folder, "p*", "p*", "*", "*_*.hea")
)

print("Header files found:", len(hea_files))
print("\nRecords containing both ECG and PPG:\n")

count = 0

for hea_file in hea_files:

    try:
        header = wfdb.rdheader(os.path.splitext(hea_file)[0])

        signals = header.sig_name

        # ECG signal names commonly found in MIMIC-IV
        ecg_names = {"I", "II", "III", "V", "aVR", "aVL", "aVF"}

        has_ecg = any(signal in ecg_names for signal in signals)

        # PPG is usually named Pleth
        has_ppg = "Pleth" in signals

        if has_ecg and has_ppg:

            record_path = os.path.splitext(hea_file)[0]

            print("Record:", record_path)
            print("Signals:", signals)
            print("Sampling frequency:", header.fs)
            print("Samples:", header.sig_len)
            print("-" * 60)

            count += 1

    except Exception as e:
        pass

print("\nTotal ECG + PPG segments found:", count)
