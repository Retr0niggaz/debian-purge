#!/usr/bin/python2
import os, time
def debian():
    print('\033[93mRUN AS ROOT\033[0m')
    print('first time to setup sudo (run as root)')
    name = raw_input('give the name of the user you want to add to the sudo group: ')
    os.system('adduser %s sudo' %name)
    reboot = raw_input('reboot or continue r/c: ')
    print('adding now repositories with more software')
    os.system('rm /etc/apt/sources.list && echo "deb http://deb.debian.org/debian stretch main contrib non-free\ndeb-src http://deb.debian.org/debian stretch main contrib non-free\n\ndeb http://deb.debian.org/debian-security/ stretch/updates main contrib non-free\ndeb-src http://deb.debian.org/debian-security/ stretch/updates main contrib non-free\n\ndeb http://deb.debian.org/debian stretch-updates main contrib non-free\ndeb-src http://deb.debian.org/debian stretch-updates main contrib non-free" > /etc/apt/sources.list && dpkg --add-architecture i386')
    print('time to (probably) quick update')
    print('ignore apt warnings')
    time.sleep(4)
    os.system('sudo apt update > /dev/null && sudo apt upgrade -y > /dev/null')
    print('\033[93mok updates done now time to install some important packages\033[0m')
    os.system('sudo apt install -y wget bleachbit preload firmware-iwlwifi libreoffice-writer libreoffice-calc build-essential libreoffice-math libreoffice-draw firmware-linux clamav gdebi needrestart debsums synaptic apt-listbugs gksu fail2ban debsecan ufw clamav brasero gimp auditd sysstat > /dev/null')
    print('done\nnow debian-purge will setup firewall')
    os.system('sudo ufw default deny incoming && sudo ufw default allow outgoing && ufw enable')
    nig = raw_input("ok some info u want to say to users who will see on your computer: ")
    os.system('echo "%s" > /etc/issue' %nig)
    os.system('echo "%s" > /etc/issue.net' %nig)
    os.system('apt autoremove && apt autocean')
    print('ok so now time for virus scan (yep on linux it is good to do it)')
    print('scanning...')
    os.system('clamav --bell --recursive -i --follow-dir-symlinks=2 --detect-pua=yes --algorithmic-detection=yes /')
    print('done')
    print('now some better icons than default')
    os.system('wget https://launchpadlibrarian.net/383884507/paper-icon-theme_1.5.721-201808151353~daily~ubuntu18.04.1_all.deb')
    os.system('dpkg -i paper* && sudo apt install -f && rm paper*')
    print('change icons in apperance menu or in tweaks')
    os.system('reset && history -c')
    print('done enjoy :)')
debian()
