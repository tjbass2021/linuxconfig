# mensagem de exibição

def msg():
    print('''

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

def help():
    print('''
    -----------AJUDA------------
      Digite 1 ou mais comandos
      separados por espaço pa-
      ra iniciar uma instalação
      ou atualização do sistema.
    -----------------------------
         s - sair da ajuda
    -----------------------------
    ''')
    op = True
    while op:
        op = input()
        if op == 's':
            op = False
            return False
        else:
            print('Digite "s" para sair!')
