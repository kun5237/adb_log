
import  requests
import  pprint
import time
###################登陆接口！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
url="https://api.hesiling.com"

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



#***********************创建组织机构
# EstOrg={
#     "name": new_time,
#     "parent_id": "0"
#
# }
# EstablishOrg=requests.post(url+'/api/manage/v1/organization',headers=Request_Headers,json=EstOrg)
# pprint.pprint(EstablishOrg.json())

#********************获取组织机构列表
GetOrg=requests.get(url+'/api/manage/v1/organization',headers=Request_Headers)
# pprint.pprint(GetOrg.json())
ZZZ=GetOrg.json()
ThisOrg=ZZZ['data'][0]['children'][-1]['id']
print(ThisOrg)

#********************删除创建的组织机构
DelOrg=requests.delete(url+'/api/manage/v1/organization/'+ThisOrg,headers=Request_Headers)
pprint.pprint(DelOrg.json())


#*******************删除所有的组织机构
allOrg_del=requests.delete(url+'/api/manage/v1/organization/all',headers=Request_Headers)
# print(LOG_token)
pprint.pprint(allOrg_del.json())


