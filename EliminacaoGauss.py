def decomposicao_LU(A):
    """
    Decomposição LU de uma matriz A (n x n) usando o método de Doolittle (sem pivotamento).

    Entrada:
        A -- matriz quadrada (lista de listas)
    Saída:
        L, U -- matrizes triangulares, tal que A = LU
    """
    n = len(A)

    # Inicializa L como matriz identidade
    L = [[0.0 for _ in range(n)] for _ in range(n)]
    #gera uma matriz nxn cheia de zeros
    for i in range(n):
        L[i][i] = 1.0

    # Inicializa U como matriz nula
    U = [[0.0 for _ in range(n)] for _ in range(n)]

    # Loop principal
    for k in range(n):
        # Calcula a linha k de U
        for j in range(k, n):
            soma = 0.0
            for s in range(k):
                soma += L[k][s] * U[s][j]
            U[k][j] = A[k][j] - soma

        # Calcula a coluna k de L
        for i in range(k + 1, n):
            soma = 0.0
            for s in range(k):
                soma += L[i][s] * U[s][k]
            if U[k][k] == 0:
                raise ZeroDivisionError("Pivô zero encontrado — use pivotamento.")
            L[i][k] = (A[i][k] - soma) / U[k][k]

    return L, U
