import os
from utils.common import run_cmd, show_option
from utils import date_cal, terminal, fun_command
from utils import firefox, espeak


__author__ = "Shubhranshu Gupta"
__copyright__ = "Copyright 2021, The Cogent Project"
__credits__ = ["Shubhranshu Gupta"]
__license__ = "MIT"
__version__ = "2.0"
__maintainer__ = "Shubhranshu Gupta"
__status__ = "Learning"


ENTRY_TEXT = os.path.join(".", "saved_file", "main_menu.txt")

def main():

    cmd = ["espeak-ng", "-a200", "-s130", "Welcome to Menu Based Project."]
    run_cmd(cmd)

    cmd = ["zenity", "--text-info", f"--filename={ENTRY_TEXT}", "--width=600", "--height=600", "--title=Project 1"]
    returncode, _ = run_cmd(cmd)

    if returncode:
        cmd = ["espeak-ng", "-a200", "-s130", "Thank you."]
        run_cmd(cmd)
        exit()

    while True:
        cmd = ["espeak-ng", "-a200", "-s130", "Select the tools."]
        run_cmd(cmd)

        rows = ["Date & Calender", "Terminal", "Fun Command", "Firefox", "Espeak", "Exit"]
        opt = show_option(rows=rows)

        if opt == 1:
            date_cal.main()
        elif opt == 2:
            terminal.main()
        elif opt == 3:
            fun_command.main()
        elif opt == 4:
            firefox.main()
        elif opt == 5:
            espeak.main()
        else:
            cmd = ["espeak-ng", "-a200", "-s150", "Thank you."]
            run_cmd(cmd)
            exit()
        

if __name__ == "__main__":
    main()