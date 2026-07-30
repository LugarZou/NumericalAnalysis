import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.optimize


def fit(x, y, n, output=False):
    A = np.zeros((n, n))
    elementList = []
    for i in range(2 * n - 1):
        val = 0
        for j in x:
            val += j**i
        elementList.append(val)
    for i in range(n):
        for j in range(n):
            A[i][j] = elementList[i + j]
    b = np.zeros(n)
    for i in range(n):
        val = 0
        for j in range(len(x)):
            val += y[j] * x[j] ** i
        b[i] = val
    return np.linalg.solve(A, b)


def rational1_1(x, p0, q0):
    return np.polyval([p0, 1], x) / np.polyval([q0, 1], x)

def rational1_2(x, p0, q0, q1):
    return np.polyval([p0, 1], x) / np.polyval([q0, q1, 1], x)

def rational1_3(x, p0, q0, q1, q2):
    return np.polyval([p0, 1], x) / np.polyval([q0, q1, q2, 1], x)

def rational1_4(x, p0, q0, q1, q2, q3):
    return np.polyval([p0, 1], x) / np.polyval([q0, q1, q2, q3, 1], x)

def rational2_1(x, p0, p1, q0):
    p = [p0, p1]
    q = [q0]
    return np.polyval(p + [1], x) / np.polyval(q + [1.0], x)

def rational2_2(x, p0, p1, q0, q1):
    p = [p0, p1]
    q = [q0, q1]
    return np.polyval(p + [1], x) / np.polyval(q + [1.0], x)

def rational2_3(x, p0, p1, q0, q1, q2):
    p = [p0, p1]
    q = [q0, q1, q2]
    return np.polyval(p + [1], x) / np.polyval(q + [1.0], x)

def rational3_1(x, p0, p1, p2, q1):
    p = [p0, p1, p2]
    q = [q1]
    return np.polyval(p + [1], x) / np.polyval(q + [1.0], x)

def rational3_2(x, p0, p1, p2, q1, q2):
    p = [p0, p1, p2]
    q = [q1, q2]
    return np.polyval(p + [1], x) / np.polyval(q + [1.0], x)

def rational4_1(x, p0, p1, p2, p3, q1):
    p = [p0, p1, p2, p3]
    q = [q1]
    return np.polyval(p + [1], x) / np.polyval(q + [1.0], x)


def calculate_mse(y_true, y_pred):
    """
    Calculate the mean square error between the true y values and the predicted y values.

    Parameters:
    - y_true: The original y values.
    - y_pred: The predicted y values from the polynomial approximation.

    Returns:
    - The mean square error.
    """
    differences = np.array(y_true) - np.array(y_pred)
    squared_differences = differences**2
    mse = squared_differences.mean()
    return mse


if __name__ == "__main__":
    x = [0, 0.1, 0.2, 0.3, 0.5, 0.8]
    y = [1, 0.41, 0.5, 0.61, 0.91, 2.02]
    if False:
        # Plot original points
        plt.scatter(x, y, color="red", label="Original Points")

        opt = [1, 2, 3, 4, 5, 6]
        mses = []
        

        for i in opt:
            coefficients = fit(x, y, i, True)
            # Generate points for the approximation line
            x_fit = np.linspace(min(x), max(x), 500)
            y_fit = sum(coefficients[j] * x_fit**j for j in range(len(coefficients)))
            # Plot approximation line
            plt.plot(x_fit, y_fit, label="Degree " + str(i - 1))
            y_pred = sum(
                coefficients[j] * np.array(x) ** j for j in range(len(coefficients))
            )

            # Calculate MSE
            mse = calculate_mse(y, y_pred)
            mses.append(mse)

        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Polynomial Approximation")
        plt.legend()
        plt.show()
        print("MSEs for different polynomial orders: ", mses)
    mserf = []
    plt.scatter(x, y, color="red", label="Original Points")
    rf1 = [rational1_1, rational1_2, rational1_3, rational1_4]
    rf2 = [rational2_1, rational2_2, rational2_3]
    rf3 = [rational3_1, rational3_2]
    rf4 = [rational4_1]

    for rf in rf1:
        popt, pcov = scipy.optimize.curve_fit(rf, x, y)
        print("Optimal parameters: ", popt)
        x_fit = np.linspace(min(x), max(x), 500)
        y_fit = rf(x_fit, *popt)
        y_fit = [max(min(y,2.1),0.25) for y in y_fit]
        label = str(rf)[10:22]
        plt.plot(x_fit, y_fit, label=label)
        y_pred = rf(np.array(x), *popt)
        mse = calculate_mse(y, y_pred)
        mserf.append(mse)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Rational Approximation")
    plt.legend()
    plt.show()

    print("MSEs for different rational functions: ", mserf)

    
