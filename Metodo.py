
def bisection(f, a, b, tol, max_iter): #f:funcion. [a,b]:intervalo
    if f(a) * f(b) >= 0:
        print("No se cumple la condición inicial: f(a) * f(b) < 0")
        return None
    
    iteraciones = 0
    while (b - a) / 2 > tol and iteraciones < max_iter: 
        iteraciones += 1
        c = (a + b) / 2 #punto medio del intervalo
        print("iteracion: {}, valor de la raiz: {}".format(iteraciones, c))
        if f(c) == 0:
            return c  # La raíz exacta se encontró
        elif f(a) * f(c) < 0: #clasificacion del signo
            b = c  # La raíz está en [a, c]
        else:
            a = c  # La raíz está en [c, b]
    
    return c  # Aproximación de la raíz
