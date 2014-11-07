from model.firefly_model import FireFlyModel


class MainFrameController:

    def start_callback(self):
        print "START callback!"

    def reset_callback(self):
        print "RESET callback!"

    def __init__(self, model):
        """
        :param model:
        :type model: FireFlyModel
        :return:
        """
        self.board = None

    def set_board(self, board):
        self.board = board