import time
import sys

def fibonacci_bottom_up(n):
    if n <= 1:
        return n
    
    fib_table = [0] * (n + 1)
    fib_table[1] = 1
    
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    
    return fib_table[n]

# Lista de valores a probar
values_to_test = [5, 10, 15, 20, 100, 200, 500, 1000, 1500, 10000]

# Medición de tiempo y memoria
results = []
for n in values_to_test:
    start_time = time.time()
    start_mem = sys.getsizeof([0] * (n + 1))  # Tamaño de la tabla en memoria
    result = fibonacci_bottom_up(n)
    end_time = time.time()
    end_mem = sys.getsizeof([0] * (n + 1))
    
    execution_time = end_time - start_time
    memory_used = end_mem - start_mem
    
    results.append((n, result, execution_time, memory_used))

# Imprimir resultados
print("n | Fibonacci(n) | Tiempo (s) | Memoria (bytes)")
print("-" * 50)
for n, fib_n, time_taken, mem_used in results:
    print(f"{n} | {fib_n} | {time_taken:.6f} | {mem_used}")
