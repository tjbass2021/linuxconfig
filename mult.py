import os
import cmd

# Função para multiplas opções de instalação
lista = ['1', '2']
def mult(lista):

    for i in range(len(lista)):

        if lista[i] == '1':
            os.system(cmd.vim)
            print('Vim instalado com sucesso!')
        elif lista[i] == '2':
            os.system(cmd.java)
            print('Java instalado com sucesso!')
        elif lista[i] == '3':
            os.system(cmd.git)
            print('Git instalado com sucesso!')


mult(lista)
