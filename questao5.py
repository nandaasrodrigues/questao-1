def count_words_up_to_sam(lista):
    soma = 0
    for word in lista:
        soma = soma + 1
        if word == 'sam':
            return soma
    #Se não tem 'sam' na lista retorna -1
    return -1


print(count_words_up_to_sam(['eu', 'estou' , 'feliz', 'sam']))