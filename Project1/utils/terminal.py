import os
from utils.common import show_option, speak, run_cmd, insatll_cmd

SHELL_SCRIPT_PATH = os.path.join(".", "shell_script", "terminal.sh")

class Terminal():
    def __init__(self):
        self.path = os.getcwd()
    
    def change_path(self):
        speak("Select path to open terminal.")

        cmd = ["zenity", "--file-selection", "--directory"]
        returncode, stdout = run_cmd(cmd)

        if not returncode:
            self.path = stdout

    def open_terminal(self):
        speak("Opening terminal.")

        cmd = f"gnome-terminal --working-directory={self.path}"
        run_cmd(cmd, shell=True)


def main():
    LOOP = True
    obj = Terminal()

    while LOOP:
        speak("Select option fot Terminal Tool.")

        rows = ["Change Path & Open Terminal", "Open Terminal Here", "Exit"]
        opt = show_option(rows=rows, for_what="Options")
        
        if opt is None:
            break

        if opt == 1:
            obj.change_path()
        elif opt == 3:
            LOOP = False
            continue
        obj.open_terminal()

# if __name__ == "__main__":
#     main()