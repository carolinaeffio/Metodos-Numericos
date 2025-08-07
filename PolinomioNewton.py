def coeficientes_newton(x, y):
    """
    Calcula os coeficientes das diferenças divididas de Newton.
    Entrada: listas x e y com os dados.
    Saída: lista com os coeficientes a_0, a_1, ..., a_n
    """
    n = len(x)
    f = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        f[i][0] = y[i]
    
    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i+1][j-1] - f[i][j-1]) / (x[i+j] - x[i])
    
    return [f[0][j] for j in range(n)]

def avalia_newton(x, coef, x_val):
    """
    Avalia o polinômio interpolador de Newton no ponto x_val.
    Entrada: lista de x, coeficientes e o ponto x_val.
    Saída: valor p(x_val)
    """
    n = len(coef)
    p = coef[0]
    produto = 1.0
    
    for k in range(1, n):
        produto *= (x_val - x[k-1])
        p += coef[k] * produto
    
    return p
