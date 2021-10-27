from utils.common import run_cmd, speak

def open_firefox():
    speak("opening firefox")
    cmd = ["firefox"]
    returncode, _ = run_cmd(cmd)

    if returncode:
        cmd = ["zenity", "--error", "--text=no DISPLAY environment variable specified"]
        run_cmd(cmd)

def main():
    open_firefox()

if __name__ == "__main__":
    main()