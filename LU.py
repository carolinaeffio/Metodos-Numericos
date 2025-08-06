def decomposicao_LU(A):
    """
    Decomposição LU de Doolittle (sem pivotamento).
    A matriz A é de ordem n x n.
    
    Retorna:
    L: matriz triangular inferior com 1s na diagonal
    U: matriz triangular superior
    """
    n = len(A)
    
    # Inicializa L com 0s e 1s na diagonal
    L = [[0.0] * n for _ in range(n)]
    #cria uma matriz cheia de zeros nxn
    for i in range(n):
        L[i][i] = 1.0
    
    # Inicializa U com 0s
    U = [[0.0] * n for _ in range(n)]
    #cria uma matriz cheia de zeros nxn
    
    # Decomposição
    for k in range(n):
        # Calcula a linha k de U
        for j in range(k, n):
            soma = sum(L[k][s] * U[s][j] for s in range(k))
            U[k][j] = A[k][j] - soma
        
        # Calcula a coluna k de L
        for i in range(k + 1, n):
            if U[k][k] == 0:
                raise ZeroDivisionError("Divisão por zero: pivô nulo em U")
            soma = sum(L[i][s] * U[s][k] for s in range(k))
            L[i][k] = (A[i][k] - soma) / U[k][k]
    
    return L, U