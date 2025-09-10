#  ###  Linear Algebra With Numpy
# What is Linear Algebra?
# Linear Algebra is the branch of mathematics that deals with vectors and matrices — the main tools for handling data in machine learning.

# - **Why it matters in ML**
#    - A dataset = matrix (rows = samples, columns = features).

#    - An image = matrix of pixel values.

#    - Predictions, weights, activations = all use vectors/matrices

# Key Applications in ML

# - Feature representation (data points as vectors)
# - Transformations and dimensionality reduction
# - Neural network operations
# - Optimization algorithms

import numpy as np
import matplotlib.pyplot as plt


#  Vectors

# What is a Vector?
#  - A vector is simply a list of numbers arranged in order. Think of it like a row of lockers, each holding a value (e.g., age, weight, score, etc.).

#  - Imagine you're holding a shopping list:

#   - ["apples", "bananas", "bread"] → text list

#   - [2, 5, 1] → quantities → This is like a vector!


# install numpy if not already installed
# pip install numpy

# importing numpy for numerical operations

import numpy as np