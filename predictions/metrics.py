__author__ = "Celso M. de Melo"
__email__ = "celsodemelo@eleveninc.com"

import numpy as np


def linear_regression_accuracy(ground_truth, predictions, error_threshold=5.0):
    abs_residuals = np.abs(np.subtract(ground_truth, predictions))

    count = 0.0
    accurate = 0.0
    for r in abs_residuals:
        count += 1
        if r <= error_threshold:
            accurate += 1

    return accurate / count


def linear_regression_accuracy_greater_or_equal_than(ground_truth, predictions, error_threshold=0):
    count = 0.0
    accurate = 0.0
    for index, g in np.ndenumerate(ground_truth):
        count += 1
        if (predictions[index] - error_threshold) <= g:
            accurate += 1

    return accurate / count

def find_error_for_accuracy_target(ground_truth, predictions, desired_accuracy=0.70, error_step=0.10):
    current_accuracy = 0.0
    current_error = 0.0

    while current_accuracy < desired_accuracy:
        current_error += error_step
        current_accuracy = linear_regression_accuracy_greater_or_equal_than(ground_truth, predictions, current_error)
        if current_error >= 100.0:
            break

    return current_accuracy, current_error