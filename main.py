n = input("Enter a number: ")
i = int(n)  # guarda quantos números primos serão impressos.

j = 2  # j guarda o valor do número atual a ser testado.
while i > 0:
    for k in range(2, j):
        if j % k == 0:
            # j não é primo.
            break
    else:  # aqui o else roda somente se o for não foi interrompido por um break.
        # j é primo.
        print(j)
        i -= 1
    j += 1
