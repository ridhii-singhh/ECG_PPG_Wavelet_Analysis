import wfdb
import pywt
import matplotlib.pyplot as plt
import numpy as np

record_path = r"E:\MIMIC4\MIMIC4\physionet.org\files\mimic4wdb\0.1.0\waves\p100\p10014354\81739927\81739927_0012"

fs = 62.4725

start_sec = 10
end_sec = 18

start_sample = int(start_sec * fs)
end_sample = int(end_sec * fs)

record = wfdb.rdrecord(
    record_path,
    sampfrom=start_sample,
    sampto=end_sample
)

ecg = record.p_signal[:, record.sig_name.index("II")]

# Haar DWT
approximation, detail = pywt.dwt(ecg, "haar")

print("Original samples:", len(ecg))
print("Approximation coefficients:", len(approximation))
print("Detail coefficients:", len(detail))

print("\nFirst 10 approximation coefficients:")
print(approximation[:10])

print("\nFirst 10 detail coefficients:")
print(detail[:10])