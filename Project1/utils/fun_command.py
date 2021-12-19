import os
from utils.common import show_option, speak, run_cmd
from utils.common import check_prog, insatll_cmd, ask_install

SAVED_FILE_PATH = os.path.join(".", "saved_file", "funcmd.txt")
COWSAY_SHAPE = ["blowfish", "bud-frogs", "bunny", "cheese", "cower", "dragon",
                "dragon-and-cow", "elephant", "elephant-in-snake", "eyes", 
                "flaming-sheep", "fox", "ghostbusters", "head-in", "hellokitty", 
                "kiss", "kitty", "koala", "kosh", "luke-koala", "mech-and-cow", 
                "meow", "milk", "moofasa", "moose", "mutilated", "ren", "sheep",
                "skeleton", "small", "stegosaurus", "stimpy", "supermilker", 
                "surgery", "three-eyes", "turkey", "turtle", "tux", "udder", 
                "vader", "vader-koala"]

class Cowsay:
    def __init__(self):
        self.shape = "default"
        self.text = None
    
    def select_shape(self):
        speak("Set Shape.")

        shape_str = "|".join(COWSAY_SHAPE)
        cmd = ["zenity", "--forms", "--text=-", "--add-combo=Select Shape",
               f"--combo-values={shape_str}", "--title=Project 1"]
        returncode, stdout = run_cmd(cmd)
        if not returncode:
            self.shape = stdout.replace("\n", "")
            print(self.shape)
    
    def save_file(self):
        if self.text != None:
            cmd = f'cowsay -f{self.shape} {self.text} > {SAVED_FILE_PATH}'
            self.text = None
        else:
            cmd = f'fortune | cowsay -f{self.shape} > {SAVED_FILE_PATH}'
        run_cmd(cmd, shell=True)
        
    def show_output(self):
        self.save_file()
        cmd = f'gedit {SAVED_FILE_PATH}'
        run_cmd(cmd, shell=True)
        os.remove(SAVED_FILE_PATH)
    
    def ask_text(self):
        speak("Enter the Text to show.")

        cmd = ['zenity', '--entry', '--text=Enter the text: ']
        returncode, stdout = run_cmd(cmd)
        if not returncode:
            self.text = stdout.replace("\n", " ")


def cowsay_main():
    r"""
    Function is used to give option to user to set all sound setting.
    """

    LOOP = True
    obj = Cowsay()

    while LOOP:
        speak("Select Cowsay option.")

        rows = ["Set Shape", "Text + Cowsay", "Fortune + Cowsay", "Exit"]
        opt = show_option(rows=rows, for_what="Options")

        if opt is None:
            break

        if opt == 1:
            obj.select_shape()
        elif opt == 2:
            obj.ask_text()
            speak("Running cowsay command.")
            obj.show_output()
        elif opt == 3:
            speak("Running cowsay command.")
            obj.show_output()
        elif opt == 4:
            LOOP = False


class FunCommand:
    def sl(self):
        if not check_prog("sl"):
            if ask_install("sl"):
                insatll_cmd("sl")
            else:
                return False
        speak("Running sl command.")
        cmd = ["gnome-terminal", "-e",  "bash -c sl"]
        run_cmd(cmd)
    
    def fortune(self):
        if not check_prog("fortune"):
            if ask_install("fortune"):
                insatll_cmd("fortune")
            else:
                return False
        speak("Running fortune command.")
        cmd = 'zenity --info --text="$(fortune)" --height=300 --width=300'
        run_cmd(cmd, shell=True)
    
    def cmatrix(self):
        if not check_prog("cmatrix"):
            if ask_install("cmatrix"):
                insatll_cmd("cmatrix")
            else:
                return None
        speak("Running cmatrix command.")
        cmd = ["gnome-terminal", "-e",  "bash -c cmatrix"]
        run_cmd(cmd)
    
    def cowsay(self):
        if not check_prog("cowsay"):
            if ask_install("cowsay"):
                insatll_cmd("cowsay")
            else:
                return None
        cowsay_main()
    
    def asciiquarium(self):
        if not check_prog("asciiquarium"):
            if ask_install("asciiquarium"):
                insatll_cmd("asciiquarium")
            else:
                return None
        speak("Running asciiquarium command.")
        cmd = ["gnome-terminal", "-e", "bash -c asciiquarium"]
        run_cmd(cmd)


def main():
    LOOP = True
    obj = FunCommand()

    while LOOP:
        speak("Select the option of fun command tool.")

        rows = ["Sl", "Fortune", "Cmatrix", "Cowsay", "Asciiquarium", "Exit"]
        opt = show_option(rows=rows, for_what="Options")
        
        if opt is None:
            break

        if opt == 1:
            obj.sl()
        elif opt == 2:
            obj.fortune()
        elif opt == 3:
            obj.cmatrix()
        elif opt == 4:
            obj.cowsay()
        elif opt == 5:
            obj.asciiquarium()
        else:
            LOOP = False


if __name__ == "__main__":
    main()
    