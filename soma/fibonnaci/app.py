def is_fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    if a == num:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."

# Exemplo de uso:
numero = int(input("Informe um número: "))
print(is_fibonacci(numero))
