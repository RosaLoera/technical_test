
def order_list(list_length = int(input("Introduce la cantidad de números que quieres agregar a la lista: "))):
    numbers = []

    for i in range(list_length):
        numbers.append(int(input("Introduce un número: ")))

    numbers.sort()
    print(f'Los números que ingresaste se han ordenado del menor al mayor: {numbers}')


order_list()

