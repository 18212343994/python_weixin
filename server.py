import threading
import socket
import requests
import time
import http.cookiejar
from http import cookiejar
import urllib.request
import urllib.request
import urllib.parse
import datetime
import random
from threading import Timer
encoding = 'utf-8'
BUFSIZE = 1024
client=socket.socket()
client.connect(('127.0.0.1',6076))


# a read thread, read data from remote
class Reader(threading.Thread):







    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client
        

    def run(self):
        while True:
            data = self.client.recv(BUFSIZE)
            if(data):
                try:
                    string = bytes.decode(data, encoding)
                    send=str(string)
                    rec = send.split("=")[-1]
                    messge=str(rec).strip()
                    long = len(messge)
                    print(long)
                except Exception:
                    print('zijieyic')
                    long=2



                
                if long==11:
                    try:
                    #print(messge)
                        yddcx(messge)
                    except Exception:
                        print('yddyc')

                elif long==5:
                    ydddl()

                elif long==15:
                    #print('express')
                    try:
                        yto(messge)
                        
                    except Exception:
                        print('快递查询异常')


                elif long>21:
                    get_cookie()#每次调用get_cookie函数获取cookie
                    try:
                        l = list(map(int, messge.split()))

                        #print("input:"+l)
                        kd= []
                        for t in l:
                            kd.append(yddplcx(t))

                        bb = "\n".join(kd)
                        send1(bb)

                    except Exception:
                        print('批量匹配异常')



                else:print('无效查询')





























                '''
                url='http://www.yto.net.cn/api/trace/waybill'
                data = {
                    'waybillNo': messge
                }
                r=requests.post(url,data=data)
                rj=r.json()
                ifjs=rj['data'][0]['traces']
                if ifjs==None:
                    #print(messge,'无走件记录')

                    a=messge+'无走件记录'
                    send1(a)

                    s={"type_msg":"EventMsg","robot_wxid":"wxid_9grk4r0ixtli22","to_wxid":"23876489726@chatroom","msg":a}
                    ss=str(s)
                    client.send(ss.encode('gbk'))


                else :
                    result0 = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(ifjs[0]['time']/1000))))+ifjs[0]['info']
                    result1 = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(ifjs[1]['time']/1000))))+ifjs[1]['info']
                    #print(messge,result0,',',result1)
                    a=messge+'\n'+'最新：'+result0+'\n'+'上一条: '+result1+'\n'

                    send1(a)


                    b=str(a)
                    s={"type_msg":"EventMsg","robot_wxid":"wxid_9grk4r0ixtli22","to_wxid":"23876489726@chatroom","msg":b}
                    ss=str(s)
                    client.send(ss.encode('gbk'))  '''














                #aa="hell0"

                #s='{"type_msg":"EventMsg","robot_wxid":"wxid_9grk4r0ixtli22","to_wxid":"23876489726@chatroom","msg":"%s"}'%a
                #client.send(s.encode('gbk'))
                #client.send('{"type_msg":"EventMsg","robot_wxid":"wxid_9grk4r0ixtli22","to_wxid":"23876489726@chatroom","msg":"hi"}'.encode('gbk'))
                #c='{"type_msg":"EventMsg","robot_wxid":"wxid_9grk4r0ixtli22","to_wxid":"23876489726@chatroom","msg":'+a+'}'
                #client.send(c.encode('gbk'))
                #print(c.encode('gbk'))
                #client.close()


            else:
                break
        print("close:", self.client.getpeername())

    

def send1(a):    
    b=str(a)
    s={"type_msg":"EventMsg","robot_wxid":"wxid_9grk4r0ixtli22","to_wxid":"23876489726@chatroom","msg":b}
    ss=str(s)
    client.send(ss.encode('gbk'))




