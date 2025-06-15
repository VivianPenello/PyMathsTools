"""
PyMathsTool - A modular mathematics library for Python.

This package provides tools for various branches of mathematics, including:
- Algebra
- Arithmetic
- Calculus
- Geometry
- Linear Algebra
- Statistics

Explore math with code!
"""

from . import calculus
from . import complex
from . import geometry
from . import linear_algebra
from . import statistic

__all__ = [
    "calculus",
    "complex",
    "geometry",
    "linear_algebra",
    "statistic",
]
