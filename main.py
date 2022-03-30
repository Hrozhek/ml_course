import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def knn_regression(file_name):
    raw_data = pd.read_csv(file_name, index_col=0)
    print(raw_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    knn_regression("resources/yacht_hydrodynamics.data")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
