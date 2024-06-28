# a = 1
# b = 0
#
# print(a/b)
try:

    with open('arquivo.txt', 'r') as file_object:
        texto = file_object.read()
        print(texto)

except:
    print('Deu ruim')
