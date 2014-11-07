from model.firefly_model import FireFlyModel
from Tkinter import *


class MainFrameController:

    @staticmethod
    def variable_names():
        return FireFlyModel.variable_names()

    @staticmethod
    def variable_defaults():
        return FireFlyModel.variable_defaults()

    def start_callback(self):
        from ui.main_frame import MainFrame
        if isinstance(self.board, MainFrame):
            board = self.board
            variables = {}
            for p in MainFrameController.variable_names():
                variables[p] = float(board.params_containers[p].param_input.get())
            self.write_to_console("Begin...")
            self.write_to_console("Initial params:")
            self.write_to_console(variables.__str__())

    def reset_callback(self):
        from ui.main_frame import MainFrame
        if isinstance(self.board, MainFrame):
            board = self.board
            for p in board.params:
                board.params_containers[p].param_input.delete(0, END)
                board.params_containers[p].param_input.insert(0, FireFlyModel.variable_defaults()[p])
        self.write_to_console("Reset...")

    def __init__(self, model):
        """
        :param model:
        :type model: FireFlyModel
        :return:
        """
        self.board = None

    def set_board(self, board):
        self.board = board

    def write_to_console(self, txt):
        self.board.console.insert(END, txt + '\n')