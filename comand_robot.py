print("Entre com os comandos")
comando_total = str(input())

pox_inicial = 20
orientacao = 'N'
saiu_quadrado = False

while (pox_inicial >= 0 and pox_inicial <= 24):
    if (comando_total == 'S'):
        print("Robo desligando...\nTenha um bom dia!")
        break
    for comando in comando_total:
        if (comando == 'M' or comando == 'L' or comando == 'R'):
            if (comando == 'L'):
                if (orientacao == 'N'):
                    orientacao = 'W'
                elif(orientacao == 'W'):
                    orientacao = 'S'
                elif(orientacao == 'S'):
                    orientacao = 'E'
                elif(orientacao == 'E'):
                    orientacao = 'N'
            elif (comando == 'R'):
                if (orientacao == 'N'):
                    orientacao = 'E'
                elif(orientacao == 'W'):
                    orientacao = 'N'
                elif(orientacao == 'S'):
                    orientacao = 'W'
                elif(orientacao == 'E'):
                    orientacao = 'S'
            elif(comando == 'M'):
                posicao_x = pox_inicial % 5
                if (orientacao == 'N'):
                    pox_inicial -= 5
                elif (orientacao == 'S'):
                    pox_inicial += 5
                elif (orientacao == 'W'):
                    if(posicao_x == 0):
                        saiu_quadrado = True
                    else:
                        pox_inicial -= 1
                elif (orientacao == 'E'):
                    if(posicao_x == 4):
                        saiu_quadrado = True
                    else:
                        pox_inicial += 1
        else:
            print("%c entrada invalida\nComando ignorado" %(comando))
    posicao_x = pox_inicial % 5
    posicao_y = pox_inicial // 5
    if(saiu_quadrado == True or posicao_y < 0 or posicao_y > 4 or posicao_x < 0 or posicao_x > 4):
        print("Comando impossivel de ser executado")
        pox_inicial = pox_inicial_backup
        orientacao = orientacao_inicial_backup
        print("Digite somente 'S' para sair")
        print("Entre com os comandos")
        comando_total = str(input())
    else:
        if (posicao_y == 4):
            posicao_y = 0
        elif (posicao_y == 3):
            posicao_y = 1
        elif (posicao_y == 1):
            posicao_y = 3
        elif (posicao_y == 0):
            posicao_y = 4
        pox_inicial_backup = pox_inicial
        orientacao_inicial_backup = orientacao
        print('(%d,%d,%c)' %(posicao_x, posicao_y, orientacao,))
        comando_total = str(input())