def baocdl(a=(random.randint(800,1800))):
    cj = http.cookiejar.CookieJar()
    # 创建一个haddler对象
    haddler = urllib.request.HTTPCookieProcessor(cj)
    # 创建一个opener对象
    opener = urllib.request.build_opener(haddler)
    formData = {
        'loginMethod': 'generalLogin',
        'deviceId': 'G4JHX6KI62LPYHWNR2OPCKX3WIBOIGU75DFFHKK6RS5QQDVF75LB4UESP5LLFN57KNYBI6Y2X3QSI3AP5KRYSMMPUY',
        'username': '13827471947',
        'password': 'qh457110'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'cookie': ''
    }
    url = "https://www.1dadan.com/security/loginMain"

    session = requests.Session()

    cookie_jar = session.post(url, formData).cookies

    cookie = requests.utils.dict_from_cookiejar(cookie_jar)
    ecs_t = cookie['ecs_t']


    
    print(ecs_t)
    url = 'https://www.1dadan.com/api/order/list'
    data = {
        'ordersTimeType': 0,
        'startdate': datetime.datetime.now().strftime('%Y-%m-%d')+' 00:00:00',
        'enddate': time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
        'shopId': 'all',
        'tradeStatus': 'all',
        'province': 'all',
        'sellerRemarkOrMarkLevel': 'all',
        'serviceType': 'all',
        'refundStatus': 'all',
        'pageNo': 1,
        'needRefresh': 1,
        'isGroupDisplay': 1,
        'isSingles': 'false',
        'sfPriceMarkupStr': 'all'
    }

    header = {
        'cookie':'_ati=2582860471517; 3AB9D23F7A4B3C9B=G4JHX6KI62LPYHWNR2OPCKX3WIBOIGU75DFFHKK6RS5QQDVF75LB4UESP5LLFN57KNYBI6Y2X3QSI3AP5KRYSMMPUY; fsno=15218833698548; _pati=a2b71ef462b5771fe5d9f95ab9dc42b8; fslb=s1b13; ecs_t=%s'%(ecs_t),
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
    r = requests.post(url, data=data,headers=header)
    rj = r.json()

    dl=rj['data']['page']['totalRecord']
    print(dl)

    t = Timer(random.randint(800,1800), baocdl, (random.randint(800,1800),))
    t.start()



def yto(messge):
    url='http://www.yto.net.cn/api/trace/waybill'
    data = {
        'waybillNo': messge
    }
    r=requests.post(url,data=data)
    rj=r.json()
    ifjs=rj['data'][0]['traces']
    if ifjs==None:
        #print(messge,'无走件记录')
        a=messge+'无走件记录'
        send1(a)
        print(a)


    else :
        result0 = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(ifjs[0]['time']/1000))))+ifjs[0]['info']
        result1 = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(ifjs[1]['time']/1000))))+ifjs[1]['info']
        #print(messge,result0,',',result1)
        a=messge+'\n'+'最新：'+result0+'\n'+'上一条: '+result1+'\n'
        send1(a)
        print(a)







