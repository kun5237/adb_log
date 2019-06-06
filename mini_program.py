import  requests
import  pprint
import time
###################登陆接口！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
url="https://rcapi.hesiling.com"

new_time = time.strftime('%Y%m%d%H%M%S',time.localtime())  # 定义时间戳变量
socket_token='463b0b64-b87a-e6f1-a56a-5ab6e6defdf7-1557719868755'

hearders_1={
"Content-Type":"application/json",
"socket-token":socket_token
}

# def login(mobile,password):
#     payload={
#     "mobile": "18888888888",
#     "password": "a6332b989b800971072fd4e843343dfd287d6750"
# }

payload={
"mobile": "18888888888",
"password": "a6332b989b800971072fd4e843343dfd287d6750"
}
r_1=requests.post(url+"/api/manage/auth/login",headers=hearders_1,json=payload)
# print(r_1.json())
A=str(r_1.json())


LOG_token=A.split(": ")[1].split('}')[0].split("'")[1]
# print(LOG_token)

for name in r_1.json():
    # name = 'token'
    if name=='token':
        print("登陆测试pass!!!!!!!")
        break
else:
    print("登陆测试fail!!!!!!")


# ###############获取用户的全部资料--------------------------------------
Request_Headers={
"Content-Type":"application/json",
"socket-token":socket_token,
"Authorization":LOG_token
}


#### 获取账号的组织机构
User_org=requests.get(url+"/api/mini/v1/organization",headers=Request_Headers)
zyk_1=User_org.json()
# print(zyk_1['data'][0]['id'])

if zyk_1['data'][0]['id']==0:
    print("获取账号的组织机构pass")
else:
    print("出现错误",User_org[0])

###获取首页banner
Banner=requests.get(url+'/api/mini/v1/banner',headers=Request_Headers)
Banner_json=Banner.json()
# pprint.pprint(Banner.json())
print("首页banner第一条为::",Banner_json['data'][0])


##检查设备WiFi连接情况
param={
    "code": "H28EDE0742C5A"
}
Check_wifi=requests.post(url+"/api/mini/v1/checkWifi",headers=Request_Headers,json=param)
print("设备WiFi状态为::",Check_wifi.json())


#检查所有设备的状态
all_info=requests.get(url+'/api/mini/v1/machine/operating_data',headers=Request_Headers)
# print(all_info.status_code)
if all_info.status_code==200:
    print("检查所有设备的状态pass")
else:
    print("异常状态码为",all_info.status_code)


###搜索门店
Search_Org=requests.get(url+'/api/mini/v1/organization/search?name=1',headers=Request_Headers)
# pprint.pprint(Search_Org.json())
if Search_Org.status_code==200:
    print("搜索门店页面结果pass")
else:
    print("搜索门店页面fail",Search_Org.status_code)

##查看未同步的设备
Notfinish=requests.get(url+'/api/mini/v1/machine/aberrant?organization_id=0&notFinish=true',headers=Request_Headers)
# pprint.pprint(Notfinish.json())
if Notfinish.status_code==200:
    print("未同步的设备接口PASS")
else:
    print("未同步的设备接口有问题，返回的值为：",Notfinish.status_code)