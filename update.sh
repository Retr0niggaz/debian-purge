echo "time to update your debian and clean it :)"
apt update
apt install -fsy > /dev/null
apt upgrade -y > /dev/null
apt dist-upgrade -y
apt autoremove -y
apt autoclean
clamscan -q --recursive --remove --detect-pua=yes /
echo "done"
