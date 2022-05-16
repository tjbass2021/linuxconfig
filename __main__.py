# imports
import os
import brave
import cmd
import unic
import msg
import mult
#---------------
opt = True

while opt:
    msg.msg()
    opt = input()
    if len(opt) == 1:
        opt =  unic.cunic(opt)


    elif len(opt) >= 2:
        cmds = opt.split(' ')
        print(cmds)
        opt = mult.mult(cmds)

