# Decode By Error x Ethan

import requests
import os
import re
import sys
import json
import time
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console
from rich.align import Align
import threading
console = Console()
session = requests.Session()
def log_share(status, post_id, current, total):
    short_id = post_id.split('_')[(-1)] if '_' in post_id else post_id
    now = time.strftime('%H:%M:%S')
    if status == 'success':
        console.print(f'[blue][{now}][/blue] [green]Share Completed[/green] [yellow]{short_id}[/yellow] [red]{current}/{total}[/red]')
    else:
        console.print(f'[blue][{now}][/blue] [red]Share Failed[/red] [yellow]{short_id}[/yellow] [red]{current}/{total}[/red]')
def approval_check():
    # irreducible cflow, using cdg fallback
    # ***<module>.approval_check: Failure: Compilation Error
    os.system('clear')
    try:
        raw = str(os.geteuid()) + os.getlogin()
    except:
        raw = str(os.getpid()) + os.name
    device_id = 'X'.join(raw)
    final_key = 'PAID-' + device_id
    title = ['🛡️ SECURE ACCESS GATEWAY 🛡️', '🔑 DEVICE AUTHORIZATION REQUIRED 🔑']
    for line in title:
        console.clear()
        console.print(Panel(Align.center(line), border_style='cyan', expand=True))
        time.sleep(0.2)
    console.print(Panel(Align.center(f'[bold cyan]     YOUR APPROVAL KEY[/bold cyan]\n[yellow]{final_key}[/yellow]'), border_style='magenta', title='[bold white]GENERATED DEVICE KEY[/bold white]', expand=True))
    console.print('[white]Send this key to the owner to get approved.[/white]')
    KEY_URL = 'https://raw.githubusercontent.com/KCL-404/meta/main/kandado.txt'
    response = requests.get(KEY_URL, timeout=5).text
    if final_key in response:
        console.print(Panel('[green]✔ Access Granted — Your device is approved.[/green]', border_style='green'))
        time.sleep(1.5)
            return True
        console.print(Panel('[red]✘ DEVICE NOT APPROVED[/red]\n[white]Please message the owner and wait for approval.[/white]', border_style='red', title='[bold red]ACCESS DENIED[/bold red]'))
        console.print(f'[yellow]Your Key:[/] [bold]{final_key}[/bold]\n')
        console.print('[cyan]Enter your details to send approval request...[/cyan]')
        console.input('[bold white]Your Name : [/bold white]')
        console.input('[bold white]Press ENTER to confirm sending...[/bold white]')
        sys.exit()
            except Exception:
                console.print(Panel('[red]⚠ Unable to reach approval server[/red]\n[white]Check your internet connection.[/white]', border_style='red'))
                console.input('Press ENTER to exit...')
                sys.exit()
def print_banner():
    banner = '    ___                   \n    | |                   \n ___| |__   __ _ _ __ ___ \n/ __| \'_ \\ / _` | \'__/ _ \\\n\\__ \\ | | | (_| | | |  __/\n|___/_| |_|\\__,_|_|  \\___|'
    lines = banner.split('\n')
    for i in range(len(lines)):
        console.clear()
        current_banner = '\n'.join(lines[:i + 1])
        console.print(Panel(Align.center(current_banner), border_style='magenta', expand=True))
        time.sleep(0.03)
def load_cookies():
    if os.path.exists('cookies.json'):
        return json.load(open('cookies.json', 'r'))
    else:
        return {}
def save_cookies(cookies):
    json.dump(cookies, open('cookies.json', 'w'), indent=4)
def add_cookie():
    os.system('clear')
    print_banner()
    console.print('[yellow]Enter Account Name:[/]')
    name = input('> ').strip()
    console.print('[yellow]Enter Cookie:[/]')
    cookie = input('> ').strip()
    cookies = load_cookies()
    cookies[name] = cookie
    save_cookies(cookies)
    console.print(f'[green]Cookie saved for {name}![/]')
    time.sleep(1)
def select_cookie():
    cookies = load_cookies()
    if not cookies:
        console.print('[red]No cookies saved![/]')
        return
    else:
        os.system('clear')
        print_banner()
        account_list = ''
        for i, acc in enumerate(cookies.keys(), start=1):
            account_list += f'[cyan]{i}.[/] {acc}\n'
        console.print(Panel(account_list.strip(), title='[bold cyan]Saved Accounts[/bold cyan]', border_style='magenta'))
        choice = int(input('\nChoose: ')) - 1
        key = list(cookies.keys())[choice]
        return (cookies[key], key)
def remove_cookie():
    # irreducible cflow, using cdg fallback
    # ***<module>.remove_cookie: Failure: Compilation Error
    cookies = load_cookies()
    if not cookies:
        console.print('[red]No cookies saved![/]')
        time.sleep(1)
        return
    else:
        os.system('clear')
        print_banner()
        console.print('[bold cyan]Saved Accounts[/]\n')
        keys = list(cookies.keys())
        for i, acc in enumerate(keys, start=1):
            console.print(f'[cyan]{i}.[/] {acc}')
    choice = int(input('\nSelect number to remove: ')) - 1
    if choice < 0 or choice >= len(keys):
        console.print('[red]Invalid choice![/red]')
        time.sleep(1)
            return
        removed = keys[choice]
        del cookies[removed]
        save_cookies(cookies)
        console.print(f'[green]Removed cookie for account:[/] {removed}')
        time.sleep(1)
            except ValueError:
                console.print('[red]Invalid input![/red]')
                time.sleep(1)
