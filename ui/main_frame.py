from Tkinter import *
from controllers.main_frame_controller import MainFrameController


class MainFrame(Frame):

    def start_button_callback(self, event):
        if self.controller is not None:
            self.controller.start_callback()

    def reset_button_callback(self, event):
        if self.controller is not None:
            self.controller.reset_callback()

    def draw_button_callback(self, event):
        if self.controller is not None:
            self.controller.draw_callback()

    def init_ui(self):
        # build top menu
        self.top_menu = Frame(self)
        self.top_menu.config(bg="orange")
        self.top_menu.pack(fill=BOTH, expand=True, side=TOP)

        for p in self.params.keys():
            self.params_containers[p] = Frame(self.top_menu)
            current_container = self.params_containers[p]
            current_container.config(bg="orange")
            current_container.pack(fill=BOTH, side=LEFT)

            current_container.param_label = Label(current_container, text=p)
            current_container.param_label.pack(padx=2, pady=2)

            current_container.param_input = Entry(current_container, width=6)
            current_container.param_input.insert(0, self.params[p])
            current_container.param_input.pack(padx=2, pady=2)

        self.start_button = Button(self.top_menu, text="Draw")
        self.start_button.pack(side=RIGHT)
        self.start_button.bind('<Button-1>', self.draw_button_callback)

        self.reset_button = Button(self.top_menu, text="Reset")
        self.reset_button.pack(side=RIGHT)
        self.reset_button.bind('<Button-1>', self.reset_button_callback)

        self.start_button = Button(self.top_menu, text="Start")
        self.start_button.pack(side=RIGHT)
        self.start_button.bind('<Button-1>', self.start_button_callback)

        # build bottom console
        self.bottom_console = Frame(self)
        self.bottom_console.config(bg="chocolate")
        self.bottom_console.pack(fill=BOTH, expand=TRUE, side=BOTTOM)

        self.bottom_console.label = Label(self.bottom_console, text="Output", font=("Purisa",25))
        self.bottom_console.label.pack(pady=10)

        self.console = Text(self.bottom_console)
        self.console.pack()

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

        self.params = MainFrameController.variable_defaults()
        self.params_containers = {}

        self.start_button = None
        self.reset_button = None
        self.draw_button = None

        # console output
        self.bottom_console = None
        self.console = None

        self.center_window()
        self.init_ui()