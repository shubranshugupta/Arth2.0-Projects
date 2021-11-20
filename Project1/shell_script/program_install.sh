#! /usr/bin/bash

echo $1

if [[ $1 == "sl" ]]
then
    sudo yum install sl -y

elif [[ $1 == "fortune" ]]
then
    sudo yum install fortune-mod -y

elif [[ $1 == "cmatrix" ]]
then
    sudo yum install perl cmake ncurses ncurses-devel git -y
    cd /tmp
    wget https://www.cpan.org/modules/by-module/Curses/Curses-1.38.tar.gz
    tar -zxvf Curses-1.38.tar.gz
    cd Curses-1.38
    sudo perl Makefile.PL && sudo make && sudo make test && sudo make install
    cd ..
    git clone https://github.com/abishekvashok/cmatrix.git
    cd cmatrix
    mkdir -p build
    cd build
    cmake ..
    sudo make && make install
    cd /tmp
    rm -f Curses-1.38.tar.gz 
    rm -f -r Curses-1.38 cmatrix

elif [[ $1 == "cowsay" ]]
then
    sudo yum install cowsay -y

elif [[ $1 == "asciiquarium" ]]
then
    sudo yum install perl
    cd /tmp
    wget https://www.cpan.org/modules/by-module/Curses/Curses-1.38.tar.gz
    tar -zxvf Curses-1.38.tar.gz
    cd Curses-1.38
    sudo perl Makefile.PL && sudo make && sudo make test && sudo make install
    cd ..
    wget https://cpan.metacpan.org/authors/id/K/KB/KBAUCOM/Term-Animation-2.6.tar.gz
    tar -zxvf Term-Animation-2.6.tar.gz
    cd Term-Animation-2.6
    sudo perl Makefile.PL && sudo make && sudo make test && sudo make install
    cd ..
    wget http://www.robobunny.com/projects/asciiquarium/asciiquarium.tar.gz
    tar -zxvf asciiquarium.tar.gz
    cd asciiquarium_1.1
    sudo cp asciiquarium /usr/local/bin/
    sudo chmod 0755 /usr/local/bin/asciiquarium
    cd /tmp
    rm -f Curses-1.38.tar.gz Term-Animation-2.6.tar.gz asciiquarium.tar.gz
    rm -f -r Curses-1.38 Term-Animation-2.6 asciiquarium_1.1

else
    echo none

fi