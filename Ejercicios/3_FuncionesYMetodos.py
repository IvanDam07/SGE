def es_primo(numero):
  if numero<2:
    return False
  for i in range(2, numero):
     if  (numero % i)== 0:
        return False
  # Hemos agotado el bucle sin encontrar divisores
  return True

def suma_primos(numeroMax):

    suma = 0

    for numero in range(numeroMax+1):
        if es_primo(numero):
            suma = suma + numero

    print(f"La suma de los números primos hasta el número {numeroMax} es: {suma}.")

suma_primos(8)