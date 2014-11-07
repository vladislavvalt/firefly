__author__ = 'vladvalt'


variables_dict = {'a0': 0, 'y': 1, 'N': 10, 'max_iter': 50}


class FireFlyModel:

    @staticmethod
    def variable_names():
        return variables_dict.keys()

    @staticmethod
    def variable_defaults():
        return variables_dict

    def __init__(self):
        pass

