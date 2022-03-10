def calculate_py(n_terms:int) -> float:
    numerador = 4.0
    denominador = 1.0
    operacao = 1.0
    pi = 0.0
    
    
    for _ in range(n_terms):
        pi += operacao * (numerador/denominador)
        denominador += 2.0
        operacao *= -1.0
        
    return pi


print(calculate_py(100000))
    
    