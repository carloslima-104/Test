def calcular():
    indc = 12
    soma = 0
    k = 1
    while k < indc:
        k = k + 1
        soma = soma + k
    return soma

# Exemplo de uso
resultado = calcular()
print("O valor da variável SOMA será {}.".format(resultado))
