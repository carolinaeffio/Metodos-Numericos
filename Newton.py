def newton(f, df, x0, tol=1e-6, max_iter=100):
    """
    Método de Newton para encontrar raízes de funções reais.

    Parâmetros:
        f        -- função f(x)
        df       -- derivada f'(x)
        x0       -- chute inicial
        tol      -- tolerância para critério de parada
        max_iter -- número máximo de iterações

    Retorna:
        Uma aproximação da raiz de f(x)
    """
    x = x0
    fx = f(x)
    iter = 0
    
    while abs(fx) > tol and iter < max_iter:
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            print(f"Convergiu em {iter} iterações.")
            return x
        
        if dfx == 0:
            raise ValueError("Derivada nula. Método falhou.")
            
        print("iteracion: {}, valor de la raiz: {}".format(iter, x))
        x = x - fx / dfx
        iter += 1

    raise ValueError("Número máximo de iterações atingido.")