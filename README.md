# ECG and PPG Signal Denoising Using Wavelet Transforms

## Project Overview

This project explores ECG (Electrocardiogram) and PPG (Photoplethysmography) signals using digital signal processing techniques. The main objective is to study signal characteristics, investigate possible noise and recording artifacts, and evaluate denoising methods while preserving important physiological waveform features.

The project begins with a detailed experiment on a single ECG record and then extends the analysis to ten ECG records to examine how the results vary across different segments.

## Objectives

- Understand ECG and PPG signals and their physiological significance.
- Explore signal characteristics using Discrete Wavelet Transform (DWT) and Continuous Wavelet Transform (CWT).
- Study approximation and detail coefficients at multiple decomposition levels.
- Analyze wavelet energy distribution and entropy.
- Compare hard and soft thresholding strategies.
- Evaluate BayesShrink wavelet denoising against conventional Butterworth filtering.
- Investigate peak-position preservation and waveform morphology.
- Conduct a controlled-noise experiment using a known synthetic noise level.
- Compare signal-processing results across ten ECG records.
- Visualize time-frequency patterns using Morlet and Mexican Hat wavelets.

## Dataset

The experiments use ECG Lead II and PPG Pleth waveform data associated with the MIMIC-IV Waveform Database.

The analysis includes:
- A detailed single-record experiment.
- A PPG signal decomposition and time-frequency analysis example.
- A controlled-noise ECG experiment.
- A comparative study of ten ECG records.

Refer to the dataset provider's access requirements and usage conditions before redistributing any data. The raw physiological recordings are not included in this repository unless explicitly permitted.

## Methodology

### 1. Signal Exploration
ECG and PPG waveforms are visualized in the time domain to understand their structure and identify segments that may require further signal-quality investigation.

### 2. Discrete Wavelet Transform
DWT decomposes a signal into approximation and detail coefficients at multiple scales.

For the Haar wavelet, the approximation and detail coefficients for a pair of samples are:

A = (x₁ + x₂) / √2

D = (x₁ − x₂) / √2

Approximation coefficients capture broader signal trends, while detail coefficients represent changes at different scales.

### 3. Wavelet Feature Analysis
The experiments examine:
- Approximation and detail coefficients.
- Relative wavelet energy.
- Entropy of wavelet-coefficient energy distributions.
- Differences between Haar, Daubechies, Symlet and Coiflet wavelet families.

### 4. Wavelet Denoising
Hard thresholding sets coefficients below a threshold to zero. Soft thresholding also reduces the magnitude of coefficients that remain above the threshold.

BayesShrink is evaluated as an adaptive wavelet-thresholding approach.

### 5. Conventional Filtering
Butterworth filtering is used as a conventional frequency-based filtering approach. Its results are compared with wavelet denoising to examine reconstruction error, waveform similarity and peak preservation.

### 6. Continuous Wavelet Transform
CWT scalograms are generated using Morlet and Mexican Hat wavelets to investigate how signal activity is distributed across time and frequency.

### 7. Controlled-Noise Experiment
Synthetic noise is added to a reference ECG signal at a specified signal-to-noise ratio (SNR). The denoising output is compared with the reference signal using quantitative metrics.

### 8. Multi-Record Analysis
The workflow is extended to ten ECG records. Waveforms, wavelet-energy distributions and denoising metrics are compared to investigate record-to-record variation and identify unusual segments for further inspection.

## Evaluation Metrics

- **RMSE:** Root Mean Square Error; measures the magnitude of reconstruction errors.
- **MAE:** Mean Absolute Error; measures average absolute differences.
- **NRMSE:** Normalized Root Mean Square Error; expresses error relative to a normalization scale.
- **PRD:** Percentage Root-mean-square Difference; measures reconstruction distortion relative to the reference signal.
- **Correlation:** Measures the strength of linear similarity between the reference and reconstructed waveforms.
- **SNR:** Signal-to-Noise Ratio; compares signal power with noise power.
- **SNR Improvement:** Difference between the output and input SNR under a consistent evaluation setup.
- **Relative Wavelet Energy:** Describes the proportion of coefficient energy in each wavelet component.
- **Wavelet Entropy:** Describes how coefficient energy is distributed within a component.
- **Peak-Position Comparison:** Checks whether detected peak locations are preserved after denoising.

Metric interpretation depends on consistent reference signals, normalization and evaluation procedures.

## Selected Experimental Results

### Single-Record Comparison

| Metric | Butterworth | BayesShrink |
|---|---:|---:|
| RMSE | 0.039629 | 0.006133 |
| MAE | 0.021790 | 0.005369 |
| Correlation | 0.928549 | 0.998432 |

In the reported single-record experiment, BayesShrink produced lower RMSE and MAE and higher correlation than the Butterworth result.

### Peak Preservation

The reported original and BayesShrink-denoised peak positions were identical:

`[34, 81, 117, 149, 201, 248, 285, 316, 368, 400, 452, 483]`

The reported peak-position differences were zero for all twelve peaks. The reported morphological correlation was 0.998432.

### Controlled-Noise Experiment

- SNR before denoising: 10.17 dB
- SNR after denoising: 10.88 dB
- SNR improvement: 0.71 dB

The reported correlation increased from 0.954355 for the noisy ECG to 0.958178 for the denoised ECG. RMSE decreased from 0.031927 to 0.029428.

These results describe the reported experiments and should not be interpreted as proof that one method performs best for every ECG or PPG recording.

## Tools and Technologies

- Python
- Jupyter Notebook
- NumPy and Pandas
- Matplotlib
- SciPy
- PyWavelets
- ECG and PPG waveform data

## Repository Contents

- Single-record ECG/PPG analysis notebook
- Ten-record comparative analysis notebook
- PowerPoint project presentation
- README documentation

The notebook filenames may differ depending on the final uploaded files.

## How to Run

1. Clone or download this repository.
2. Install Python and Jupyter Notebook.
3. Install the required scientific computing and signal-processing libraries.
4. Obtain authorized access to the required waveform data.
5. Update notebook dataset paths to match your local environment.
6. Run the notebooks in order, beginning with the single-record experiment.

Example installation command:

```bash
pip install numpy pandas matplotlib scipy PyWavelets jupyter
```

Additional dependencies may be required depending on the dataset-loading code in the notebooks.

## Limitations

- Visual inspection alone cannot confirm that a real ECG or PPG recording contains noise.
- Unusual waveforms may reflect physiological events, artifacts or data-quality issues.
- Controlled-noise results do not automatically generalize to real-world noise.
- The ten-record experiment is a limited evaluation and does not establish clinical validity.
- Results depend on sampling rate, preprocessing, wavelet configuration, thresholds and evaluation procedures.

## Conclusion

This project provides a comparative study of wavelet-based signal analysis and denoising for ECG and PPG waveforms. It combines multiscale decomposition, time-frequency visualization, conventional filtering, adaptive thresholding and quantitative evaluation.

The central objective is to reduce unwanted disturbances while preserving important physiological waveform information. The multi-record analysis further illustrates why signal-processing methods should be evaluated across different recordings rather than judged from a single example.

## Future Work

- Expand evaluation to a larger and more diverse set of recordings.
- Investigate additional wavelet families and threshold-selection strategies.
- Validate signal-quality
