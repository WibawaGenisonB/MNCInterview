#!/bin/bash

#####################################################################
#
#  From my understanding of the question, I wrote this script to:
#    1. automatically handle all required hardening processes
#    2. everything is encapsulated in this script, no other dependancies needed. script could be ran by
#         simply executing this bash script with sudo permissions
#    3. this hardening is meant for freshly deployed servers, so minimal conflicts are anticipated
#
####################################################################

#Update Dependecy
apt-get install wget sed git -y
apt-get install -f

#Update system
#this chained command should check and say yes to update all system
apt-get update -y && apt-get full-upgrade -y

#Setup Network (IP: 172.31.137.90, IP Gateway: 172.31.137.1, Nameserver: 103.84.10.201 )
#this can be achieved by configuring netplan
#we cat and overwrite the current (empty) netplan with the ipv4, gateway, nameserver settings provided
#assumed the IPv4 provided is /24
cat <<EOF >/etc/netplan/01-network-manager-all.yaml
network:
  version: 2
  renderer: NetworkManager
  ethernets: 
    emp0s3:
      dhcp4: no
      addresses: [172.31.137.90/24]
      gateway4: 172.31.137.11
      nameservers:
          addresses: [103.84.10.201]
EOF

netplan apply

#Secure Network (IP Spoofing protection, Block SYN attacks, Disable IPv6, Hide kernel pointers,
#Enable panic on OOM)
#to achieve this, we could edit the sysctl.conf file located in /etc/sysctl.conf
#we use the search and replace function on sed to change sysctl.conf
#Explored the manual on what settings to change to achieve the desired results.

file='/etc/sysctl.conf'

cat <<EOF >> $file
#IP spoofing protection
net.ipv4.conf.default.rp_filter=1
net.ipv4.conf.all.rp_filter=1

#Block SYN Attacks
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 2048
net.ipv4.tcp_synack_retries = 2
net.ipv4.tcp_syn_retries = 5

#Disable IPv6
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1

#Hide Kernel Pointers
kernel.kptr_restrict = 2


#Enable Panic on OOM
vm.panic_on_oom = 1
EOF

#Secure SSHD (disable tunneled clear text passwords, Do not allow empty passwords, log all
#activity, change SSH default port)
#to achieve this, we could edit the ssh_config file located in /etc/ssh/ssh_config

file='/etc/ssh/ssh_config'

cat <<EOF >>$file
#disable tunneled clear text passwords
PasswordAuthentication no

#Do not allow empty passwords
PermitEmptyPasswords no

#log all activity
LogLevel INFO
SyslogFacility AUTHPRIV
EOF

#configure firewall (allow only http, https, ssh)
#we could achieve this by utilising the ufw command
#read the manual of the ufw command, and figured out what to do step by step

ufw disable
echo "y" | sudo ufw reset
ufw logging off
ufw default deny incoming
ufw default allow outgoing
#allow http
ufw allow 80/tcp
#allow https
ufw allow 443/tcp

#allow ssh
#change SSH default port
    ufw allow ${prompt}/tcp
    sed -i "/Port /Id" /etc/ssh/sshd_config
    echo "Port ${prompt}" | sudo tee -a /etc/ssh/sshd_config
    ufw allow 2222/tcp
#changed ssh default port to 2222

#free disk space
find /var/log -type f -delete
rm -rf /usr/share/man/*
#autoremove cleans unneeded dependancies 
apt-get autoremove -y
#autoclean cleans current directory
apt-get autoclean -y



