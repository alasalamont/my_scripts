#!/usr/bin/python
from colorama import Fore,Back,Style,init
init(autoreset=True) #Auto reset color for each print


print(Fore.GREEN + "=====")
print(Fore.BLUE + "Fuzzing common files when don't know targe-framework")
print(f"{Style.BRIGHT}ffuf -c -w /usr/share/seclists/Discovery/Web-Content/raft-large-files.txt -u $URL -fc 404 -t 150 -ic")

print("")
print(Fore.BLUE + "Fuzzing file that has no extension")
print(f"{Style.BRIGHT}ffuf -c -w /usr/share/seclists/Discovery/Web-Content/raft-large-words.txt -u $URL -fc 404 -t 150 -ic")

print("")
print(Fore.BLUE + "Fuzzing file with specific extension")
print(f"{Fore.RED}{Style.BRIGHT}+ Don't forget add extension at $URL - export URL=http://example.com/FUZZ.php")
print(f"{Style.BRIGHT}ffuf -c -w /usr/share/seclists/Discovery/Web-Content/raft-large-words.txt -u $URL -fc 404 -t 150 -ic")

print("")
print(Fore.BLUE + "Fuzzing PHP files from Common-PHP-Filenames.txt")
print(f"{Style.BRIGHT}ffuf -c -w /usr/share/seclists/Discovery/Web-Content/Common-PHP-Filenames.txt -u $URL -fc 404 -t 150 -ic")

print("")
print(Fore.BLUE + "Fuzzing files and directories when target-web-server is IIS")
print(f"{Fore.RED}{Style.BRIGHT}+ Because the wordlist IIS.fuzz.txt contains directories & files name → Using feroxbuster to faster fuzzing")
print(f"{Style.BRIGHT}feroxbuster -u $URL -w /usr/share/seclists/Discovery/Web-Content/IIS.fuzz.txt")



print("")
print("")
print(Fore.GREEN + "=====")
print(Fore.BLUE + "Fuzzing directories based on raft-large-directories.txt")
print(f"{Style.BRIGHT}ffuf -c -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories.txt -u $URL -fc 404 -t 150 -ic")

print("")
print(Fore.BLUE + "Fuzzing directories based on directory-list-2.3-medium.txt")
print(f"{Style.BRIGHT}ffuf -c -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -u $URL -fc 404 -t 150 -ic")


print("")
print("")
print(Fore.GREEN + "=====")
print(Fore.BLUE + "Fuzzing blank-page or page-show-error-message")
print(f"{Fore.RED}{Style.BRIGHT}+ Don't forget to add flag `-fs` or `-fw` to filter out false result")
print(f"{Style.BRIGHT}ffuf -c -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -u $URL -t 150 -ic")

print("")
print("")
print(Fore.GREEN + "=====")
print(Fore.BLUE + "Fuzzing sub-domain via V-Host")
print(f"{Fore.RED}{Style.BRIGHT}+ Don't forget to add flag `-fs` or `-fw` to filter out non-existing-sub-domain")
print(f"{Style.BRIGHT}ffuf -c -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -u $URL -t 150 -ic")

