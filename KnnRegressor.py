import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import seaborn as sns


# let's make sure it's continuous hypothesis
def visualize_data(residuary_resistances):
    sorted(residuary_resistances)
    plt.plot(residuary_resistances)


def knn_regression(raw_data, feature_names, target_name):
    residuary_resistances = (raw_data[target_name])
    print(residuary_resistances)
    # visualize_data(residuary_resistances)
    # features = torch.tensor(raw_data[feature_names].values)
    # print(features)