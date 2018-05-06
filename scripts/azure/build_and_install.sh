sudo apt-get -y update
sudo apt-get -y upgrade
RAY=/home/azure-user/ray
git clone -b fulcrumv2 https://github.com/smkuls/ray $RAY
sudo -H pip install -e $RAY/python --verbose
