import wfdb
import matplotlib.pyplot as plt
import numpy as np


candidates = [

    r"E:\MIMIC4\MIMIC4\physionet.org\files\mimic4wdb\0.1.0\waves\p101\p10112163\88501826\88501826_0009",

    r"E:\MIMIC4\MIMIC4\physionet.org\files\mimic4wdb\0.1.0\waves\p102\p10209410\84248019\84248019_0002"

]


for record_path in candidates:

    print("\nLoading:", record_path)

    # Read header first
    header = wfdb.rdheader(record_path)

    fs = header.fs

    # Only first 30 seconds
    samples_30sec = min(int(30 * fs), header.sig_len)

    record = wfdb.rdrecord(
        record_path,
        sampfrom=0,
        sampto=samples_30sec
    )

    # Find ECG Lead II
    ecg_index = record.sig_name.index("II")

    # Find PPG
    ppg_index = record.sig_name.index("Pleth")

    ecg = record.p_signal[:, ecg_index]
    ppg = record.p_signal[:, ppg_index]

    # Time axis
    time = np.arange(len(ecg)) / fs

    print("Sampling frequency:", fs)
    print("Samples plotted:", len(ecg))
    print("ECG min/max:", np.min(ecg), np.max(ecg))
    print("PPG min/max:", np.min(ppg), np.max(ppg))

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

    fig.suptitle(record_path.split("\\")[-1])

    plt.tight_layout()
    plt.show()