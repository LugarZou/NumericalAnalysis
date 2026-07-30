from cal_num import calculate_n
def stationary_point(x0, f, tol=1e-6, max_iter=1000):
    x = x0
    for i in range(max_iter):
        x_new = f(x)
        if abs(x_new - x) < tol:
            print("Converge after %d iterations" % i)
            return x
        x = x_new
    raise ValueError("Failed to converge in %d iterations" % max_iter)


def f(x):
    return x**3 - 3 * x - 1


def df(x):
    return 3 * x**2 - 3


def newton_method(x0, f, df, tol=4, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        print("x_%d = %f, x_%d = %f" % (i, x, i + 1, x_new))
        if calculate_n(x_new, 1.87938524) >= tol:
            print("Converge after %d iterations" % i)
            return x_new
        x = x_new
    return x


x0 = 2
x_star_newton = newton_method(x0, f, df)
print(x_star_newton)


def secant_method(x0, x1, f, tol=4, max_iter=100):
    for i in range(max_iter):
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print("x_%d = %f, x_%d = %f x_%d = %f" % (i, x0, i + 1, x1, i+2, x_new))
        if calculate_n(x_new, 1.87938524) >= tol:
            print("Converge after %d iterations" % i)
            return x_new
        x0, x1 = x1, x_new
    return x1


x0, x1 = 2, 1.9
x_star_secant = secant_method(x0, x1, f)
print(x_star_secant)

# if __name__ == "__main__":
#     f = lambda x: 1 / ((x - 1)**0.5)
#     x0 = 1.5
#     x = stationary_point(x0, f)
#     print(x)
