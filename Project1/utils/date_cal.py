from utils.common import run_cmd, speak, show_option

class Date():
    def speak_date(self):
        cmd = "espeak-ng -a200 -s140 \"Today date is $(date \"+%d %m %Y\")\""
        run_cmd(cmd, shell=True)
    
    def speak_day(self):
        cmd = "espeak-ng -a200 -s140 \"Today day is $(date \"+%A\")\""
        run_cmd(cmd, shell=True)
    
    def speak_time(self):
        cmd = "espeak-ng -a200 -s140 \"Current time is $(date \"+%H:%M:%S\")\""
        run_cmd(cmd, shell=True)

def show_cal():
    speak("Showing calender.")

    cmd = 'zenity --info --width=300 --text="$(cal)"'
    _, _ = run_cmd(cmd, shell=True)

def main():
    LOOP = True
    obj = Date()

    while LOOP:
        speak("Select the option of date tool.")

        rows = ["Date", "Day", "Time", "Calender", "Exit"]
        opt = show_option(rows=rows, for_what="Options")
        
        if opt is None:
            break

        if opt == 1:
            obj.speak_date()
        elif opt == 2:
            obj.speak_day()
        elif opt == 3:
            obj.speak_time()
        elif opt == 4:
            show_cal()
        else:
            LOOP = False


# if __name__ == "__main__":
#     main()
