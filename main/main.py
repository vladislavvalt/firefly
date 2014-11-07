from Tkinter import *
from model.firefly_model import FireFlyModel
from ui.main_frame import MainFrame
from controllers.main_frame_controller import MainFrameController

root = Tk()

model = FireFlyModel()
controller = MainFrameController(model=model)
app = MainFrame(master=root, controller=controller)

root.mainloop()