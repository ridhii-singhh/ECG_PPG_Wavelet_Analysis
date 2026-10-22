import os
import glob
import wfdb
import matplotlib.pyplot as plt
import numpy as np


waves_folder = r"E:\MIMIC4\MIMIC4\physionet.org\files\mimic4wdb\0.1.0\waves"


candidate_names = [
    "81739927_0008",
    "81739927_0012",
    "81739927_0016",
    "83404654_0001"
]


for candidate in candidate_names:

    # Find this record anywhere inside waves folder
    matches = glob.glob(
        os.path.join(waves_folder, "p*", "p*", "*", candidate + ".hea")
    )

    if len(matches) == 0:
        print("Not found:", candidate)
        continue

    record_path = os.path.splitext(matches[0])[0]

    print("\nLoading:", record_path)

    header = wfdb.rdheader(record_path)

    fs = header.fs

    # First 30 seconds
    samples = min(
        int(30 * fs),
        header.sig_len
    )

    record = wfdb.rdrecord(
        record_path,
        sampfrom=0,
        sampto=samples
    )

    # ECG Lead II
    ecg_index = record.sig_name.index("II")
    ecg = record.p_signal[:, ecg_index]

    # PPG
    ppg_index = record.sig_name.index("Pleth")
    ppg = record.p_signal[:, ppg_index]

    time = np.arange(len(ecg)) / fs

    print("ECG std:", np.std(ecg))
    print("PPG std:", np.std(ppg))

    # Plot
    fig, axes = plt.subplots(
        2,
        1,
        figsize=(12, 7),
        sharex=True
    )

    axes[0].plot(time, ecg)
    axes[0].set_title("ECG Lead II")
    axes[0].set_ylabel("Amplitude")

    axes[1].plot(time, ppg)
    axes[1].set_title("PPG (Pleth)")
    axes[1].set_xlabel("Time (seconds)")
    axes[1].set_ylabel("Amplitude")

    fig.suptitle(candidate)

    plt.tight_layout()
    plt.show()
    