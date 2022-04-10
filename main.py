import KnnRegressor
import Util


def do_first_task():
    filename = "resources/yacht_hydrodynamics.data"
    feature_names = ["long_position", "prismatic_coef", "len_to_displacement", "beam_to_draught", "len_to_beam",
                     "froude_num"]
    target_name = ["residuary_resist"]
    yacht_data = Util.read_file(filename, ' ', feature_names + target_name)

    KnnRegressor.knn_regression(yacht_data, feature_names, target_name)


def do_second_task():
    filename = "resources/balance-scale.data"
    feature_names = ["left_weight", "left-distance", "right-weight", "right-distance"]
    target_name = ["scale"]
    balance_data = Util.read_file(filename, ',', target_name + feature_names)
    print(balance_data)


if __name__ == '__main__':
    # do_first_task()
    do_second_task()
