def fibonacci(n):
    """рекурсивная функция, возвращает число Фибоначчи"""
    cur = 1
    if n > 2:
        cur = fibonacci(n-1) + fibonacci(n-2)
        return cur
    if n<1:
       return "error" 
    
 
 