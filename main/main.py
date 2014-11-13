from Tkinter import *
from model.firefly_model import FireflyModel
from ui.main_frame import MainFrame
from controllers.main_frame_controller import MainFrameController
import numpy as np

root = Tk()

#init_actual_func = lambda x: x ** 2

#init_actual_func = lambda x: 3 - 3 * np.cos(2 * np.pi * x)

init_actual_func = lambda x: 3 + x ** 2 - 3 * np.cos(2 * np.pi * x)

init_energy_func = lambda x: np.exp(-init_actual_func(x))

model = FireflyModel(energy_func=init_energy_func, actual_func=init_actual_func)
controller = MainFrameController(model=model)
model.set_output_writer(controller)
app = MainFrame(master=root, controller=controller)

root.mainloop()