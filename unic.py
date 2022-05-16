import os
import cmd
import msg
def cunic(c):
    if c == '1':
        os.system(cmd.vim)
        print('Vim instalado com sucesso')
    elif c == '2':
        os.system(java)
        print('Java instalado com sucesso')
    elif c == '3':
        os.system(git)
        print('Git instalado com sucesso')
    elif c == 'h':
        msg.help()
        return True
    elif c == 's':
        opt = False
        print('Fim do programa')
        return opt


