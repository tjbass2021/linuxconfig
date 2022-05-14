# imports
import os
import brave

#---------------
opt = True

while opt:
    opt = input('''
    Escolha uma ou mais opções abaixo:
    ---------------------------------
        1 - vim
        2 - java
        3 - zsh
        4 - brave
    =================================
        h - ajuda s - sair
    ---------------------------------
''')
    if len(opt) == 1:

        if opt == '1':
            print('vim instalado')
        elif opt == '2':
            print('java instalado')
        elif opt == '3':
            print('zsh instalado')
        elif opt == 'h':
            print('menu de ajuda')
        elif opt == 's':
            print('programa finalizado')
            opt = False

    elif len(opt) >= 2:
        cmds = opt.split(' ')
        print(cmds)

        for i in range(len(cmds)):

            if cmds[i] == '1':
                print('vim instalado')

            elif cmds[i] == '2':
                print('java instalado')
            elif cmds[i] == '3':
                print('zsh instalado')
            elif cmds[i] == '4':
                brave.braveInstall()

            elif cmds[i] == 'h':
                print('menu de ajuda')

            elif cmds[i] == 's':
                print('programa finalizado')
                opt = False
            else:
                print('digite um comando válido')
