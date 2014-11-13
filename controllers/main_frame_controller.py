from model.firefly_model import FireflyModel, IOutputWriter
from Tkinter import *


class MainFrameController(IOutputWriter):

    @staticmethod
    def variable_names():
        return FireflyModel.variable_names()

    @staticmethod
    def variable_defaults():
        return FireflyModel.variable_defaults()

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

            if self.model is not None:
                self.model.start(variables)

    def reset_callback(self):
        from ui.main_frame import MainFrame
        if isinstance(self.board, MainFrame):
            board = self.board
            for p in board.params:
                board.params_containers[p].param_input.delete(0, END)
                board.params_containers[p].param_input.insert(0, FireflyModel.variable_defaults()[p])
        self.write_to_console("Reset...")
        if self.model is not None:
            self.model.stop_current_process()

    def draw_callback(self):
        if self.model is not None:
            self.model.draw_func()

    def __init__(self, model):
        """
        :param model:
        :type model: FireFlyModel
        :return:
        """
        self.board = None
        self.model = None
        if isinstance(model, FireflyModel):
            self.model = model

    def set_board(self, board):
        self.board = board

    def write_to_console(self, txt):
        self.board.console.insert(END, txt + '\n')

    def write_output(self, output):
        return self.write_to_console(output)