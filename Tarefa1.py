def estica(intList):
    tamanho = len(lista)
    for i in range (tamanho):
        valor = lista.pop(0)
        if (valor%2 == 0):
            metade = valor/2
            for j in range(2):
                lista.append(metade)
        else:
            lista.append(valor/2 + 1)
            lista.append(valor/2)
            
lista = [18, 7, 4, 24, 11]
estica(lista)
print lista
