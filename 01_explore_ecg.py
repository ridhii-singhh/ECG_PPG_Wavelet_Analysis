import wfdb

record_path = r"E:\MIMIC4\MIMIC4\physionet.org\files\mimic4wdb\0.1.0\waves\p100\p10014354\81739927\81739927_0002"

# Read physical signal
record = wfdb.rdrecord(record_path)

print("Signal names:", record.sig_name)
print("Sampling frequency:", record.fs)
print("Signal shape:", record.p_signal.shape)

# Read raw digital signal
digital_record = wfdb.rdrecord(record_path, physical=False)

print("\nRaw digital ECG values:")
print(digital_record.d_signal[:20])

print("\nADC gain:")
print(digital_record.adc_gain)

print("\nBaseline:")
print(digital_record.baseline)

print("\nUnits:")
print(digital_record.units)

print("\nFormat:")
print(digital_record.fmt)