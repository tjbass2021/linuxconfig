# imports
import os
import brave
import cmd
import unic
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
       unic.cunic(opt)


    elif len(opt) >= 2:
        cmds = opt.split(' ')
        print(cmds)
        cmd(cmds)
