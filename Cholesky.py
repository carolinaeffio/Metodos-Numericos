import math

def chol(A):
    """
    Realiza a decomposição de Cholesky da matriz A.
    A deve ser simétrica definida positiva.
    
    Entrada:
        A -- matriz (n x n), lista de listas
    Saída:
        L -- matriz triangular inferior, tal que A = L * L^T
    """
    n = len(A)
    
    # Inicializa L com zeros
    L = [[0.0 for _ in range(n)] for _ in range(n)]

    # Loop principal
    for i in range(n):
        for j in range(i + 1):  # j de 0 até i
            s = 0.0  # soma

            for k in range(j):
                s += L[i][k] * L[j][k]

            if i == j:
                val = A[i][i] - s
                if val <= 0:
                    raise ValueError("A matriz não é definida positiva.")
                L[i][j] = math.sqrt(val)
            else:
                if L[j][j] == 0:
                    raise ZeroDivisionError("Divisão por zero detectada.")
                L[i][j] = (A[i][j] - s) / L[j][j]

    return L
