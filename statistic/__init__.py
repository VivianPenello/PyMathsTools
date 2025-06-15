"""

Statistics subpackage for PyMathsTool.

This subpackage provides tools for statistical operations.

"""

from .statistic import mean, median, mode, variance, standard_deviation, correlation_coefficient, linear_regression, histogram, box_plot, t_test, chi_square_test, anova, normal_distribution

__all__ = [
    "mean",
    "median",
    "mode",
    "variance",
    "standard_deviation",
    "correlation_coefficient",
    "linear_regression",
    "histogram",
    "box_plot",
    "t_test",
    "chi_square_test",
    "anova",
    "normal_distribution"
]