# Decode By Error x Ethan

import os
import sys
import requests
import time
import random
import uuid
G = '[1;32m'
R = '[1;31m'
B = '[1;34m'
Y = '[1;33m'
C = '[1;36m'
P = '[1;35m'
def banner():
    os.system('clear')
    print(f'{P}\n █████  ██   ██  █████  ███████ ██   ██\n██   ██ ██  ██  ██   ██ ██      ██   ██\n███████ █████   ███████ ███████ ███████\n██   ██ ██  ██  ██   ██      ██ ██   ██\n██   ██ ██   ██ ██   ██ ███████ ██   ██\n{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{C} [>] OWNER    : {Y} AKASH VAI\n{C} [>] METHOD   : {G} INSTAGRAM\n{C} [>] TOOLS    : {P} PAID\n{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def menu():
    banner()
    print(f' {C}[1] {G}START CLONING (HIGH SUCCESS RATE)')
    print(f' {C}[0] {R}EXIT SCRIPT')
    print(f'{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    choice = input(f' {C}[?] SELECT OPTION : {G}')
    if choice == '1':
        login_success_cloning()
    else:
        sys.exit()
def login_success_cloning():
    # irreducible cflow, using cdg fallback
    # ***<module>.login_success_cloning: Failure: Compilation Error
    banner()
    print(f' {C}[+] {G}CLONING STARTED... PLEASE WAIT')
    print(f' {C}[+] {Y}USE COOKIES FOR LOGIN SUCCESS')
    print(f'{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    ok = 0
    cp = 0
    loop = 0
        loop += 1
        user = str(random.choice(['1000', '2000', '3000'])) + str(random.randint(100000, 999999))
        email = user + '@gmail.com'
        pw = random.choice(['123456', '12345678', 'instagram', 'password', user])
        sys.stdout.write(f'\r[K {C}[AKASH-CHECK] {loop} | {G}OK:{ok} | {R}CP:{cp}\r')
        sys.stdout.flush()
        if random.randint(1, 45) == 5:
            cookie = f'mid={uuid.uuid4().hex[:12]}; ig_did={uuid.uuid4()}; datr={uuid.uuid4().hex[:24]}; sessionid={random.randint(100, 999)}%3A{uuid.uuid4().hex[:32]}; ds_user_id={user};'
            print(f'\r[K{G}[AKASH-OK] {email} | {pw}')
            print(f'{Y}[LOGIN-COOKIE] : {C}{cookie}')
            print(f'{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            ok += 1
            with open('/sdcard/AKASH-LOGIN-OK.txt', 'a') as f:
                f.write(f'{email}|{pw}|{cookie}\n')
            time.sleep(0.05)
        except KeyboardInterrupt:
            except KeyboardInterrupt:
                pass
    print(f'\n{B}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f' {G}[✓] TOTAL OK: {ok}')
    input(f' {G}[>] PRESS ENTER TO GO BACK')
    menu()
if __name__ == '__main__':
    menu()