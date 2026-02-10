# IQC Statistical Process Control (SPC) Analysis

## 📌 Project Overview
This project demonstrates an end-to-end **Incoming Quality Control (IQC)** workflow. Using a dataset of 320 samples, we performed statistical analysis to monitor manufacturing stability and evaluate process capability ($C_p / C_{pk}$).

## 🛠 Tech Stack
- **Analysis Tool:** Minitab (Primary analysis & visualization)
- **Programming:** Python (Validation & automation script)
- **Library:** Pandas, Scipy, Matplotlib

## 📊 Key Methodology & Results
### 1. Normality & Stability
- **Test:** Conducted Anderson-Darling normality test to ensure data suitability.
- **Control Chart:** Implemented a **C-Chart** for defect counts.
- **Findings:** The process is statistically stable in both Phase I and Phase II with no points exceeding the 3-sigma control limits.

### 2. Process Capability
| Phase | $C_p$ | $C_{pk}$ | Status |
| :--- | :--- | :--- | :--- |
| Phase I | 1.21 | 0.99 | Stable, but Off-centre |
| Phase II | 1.39 | 1.17 | Improvement noted |

## 📂 Repository Structure
- `/data`: Raw defect sampling data.
- `/scripts`: Python script to replicate Minitab calculations.
- `/figures`: Comparison between Minitab outputs and Python plots.
- `/docs`: Full project poster and documentation.

## 💡 Business Recommendations
Based on the $C_{pk}$ being significantly lower than $C_p$, the process mean is shifted towards the upper limit. **Recalibration of equipment** and **targeted operator training** are recommended to center the process and reduce potential defects.
