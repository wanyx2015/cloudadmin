#!/bin/sh

yum install zip unzip -y
yum -y install wget
yum install dstat
yum install mtr


yum install epel-release
yum install nginx
/etc/init.d/nginx start
service nginx restart

# enable 80 port
iptables -I INPUT 5 -i eth0 -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
service iptables save
service iptables restart


wget -N --no-check-certificate https://softs.fun/Bash/ssr.sh && chmod +x ssr.sh && bash ssr.sh



stty erase ^?
echo "stty erase ^?" >> ~/.bashrc
source ~/.bashrc

mtr -rw 117.60.176.31

# make swap on linux

dd if=/dev/zero of=/swapfile bs=1024 count=4000k
mkswap /swapfile
swapon /swapfile
swapon -s
vi /etc/fstab
# add following line

/swapfile          swap            swap    defaults        0 0

chown root:root /swapfile



# for GitHub on linux


git remote add origin git@github.com:username/repo.git

git remote show

git push -u origin master


