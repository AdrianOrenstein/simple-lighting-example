# import pytorch_lightning as pl
from src.ml.resnet import BasicBlock, Resnet
import torch

if __name__ == "__main__":

    # Use our own
    resnet18_classifier = Resnet(num_classes=10, block=BasicBlock, layers=[2, 2, 2, 2])

    example_image = torch.rand(1, 3, 256, 256)

    print(resnet18_classifier(example_image).shape)
