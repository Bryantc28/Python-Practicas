lista_str = input("Ingrese una lista de números separados por comas: ")

lista_str = lista_str.split(',')
# print(lista_str)

# Convierte cada string de la lista a un entero
lista = [int(n) for n in lista_str]

suma = sum(lista)

print(f"La suma de los números es: {suma}")
