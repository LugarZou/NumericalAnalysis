def f(x, y):
    return x**2 + x - y


def EulerMethod(f, y0, x0, h, n):
    ys = [y0]
    x = x0
    y = y0
    for i in range(n):
        print(ys)
        y = y + h * f(x, y)
        x = x + h
        ys.append(y)
    return ys


def optimizedEulerMethod(f, y0, x0, h, n):
    ys = [y0]
    ygs = [y0]
    x = x0
    y_correct = y0
    y_guess: float = 0
    for i in range(n):
        y_guess = y_correct + h * f(x, y_correct)
        y_correct = y_correct + h * (f(x, y_correct) + f(x + h, y_guess)) / 2
        x = x + h
        ygs.append(y_guess)
        ys.append(y_correct)
    return ygs, ys


x0 = 0.0
y0 = 0.0
ygs, ys = optimizedEulerMethod(f, y0, x0, 0.1, 5)
print(ygs)
print(ys)
