# -*- mode: ruby -*-
# vi: set ft=ruby :

$tex = <<-TEX
curl -L -O https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz

tar -xvf install-tl-unx.tar.gz

# TODO: Find a cleaner way to do this.
find . -type f -name "install-tl" -exec perl {} -profile /vagrant/texlive.profile \';'

echo 'export PATH=$PATH:/usr/local/texlive/2023/bin/x86_64-linux' >> /home/vagrant/.bashrc

# Not necessary for root to have tlmgr in its path
# lwarp packages
/usr/local/texlive/2023/bin/x86_64-linux/tlmgr install lwarp \
luatex \
xindy \
pdfcrop \
ifptex \
etoolbox \
verifycommand \
xpatch \
catchfile \
newunicodechar \
upquote \
comment \
microtype \
xifthen \
newfloat \
xstring \
environ \
printlen \
cleveref \
ifmtarg \
capt-of \
filehook \
svn-prov

# other packages
/usr/local/texlive/2023/bin/x86_64-linux/tlmgr install pgf pgfplots amsmath standalone xcolor bibtex algorithmicx
TEX

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "fedora/39-cloud-base"
  config.vm.box_version = "39.20231031.1"

  config.vm.provision "update", type: "shell", privileged: true, inline: "dnf update -y"
  config.vm.provision "lwarp dependencies", type: "shell", privileged: true, inline: <<-DEPS
  dnf install -y perl-core poppler-utils ghostscript
  DEPS

  config.vm.provision "tex", type: "shell", privileged: true do |s|
    s.inline = $tex
  end

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", type: "dhcp"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Disable the default share of the current code directory. Doing this
  # provides improved isolation between the vagrant box and your host
  # by making sure your Vagrantfile isn't accessable to the vagrant box.
  # If you use this you may want to enable additional shared subfolders as
  # shown above.
  # config.vm.synced_folder ".", "/vagrant", disabled: true

  # Necessary due to lwarp workflow
  config.vm.synced_folder "src/", "/vagrant/src"
  config.vm.synced_folder "dist/", "/vagrant/dist"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    vb.gui = false

    # Customize the amount of memory on the VM:
    vb.cpus = 2
    vb.memory = "4096"
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
end
