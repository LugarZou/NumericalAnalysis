import numpy as np

def spectral_radius(A, output=False):
    eigvals = np.linalg.eigvals(A)
    if output:
        print("Eigenvalues = ", eigvals)
    return np.max(np.abs(eigvals))

def Jacobi(A, b, x0, tol = 1e-4, max_iter=10, output=False):
    D = np.diag(np.diag(A))
    L = -np.tril(A, k=-1)
    U = -np.triu(A, k=1)
    B = np.linalg.inv(D)@(L+U)
    c = np.linalg.inv(D)@b
    if spectral_radius(B) >= 1:
        msg = "Spectral radius of B is {}, ".format(spectral_radius(B))
        msg += "Jacobi method may not converge"
        print(msg)
    if output:
        print("D = ", D)
        print("L = ", L)
        print("U = ", U)
        print("B = ", B)
        print("Spectral radius of B = ", spectral_radius(B, output=True))
        print("c = ", c)
    x = np.copy(x0)
    for k in range(max_iter):
        x_new = B@x + c
        if np.linalg.norm(x_new - x, np.inf) < tol:
            break
        x = np.copy(x_new)
    if output:
        print("Number of iterations = ", k)
    return x

def GaussSeidel(A, b, x0, tol=1e-4, max_iter=10, output=False):
    return SOR(A, b, x0, w=1, tol=tol, max_iter=max_iter, output=output)

def SOR(A, b, x0, w=1, tol=1e-4, max_iter=10, output=False):
    D = np.diag(np.diag(A))
    L = -np.tril(A, k=-1)
    U = -np.triu(A, k=1)
    B = np.linalg.inv(D-w*L)@((1-w)*D + w*U)
    c = w*np.linalg.inv(D-w*L)@b
    if spectral_radius(B) >= 1:
        msg = "Spectral radius of B is {}, ".format(spectral_radius(B))
        msg += "SOR method may not converge"
        print(msg)
    if output:
        print("D = ", D)
        print("L = ", L)
        print("U = ", U)
        print("B = ", B)
        print("Spectral radius of B = ", spectral_radius(B, output=True))
        print("c = ", c)
    x = np.copy(x0)
    for k in range(max_iter):
        x_new = B@x + c
        if np.linalg.norm(x_new - x, np.inf) < tol:
            break
        x = np.copy(x_new)
    if output:
        print("Number of iterations = ", k)
    return x

if __name__ == "__main__":
    A = np.array([[5, 2, 1],
                  [-1, 4, 2],
                  [2, -3, 10]])
    b = np.array([-12, 20, 3])
    x0 = np.array([0, 0, 0])
    x = SOR(A, b, x0, w=0.9, tol=1e-6, max_iter=2, output=True)
    print("x = ", x)