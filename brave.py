import os

curl = 'sudo apt install apt-transport-https curl'
update = 'sudo apt update'
braveinst = 'sudo apt install brave-browser'
curlDown = 'sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg'
echo = 'echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list'

def braveInstall():
    os.system(curl)
    os.system(curlDown)
    os.system(echo)
    os.system(update)
    os.system(braveinst)