def yddcx(messge):

    cj = http.cookiejar.CookieJar()
    # 创建一个haddler对象
    haddler = urllib.request.HTTPCookieProcessor(cj)
    # 创建一个opener对象
    opener = urllib.request.build_opener(haddler)
    formData = {
        'loginMethod': 'generalLogin',
        'deviceId': 'ER7G7IZ5N4YKVM2UQJGQA7TM2KR2JNTKD4XIZZTBINET4NE6BPZMSPX2EFQM2EHHGLCBSFJUX4L62XB4NNDHI6WRAA',
        'username': '13827471947',
        'password': 'qh457110'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'cookie': ''
    }
    url = "https://www.1dadan.com/security/loginMain"

    session = requests.Session()

    cookie_jar = session.post(url, formData).cookies

    cookie = requests.utils.dict_from_cookiejar(cookie_jar)
    ecs_t = cookie['ecs_t']











    url = 'https://www.1dadan.com/api/order/list'
    data = {
    'ordersTimeType': 0,
    'startdate': '2020-8-12 00:00:00',
    'enddate': time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
    'shopId': 'all',
    'tradeStatus': 'all',
    'province': 'all',
    'sellerRemarkOrMarkLevel': 'all',
    'serviceType': 'all',
    'refundStatus': 'all',
    'searchKey': 18,
    'searchValue': messge,
    'pageNo': 1,
    'needRefresh': 1,
    'isGroupDisplay': 1,
    'isSingles': 'false',
    'sfPriceMarkupStr': 'all'
    }

    header = {
        'cookie':'_ati=2582860471517; 3AB9D23F7A4B3C9B=G4JHX6KI62LPYHWNR2OPCKX3WIBOIGU75DFFHKK6RS5QQDVF75LB4UESP5LLFN57KNYBI6Y2X3QSI3AP5KRYSMMPUY; fsno=15218833698548; _pati=a2b71ef462b5771fe5d9f95ab9dc42b8; fslb=s1b13; ecs_t=%s'%(ecs_t),
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
    r = requests.post(url, data=data,headers=header)
    rj = r.json()


    ifresult1=rj['data']['page']['data']

    if ifresult1==[]:
        a2=messge+'最近一个月没有查询结果'
        send1(a2)
    else:
        a3=messge+'总单数：'+str(rj['data']['page']['totalRecord'])
        result1 = rj['data']['page']['data'][0]['data']
        for b in result1:
            ajjr='寄件人：'+b['shipperName']
            a4='姓名电话: '+b['receiverName']+str(b['receiverMobile'])
            a44='详细地址：'+b['receiverFullAddress']
            a5='打印时间：'+time.strftime("%Y-%m-%d %H:%M:%S", (time.localtime(float(b['printDate']/1000))))
            a6='快递单号：'+b['logisticsNo']
            a16=b['logisticsNo']
            a7='订单编号：'+b['trades'][0]['tradeNo']
            a8='产品：'
            list = []
            for c in b['goods']:
                a9=str(c['quantity'])+'件 '+c['goodsName']
                list.append(a9)


            send1(a3+'\n'+ajjr+'\n'+a4+'\n'+a44+'\n'+a5+'\n'+a6+'\n'+a7+'\n'+a8+'\n'+str(list)+'\n')

            yto(a16)

#查看易打单今天有多少单
def ydddl():#这个是查询今天有多少单

    cj = http.cookiejar.CookieJar()
    # 创建一个haddler对象
    haddler = urllib.request.HTTPCookieProcessor(cj)
    # 创建一个opener对象
    opener = urllib.request.build_opener(haddler)
    formData = {
        'loginMethod': 'generalLogin',
        'deviceId': 'G4JHX6KI62LPYHWNR2OPCKX3WIBOIGU75DFFHKK6RS5QQDVF75LB4UESP5LLFN57KNYBI6Y2X3QSI3AP5KRYSMMPUY',
        'username': '13827471947',
        'password': 'qh457110'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'cookie': ''
    }
    url = "https://www.1dadan.com/security/loginMain"

    session = requests.Session()

    cookie_jar = session.post(url, formData).cookies

    cookie = requests.utils.dict_from_cookiejar(cookie_jar)
    ecs_t = cookie['ecs_t']
    url = 'https://www.1dadan.com/api/order/list'
    data = {
        'ordersTimeType': 0,
        'startdate': datetime.datetime.now().strftime('%Y-%m-%d')+' 00:00:00',
        'enddate': time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
        'shopId': 'all',
        'tradeStatus': 'all',
        'province': 'all',
        'sellerRemarkOrMarkLevel': 'all',
        'serviceType': 'all',
        'refundStatus': 'all',
        'pageNo': 1,
        'needRefresh': 1,
        'isGroupDisplay': 1,
        'isSingles': 'false',
        'sfPriceMarkupStr': 'all'
    }

    header = {
        'cookie':'_ati=2582860471517; 3AB9D23F7A4B3C9B=G4JHX6KI62LPYHWNR2OPCKX3WIBOIGU75DFFHKK6RS5QQDVF75LB4UESP5LLFN57KNYBI6Y2X3QSI3AP5KRYSMMPUY; fsno=15218833698548; _pati=a2b71ef462b5771fe5d9f95ab9dc42b8; fslb=s1b13; ecs_t=%s'%(ecs_t),
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
    r = requests.post(url, data=data,headers=header)
    rj = r.json()

    dl=rj['data']['page']['totalRecord']
    s=time.strftime('%Y-%m-%d',time.localtime(time.time()))+' 打单数为：'+str(dl)+'单'

    send1(s)



def get_cookie():
    global cok
    cj = http.cookiejar.CookieJar()
    # 创建一个haddler对象
    haddler = urllib.request.HTTPCookieProcessor(cj)
    # 创建一个opener对象
    opener = urllib.request.build_opener(haddler)
    formData = {
        'loginMethod': 'generalLogin',
        'deviceId': 'G4JHX6KI62LPYHWNR2OPCKX3WIBOIGU75DFFHKK6RS5QQDVF75LB4UESP5LLFN57KNYBI6Y2X3QSI3AP5KRYSMMPUY',
        'username': '13827471947',
        'password': 'qh457110'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'cookie': ''
    }
    url = "https://www.1dadan.com/security/loginMain"

    session = requests.Session()

    cookie_jar = session.post(url, formData).cookies

    cookie = requests.utils.dict_from_cookiejar(cookie_jar)
    cok = cookie['ecs_t']
    return cok

def yddplcx(p):
    url = 'https://www.1dadan.com/api/order/list'
    data = {
        'ordersTimeType': 0,
        'startdate': datetime.datetime.now().strftime('%Y-%m-%d')+' 00:00:00',
        'enddate': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
        'shopId': 'all',
        'tradeStatus': 'all',
        'province': 'all',
        'sellerRemarkOrMarkLevel': 'all',
        'serviceType': 'all',
        'refundStatus': 'all',
        'searchKey': 18,
        'searchValue': p,
        'pageNo': 1,
        'needRefresh': 1,
        'isGroupDisplay': 1,
        'isSingles': 'false',
        'sfPriceMarkupStr': 'all'
    }

    header = {
        'cookie': '_ati=2582860471517; 3AB9D23F7A4B3C9B=G4JHX6KI62LPYHWNR2OPCKX3WIBOIGU75DFFHKK6RS5QQDVF75LB4UESP5LLFN57KNYBI6Y2X3QSI3AP5KRYSMMPUY; fsno=15218833698548; _pati=a2b71ef462b5771fe5d9f95ab9dc42b8; fslb=s1b13; ecs_t=%s' % (
            cok),
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
    r = requests.post(url, data=data, headers=header)
    rj = r.json()

    ifresult1 = rj['data']['page']['totalRecord']
    a = []

    if ifresult1 == 0:
        #print("none")
        a.append("none")
    else:
        result1 = rj['data']['page']['data'][0]['data'][0]['logisticsNo']
        #print(result1)
        a.append(result1)

    b=",".join(a)
    return b





    def readline(self):
        rec = self.inputs.readline()
        if rec:
            string = bytes.decode(rec, encoding)
            if len(string)>2:
                string = string[0:-2]
            else:
                string = ' '
        else:
            string = False
        return string
 
















# a listen thread, listen remote connect
# when a remote machine request to connect, it will create a read thread to handle
class Listener(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("0.0.0.0", port))
        self.sock.listen(0)
    def run(self):
        print("listener started")
        while True:
            client, cltadd = self.sock.accept()
            Reader(client).start()
            cltadd = cltadd
            print("accept a connect")
 
lst  = Listener(6074)   # create a listen thread
lst.start() # then start


#baocdl()
