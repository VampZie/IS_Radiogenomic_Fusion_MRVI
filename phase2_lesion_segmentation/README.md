# Phase 2: Lesion Segmentation & Recursive Swarm Discovery

## 🔬 Overview
Phase 2 scales the classification logic into a **Recursive Swarm Segmentation** system. It uses a high-dimensional consensus matrix and an optimization-based scouting algorithm to identify focal ischemic centers across a multi-model ensemble.

## 🛠️ Key Components

### 1. 12-Way Consensus Matrix
The decision-making heart of the suite. It intersects **3 backbone architectures** (ConvNeXt, DenseNet, EfficientNet) with **4 XAI modalities** (Grad-CAM, ScoreCAM, SHAP, and Pixel Importance). This 12-way intersection ensures that only regions where all tools and models agree are promoted for segmentation.

### 2. Recursive Swarm Scout (PSO Optimization)
To identify the most "clinically potent" ROI center, we utilize **Particle Swarm Optimization (PSO)**.
- **Inertia & Cognitive Pull**: Particles are driven by both their personal discovery and the global ensemble "best" signal.
- **Goal**: Auto-snapping to the primary ischemic island while ignoring transient noise flecks.

### 3. Noise & Artifact Exclusion 
A rigorous "Exclusion Suite" to handle radiological edge cases:
- **Ventricular Blanking**: Removes signals that leak into the low-density CSF of the ventricles.
- **Symmetry Filtering**: Detects and eliminates bilateral signals (e.g., bone-thinning artifacts) which the AI might mistake for ischemia.

### 4. Omega-Level Adversarial Stress Test
This module verifies the reliability of the AI findings. By injecting Gaussian noise into the input CT and measuring the **Jensen-Shannon Divergence** between original and noisy heatmaps, the system calculates a % Reliability Metric.

## 📊 Technical Capabilities
- **Focal Point Discovery**: Identifies N separate ischemic islands per slice.
- **Stability Reporting**: Output Includes a "Reliability Score" to assist clinical interpretation.
- **Clinical Verification**: Generates multi-panel "Clinical Proofs" with dynamic zoom on the primary swarm-discovered core.

---
*Developed by Vidit Zainith — Implementing robust, swarm-guided lesion discovery architectures.*
