#!/usr/bin/python3

from colorama import Fore,Back,Style,init
init(autoreset=True) #Auto reset color for each print

def main():
    print(f"{Style.BRIGHT}{Fore.GREEN}+ This script will:")
    print(f"{Style.BRIGHT}1: restore the default $PATH for both Windows + Linux")
    print(f"{Style.BRIGHT}2: upgrade shell for Linux only")
    print(f"")
    print(f"{Style.BRIGHT}{Fore.GREEN}+ Please choose platform:")
    print("- Option 1: Linux")
    print("- Option 2: Windows")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print(f"{Fore.GREEN}\n=====")
        print(f"You chose {Style.BRIGHT}Option 1 - {Fore.BLUE}Linux")
        print(f"{Style.BRIGHT}{Fore.BLUE}+ Step 1: From terminal-victim, reset $PATH and set color for terminal")
        print(f"""{Style.BRIGHT}export PATH="/usr/bin:/usr/sbin:/sbin:/bin:/usr/local/bin:/usr/local/sbin" && export TERM=xterm-256color""")
        print(f"")
        print(f"{Style.BRIGHT}{Fore.BLUE}+ Step 2: Check target-server has python, python3, or perl?")
        print(f"{Style.BRIGHT}which python; which python3; which perl")
        print(f"")
        print(f"{Style.BRIGHT}{Fore.BLUE}+ Step 3: Select option below to spawn a shell")
        print(f"""{Style.BRIGHT}python -c 'import pty; pty.spawn("/bin/bash")'""")
        print(f"""{Style.BRIGHT}python3 -c 'import pty; pty.spawn("/bin/bash")'""")
        print(f"""{Style.BRIGHT}perl -e 'exec "/bin/sh";'""")
        print(f"")
        print(f"{Style.BRIGHT}{Fore.BLUE}+ Step 4: From terminal-victim, switch back to terminal-attacker by pressing")
        print(f"""{Style.BRIGHT}Ctrl + Z""")
        print(f"")
        print(f"{Style.BRIGHT}{Fore.BLUE}+ Step 5: Check current rows & columns of terminal-attacker")
        print(f"{Style.BRIGHT}echo $(stty size | awk '{{print \"rows \" $1 \", columns \" $2}}')")
        print(f"")
        print(f"{Style.BRIGHT}{Fore.BLUE}+ Step 6: From the terminal-attacker, run command below, and press 2 times ENTER to switch back terminal-victim")
        print(f"""{Style.BRIGHT}stty raw -echo; fg; reset""")
        print(f"""{Style.BRIGHT}Enter 2-times""")
        print(f"")
        print(f"{Style.BRIGHT}{Fore.BLUE}+ Step 7: Set terminal-victim has the same columns & rows of attacker")
        print(f"{Style.BRIGHT}stty rows {{rows-num}} cols {{columns-num}}")
        print(f"")
        print(f"{Style.BRIGHT}{Fore.BLUE}+ Step 8: Adding color when run command ll")
        print(f"{Style.BRIGHT}alias ll='ls -lsaht --color=auto'")
        print(f"")
        print(f"{Fore.GREEN}END=====\n")
        
    elif choice == '2':
        print(f"{Fore.GREEN}\n=====")
        print(f"You chose {Style.BRIGHT}+ Option 2 - {Fore.BLUE}Windows")
        print(f"{Style.BRIGHT}{Fore.RED}+ Note that, cannot upgrade shell in Windows")
        print(f"{Style.BRIGHT}{Fore.BLUE}→ Can only reset $PATH and set color for terminal")
        print(f"{Style.BRIGHT}set PATH=%SystemRoot%\\system32;%SystemRoot%;%SystemRoot%\\System32\\Wbem;%SystemRoot%\\System32\\WindowsPowerShell\\v1.0;%WINDIR%\\System32\\OpenSSH;%SystemRoot%\\System32\\config\\systemprofile.dnx\\bin;C:\\Program Files\\Python39;%SystemRoot%\\System32\\OpenSSH;C:\\ProgramData\\chocolatey\\bin;")
        print(f"")
        print(f"{Fore.GREEN}END=====\n")
    else:
        print("Invalid choice, please enter 1 or 2.")

if __name__ == "__main__":
    main()
