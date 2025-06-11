import time

def leMatriz(entrada):
    with open(entrada, 'r') as arquivo:
        linhas = arquivo.readlines()
    nLinhas, nColunas = map(int, linhas[0].strip().split())
    matriz = []
    for linha in linhas[1:nLinhas + 1]:
        elementos = linha.strip().split()
        matriz.append(elementos)
    return matriz


def extraiCoordenadas(matriz):
    coordenadas = {}
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            celula = matriz[i][j]
            if celula != '0':
                coordenadas[celula] = (i, j)
    return coordenadas


def distancia(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1 - x2) + abs(y1 - y2)


def permutas(lista):
    if len(lista) <= 1:
        return [lista]
    listaPermutas = []
    for i in range(len(lista)):
        primeiro = lista[i]
        resto = lista[:i] + lista[i + 1:]
        for p in permutas(resto):
            listaPermutas.append([primeiro] + p)
    return listaPermutas


def main(entrada):
    matriz = leMatriz(entrada)
    coords = extraiCoordenadas(matriz)

    pontosEntrega = [p for p in coords.keys() if p != 'R']

    if not pontosEntrega:
        return ""

    todasPermutas = permutas(pontosEntrega)
    validarRotas = [rota for rota in todasPermutas if len(rota) == 1 or rota[0] < rota[-1]]

    menorCusto = float('inf')
    melhorRota = None
    coordDoR = coords['R']

    for rota in validarRotas:
        custoRota = distancia(coordDoR, coords[rota[0]])
        for i in range(len(rota) - 1):
            custoRota += distancia(coords[rota[i]], coords[rota[i + 1]])
        custoRota += distancia(coords[rota[-1]], coordDoR)

        if custoRota < menorCusto:
            menorCusto = custoRota
            melhorRota = rota

    return " ".join(melhorRota)


if __name__ == "__main__":
    entrada = "entrada.txt"

    inicio = time.time()
    resultado = main(entrada)
    fim = time.time()

    print("Melhor rota:", resultado)
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")