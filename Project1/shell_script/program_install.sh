#! /usr/bin/bash

Install(){
    LOOP=1

    while (( $LOOP == 1 ))
    do
        USER=$(whoami)
        if [[ "$USER" != "root" && "$2" != "system" ]]
        then
            PASSWD="$(zenity --password --title=Authentication)\n"
        else
            PASSWD="none"
        fi

        if [[ $PASSWD == "none" ]]
        then 
            sudo yum install $1 -y
        else
            echo -e $PASSWD | sudo -S yum install $1 -y
        fi
        LOOP=$?
    done
}

CMD=$1

if [[ $CMD == "system" ]]
then
    if ! which zenity
    then
        Install zenity $CMD
    fi
    if ! which espeak-ng
    then
        Install espeak-ng $CMD
    fi

elif [[ $CMD == "sl" ]]
then
    Install $CMD

elif [[ $CMD == "fortune" ]]
then
    Install fortune-mod

elif [[ $CMD == "cowsay" ]]
then
    Install $CMD

elif [[ $CMD == "cmatrix" ]]
then
    Install perl
    sudo yum install cmake ncurses ncurses-devel git -y
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
    sudo rm -f Curses-1.38.tar.gz 
    sudo rm -f -r Curses-1.38 cmatrix

elif [[ $CMD == "asciiquarium" ]]
then
    Install perl
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
    sudo rm -f Curses-1.38.tar.gz Term-Animation-2.6.tar.gz asciiquarium.tar.gz
    sudo rm -f -r Curses-1.38 Term-Animation-2.6 asciiquarium_1.1

else
    echo "hi"
fi