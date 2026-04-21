# Methodology: The Molecular Radiomics Vulnerability Index (MRVI)

## 1. Unsupervised Segmentation via Juror Consensus
To eliminate the bottleneck of high-quality manual segmentation in ischemic stroke, we implemented an **unsupervised consensus protocol**. 

- **Concept**: Three independent segmentation models (Jurors) operate on different image features: Intensity, Texture, and Spatial Gradient. 
- **Consensus Logic**: A voxel is only labeled as 'ischemic core' if the weighted agreement between the three jurors exceeds a predetermined consensus threshold (redacted for public release).
- **Anatomical Snapping**: The resulting raw consensus mask undergoes the **Triple-Gate Protocol**, which snaps the borders to the nearest anatomical brain structures using a standard MNI template, removing typical artifacts like skull leakage or vessel noise.

## 2. High-Dimensional Radiomic Swarms
We extract a comprehensive feature set (1,200+ metrics) for each lesion. 
- **Scale**: To handle large clinical cohorts, we utilized a **50-thread CPU swarm architecture**.
- **Features**: We leverage GLCM (Gray Level Co-occurrence Matrix) and GLSZM (Gray Level Size Zone Matrix) to capture fine-grained tissue heterogeneity, which serves as a proxy for underlying cellular stress.

## 3. The MRVI Formula & Fusion
The MRVI represents a novel quantitative bridge between voxel-level imaging and cluster-level transcriptomics (scRNA-seq).

### 3.1 Molecular Stress Scoring
scRNA-seq data from ischemic regions (e.g., penumbra vs. core) was processed to identify cluster-specific inflammatory markers (TNF, IL-1β, GFAP, etc.). These markers are aggregated into a **Molecular Stress Score** for each relevant cell cluster.

### 3.2 Fusion Logic
The MRVI fuses these domains using a weighted linear combination:
`MRVI = (w1 * Radiomic_Entropy) + (w2 * Molecular_Stress_Score)`

- **w1 & w2**: Optimized through cross-modality importance modeling (redacted).
- **Interpretability**: A high MRVI score indicates a "Vulnerability Hotspot"—a region where macro-scale texture predicts severe micro-scale molecular damage, marking it as high-priority for therapeutic intervention.
