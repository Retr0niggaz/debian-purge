echo "time to update your debian and clean it :)"
sudo dpkg --add-architecture i386
sudo apt update > /dev/null
sudo apt install -fy
sudo apt upgrade -y
sudo apt full-upgrade -y
sudo apt dist-upgrade -y
sudo apt autoremove
sudo apt autoclean
sudo apt clean
sudo freshclam > /dev/null
sudo clamscan --quiet --recursive --remove --detect-pua=yes / &
echo "done"
echo "enjoy"