def get_token(cookie):
    r = session.get('https://business.facebook.com/business_locations', headers={'User-Agent': 'Mozilla/5.0', 'Cookie': cookie})
    match = re.search('(EAAG\\w+)', r.text)
    if match:
        return match.group(1)
    else:
        return None
def bot(cookie):
    token = open('token.txt', 'r').read()
    lmnx9_share(cookie, token)
def lmnx9_share(cookie, token):
    header = {'user-agent': 'Mozilla/5.0'}
    post_link = Prompt.ask('[magenta]Enter Post Link[/]')
    share_limit = int(Prompt.ask('[cyan]Share Limit[/] :'))
    coki = {'cookie': cookie}
    console.print('[blue]Post Share Started...[/blue]')
    for i in range(share_limit):
        try:
            res = session.post(f'https://graph.facebook.com/me/feed?link={post_link}&published=0&access_token={token}', headers=header, cookies=coki).json()
            post_id = res.get('id') or res.get('post_id') or 'ERROR'
            if 'error' in res:
                log_share('failed', post_id, i + 1, share_limit)
            else:
                log_share('success', post_id, i + 1, share_limit)
        except Exception as e:
            log_share('failed', f'ERROR ({e})', i + 1, share_limit)
        time.sleep(0.35)
def share_with_cookie_limited(name, cookie, post_link, token, counter, total):
    # irreducible cflow, using cdg fallback
    # ***<module>.share_with_cookie_limited: Failure: Compilation Error
    header = {'user-agent': 'Mozilla/5.0'}
    coki = {'cookie': cookie}
    res = session.post(f'https://graph.facebook.com/me/feed?link={post_link}&published=0&access_token={token}', headers=header, cookies=coki).json()
    post_id = res.get('id') or res.get('post_id') or 'ERROR'
    if 'error' in res:
        log_share('failed', post_id, counter, total)
        log_share('success', post_id, counter, total)
            except Exception as e:
                    log_share('failed', f'ERROR ({e})', counter, total)
                        pass
def multi_thread_share_limited():
    os.system('clear')
    print_banner()
    cookies = load_cookies()
    if not cookies:
        console.print('[red]No saved cookies found![/red]')
        time.sleep(1)
        return
    else:
        post_link = Prompt.ask('[magenta]Enter Post Link[/]')
        total_share = int(Prompt.ask('[cyan]Share Limit[/] :'))
        tokens = {}
        accounts = list(cookies.items())
        for acc, coki in accounts:
            token = get_token(coki)
            if token:
                tokens[acc] = token
            else:
                console.print(f'[red]Token failed for {acc} (Dead cookie)[/red]')
        if not tokens:
            console.print('[red]No valid accounts to share.[/red]')
            time.sleep(1)
            return
        else:
            console.print(f'[blue]Starting multi-threaded sharing for {total_share} total shares...[/blue]')
            counter = 0
            idx = 0
            while counter < total_share:
                threads = []
                for _ in range(len(tokens)):
                    if counter >= total_share:
                        break
                    else:
                        acc, coki = accounts[idx % len(accounts)]
                        if acc not in tokens:
                            idx += 1
                            continue
                        else:
                            t = threading.Thread(target=share_with_cookie_limited, args=(acc, coki, post_link, tokens[acc], counter + 1, total_share))
                            t.start()
                            threads.append(t)
                            counter += 1
                            idx += 1
                for t in threads:
                    t.join()
                time.sleep(0.35)
            console.print(f'[green]✔ Completed {total_share} shares across all accounts![/green]')
            input('Press ENTER to return...')
def main_menu():
    # irreducible cflow, using cdg fallback
    # ***<module>.main_menu: Failure: Compilation Error
    selected = None
    os.system('clear')
    print_banner()
    console.print(Panel('[cyan]1.[/] Add Cookie\n[cyan]2.[/] Select Cookie\n[cyan]3.[/] Remove Cookie\n[cyan]4.[/] Start Spam Share\n[cyan]5.[/] Multi-Thread Share (All Cookies)\n[cyan]0.[/] Exit', title='[white]SPAM SHARE MENU[/]', border_style='magenta'))
    choice = input('Choose: ').strip()
    if choice == '1':
        add_cookie()
        continue
    if choice == '2':
        result = select_cookie()
        if result:
            selected, account_name = result
            console.print(Panel(f'[green]Selected account:[/] {account_name}', border_style='magenta'))
            time.sleep(1)
        continue
    if choice == '3':
        remove_cookie()
        selected = None
        continue
    if choice == '4':
        if not selected:
            console.print(Panel('[red]No cookie selected! Please select a cookie first.[/red]', border_style='magenta'))
            time.sleep(1.5)
            continue
        else:
            cookie = selected
            console.print(Panel('[yellow]Getting token...[/yellow]', border_style='magenta'))
            token = get_token(cookie)
            if not token:
                console.print(Panel('[red]Token not found! Cookie may be dead.[/red]', border_style='magenta'))
                time.sleep(1.5)
            else:
                open('token.txt', 'w').write(token)
                bot(cookie)
        if choice == '5':
            multi_thread_share_limited()
            if choice == '0':
                console.print(Panel('[yellow]Exiting...[/yellow]', border_style='magenta'))
            else:
                console.print(Panel('[red]Invalid option![/red]', border_style='magenta'))
                time.sleep(1)
if __name__ == '__main__':
    approval_check()
    main_menu()