import os

def menu():

    print(""" 
.########..#######...#######..##........######..########.
....##....##.....##.##.....##.##.......##....##.##....##
....##....##.....##.##.....##.##.......##.......##....##
....##....##.....##.##.....##.##........######..########
....##....##.....##.##.....##.##.............##.##.....##
....##....##.....##.##.....##.##.......##....##.##......##
....##.....#######...#######..########..######..##.......##
========================================
Created By RoyHacker

Ver: 0.1
----
ONLY FOR TERMUX!
----
This is only for education purpose... 
==========================================
Other tools adding in such weeks.....
------------------------------------------
1. Install Nmap 
2. Install SQLMap
3. Instagram Bruteforcer (instahack)
4. Install Hash-Buster
------------------------------------------
99. Exit
==========================================
""")

loop = true

loop = True

while loop:
    menu()
    what = input("#: ")
     if what == "1":
             
        
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] nmap installed successfully :)")
        print("[+] Type 'nmap' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break

    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap installed successfully :)")
        print("[+] Go to sqlmap folder and type 'python2 sqlmap.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break

    elif what == "3":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
        print("====================================")
        print("[+] Instahack installed successfully :)")
        print("[+] Go to instahack folder and type 'python hackinsta.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
        
    elif what == "4":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
        print("====================================")
        print("[+] Hash-Buster installed successfully :)")
        print("[+] Go to Hash-Buster folder and type 'python2 hash.py' to start.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "99":
        print("Bye.")
        break



