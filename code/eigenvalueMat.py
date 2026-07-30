import numpy as np


def powerMethod(A, u, rep, inv = False, output=False):
    if inv:
        A = np.linalg.inv(A)
    for i in range(rep):
        v = A @ u
        mu = np.linalg.norm(v, ord=np.inf)
        u = np.divide(v, mu)
        if inv:
            eig = 1.0/mu
        else:
            eig = mu
        if output:
            print("Iteration: ", i+1)
            print("Eigenvalue: ", eig)
            print("Eigenvector: ", u)
            print()
    return eig, u


A = np.array([[0, 2, 1], [2, -3, 1], [1, 1, -5]])
u = np.array([1, 1, 1])
rep = 5
mu, u = powerMethod(A, u, rep, inv=True, output=True)
print(mu, u)

