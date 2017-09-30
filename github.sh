#!/bin/sh

# for GitHub on linux


# Step1: Generate public/private ssh key

cd ~/.ssh
ssh-keygen
cat ~/.ssh/id_rsa.pub

# copy public key to github.com setting

# Step 2

git clone https://github.com/wanyx2015/cloudadmin.git
git remote rm origin
git remote add origin git@github.com:wanyx2015/cloudadmin.git
git remote show
git config --global user.name "Wan"
git config --global user.email "yuxi.wan@gmail.com"


# will output Hi wanyx2015! You've successfully authenticated, but GitHub does not provide shell access.
ssh -T git@github.com
git push -u origin master



