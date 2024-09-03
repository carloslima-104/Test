def contar_letras(text):
    cnt = text.lower().count('a')
    return cnt

stg = input("Digite uma string: ")

qtd = contar_letras(stg)
print("A letra 'a' aparece {} vez(es) na string.".format(qtd))
