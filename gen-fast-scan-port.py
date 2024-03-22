#!/usr/bin/python3

#This python script will do 2 things
#1. Use `rustscan` to detect all open-port
#2. Use `nmap` to scan all ports from the result of `rustscan`

import subprocess

def main():
    # Ask the user for IP input
    ip_address = input("Please provide an IP address: ")

    # Define the command to run
    command = f"rustscan -a {ip_address} -g | grep -o '\\[[0-9,]*\\]' | sed 's/[][]//g' | xargs -I {{}} nmap -Pn -sV -sC -sT -T4 -p {{}} {ip_address}"

    # Execute the command
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred while executing the command.")
        print(e.stderr)

if __name__ == "__main__":
    main()
