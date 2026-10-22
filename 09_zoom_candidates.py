import wfdb
import matplotlib.pyplot as plt
import numpy as np


candidates = [

    (
        "81739927_0012",
        r"E:\MIMIC4\MIMIC4\physionet.org\files\mimic4wdb\0.1.0\waves\p100\p10014354\81739927\81739927_0012",
        10,
        18
    ),

    (
        "81739927_0016",
        r"E:\MIMIC4\MIMIC4\physionet.org\files\mimic4wdb\0.1.0\waves\p100\p10014354\81739927\81739927_0016",
        11,
        18
    )

]


for name, record_path, start_sec, end_sec in candidates:

    header = wfdb.rdheader(record_path)

    fs = header.fs

    start_sample = int(start_sec * fs)
    end_sample = int(end_sec * fs)

    record = wfdb.rdrecord(
        record_path,
        sampfrom=start_sample,
        sampto=end_sample
    )

    ecg = record.p_signal[:, record.sig_name.index("II")]
    ppg = record.p_signal[:, record.sig_name.index("Pleth")]

    time = start_sec + np.arange(len(ecg)) / fs

    fig, axes = plt.subplots(
        2,
        1,
        figsize=(12, 6),
        sharex=True
    )

    axes[0].plot(time, ecg)
    axes[0].set_title(name + " - ECG Lead II")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(True)

    axes[1].plot(time, ppg)
    axes[1].set_title(name + " - PPG (Pleth)")
    axes[1].set_xlabel("Time (seconds)")
    axes[1].set_ylabel("Amplitude")
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()