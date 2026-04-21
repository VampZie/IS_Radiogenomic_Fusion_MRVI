"""
Model Architectures — Radiogenomic Binary Classification
=============================================================================
PURPOSE:
    Defines the deep learning backbone models used in the Juror Ensemble.
    Optimized for high-resolution CT feature extraction.
"""

import torch.nn as nn
from torchvision import models

def get_ensemble_member(name, num_classes=1):
    """
    Returns a modified production-grade backbone model.
    """
    if name == 'convnext':
        # ConvNeXt-Tiny: SOTA Transformer-inspired CNN
        model = models.convnext_tiny(weights='DEFAULT')
        model.classifier[2] = nn.Linear(model.classifier[2].in_features, num_classes)
        
    elif name == 'densenet':
        # DenseNet-121: Superior gradient flow via feature reuse
        model = models.densenet121(weights='DEFAULT')
        model.classifier = nn.Linear(model.classifier.in_features, num_classes)
        
    elif name == 'efficientnet':
        # EfficientNet-B0: Efficient scaling for medical imaging
        model = models.efficientnet_b0(weights='DEFAULT')
        model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
        
    else:
        raise ValueError(f"Model {name} not supported in production suite.")
        
    return model

if __name__ == "__main__":
    print("[SKELETON] Ensembler models initialized.")
