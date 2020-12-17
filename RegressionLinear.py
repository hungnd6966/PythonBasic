from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
import time


def get_param_Linear_Regression(X, y):
    '''
    Parameter:
        X: numpy array with X.shapre = (n, 1) and n is size of data
        y: numpy array with y.shapre = (n, 1) and n is size of data
    Output:
        return [w_0, w_1] with line y = w_0 + w_1*x is fitting line of linear regression method for data (X, y)
    '''

    # Building Xbar
    one = np.ones((X.shape[0], 1))
    Xbar = np.concatenate((one, X), axis=1)
    regr = linear_model.LinearRegression(
        fit_intercept=False)        # fit_intercept = False for calculating the bias
    regr.fit(Xbar, y)
    return regr.coef_[0]


def draw_LR_fitting_line(X, y, w_0, w_1):
    '''
    Parameter:
        X: numpy array with X.shapre = (n, 1) and n is size of data
        y: numpy array with y.shapre = (n, 1) and n is size of data
        [w_0, w_1] is linear regression result of data (X, y)
    Output:
        Drawing the fitting line
    '''

    # Drawing the fitting line
    x0 = np.linspace(145, 185, 2)
    y0 = w_0 + w_1*x0

    plt.plot(X.T, y.T, 'ro')        # data
    plt.plot(x0, y0)                # the fitting line
    plt.axis([140, 190, 45, 75])
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')
    plt.show()


def main():
    start = time.time()
    # height (cm)
    X = np.array(
        [[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
    # weight (kg)
    y = np.array([[49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

    w_0, w_1 = get_param_Linear_Regression(X, y)
    print("Fitting Line: y = {0:.2f} + {1:.2f}*x".format(w_0, w_1))

    print("Running time: {0:.3f} s".format(time.time()-start))

    # Drawing result
    draw_LR_fitting_line(X, y, w_0, w_1)


if __name__ == "__main__":
    main()
