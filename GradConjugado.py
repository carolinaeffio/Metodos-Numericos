import numpy as np

def gradiente_conjugado(A, b, x0, tol=1e-10, max_iter=1000):
    x = x0
    r = b - np.dot(A, x)
    d = r.copy()

    iter = 0
    for k in range(max_iter):
        print("iteração: {}, valor de x: {}".format(iter, x))
        Ad = np.dot(A, d)
        r_dot = np.dot(r, r)
        alpha = r_dot / np.dot(d, Ad)

        x = x + alpha * d
        r_new = r - alpha * Ad

        if np.linalg.norm(r_new) < tol:
            return x

        beta = np.dot(r_new, r_new) / r_dot
        d = r_new + beta * d
        r = r_new
        iter += 1

    return x
