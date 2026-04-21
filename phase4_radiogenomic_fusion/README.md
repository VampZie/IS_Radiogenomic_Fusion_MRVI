# Phase 4: Radiogenomic Fusion & MRVI Generation

## 🔬 Overview
Phase 4 acts as the "Grand Bridge" of the repository. It integrates the spatial features from Phase 2 (Radiomics) with the molecular insights from Phase 3 (scRNA-seq) to produce the **Molecular Radiomics Vulnerability Index (MRVI)**.

## 🛠️ Key Components

### 1. HPC Radiogenomic Harvester
A high-performance feature extraction engine designed for massive cohort auditing:
- **70-Thread Swarm Orchestration**: Bypasses traditional GPU bottlenecks for efficient batch extraction.
- **XAI-Anchored ROI Selection**: Extracts 100+ radiomic features (Shape, Intensity, Texture) exclusively from the "Triple-Gate" snapped ischemic islands.

### 2. Adaptive Texture Binning
A technical innovation to ensure digital fidelity in low-contrast CT images:
- **Dynamic Resolution Scaling**: Automatically adjusts `binWidth` based on intra-patient noise and Hounsfield Unit variance to prevent feature collapse.

### 3. Molecularly-Calibrated Risk Index (MRVI)
The flagship contribution of this framework:
- **Priori-Weighted Integration**: Select radiomic texture features (GLCM, GLSZM) are weighted according to their correlation with **Endothelial and Immune dysfunction** discovered in Phase 3.
- **Sigmoid Calibration**: The raw score is calibrated into a 0-1 probability index, allowing for high-precision risk stratification.

## 📊 Technical Capabilities
- **Cross-Modal Integration**: Seamlessly fuses 2D/3D imaging features with single-cell molecular functional priors.
- **Automated Feature Engineering**: Generates the consolidated "Master Fusion Table" across all 1,130 patient slices.
- **HPC Optimized**: Built for multi-core server environments using `ProcessPoolExecutor`.

---
*Developed by Vidit Zainith — Characterizing the digital shadow of molecular dysfunction.*
