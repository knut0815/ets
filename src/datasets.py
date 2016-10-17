import numpy as np


# Test data, taken from the R expsmooth package (expsmooth::bonds).
bonds = np.asarray([
    5.83, 6.06, 6.58, 7.09, 7.31, 7.23, 7.43, 7.37, 7.6, 7.89, 8.12, 7.96,
    7.93, 7.61, 7.33, 7.18, 6.74, 6.27, 6.38, 6.6, 6.3, 6.13, 6.02, 5.79,
    5.73, 5.89, 6.37, 6.62, 6.85, 7.03, 6.99, 6.75, 6.95, 6.64, 6.3, 6.4,
    6.69, 6.52, 6.8, 7.01, 6.82, 6.6, 6.32, 6.4, 6.11, 5.82, 5.87, 5.89,
    5.63, 5.65, 5.73, 5.72, 5.73, 5.58, 5.53, 5.41, 4.87, 4.58, 4.89, 4.69,
    4.78, 4.99, 5.23, 5.18, 5.54, 5.9, 5.8, 5.94, 5.91, 6.1, 6.03, 6.26,
    6.66, 6.52, 6.26, 6, 6.42, 6.1, 6.04, 5.83, 5.8, 5.74, 5.72, 5.23,
    5.14, 5.1, 4.89, 5.13, 5.37, 5.26, 5.23, 4.97, 4.76, 4.55, 4.61, 5.07,
    5, 4.9, 5.28, 5.21, 5.15, 4.9, 4.62, 4.24, 3.88, 3.91, 4.04, 4.03,
    4.02, 3.9, 3.79, 3.94, 3.56, 3.32, 3.93, 4.44, 4.29, 4.27, 4.29, 4.26,
    4.13, 4.06, 3.81, 4.32, 4.7])