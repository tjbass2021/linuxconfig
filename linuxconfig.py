import os
# Lista de comandos
cmd = {
    "update": "sudo apt update && sudo apt upgrade -y",
    "evince": "sudo apt install evince -y",
    "vlc": "sudo apt install vlc -y",
    "vim": "sudo apt install vim -y",
    "zsh": "sudo apt install zsh -y",
    "git": "sudo apt install git -y",
    "gimp": "sudo apt install gimp -y",
    "inkscape": "sudo apt install inkscape -y",
    "krita": "sudo apt install krita -y",
    "ghost": "sudo flatpak install ghostwriter -y",
    "planner": "sudo flatpak install planner -y",
    "obsidian": "sudo flatpak install obsidian -y",
    "telegram": "sudo flatpak install telegram -y",
    "zoom": "sudo flatpak install zoom -y",
    "java": "sudo apt install default-jdk -y",
    "node": "sudo apt install nodejs -y",
    #------Essencial------------
    "dev": "sudo apt install default-jdk nodejs vim -y",


}


opcao = ''
while True:

    print('''
          Escolha uma opção abaixo
          ========================
          1 - Atualização
          2 - Instalar o Vim
          3 - Instalar o VLC
          4 - Instalar o ZSH
          5 - Instalar o GIT
          6 - Instalar o Gimp
          7 - Instalar o Inkscape
          8 - Instalar o Krita
          9 - Instalar o Ghoswriter
          10 - Instalar o Planner
          11 - Instalar o Obsidian
          12 - Instalar o Telegram
          13 - Instalar o Zoom
          14 - Instalar o Qbittorrent
          15 - Instalar o Kdeconnect
          16 - Instalar o Node
          17 - Instalar o Java
          ==========================
          INSTALAÇÃO ESSENCIAL
          ==========================
          18 - Apps de Desenho
          19 - Desenvolvimento
          ==========================
          0 - SAIR
          --------------------------
          ''')
    opcao = input("\n")

    if opcao == '1':
        os.system(cmd["update"])

    elif opcao == '2':
        os.system(cmd["vim"])
    elif opcao == '0':
        print('Programa finalizado.\n')
        break
    else:
        print('Digite uma opção válida!\n============================================')

'''
    Ideia de imprelementação: adicionar à ferramenta a opção de selecionar mais de um
    comando para instalação de programas, para isso usarei o método split para
    desmembrar a string em uma lista de strings com os comandos, onde será iterada
    através de um laço for e executará cada comando correspondente.

'''
