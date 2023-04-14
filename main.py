numTest = int(input("Digite um número: ")) 
  
 # imprimir os n primeiros números primos, um por linha. 
def primoTeste(numero): 
  e_primo = True 
  
  if numero == 1: 
    return False 
    
  for i in range(2, numero): 
    if numero % i == 0 or numero == 1: 
      return False
      break 
  return True 
  
n = numTest
x = 2
while n != 0: 
  if primoTeste(x) : 
    print(x)
    n -= 1
  x += 1