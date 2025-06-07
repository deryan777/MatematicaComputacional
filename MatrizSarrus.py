def calcular_determinante_sarrus(matriz):
    """
    Calcula o determinante de uma matriz 3x3 usando a Regra de Sarrus
    
    Args:
        matriz: lista de listas representando uma matriz 3x3
        
    Returns:
        O valor do determinante
    """
    if len(matriz) != 3 or any(len(linha) != 3 for linha in matriz):
        raise ValueError("A matriz deve ser 3x3")
    
    # Aplicando a Regra de Sarrus:
    # 1. Repetir as duas primeiras colunas ao lado da matriz
    # 2. Somar os produtos das diagonais principais
    # 3. Subtrair os produtos das diagonais secundárias
    
    # Diagonal principal e paralelas
    dp = matriz[0][0] * matriz[1][1] * matriz[2][2]
    dp1 = matriz[0][1] * matriz[1][2] * matriz[2][0]
    dp2 = matriz[0][2] * matriz[1][0] * matriz[2][1]
    
    # Diagonal secundária e paralelas
    ds = matriz[0][2] * matriz[1][1] * matriz[2][0]
    ds1 = matriz[0][0] * matriz[1][2] * matriz[2][1]
    ds2 = matriz[0][1] * matriz[1][0] * matriz[2][2]
    
    determinante = (dp + dp1 + dp2) - (ds + ds1 + ds2)
    
    return determinante

def main():
    # Entrada da matriz 3x3
    print("Digite os elementos da matriz 3x3:")
    matriz = []
    for i in range(3):
        linha = list(map(float, input(f"Linha {i+1} (separado por espaços): ").split()))
        matriz.append(linha)
    
    # Entrada do vetor de termos independentes (não usado no cálculo do determinante)
    print("\nDigite os termos independentes (vetor 3x1):")
    vetor = list(map(float, input("Separado por espaços: ").split()))
    
    # Calcular e mostrar o determinante
    try:
        det = calcular_determinante_sarrus(matriz)
        print(f"\nO determinante da matriz é: {det}")
        
        if det == 0:
            print("A matriz é singular (não invertível).")
        else:
            print("A matriz é invertível.")
            
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()