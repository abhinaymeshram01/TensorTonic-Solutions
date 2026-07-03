import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    X = np.array(X)
    y = np.array(y)

    X_T = X.T

    XTX = np.dot(X_T, X)
    XTy = np.dot(X_T, y)

    XTX_inv = np.linalg.inv(XTX)

    w = np.dot(XTX_inv, XTy)

    return w