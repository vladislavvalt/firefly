from threading import Thread
import threading
import numpy as np
import time
import math
from model.firefly import Firefly

__author__ = 'vladvalt'


class FireflyEmulation(Thread):

    def run(self):
        self.begin()
        self.execution_finished = True

    def __init__(self, a0, y, n, N, max_iter, energy_func, t=0.01, l_bound=-10, r_bound=10,
                 output_writer=None, callback=None):
        threading.Thread.__init__(self)
        self.a0 = a0
        self.y = y
        self.n = n
        self.N = N
        self.max_iter = max_iter
        self.energy_func = energy_func
        self.l_bound = l_bound
        self.r_bound = r_bound
        self.callback = callback

        self.t = 0.01
        if t is not None:
            self.t = t

        from model.firefly_model import IOutputWriter
        self.output_writer = None
        if output_writer is not None and isinstance(output_writer, IOutputWriter):
            self.output_writer = output_writer

        self.fire_flies = []

        self.should_stop = False
        self.execution_finished = False

    def begin(self):
        self.write_output('')
        self.write_output('')

        for i in range(self.N):
            firefly = Firefly(id=i,
                              position=np.random.uniform(self.l_bound, self.r_bound))
            self.fire_flies.append(firefly)
            self.write_output('New firefly appended')

        self.write_output('')

        self.write_output('Initial state:')
        for sf in self.fire_flies:
            self.write_output(str(sf))
        self.write_output('')

        sorted_fireflies = self.fire_flies

        time.sleep(self.t)

        for i in range(self.max_iter):
            if not self.should_stop:
                sorted_fireflies = sorted(sorted_fireflies, key=lambda x: x.energy(self.energy_func))
                for j in range(len(sorted_fireflies) - 1):
                    moving_firefly = sorted_fireflies[j]
                    staying_firefly = sorted_fireflies[j + 1]
                    if isinstance(moving_firefly, Firefly) and isinstance(staying_firefly, Firefly):
                        move_step = self.attractiveness(moving_firefly, staying_firefly) \
                        * (staying_firefly.position - moving_firefly.position)
                        alpha = np.random.uniform(-1, 1) * (1.0 / (i+1))
                        moving_firefly.position += move_step + alpha

                self.write_output('State after ' + str(i) + ' iteration:')
                for sf in sorted_fireflies:
                    self.write_output(str(sf))
                self.write_output('')
            else:
                sorted_fireflies = None
                break

            time.sleep(self.t)

        if sorted_fireflies is not None and len(sorted_fireflies) == 0:
            sorted_fireflies = None

        if sorted_fireflies is not None:
            result_fireflies = [x for x in sorted_fireflies
                                if math.floor(x.position) in range(int(self.l_bound), int(self.r_bound))]

            self.write_output('')
            self.write_output('The best founded solution:')
            self.write_output(str(result_fireflies[-1]))
            if self.callback is not None and callable(self.callback):
                solutions = map(lambda x: x.position, result_fireflies)
                self.callback(solutions)

    def attractiveness(self, firefly_i, firefly_j):
        if isinstance(firefly_i, Firefly) and isinstance(firefly_j, Firefly):
            return self.a0 * np.exp(-self.y * (firefly_i.distance(firefly_j) ** self.n))

    def write_output(self, output):
        if self.output_writer is not None:
            self.output_writer.write_output(output)

    def stop_execution(self):
        self.should_stop = True

    def is_execution_finished(self):
        return self.execution_finished