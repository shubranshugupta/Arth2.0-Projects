from subprocess import run
import subprocess

def speak(msg):
    cmd = ["espeak-ng", f"{msg}"]
    run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

def show_option(rows, for_what="Tools"):
    if for_what in ["Tools", "Options"]:
        cmd = ["zenity", "--list", "--column=Select", "--column=Sr. No.", f"--column={for_what}", 
                   "--radiolist", "--height=500", "--width=400", "--title=Project 1"]
    
        for idx, element in enumerate(rows):
            cmd.extend([f"{idx}", f"{idx+1}", f"{element}"])
        
        process = run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        if not process.returncode:
            return int(process.stdout)

def run_cmd(cmd, shell=False):
    process = run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, shell=shell)

    return (int(process.returncode), process.stdout)

def check_prog(prog):
    cmd = ["which", prog]
    returncode, _ = run_cmd(cmd)
    if returncode == 0:
        return True
    return False

def insatll_cmd(script_path, prog):
    cmd = f"{script_path} {prog} | zenity --progress --title Project 1 --text='Installing {prog}'"
    returncode, _ = run_cmd(cmd, shell=True)
    if returncode:
        cmd = ["zenity", "--error", "--text=An error occure during installation"]
        run_cmd(cmd)

def ask_install(prog):
    speak(f"Do you want to install {prog}")
    
    cmd = ["zenity", "--question", f"--text=Do you want to install {prog}?"]
    returncode, _ = run_cmd(cmd)
    if returncode == 0:
        return True
    return False

# if __name__ == "__main__":
#     print(show_option(["a v", "b", "c"]))
