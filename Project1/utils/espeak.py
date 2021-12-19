import os
import subprocess
from subprocess import run
from utils.common import show_option, speak, run_cmd

"""

1. LANG variable contain all different language and its code.
2. VOICES variable contain all voices and its code.

"""


LANG = {"English-American":"en-us", "English-British":"en", "French-France":"fr", "French-Belgium":"fr-be",
        "French-Switzerland":"fr-ch", "Greek":"el", "Hindi":"hi", "Russian":"ru", "Portuguese":"pt",
        "Nepali":"ne", "Korean":"ko", "Japanese":"ja", "Italian":"it", "Indonesian":"id", "Persian":"fa",
        "Chinese":"cmn", "Dutch":"nl", "Latin":"la"}


VOICES = {"Female 1":"f1", "Female 2":"f2", "Female 3":"f3", "Female 4":"f4", "Female 5":"f5",
          "Male 1":"m1", "Male 2":"m2", "Male 3":"m3", "Male 4":"m4", "Male 5":"m5"}


class eSpeakClass():
    def __init__(self):
        r"""

        AUDIOPATH: Path to save Audio file.
        volume:    This variable store the volume of sound.
        pause:     This variable store the pause between two word, it is in milisec.
        pitch:     It is used to store pitch of sound.
        speed:     Its use for contolling speed (word/sec).
        lang:      Select the language.
        voice:     Select male of female voice.
        text:      Text to speak.
        file:      file to speak.

        """
        self.AUDIOPATH = None
        self.volume = 50
        self.pause = 10
        self.pitch = 50
        self.speed = 175
        self.lang = "en-us"
        self.voice = "m1"
        self.text = None
        self.file = None
    
    # ===========================  Sound Option  ================================ #
    def adjust_volume(self):
        r"""
        Function is used to set volume by asking from user using Zenity GUI.
        """

        speak("Set Volume")
        cmd = ["zenity", "--scale", "--text=Select volume: ", "--title=Project 1",
               "--min-value=0", "--max-value=200", "--step=1", "--value=50"]
        returncode, stdout = run_cmd(cmd)
        if not returncode:
            self.volume = int(stdout)
    
    def pause_btw_word(self):
        r"""
        Function is used to set pause between word by asking from user using Zenity GUI.
        """

        speak("Set Pause between words")
        cmd = ["zenity", "--scale", "--text=Select pause between word(ms): ", "--title=Project 1",
               "--min-value=0", "--max-value=100", "--step=1", "--value=10"]
        returncode, stdout = run_cmd(cmd)
        if not returncode:
            self.pause = int(stdout)
    
    def adjust_pitch(self):
        r"""
        Function is used to set pitch by asking from user using Zenity GUI.
        """

        speak("Set Pitch")
        cmd = ["zenity", "--scale", "--text=Select pitch: ", "--title=Project 1",
               "--min-value=0", "--max-value=100", "--step=1", "--value=50"]
        returncode, stdout = run_cmd(cmd)
        if not returncode:
            self.pitch = int(stdout)
    
    def adjust_speed(self):
        r"""
        Function is used to set speed by asking from user using Zenity GUI.
        """

        speak("Set Speed")
        cmd = ["zenity", "--scale", "--text=Set Speed(word/min): ", "--title=Project 1",
               "--min-value=1", "--max-value=250", "--step=2", "--value=175"]
        returncode, stdout = run_cmd(cmd)
        if not returncode:
            self.speed = int(stdout)
    
    def select_lang(self):
        r"""
        Function is used to set language by asking from user using Zenity GUI.
        """

        speak("Set Language")
        lang_lst = list(LANG.keys())
        lang_lst.sort()
        lang_str = "|".join(lang_lst)

        cmd = ["zenity", "--forms", "--text=-", "--add-combo=Select Language",
               f"--combo-values={lang_str}", "--title=Project 1"]
        
        returncode, stdout = run_cmd(cmd)
        if returncode == 0:
            self.lang = LANG[stdout.replace("\n", "")]
        elif returncode == -6:
            self.lang = LANG[stdout.replace("\n", "")]
    
    def select_voice(self):
        r"""
        Function is used to set voice by asking from user using Zenity GUI.
        """

        speak("Set Voice")
        voice_lst = list(VOICES.keys())
        voice_lst.sort()
        voice_str = "|".join(voice_lst)

        cmd = ["zenity", "--forms", "--text=-", "--add-combo=Select Voices",
               f"--combo-values={voice_str}", "--title='Project 1'", "--title=Project 1"]
        
        returncode, stdout = run_cmd(cmd)
        if not returncode:
            self.voice = VOICES[stdout.replace("\n", "")]
    
    # ===========================  Speak  ================================ #
    def speak(self):
        r"""
        Function is used to speak the text or particular file.
        """

        cmd = ["espeak-ng", f"-a{self.volume}", f"-g{self.pause}", f"-s{self.speed}",
               f"-p{self.pitch}", f"-v{self.lang}+{self.voice}"]
        
        if self.file is None:
            cmd.append(self.text)
        else:
            cmd.append(f"-f{self.file}")
        
        _, _ = run_cmd(cmd)
    
    # ===========================  Save as Audio  ================================ #
    def set_audio_path(self):
        usr = os.environ.get("USER")
        if usr == "root":
            self.AUDIOPATH = os.path.join("/", "root", "Music")
        else:
            self.AUDIOPATH = os.path.join("/", "home", usr, "Music")
    
    def save_as_audio(self, file_name):
        r"""
        Function is used to save the file or text as audio format at AUDIOPATH location.
        """
        
        self.set_audio_path()
        file_name = os.path.join(self.AUDIOPATH, file_name)

        if not file_name.endswith(".wav"):
            file_name += ".wav"

        cmd1 = ["espeak-ng", f"-w{file_name}", f"-a{self.volume}", f"-g{self.pause}", 
               f"-p{self.pitch}", f"-v{self.lang}+{self.voice}", f"-s{self.speed}"]
        cmd2 = ["|", "zenity", "--progress", "--title=Project 1", "--text=Converting...", 
                "--auto-kill", "--auto-close"]
        
        if self.file is None:
            cmd1.append(f"'{self.text}'")
        else:
            cmd1.append(f"-f{self.file}")
        
        cmd1.extend(cmd2)
        cmd = " ".join(cmd1)
        del cmd2, cmd1

        if not run(cmd, shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.PIPE).returncode:
            cmd = ["zenity", "--info", f"--text=Audio Save Sucessfully at {self.AUDIOPATH}!!", "--title=Project 1"]
            run_cmd(cmd)
            self.file = None
        else:
            cmd = ["zenity", "--error", "--text=Error!!", "--title=Project 1"]
            run_cmd(cmd)
    
    def ask_to_save(self):
        cmd = ["zenity", "--title=Project 1", "--question", "--text=Do you want to save as Audio?"]

        returncode, _ = run_cmd(cmd)
        if not returncode:
            speak("Set File name.")

            cmd = ["zenity", "--entry", "--title=Project 1", "--text=Enter File Name"]
            returncode, stdout = run_cmd(cmd)
            if not returncode:
                self.save_as_audio(stdout.replace("\n", ""))
    
    # ===========================  Take Text as Input  ================================ #
    def type_text(self):
        r"""
        Function is used to ask user for text to speak.
        """

        speak("Type text to speak.")

        cmd = ["zenity", "--entry", "--title=Project 1", "--text=Enter text to speak"]
        returncode, stdout = run_cmd(cmd)
        if not returncode:
            self.text = stdout

        if self.text != "" and len(self.text)<300:
            self.speak()
            self.ask_to_save()
        else:
            cmd = ["zenity", "--error", "--title=Project 1", "--text=Length of string should between 0-300"]
            _, _ = run_cmd(cmd)
            self.text = None
    
    # ===========================  Take File as Input  ================================ #
    def read_file(self):
        r"""
        Function is used to ask user for file to speak.
        """

        speak("Select file to speak.")

        cmd = ["zenity", "--file-selection", "--title=Project 1"]
        returncode, stdout = run_cmd(cmd)
        if not returncode:
            self.file = stdout.replace("\n", "")
            self.speak()
            self.ask_to_save()
        else:
            self.file = None


def sound_setting(obj):
    r"""
    Function is used to give option to user to set all sound setting.
    """

    LOOP = True

    while LOOP:
        speak("Select the option to set sound.")

        rows = ["Volume", "Pause between word", "Speed", "Pitch", "Language", "Voice", "Exit"]
        opt = show_option(rows=rows, for_what="Options")

        if opt is None:
            break

        if opt == 1:
            obj.adjust_volume()
        elif opt == 2:
            obj.pause_btw_word()
        elif opt == 3:
            obj.adjust_speed()
        elif opt == 4:
            obj.adjust_pitch()
        elif opt == 5:
            obj.select_lang()
        elif opt == 6:
            obj.select_voice()
        elif opt == 7:
            LOOP = False
 
def main():
    LOOP = True
    obj = eSpeakClass()

    while LOOP:
        speak("Select the option of espeak-ng tool.")

        rows = ["Sound Setting", "Read Text", "Read File", "Exit"]
        opt = show_option(rows=rows, for_what="Options")
        
        if opt is None:
            break

        if opt == 1:
            sound_setting(obj=obj)
        elif opt == 2:
            obj.type_text()
        elif opt == 3:
            obj.read_file()
        else:
            LOOP = False


# if __name__ == "__main__":
#     main()