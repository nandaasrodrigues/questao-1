def reverse(word):
    rev = ''
    tam = len(word)
    for i in range(tam):
        rev = rev + word[tam-1-i]
    return rev

def is_palindrome(word):
    #Retorna string 'Empty' se for uma palavra vazia
    if len(word) == 0:
        return 'Empty'
    return word == reverse(word)

print(is_palindrome(""))