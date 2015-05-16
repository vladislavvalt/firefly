__author__ = 'vladvalt'

from model.firefly_model import FireflyModel
import numpy as np
import collections
import time


def load_variable_set():
    variables_1 = collections.OrderedDict([('a0', 0), ('y', 1), ('N', 30), ('max_iter', 50), ('n', 1), ('t', 0.01),
                                           ('l_bound', -50), ('r_bound', 500)])
    variables_2 = collections.OrderedDict([('a0', 10), ('y', 1), ('N', 30), ('max_iter', 50), ('n', 1), ('t', 0.01),
                                           ('l_bound', -50), ('r_bound', 500)])
    variables_3 = collections.OrderedDict([('a0', 0), ('y', 1), ('N', 50), ('max_iter', 50), ('n', 1), ('t', 0.01),
                                           ('l_bound', -50), ('r_bound', 500)])
    variables_4 = collections.OrderedDict([('a0', 10), ('y', 1), ('N', 50), ('max_iter', 50), ('n', 1), ('t', 0.01),
                                           ('l_bound', -50), ('r_bound', 500)])
    variables_5 = collections.OrderedDict([('a0', 10), ('y', 1), ('N', 30), ('max_iter', 50), ('n', 2), ('t', 0.01),
                                           ('l_bound', -50), ('r_bound', 500)])
    variables_6 = collections.OrderedDict([('a0', 10), ('y', 4), ('N', 30), ('max_iter', 50), ('n', 5), ('t', 0.01),
                                           ('l_bound', -50), ('r_bound', 500)])
    variables_7 = collections.OrderedDict([('a0', 2), ('y', 1), ('N', 50), ('max_iter', 50), ('n', 1), ('t', 0.01),
                                           ('l_bound', -50), ('r_bound', 500)])
    variables_8 = collections.OrderedDict([('a0', 5), ('y', 1), ('N', 100), ('max_iter', 50), ('n', 1), ('t', 0.01),
                                           ('l_bound', -50), ('r_bound', 500)])
    variables_9 = collections.OrderedDict([('a0', 10), ('y', 1), ('N', 30), ('max_iter', 25), ('n', 1), ('t', 0.01),
                                           ('l_bound', -50), ('r_bound', 500)])
    variables_10 = collections.OrderedDict([('a0', 10), ('y', 1), ('N', 50), ('max_iter', 75), ('n', 1), ('t', 0.01),
                                            ('l_bound', -50), ('r_bound', 500)])
    # return [variables_1]
    return [variables_1, variables_2, variables_3, variables_4, variables_5,
            variables_6, variables_7, variables_8, variables_9, variables_10]

variable_sets = load_variable_set()

import xlsxwriter

workbook = xlsxwriter.Workbook('../output/report.xlsx')
worksheet = workbook.add_worksheet("Page1")

config_merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#969696'})

task1_merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '9999FF'})

task2_merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#99CC00'})

task3_merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#339966'})

run1_merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#008000'})

run2_merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#FFFF99'})

run3_merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#FF8080'})

average_merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#FFFFCC'})

best_merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#FF0000'})

worksheet.merge_range('A1:G2', 'Configuration', config_merge_format)
worksheet.merge_range('H1:V1', 'Task1(Rastirigin)', task1_merge_format)
worksheet.merge_range('W1:AK1', 'Task2(Graivonok)', task2_merge_format)
worksheet.merge_range('AL1:AZ1', 'Task3(Shefel)', task3_merge_format)

worksheet.merge_range('H2:J2', 'Run1', run1_merge_format)
worksheet.merge_range('K2:M2', 'Run2', run2_merge_format)
worksheet.merge_range('N2:P2', 'Run3', run3_merge_format)
worksheet.merge_range('Q2:S2', 'Average', average_merge_format)
worksheet.merge_range('T2:V2', 'Best result', best_merge_format)

worksheet.merge_range('W2:Y2', 'Run1', run1_merge_format)
worksheet.merge_range('Z2:AB2', 'Run2', run2_merge_format)
worksheet.merge_range('AC2:AE2', 'Run3', run3_merge_format)
worksheet.merge_range('AF2:AH2', 'Average', average_merge_format)
worksheet.merge_range('AI2:AK2', 'Best result', best_merge_format)

worksheet.merge_range('AL2:AN2', 'Run1', run1_merge_format)
worksheet.merge_range('AO2:AQ2', 'Run2', run2_merge_format)
worksheet.merge_range('AR2:AT2', 'Run3', run3_merge_format)
worksheet.merge_range('AU2:AW2', 'Average', average_merge_format)
worksheet.merge_range('AX2:AZ2', 'Best result', best_merge_format)


