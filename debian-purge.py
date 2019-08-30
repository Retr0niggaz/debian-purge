#!/usr/bin/python3
import os, time

def c():
    os.system("clear")

def debian():
    if os.getuid() != 0:
        c()
        print('\033[91mRUN AS ROOT\033[0m')
        exit()
    print('first time to setup sudo')

    name = input('who u want to add to sudo group (press enter with nothing to continue): ')
    if name != "":
        os.system('adduser %s sudo' %name)#adding user to sudo

    os.system('dpkg --add-architecture i386')#enabling 32 bit support

    print('time to (probably) quick update')
    print('ignore apt warnings')
    time.sleep(3)

    os.system('sudo apt update && sudo apt upgrade -y')#updating
    print('\033[93mok updates done now time to install some important packages\033[0m')
    os.system('sudo apt install -y needrestart debsums gksu debsecan ufw clamav gnome-tweak-tool')
    c()
    print('done\nnow debian-purge will setup firewall')
    time.sleep(2)
    os.system('sudo ufw default deny incoming && sudo ufw default allow outgoing && ufw enable')
    c()
    issue = input("ok some info u want to say to users who will see on your computer (nothing to continue) : ")
    if issue != "":
        os.system('echo "%s" > /etc/issue' %issue)
        os.system('echo "%s" > /etc/issue.net' %issue)
    c()

    os.system('apt autoremove && apt autocean')
    c()

    print('ok so now time for virus scan (yep on linux it is good to do it)')#sometimes
    print('but before need to update virus definitions db')
    time.sleep(2)
    c()

    print("wait...")
    os.system('sudo freshclam > /dev/null')
    c()

    os.system('clamscan --bell --recursive -i --follow-dir-symlinks=2 --detect-pua=yes --algorithmic-detection=yes / & > /dev/null')

    print('now some better icons than default...')
    os.system('dpkg -i .assets/paper-icon.deb && sudo apt install -fy')#installing icons
    c()

    print("Done change icons in tweaks")
debian()
