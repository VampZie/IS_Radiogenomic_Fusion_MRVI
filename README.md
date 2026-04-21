# IS_Radiogenomic_Fusion_MRVI

> **Molecular Radiomics Vulnerability Index (MRVI): An Unsupervised Radiogenomic Pipeline for Ischemic Stroke Characterization.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Python%20%7C%20PyTorch-3776AB?logo=python)]()
[![Workflow](https://img.shields.io/badge/Workflow-Swarm%20HPC-orange)]()

---

## 🔬 Scientific Abstract

This repository implements a multi-modal radiogenomic pipeline designed to quantify ischemic tissue vulnerability by fusing deep-learning-based lesion segmentation with single-cell transcriptomic (scRNA-seq) markers. 

The core innovation is the **Molecular Radiomics Vulnerability Index (MRVI)** — a quantitative metric that maps high-dimensional radiomic textures (GLCM, GLSZM) onto cluster-specific molecular stressors. The pipeline utilizes an unsupervised **"Juror" Ensemble** for lesion segmentation, refined by a **Triple-Gate anatomical snapping protocol** to ensure clinical fidelity without requiring large labeled datasets.

---

## 🛠️ Pipeline Architecture

```
IS_Radiogenomic_Fusion_MRVI/
│
├── 01_lesion_segmentation/       ← Unsupervised "Juror" Ensemble
│   ├── jurors/                   ← Consensus model definitions (3-Model Jury)
│   ├── triple_gate/              ← Anatomical snapping & noise suppression
│   └── evaluate/                 ← Robust metrics suite (DICE, IoU, HD95)
│
├── 02_radiomic_extraction/       ← Swarm-Gated Feature Engineering
│   ├── pyradiomics_suite/        ← Shape, Intensity, and Texture extraction
│   └── swarm_feat_extract.py     ← 50-thread parallel orchestration script
│
├── 03_molecular_fusion/          ← scRNA-seq + Imaging Integration
│   ├── mapping/                  ← Voxel-to-Cluster coordinate registration
│   └── mrvi_engine/              ← Molecular Radiomics Vulnerability Index logic
│
├── orchestration/                ← End-to-end pipeline launcher
└── examples/                     ← Sample ROI data + template markers
```

---

## 🚀 Key Methodologies

### 1. The Juror Ensemble & Triple-Gate Protocol
Unlike traditional supervised U-Nets, this pipeline uses a **Juror Ensemble** that reaches a consensus on ischemic core boundaries. The **Triple-Gate Protocol** then snaps these boundaries to anatomical brain atlases, filtering out intensity noise and anatomical artifacts.

- **Gate 1**: Signal-to-Noise Intensity Thresholding
- **Gate 2**: Morphological Continuity Enforcer
- **Gate 3**: Anatomical Atlas Registration (Snapping)

### 2. High-Dimensional Radiomic Swarm
We extract 1,200+ features per lesion using a **50-thread CPU swarm architecture**. Features include:
- **First-order statistics** (Voxel intensity distributions)
- **Texture** (GLCM, Gray Level Co-occurrence Matrix)
- **Geometry** (Shape-based vulnerability markers)

### 3. Molecular Radiomics Vulnerability Index (MRVI)
The MRVI fuses these radiomic signatures with scRNA-seq derived molecular scores. It identifies "Vulnerability Hotspots" where texture-based entropy predicts high molecular stress, providing a bridge between macro-level imaging and micro-level genomic state.

---

## 📊 Performance Metrics

| Metric | Target | Description |
|--------|---------|-------------|
| **DICE** | > [REDACTED] | Spatial overlap consistency |
| **IoU** | > [REDACTED] | Jaccard Index for segmentation precision |
| **HD95** | < [REDACTED] | 95th percentile Hausdorff Distance |
| **SSIM** | > [REDACTED] | Structural Similarity Index Measure |

---

## 📦 Installation & Setup

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/IS_Radiogenomic_Fusion_MRVI.git
cd IS_Radiogenomic_Fusion_MRVI

# Environment
conda create -n radiogenomics python=3.9
conda activate radiogenomics
pip install -r requirements.txt
```

---

## Reference

This framework was developed for characterizing molecular-radiomic interplay in ischemic stroke lesions. The MRVI represents a novel integration strategy for translating radiomic texture into pathophysiological insights.

> *Unsupervised Juror Ensembles reveal molecular vulnerability hotspots: The MRVI framework.*

---

## License

MIT License — see [LICENSE](LICENSE) for details.
