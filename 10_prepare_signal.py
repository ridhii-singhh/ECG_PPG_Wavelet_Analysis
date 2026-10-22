import wfdb
import numpy as np

# Record path
record_path = r"E:\MIMIC4\MIMIC4\physionet.org\files\mimic4wdb\0.1.0\waves\p100\p10014354\81739927\81739927_0012"

# Read header first
header = wfdb.rdheader(record_path)

fs = header.fs

# Select the 10 to 18 second portion
start_sec = 10
end_sec = 18

start_sample = int(start_sec * fs)
end_sample = int(end_sec * fs)

# Read only this portion
record = wfdb.rdrecord(
    record_path,
    sampfrom=start_sample,
    sampto=end_sample
)

# Find ECG and PPG channels
ecg_index = record.sig_name.index("II")
ppg_index = record.sig_name.index("Pleth")

# Extract signals
ecg = record.p_signal[:, ecg_index]
ppg = record.p_signal[:, ppg_index]

# Create time axis
time = start_sec + np.arange(len(ecg)) / fs

# Display basic information
print("Sampling frequency:", fs)
print("Start time:", start_sec, "seconds")
print("End time:", end_sec, "seconds")
print("Number of samples:", len(ecg))
print("Duration:", len(ecg) / fs, "seconds")

print("\nECG Lead II")
print("Minimum:", np.min(ecg))
print("Maximum:", np.max(ecg))
print("Mean:", np.mean(ecg))
print("Standard deviation:", np.std(ecg))

print("\nPPG (Pleth)")
print("Minimum:", np.min(ppg))
print("Maximum:", np.max(ppg))
print("Mean:", np.mean(ppg))
print("Standard deviation:", np.std(ppg))
