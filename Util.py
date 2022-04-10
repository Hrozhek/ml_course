import pandas as pd


def read_file(filename, delimiter, columns):
    data = pd.read_csv(filepath_or_buffer=filename, delimiter=delimiter, header=None)
    data.columns = columns
    return data


def split_set(data, train_ratio):
    pass  # todo: class with two fields? Or maybe it is possible to return two values?
