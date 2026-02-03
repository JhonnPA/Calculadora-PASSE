def calc_nc(e1, e2, e3):
    return (0.2 * e1) + (0.3 * e2) + (0.5 * e3)

def pegar_num(texto):
    while True:
        try:
            return float(input(texto).replace(',', '.'))
        except ValueError:
            print("Valor inválido. Tente novamente.")

def main():
    print("--- Calculadora PASSE-UFMS ---\n")

    print("1. Defina os pesos do curso:")
    pesos = {
        'red': pegar_num("Peso Redação: "),
        'hum': pegar_num("Peso Humanas: "),
        'nat': pegar_num("Peso Natureza: "),
        'lin': pegar_num("Peso Linguagens: "),
        'mat': pegar_num("Peso Matemática: ")
    }

    materias = {
        'hum': "Ciências Humanas",
        'nat': "Ciências da Natureza",
        'lin': "Linguagens",
        'mat': "Matemática"
    }

    notas_nc = {}
    print("\n2. Notas de cada etapa (EP):")
    
    for id, nome in materias.items():
        print(f"\n> {nome}")
        n1 = pegar_num("  Etapa 1: ")
        n2 = pegar_num("  Etapa 2: ")
        n3 = pegar_num("  Etapa 3: ")
        
        nc = calc_nc(n1, n2, n3)
        notas_nc[id] = nc
        print(f"  NC calculada: {nc:.2f}")

    print("\n3. Redação")
    nota_red = pegar_num("Nota da Redação (Etapa 3): ")

    soma_notas = (pesos['red'] * nota_red) + sum(pesos[m] * notas_nc[m] for m in materias)
    total_pesos = sum(pesos.values())

    if total_pesos == 0:
        return print("Erro: A soma dos pesos é zero.")

    media_final = soma_notas / total_pesos

    print("\n" + "="*20)
    print(f"MÉDIA FINAL: {media_final:.3f}")
    print("="*20)

if __name__ == "__main__":
    main()