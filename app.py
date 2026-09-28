#ENTRADA E PROCESSAMENTO:
TOTAL_ENTREVISTADOS = 50
excelente = 0
bom = 0
ruim = 0
for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print("Entrevistado", i, "de", TOTAL_ENTREVISTADOS)
    NOME_CLIENTE = input("Insira seu nome:")
    IDADE_CLIENTE = int(input("Agora insira sua idade:"))
    OPINIAO_CLIENTE = int(input("Digite sua opinião (1-Excelente / 2-Bom / 3-Ruim): "))
    if OPINIAO_CLIENTE == 1:
        excelente += 1
        print ("Resposta registrada: EXCELENTE")
    elif OPINIAO_CLIENTE == 2:
        bom += 1
        print ("Resposta registrada: BOM")
    elif OPINIAO_CLIENTE == 3:
        ruim += 1
        print ("Resposta registrada: RUIM")
    else:
        print ("Resposta inválida! resposta não contabilizada")
#SAIDA:
print("\n RESULTADO DA PESQUISA")
print("Quantidade de respostas EXCELENTE:" , excelente)
print("Quantidade de respostas RUIM:" , ruim)