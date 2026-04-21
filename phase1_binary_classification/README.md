# Phase 1: Binary Classification & Anatomical Snapping (Triple-Gate)

## 🔬 Overview
Phase 1 implements the foundational **Binary Classification Ensemble** used to detect ischemic stroke in non-contrast CT (NCCT) images. Beyond simple classification, this module introduces the **"Triple-Gate Protocol"**, a novel XAI-fidelity framework that anchors AI signals to clinical anatomical structures.

## 🛠️ Key Components

### 1. The Juror Ensemble
A high-throughput ensemble consisting of three state-of-the-art architectures:
- **ConvNeXt-Tiny**: For advanced spatial feature extraction.
- **DenseNet-121**: For dense feature reuse.
- **EfficientNet-B0**: For optimized multi-scale perception.

The module utilizes a **Majority Voting Protocol**, ensuring high-precision classification by requiring a consensus between multiple architectures.

### 2. The Triple-Gate Snapping Protocol (Proprietary Logic)
This is the "Gold Standard" logic that transforms raw AI heatmaps into clinically valid Regions of Interest (ROIs).
- **Gate 1 (Tissue Isolation)**: Automatic Hounsfield Unit (HU) filtering to isolate brain parenchyma and exclude bone/CSF artifacts.
- **Gate 2 (Patient Calibration)**: Dynamic calculation of intra-patient mean brain intensity to establish baseline density.
- **Gate 3 (Hypodensity Mapping)**: Identification of the "Ischemic Shelf"—regions dark enough to represent ischemia but above CSF noise.

### 3. XAI Fusion Suite
Integration of multiple Explainable AI methods:
- **Grad-CAM & Score-CAM**: Gradient-based and Activation-based localization.
- **SHAP (SHapley Additive exPlanations)**: Shapley-value voxel importance.
- **PLI (Pixel-Level Importance)**: Direct gradient attribution.

## 📊 Technical Capabilities
- **Batch Processing**: Orchestrated for auditing large cohorts (1,500+ slices).
- **Clinical Proofing**: Generates unified "Clinical Mosaics" showing raw CT, XAI pillars, and the final **Triple-Gate ROI**.
- **Redacted Parameters**: Note that specific HU thresholds and fusion weights are redacted in this public skeleton to protect proprietary clinical discoveries.

---
*Developed by Vidit Zainith — Characterizing the intersection of deep learning and radiological physics.*
