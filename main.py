# O programa deve receber um número inteiro n digitado pelo usuário
numTest = int(input("Digite um número: ")) 
  
 # imprimir os n primeiros números primos, um por linha. 
 def primoTeste(numero): 
     if numero == 1: 
         return False 
      
     e_primo = True 
     for i in range(2, numero): 
         if numero % i == 0 or numero == 1: 
             e_primo = False 
             break 
     return e_primo 
  
 n = int(numTest)
 x = 1
 while n <= numTest: 
     if primoTeste(x) : 
         print(x) 
     n -= 1
     x += 1
 
