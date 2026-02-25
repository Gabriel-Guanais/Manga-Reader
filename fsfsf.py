resposta = int(input("qual o numero"))
lista = []

while resposta > 0:
    resposta = resposta - 1
    lista.append(resposta)
    
if resposta % 3 ==0:
    print('Fizz')
elif resposta % 5 ==0:
    print('Buzz')
else:
    print('FizzBuzz')
    
lista.reverse()
print(lista)


class Genero:
    def __init__(self,nome):
        self.nome = nome
        pass