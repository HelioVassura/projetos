# Inicialização dos contadores
qtd_excelente = 0
qtd_ruim = 0

# Definição do número de entrevistados para o teste (altere para 50 na versão final)
TOTAL_ENTREVISTADOS = 10 

print(f"--- INÍCIO DA PESQUISA DE SATISFAÇÃO ({TOTAL_ENTREVISTADOS} ENTREVISTADOS) ---\n")

# Estrutura de repetição para coletar as respostas
for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"--- Entrevistado {i} ---")
    nome = input("Digite o nome: ")
    
    # Validação do campo Idade (para não quebrar o programa se digitarem letras)
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade > 0:
                break
            else:
                print("Por favor, digite uma idade válida (maior que zero).\n")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros para a idade.\n")
    
    # Validação do menu de opinião
    while True:
        print("Opinião sobre o atendimento:")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")
        
        try:
            opiniao = int(input("Escolha uma opção (1, 2 ou 3): "))
            if opiniao in [1, 2, 3]:
                break
            else:
                print("Opção inválida! Por favor, escolha 1, 2 ou 3.\n")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros (1, 2 ou 3).\n")
    
    # Estrutura de decisão para contabilizar a opinião
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 3:
        qtd_ruim += 1
        
    print("Resposta registrada com sucesso!\n")

# Exibição dos resultados finais
print("=" * 40)
print("          RESULTADO DA PESQUISA         ")
print("=" * 40)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
print("=" * 40)