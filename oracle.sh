 sudo yum clean metadata && sudo yum upgrade
sudo yum install binutils.x86_64 compat-libcap1.x86_64 compat-libstdc++-33.x86_64 compat-libstdc++-33.i686 \ 
vi /etc/sysctl.conf
sysctl -p
groupadd -g 54321 oracle
sudo groupadd -g 54322 dba
groupadd -g 54323 oper
useradd -u 54321 -g oracle -G dba,oper oracle
usermod -a -G wheel oracle


mkdir -p /u01/app/oracle/product/12.1.0/db_1
chown -R oracle:oracle /u01
chmod -R 775 /u01


 mkswap /swapfile
   58  swapon /swapfile
   59  swapon -s
   60  vi /etc/fstab
   61  chown root:root /swapfile 
   62  chmod 0600 /swapfile
   63  chmod 0644 /swapfile

yum groupinstall "Development tools"
yum install libaio libaio-devel ksh sysstat smartmontool unzips
