#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Plínio Pereira
# Email : pliniojr@gmail.com
# Created Date: Mon May 30 2021
# =============================================================================
"""Desafio técnico para vaga de estágio"""
"""Desafio Python - Lógica de Programação"""
# =============================================================================

pox_inicial = 20
orientacao = 'N'
saiu_quadrado = False

def desenhar(eixo_x, eixo_y, direcao):
    if (direcao == 'N'):
        direcao = "\u2B06\uFE0F"
    elif (direcao == 'S'):
        direcao = "\u2B07\uFE0F"
    elif (direcao == 'W'):
        direcao = "\u2B05\uFE0F"
    elif (direcao == 'E'):
        direcao = "\u27A1\uFE0F"
    for i in range(0, 5):
        for j in range(0, 5):
            if(i == eixo_y and j == eixo_x):
                print(direcao + " ", end = " ")
            else:
                print('\U0001f7e5', end = " ")
        print()

desenhar(0, 4, 'N')
print('(%d,%d,%c)' %(0, 0, 'N'))

pox_inicial_backup = 20
orientacao_inicial_backup = 'N'

print("Entre com os comandos")
print("Digite \"EXIT\" para sair")
comando_total = str(input())

while (comando_total != "EXIT"):
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
                posicao_y = pox_inicial // 5
                posicao_x = pox_inicial % 5
                if (orientacao == 'N'):
                    if (posicao_y > 0):
                        pox_inicial -= 5
                    else:
                        saiu_quadrado = True
                elif (orientacao == 'S'):
                    if (pox_inicial <= 19):
                        pox_inicial += 5
                    else:
                        saiu_quadrado = True
                elif (orientacao == 'W'):
                    if (posicao_x > 0):
                        pox_inicial -= 1
                    else:
                        saiu_quadrado = True
                elif (orientacao == 'E'):
                    if (posicao_x < 4):
                        pox_inicial += 1
                    else:
                        saiu_quadrado = True
        else:
            print("%c entrada invalida\nComando ignorado" %(comando))

    if(saiu_quadrado == True):
        pox_inicial = pox_inicial_backup
        orientacao = orientacao_inicial_backup
        saiu_quadrado = False
        posicao_x = pox_inicial % 5
        posicao_y = pox_inicial // 5
        print("Comando impossivel de ser executado")
        desenhar(posicao_x, posicao_y, orientacao)
        print("Digite \"EXIT\" para sair")
        print("Entre com novos comandos")
        comando_total = str(input())
    else:
        pox_inicial_backup = pox_inicial
        orientacao_inicial_backup = orientacao
        posicao_x = pox_inicial % 5
        posicao_y = pox_inicial // 5
        desenhar(posicao_x, posicao_y, orientacao)
        if (posicao_y == 4):
            posicao_y_eixo = 0
        elif (posicao_y == 3):
            posicao_y_eixo = 1
        elif (posicao_y == 2):
            posicao_y_eixo = 2
        elif (posicao_y == 1):
            posicao_y_eixo = 3
        elif (posicao_y == 0):
            posicao_y_eixo = 4
        print('(%d,%d,%c)' %(posicao_x, posicao_y_eixo, orientacao))
        comando_total = str(input())

print("Robo desligando...\n""\U0001F4A4\U0001F916\U0001F4A4""\nTenha um bom dia!")
