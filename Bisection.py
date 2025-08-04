
def bisec(f, a, b, tol, max_iter): #f:funcion. [a,b]:intervalo
    if f(a) * f(b) >= 0:
        print("Não satisfaz a condição inicial: f(a) * f(b) < 0")
        return None
    
    iter = 0
    while (b - a) / 2 > tol and iter < max_iter: 
        
        c = (a + b) / 2 #punto medio del intervalo
        print("iteração: {}, valor da raiz: {}".format(iter, c))
        if f(c) == 0:
            return c  # La raíz exacta se encontró
        elif f(a) * f(c) < 0: #clasificacion del signo
            b = c  # La raíz está en [a, c]
        else:
            a = c  # La raíz está en [c, b]
        iter += 1
    return c  # Aproximación de la raíz
