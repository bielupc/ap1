
def factorial(n:int) -> int:
    """Retorna el factorial de qualsevol nombre n tal que 0 ≤ n ≤ 1000"""
    factorial = 1 
    for i in range(1, n+1):
        factorial *= i
    return factorial


