def es_primo(numero):#this funtion check if the number that i send is or isn´t a primo
      if numero<2:
        return 0
      for i in range(2, numero):#With helps of the mod
         if  (numero % i)== 0:
            return 0
         else:
            continue
      return 1


def contar_primos(n):#This funcion helps by counting how many number primos the number have between 1 to de number(n)
    count = 0
    for i in range(1,n+1):
        if es_primo(i) == 1:
            count += 1
        else:
            continue
    return count

def final(n):#n is the number that we want for a primo and if it's not a primo, count how many there are from 0 to n
    m=contar_primos(n)
    if es_primo(n)==1: #If the n if primo only advise the client that the number is primo
        print(f"El numero {n} es primo")
    else:#In the other hand if there is not
        print(f"El numero {n} no es primo y tiene {m} primos")

final(194)