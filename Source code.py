#CODED IN PYTHON3.13: (code for networkkillswitch1) (my computer was giving me problems so I had to upload it this way.) - By LiquiditySweep-FVG

import subprocess #allows for commands to be ran
from colorama import init, Fore # colours
import sys #allows for sys exit
import os #allows for code to be ran and interact with computer
import ctypes #allows for commands to be ran

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() #checks if admin
    except:
        return False


if not is_admin():
    print("Requesting administrator privileges...")
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([f'"{arg}"' for arg in sys.argv[1:]])
    try:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, f'"{script}" {params}', None, 1
        )
    except Exception as e:
        print(f"Failed to elevate privileges: {e}")
    sys.exit()  # Exit the original (non-admin) process #exits


# Define PowerShell commands
DISABLE = """Get-NetAdapter | Disable-NetAdapter -Confirm:$false"""
ENABLE = """Get-NetAdapter | Enable-NetAdapter -Confirm:$false"""

def run_powershell(command):
    try:
        subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-Command', command], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the PowerShell command: {e}")

def main():
    init()  # Initialize colorama for colored output

    by = "BY LiquiditySweep-FVG"
    print(Fore.RED + f"{by} ")  #shows the stuff

    while True: #while loop to ensure it doesnt stop running, because its ALWAYS TRUE.
        print("Select an option:")
        print("1. Disable network adapters")
        print("2. Enable network adapters")
        print("3. Exit")

        choice = input("Enter the number corresponding to what you want to do: ") #assigns the variable choice to whatever is written in select option

        if choice == "1":
            run_powershell(DISABLE) #runs the disable command for internet
        elif choice == "2":
            run_powershell(ENABLE) #runs enable command for internet
        elif choice == "3":
            print("Exiting...")
            sys.exit(0)  # ends the code essentially
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main() # this is essentially just something to put at the end of every code from now on, it stops it from ending basically. thats not what it is, but thats what it essentially does.


