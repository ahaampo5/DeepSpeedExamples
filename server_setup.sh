chmod 1777 /tmp
apt update
apt install sudo -y
apt install curl -y
apt install wget -y
apt install git -y
apt install vim -y

sudo apt update
sudo apt install software-properties-common -y
VERSION=3.12
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
# set timezone to seoul
sudo timedatectl set-timezone Asia/Seoul
sudo apt install python$VERSION-dev python$VERSION-venv -y

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python$VERSION 2

sudo apt update
sudo apt install python3-distutils -y

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

pip install --upgrade pip setuptools wheel

sudo apt install pdsh -y
sudo apt install -y ninja-build

sudo apt install -y openssh-server

CONFIG="/etc/ssh/sshd_config"

sudo sed -i -E 's|^\s*#\s*Port\s+[0-9]+|Port 25020|' "$CONFIG"

if ! grep -Eq '^\s*Port\s+25020' "$CONFIG"; then
  echo "Port 25020" | sudo tee -a "$CONFIG" >/dev/null
fi

sudo sed -i -E 's|^\s*#\s*PermitRootLogin\s+.*|PermitRootLogin yes|' "$CONFIG"
if ! grep -Eq '^\s*PermitRootLogin\s+yes' "$CONFIG"; then
  echo "PermitRootLogin yes" | sudo tee -a "$CONFIG" >/dev/null
fi

sudo sed -i -E 's|^\s*#\s*PubkeyAuthentication\s+no|PubkeyAuthentication yes|' "$CONFIG"
sudo sed -i -E 's|^\s*#\s*PubkeyAuthentication\s+yes|PubkeyAuthentication yes|' "$CONFIG"
if ! grep -Eq '^\s*PubkeyAuthentication\s+yes' "$CONFIG"; then
  echo "PubkeyAuthentication yes" | sudo tee -a "$CONFIG" >/dev/null
fi

sudo sed -i -E 's|^\s*#\s*PasswordAuthentication\s+.*|PasswordAuthentication no|' "$CONFIG"
sudo sed -i -E 's|^\s*PasswordAuthentication\s+yes|PasswordAuthentication no|' "$CONFIG"
if ! grep -Eq '^\s*PasswordAuthentication\s+no' "$CONFIG"; then
  echo "PasswordAuthentication no" | sudo tee -a "$CONFIG" >/dev/null
fi

git config --global user.email "ahaampo5@gmail.com"
git config --global user.name "ahaampo5"
