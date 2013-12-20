# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box     = "mesos-docker-fluentd"
  config.vm.box_url = "https://dl.dropboxusercontent.com/s/hh5c8vxgnyb8iqj/package.box?token_hash=AAFS4lJ7talouKF1kpq64MEsrQ_5EWCN5gg9rRq-Wk8Vhg"

  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--memory", 512]
    v.customize ["modifyvm", :id, "--cpus", 4]
  end

  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true

  config.vm.define "mesos-master" do |master|
    master.vm.hostname = "mesos-master"
    master.vm.network "private_network", ip: '192.168.50.4'
    master.vm.provision "hostmanager"
    master.vm.provision "shell", inline: "sed -ri 's/^127\..\+mesos-master//g' /etc/hosts"
    master.vm.provision "shell", inline: 'service lxc-net restart'
    master.vm.provision "shell", inline: "echo manual >> /etc/init/mesos-slave.conf && service mesos-slave stop; true"
    master.vm.provision "shell", inline: "echo 'zk://mesos-master:2181/mesos' > /etc/mesos/zk"
    master.vm.provision "shell", inline: "service mesos-master restart"
    master.vm.provision "shell", inline: "service marathon restart"
  end

  config.vm.define "mesos-slave1" do |slave|
    slave.vm.hostname = "mesos-slave1"
    slave.vm.network "private_network", ip: '192.168.50.5'
    slave.vm.provision "hostmanager"
    slave.vm.provision "shell", inline: "sed -ri 's/^127\..\+mesos-slave1//g' /etc/hosts"
    slave.vm.provision "shell", inline: 'service lxc-net restart'
    slave.vm.provision "shell", inline: "echo manual >> /etc/init/mesos-master.conf && service mesos-master stop; true"
    slave.vm.provision "shell", inline: "echo manual >> /etc/init/marathon.conf && service marathon stop; true"
    slave.vm.provision "shell", inline: "echo manual >> /etc/init/zookeeper.conf && service zookeeper stop; true"
    slave.vm.provision "shell", inline: "echo 'zk://mesos-master:2181/mesos' > /etc/mesos/zk"
    slave.vm.provision "shell", inline: "service mesos-slave restart"
  end

  config.vm.define "mesos-slave2" do |slave|
    slave.vm.hostname = "mesos-slave1"
    slave.vm.network "private_network", ip: '192.168.50.6'
    slave.vm.provision "hostmanager"
    slave.vm.provision "shell", inline: "sed -ri 's/^127\..\+mesos-slave2//g' /etc/hosts"
    slave.vm.provision "shell", inline: 'service lxc-net restart'
    slave.vm.provision "shell", inline: "echo manual >> /etc/init/mesos-master.conf && service mesos-master stop; true"
    slave.vm.provision "shell", inline: "echo manual >> /etc/init/marathon.conf && service marathon stop; true"
    slave.vm.provision "shell", inline: "echo manual >> /etc/init/zookeeper.conf && service zookeeper stop; true"
    slave.vm.provision "shell", inline: "echo 'zk://mesos-master:2181/mesos' > /etc/mesos/zk"
    slave.vm.provision "shell", inline: "service mesos-slave restart"
  end
end
