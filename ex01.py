def fibonacci(n):
    antecess, sucess = 0, 1
    while sucess < n:
        antecess, sucess = sucess, antecess + sucess
    return sucess == n or n == 0

numero = int(input("Digite um número: "))
if fibonacci(numero):
    print("O número {} pertence à sequência de Fibonacci.".format(numero))
else:
    print("O número {} não pertence à sequência de Fibonacci.".format(numero))
