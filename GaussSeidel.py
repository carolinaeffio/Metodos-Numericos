def gauss_seidel(A, b, x0, tol=1e-10, max_iter=100):
    """
    Método de Gauss-Seidel para resolver Ax = b

    Parâmetros:
        A        -- matriz dos coeficientes (n x n)
        b        -- vetor do lado direito (n)
        x0       -- vetor inicial (n)
        tol      -- tolerância para critério de parada
        max_iter -- número máximo de iterações

    Retorna:
        x        -- vetor solução aproximada
    """
    n = len(A)
    x = x0[:]
    iter = 0
    for k in range(max_iter):
        print("iteração: {}, valor de x: {}".format(iter, x))
        x_new = x[:]
        for i in range(n):
            s1 = 0.0
            for j in range(i):
                s1 += A[i][j] * x_new[j]

            s2 = 0.0
            for j in range(i + 1, n):
                s2 += A[i][j] * x[j]

            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        # Critério de parada: norma do infinito
        diff = [abs(x_new[i] - x[i]) for i in range(n)]
        if max(diff) < tol:
            return x_new

        x = x_new[:]
        iter +=1

    return x