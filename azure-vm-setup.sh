# Update before starting
sudo apt-get update

# Clone and build ray
git clone https://github.com/smkuls/ray
cd ~/ray/python
sudo -H pip install -e . --verbose

# Clone roboschool and install dependencies
cd ~
git clone https://github.com/openai/roboschool
ROBOSCHOOL_PATH=~/roboschool
sudo apt-get install -y cmake ffmpeg pkg-config qtbase5-dev libqt5opengl5-dev libassimp-dev libpython3.5-dev libboost-python-dev libtinyxml-dev libsnappy-dev
sudo -H pip install python-snappy tensorflow gym opencv-python scipy    
git clone https://github.com/olegklimov/bullet3 -b roboschool_self_collision
mkdir bullet3/build
cd    bullet3/build
cmake -DBUILD_SHARED_LIBS=ON -DUSE_DOUBLE_PRECISION=1 -DCMAKE_INSTALL_PREFIX:PATH=$ROBOSCHOOL_PATH/roboschool/cpp-household/bullet_local_install -DBUILD_CPU_DEMOS=OFF -DBUILD_BULLET2_DEMOS=OFF -DBUILD_EXTRAS=OFF  -DBUILD_UNIT_TESTS=OFF -DBUILD_CLSOCKET=OFF -DBUILD_ENET=OFF -DBUILD_OPENGL3_DEMOS=OFF ..
sudo make -j4
sudo make install
cd ../..
sudo -H pip install -e $ROBOSCHOOL_PATH --verbose

#==================
#sudo apt-get install -y cmake pkg-config build-essential autoconf curl libtool unzip flex bison python python-dev python-pip
#sudo -H pip install --upgrade pip
#sudo -H pip install cython

# Edit ray/python/ray/rllib/agent.py to add import statement [this can be checked in to git]
# python ray/python/ray/rllib/train.py --run A3C --env RoboschoolHumanoid-v1