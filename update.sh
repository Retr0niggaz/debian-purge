echo "time to update your debian and clean it :)"
apt update
apt upgrade -y
apt dist-upgrade -y
apt autoremove -y
apt autoclean
echo "done"
