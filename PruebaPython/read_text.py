
file = open('text_file.txt', 'r')
count = 0

for line in file:
    words = line.split(" ")
    count += len(words)

file.close()
print(f'La cantidad de palabras que contiene el archivo es: {count}')