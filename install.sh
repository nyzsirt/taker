#!/usr/bin/env bash
yum update -y
yum -y groupinstall development
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install python36u python36u-pip python36u-devel mlocate net-tools redis supervisor vim
systemctl start redis
systemctl enable redis
hostnamectl set-hostname taker

# https://www.tecmint.com/install-google-chrome-on-redhat-centos-fedora-linux/
echo "[mongodb-org-3.4]">>/etc/yum.repos.d/mongodb.repo
echo "name=MongoDB Repository">>/etc/yum.repos.d/mongodb.repo
echo "baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.4/x86_64/">>/etc/yum.repos.d/mongodb.repo
echo "gpgcheck=1">>/etc/yum.repos.d/mongodb.repo
echo "enabled=1">>/etc/yum.repos.d/mongodb.repo
echo "gpgkey=https://www.mongodb.org/static/pgp/server-3.4.asc">>/etc/yum.repos.d/mongodb.repo
echo "">>/etc/yum.repos.d/mongodb.repo
yum -y install mongodb-org
systemctl stop mongod
systemctl enable mongod

# https://www.tecmint.com/install-google-chrome-on-redhat-centos-fedora-linux/
echo "[google-chrome]">>/etc/yum.repos.d/google-chrome.repo
echo "name=google-chrome">>/etc/yum.repos.d/google-chrome.repo
echo "baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch">>/etc/yum.repos.d/google-chrome.repo
echo "enabled=1">>/etc/yum.repos.d/google-chrome.repo
echo "gpgcheck=1">>/etc/yum.repos.d/google-chrome.repo
echo "gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub">>/etc/yum.repos.d/google-chrome.repo
echo "">>/etc/yum.repos.d/google-chrome.repo
yum install -y google-chrome-stable