parameters_format = workbook.add_format({
    'border': 1,
    'align': 'center',
    'fg_color': '#FF9900'
})
parameters_format.set_rotation('90')

metrics_format = workbook.add_format({
    'border': 1,
    'align': 'center',
})
metrics_format.set_rotation('90')


worksheet.write('A3', 'a0', parameters_format)
worksheet.write('B3', 'y', parameters_format)
worksheet.write('C3', 'N', parameters_format)
worksheet.write('D3', 'max_iter', parameters_format)
worksheet.write('E3', 'n', parameters_format)
worksheet.write('F3', 'left_bound', parameters_format)
worksheet.write('G3', 'right_bound', parameters_format)

for i in range(len(variable_sets)):
    variable_set = variable_sets[i]
    index = 3 + i
    worksheet.write(index, 0, variable_set['a0'])
    worksheet.write(index, 1, variable_set['y'])
    worksheet.write(index, 2, variable_set['N'])
    worksheet.write(index, 3, variable_set['max_iter'])
    worksheet.write(index, 4, variable_set['n'])
    worksheet.write(index, 5, variable_set['l_bound'])
    worksheet.write(index, 6, variable_set['r_bound'])


solution_area_col_index = 7
solution_area_row_index = 3

for i in range(solution_area_col_index, 52):
    modulo = (i - 7) % 3
    msg = ""
    if modulo == 0:
        msg = "Answer is near the optimal"
    elif modulo == 1:
        msg = "Difference between f(x) and y"
    else:
        msg = "Energy function value"
    worksheet.write(2, i, msg, metrics_format)


variables_dict = collections.OrderedDict([('a0', 0), ('y', 1), ('N', 10), ('max_iter', 50), ('n', 1), ('t', 0.01),
                                          ('l_bound', -10), ('r_bound', 10)])


eps = 0.25
rastrigin_func = lambda x: 3 + x ** 2 - 3 * np.cos(2 * np.pi * x)
graivonok_func = lambda x: x ** 2 / 4000 - np.cos(x) + 1
shefel_func = lambda x: - x * np.sin(abs(x) ** 0.5)

functions = [rastrigin_func, graivonok_func, shefel_func]
x_optimals = [0.0, 0.0, 420.9687]
y_optimals = [0.0, 0.0, -418.98]


for i in range(len(functions)):
    x_optimal = x_optimals[i]
    y_optimal = y_optimals[i]
    actual_func = functions[i]
    energy_func = lambda x: np.exp(-abs(y_optimal-actual_func(x)))
    current_col_index = solution_area_col_index + i * 15

    for k in range(len(variable_sets)):
        agregation_params = [0.0, 0.0, 0.0]
        max_params = ['-', 100.0, 0.0]
        counter = 0
        for j in range(3):
            variable_set = variable_sets[k]
            model = FireflyModel(energy_func=energy_func, actual_func=actual_func)

            model.start(variable_set)

            while model.current_solutions is None:
                time.sleep(0.1)
            best_solution = model.best_current_solution()
            abs_diff = abs(actual_func(best_solution) - y_optimal)

            if abs(x_optimal - best_solution) < eps:
                agregation_params[0] += 1
                max_params[0] = '+'
                close = '+'
            else:
                close = '-'

            agregation_params[1] += abs_diff
            agregation_params[2] += energy_func(best_solution)
            max_params[1] = min(max_params[1], abs_diff)
            max_params[2] = max(max_params[2], energy_func(best_solution))
            counter += 1

            col_index_to_use = current_col_index + j * 3
            worksheet.write(solution_area_row_index + k, col_index_to_use, close)
            worksheet.write(solution_area_row_index + k, col_index_to_use + 1, abs_diff)
            worksheet.write(solution_area_row_index + k, col_index_to_use + 2, energy_func(best_solution))

        average_params = [0.0, agregation_params[1] / counter, agregation_params[2] / counter]
        if agregation_params[0] > 1:
            average_params[0] = '+'
        else:
            average_params[0] = '-'

        col_index_to_use_after = current_col_index + 3 * 3
        col_index_to_use_after_after = current_col_index + 4 * 3
        for j in range(3):
            worksheet.write(solution_area_row_index + k, col_index_to_use_after + j, average_params[j])
            worksheet.write(solution_area_row_index + k, col_index_to_use_after_after + j, max_params[j])

workbook.close()



