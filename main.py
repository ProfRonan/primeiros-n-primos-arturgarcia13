# O programa deve receber um número inteiro n digitado pelo usuário
numTest = int(input("Digite um número: "))

# imprimir os n primeiros números primos, um por linha.
def primoTeste(numero):
    e_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            e_primo = False
            break
    return e_primo
    
n = 2
while n < numTest :
    if primoTeste(n) :
        print(n)
    n += 1
