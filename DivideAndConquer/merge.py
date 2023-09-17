def mergesort(lista, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2 
        mergesort(lista, inicio, meio)
        mergesort(lista, meio + 1, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    tamanhoEsquerdo = meio - inicio + 1
    tamanhoDireito = fim - meio
    vetoresquerdo = [0] * tamanhoEsquerdo
    vetordireito = [0] * tamanhoDireito

    for i in range(tamanhoEsquerdo):
        vetoresquerdo[i] = lista[inicio + i]

    for j in range(tamanhoDireito):
        vetordireito[j] = lista[meio + 1 + j]

    idxEsq = 0
    idxDir = 0
    k = inicio

    while idxEsq < tamanhoEsquerdo and idxDir < tamanhoDireito:
        if vetoresquerdo[idxEsq] <= vetordireito[idxDir]:
            lista[k] = vetoresquerdo[idxEsq]
            idxEsq += 1
        else:
            lista[k] = vetordireito[idxDir]
            idxDir += 1
        k += 1

    while idxEsq < tamanhoEsquerdo:
        lista[k] = vetoresquerdo[idxEsq]
        idxEsq += 1
        k += 1

    while idxDir < tamanhoDireito:
        lista[k] = vetordireito[idxDir]
        idxDir += 1
        k += 1

vetor = [14,2,8,6,10,1,5,12]
mergesort(vetor, 0, len(vetor) - 1)
print(vetor)