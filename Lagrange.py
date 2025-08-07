# Lagrange.py

def lagrange_interpolacao(x, y, x_val):
    """
    Interpolação de Lagrange
    Entrada:
        x: lista de abscissas [x0, x1, ..., xn]
        y: lista de ordenadas [y0, y1, ..., yn]
        x_val: valor onde interpolar
    Saída:
        P(x_val): valor do polinômio interpolador em x_val
    """
    n = len(x)
    P = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if j != i:
                L *= (x_val - x[j]) / (x[i] - x[j])
        P += y[i] * L
    return P