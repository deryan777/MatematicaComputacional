def calcular_determinante_sarrus(matriz):

    if len(matriz) != 3 or any(len(linha) != 3 for linha in matriz):
        raise ValueError("A matriz deve ser 3x3")
    
    dp = matriz[0][0] * matriz[1][1] * matriz[2][2]
    dp1 = matriz[0][1] * matriz[1][2] * matriz[2][0]
    dp2 = matriz[0][2] * matriz[1][0] * matriz[2][1]

    ds = matriz[0][2] * matriz[1][1] * matriz[2][0]
    ds1 = matriz[0][0] * matriz[1][2] * matriz[2][1]
    ds2 = matriz[0][1] * matriz[1][0] * matriz[2][2]

    determinante = (dp + dp1 + dp2) - (ds + ds1 + ds2)
    return determinante

def substituir_coluna(matriz, coluna, vetor):
    """
    Substitui uma coluna da matriz pelo vetor fornecido.
    """
    nova_matriz = []
    for i in range(3):
        nova_linha = matriz[i][:]  # copia da linha
        nova_linha[coluna] = vetor[i]
        nova_matriz.append(nova_linha)
    return nova_matriz

def resolver_por_cramer(matriz, vetor):
    """
    Resolve um sistema 3x3 usando a Regra de Cramer.
    """
    det_principal = calcular_determinante_sarrus(matriz)
    if det_principal == 0:
        raise ValueError("O sistema não possui solução única (determinante zero).")

    # Calcula determinantes das matrizes com colunas substituídas
    det_x = calcular_determinante_sarrus(substituir_coluna(matriz, 0, vetor))
    det_y = calcular_determinante_sarrus(substituir_coluna(matriz, 1, vetor))
    det_z = calcular_determinante_sarrus(substituir_coluna(matriz, 2, vetor))

    # Cálculo das incógnitas
    x = det_x / det_principal
    y = det_y / det_principal
    z = det_z / det_principal

    return x, y, z

def main():
    print("Digite os elementos da matriz 3x3:")
    matriz = []
    for i in range(3):
        linha = list(map(float, input(f"Linha {i+1} (separado por espaços): ").split()))
        matriz.append(linha)
    
    print("\nDigite os termos independentes (vetor 3x1):")
    vetor = list(map(float, input("Separado por espaços: ").split()))
    
    try:
        det = calcular_determinante_sarrus(matriz)
        print(f"\nO determinante da matriz é: {det}")
        
        if det == 0:
            print("A matriz é singular (não invertível). O sistema pode não ter solução única.")
        else:
            print("A matriz é invertível, portanto o sistema possui solução única.")

            x, y, z = resolver_por_cramer(matriz, vetor)
            aredondar_x = round(x,2)
            aredondar_y = round(y,2)
            aredondar_z = round(z,2)
            print(f"\nSolução do sistema pelo método de Cramer:")
            print(f"x = {aredondar_x}")
            print(f"y = {aredondar_y}")
            print(f"z = {aredondar_z}")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
