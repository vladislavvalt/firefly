from Tkinter import *
from controllers.main_frame_controller import MainFrameController


class MainFrame(Frame):

    def start_button_callback(self, event):
        if self.controller is not None:
            self.controller.start_callback()

    def reset_button_callback(self, event):
        if self.controller is not None:
            self.controller.reset_callback()

    def init_ui(self):
        # build top menu
        self.top_menu = Frame(self)
        self.top_menu.config(bg="blue")
        self.top_menu.pack(fill=BOTH, expand=True, side=TOP)

        self.param_a_input = Entry(self.top_menu)
        self.param_a_input.pack(padx=2, pady=2, side=LEFT)

        self.param_b_input = Entry(self.top_menu)
        self.param_b_input.pack(padx=2, pady=2, side=LEFT)

        self.start_button = Button(self.top_menu, height=4, text="Start")
        self.start_button.pack(padx=2, pady=2, side=LEFT)
        self.start_button.bind('<Button-1>', self.start_button_callback)

        self.reset_button = Button(self.top_menu, height=4, text="Reset")
        self.reset_button.pack(padx=2, pady=2, side=LEFT)
        self.reset_button.bind('<Button-1>', self.reset_button_callback)

        # build bottom console
        self.bottom_console = Frame(self)
        self.bottom_console.config(bg="yellow")
        self.bottom_console.pack(fill=BOTH, expand=TRUE, side=BOTTOM)

        self.console = Text(self.bottom_console, height=5)
        self.console.pack(padx=2, pady=2)

    def center_window(self):
        w = 800
        h = 640
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) * 0.25
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def __init__(self, master, controller):
        """
        :param master:
        :param controller:
        :type controller: MainFrameController
        :return:
        """
        Frame.__init__(self, master)
        self.parent = master
        if controller is not None:
            self.controller = controller
            controller.set_board(self)
        self.parent.title('Firefly!')

        self.config({"bg": "chocolate"})
        self.pack(fill=BOTH, expand=True)

        # menu params
        self.top_menu = None
        self.param_a_input = None
        self.param_b_input = None
        self.start_button = None
        self.reset_button = None

        #console output
        self.bottom_console = None
        self.console = None

        self.center_window()
        self.init_ui()