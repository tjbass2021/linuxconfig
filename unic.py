import os
import brave
import cmd
import msg
def cunic(c):
    if c == '1':
        os.system(cmd.vim)
        print('\nVim instalado com sucesso')
    elif c == '2':
        os.system(cmd.java)
        print('\nJava instalado com sucesso')
    elif c == '3':
        os.system(cmd.zsh)
        print('\nZsh instalado com sucesso')
    elif c == '4':
        os.system(brave.braveInstall())
        print('\nBrave instalado com sucesso')
    elif c == '5':
        os.system(cmd.git)
        print('\nGit instalado com sucesso')
    elif c == '6':
        os.system(cmd.qbit)
        print('\nQbittorrent instalado com sucesso')
    elif c == '7':
        os.system(cmd.krita)
        print('\nKrita instalado com sucesso')
    elif c == '8':
        os.system(cmd.gimp)
        print('\nGimp instlado com sucesso')
    elif c == '9':
        os.system(cmd.kde)
        print('\nKdeConnect instalado com sucesso')
    elif c == '10':
        os.system(cmd.vlc)
        print('\nVlc instalado com sucesso')
    elif c == 'h':
        msg.help()
        return True
    elif c == 's':
        opt = False
        print('Fim do programa')
        return opt


