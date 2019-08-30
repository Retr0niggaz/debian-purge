echo "time to purge your beautiful, lightweight system" #it's as well incredible, clean, easy to use and lovely system

sudo dpkg --add-architecture i386 # adding 32 bit support 
sudo apt update > /dev/null
sudo apt install clamav -fy #fixing depends errors

#vvvvvvvvvvvvvvvvvvvvvvvv purging
sudo apt upgrade -y
sudo apt full-upgrade -y
sudo apt dist-upgrade -y
sudo apt autoremove
sudo apt autoclean
sudo apt clean
clear
#^^^^^^^^^^^^^^^^^^^^^^^ purging

sudo freshclam > /dev/null #updates malware db
sudo clamscan --quiet --recursive --remove --detect-pua=yes / & > /dev/null #scans system in background

clear
echo "done" #really enjoy it 
echo "enjoy"
