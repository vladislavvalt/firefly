import collections
from model.firefly_emulation import FireflyEmulation

__author__ = 'vladvalt'


variables_dict = collections.OrderedDict([('a0', 0), ('y', 1), ('N', 10), ('max_iter', 50), ('n', 1), ('t', 0.01),
                                          ('l_bound', -10), ('r_bound', 10)])

# collections.OrderedDict(
# {'a0': 0, 'y': 1, 'N': 10, 'max_iter': 50, 'n': 1, 't': 0.01, 'left_b': -100, 'right_b': 100})


class FireflyModel:

    @staticmethod
    def variable_names():
        return variables_dict.keys()

    @staticmethod
    def variable_defaults():
        return variables_dict

    def __init__(self, energy_func, actual_func, output_writer=None):
        self.variables = variables_dict.copy()
        self.energy_func = energy_func
        self.actual_func = actual_func
        self.output_writer = None
        self.current_emulation = None
        self.current_solutions = None
        self.l_bound = variables_dict['l_bound']
        self.r_bound = variables_dict['r_bound']
        if output_writer is not None and isinstance(output_writer, IOutputWriter):
            self.output_writer = output_writer

    def best_current_solution(self):
        if self.current_emulation is not None and len(self.current_solutions) > 0:
            return self.current_solutions[-1]

    def set_output_writer(self, output_writer):
        if output_writer is not None and isinstance(output_writer, IOutputWriter):
            self.output_writer = output_writer

    def start(self, variables):
        if isinstance(variables, dict):
            variables_correct = True
            for v in FireflyModel.variable_names():
                if v not in variables:
                    variables_correct = False
                    break

            if variables_correct:
                if self.output_writer is not None:
                    self.output_writer.write_output("Variables correct")
                self.variables = variables

                self.l_bound = variables['l_bound']
                self.r_bound = variables['r_bound']

                if self.current_emulation is None or self.current_emulation.is_execution_finished():
                    emulation = FireflyEmulation(a0=self.variables['a0'],
                                                 y=self.variables['y'],
                                                 n=self.variables['n'],
                                                 N=int(self.variables['N']),
                                                 max_iter=int(self.variables['max_iter']),
                                                 energy_func=self.energy_func,
                                                 t=self.variables['t'],
                                                 l_bound=self.variables['l_bound'],
                                                 r_bound=self.variables['r_bound'],
                                                 output_writer=self.output_writer,
                                                 callback=self.emulation_done_callback)
                    self.current_emulation = emulation
                    emulation.start()
            else:
                if self.output_writer is not None:
                    self.output_writer.write_output("Variables incorrect!")

    def stop_current_process(self):
        emulation_to_stop = self.current_emulation
        if emulation_to_stop is not None and isinstance(emulation_to_stop, FireflyEmulation):
            emulation_to_stop.stop_execution()
            self.current_emulation = None

    def emulation_done_callback(self, solutions):
        if solutions is not None:
            self.current_solutions = solutions

    def draw_func(self):
        import numpy as np
        import matplotlib.pyplot as plt

        x = np.arange(self.l_bound, self.r_bound, 0.1);
        y = self.actual_func(x)
        plt.plot(x, y)

        plt.title('Current function', fontsize=14, fontweight='bold')

        if self.current_solutions is not None:
            plt.plot(self.current_solutions[-1], self.actual_func(self.current_solutions[-1]), 'ro', markersize=20)
            for i in range(len(self.current_solutions) - 1):
                plt.plot(self.current_solutions[i], self.actual_func(self.current_solutions[i]), 'go', markersize=5)
        plt.show()


class IOutputWriter:

    def write_output(self, output):
        pass

    def __init__(self):
        pass