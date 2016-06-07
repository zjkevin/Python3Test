yum -y install wget
yum -y install gcc
yum -y install make
wget http://www.python.org/ftp/python/3.4.4/Python-3.4.4.tgz
tar -xzvf Python-3.4.4.tgz 
cd Python-3.4.4
mkdir /usr/local/python3
./configure --prefix=/usr/local/python3 --enable-shared
make all
make install
rm -r Python-3.4.4 --force
rm Python-3.4.4.tgz --force

#make clean
#make distclean 
cd /usr/lib64 && ln -s /usr/local/python3/lib/libpython3.4m.so.1.0 libpython3.4m.so.1.0
cd /usr/bin/ && ln -s /usr/local/python3/bin/python3 python3