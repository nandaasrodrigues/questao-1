def sum_up_to_even(lista):
    soma = 0
    for i in lista:
        soma = soma + i
        if i%2 == 0:
            return soma - i
#Se não existir número par retorna -1
    return -1

print(sum_up_to_even([1,3,8, 9, 10]))