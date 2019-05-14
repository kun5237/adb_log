# s="adadsadad"
# for letter in s:
#     print("当前是：",letter)
#
# dict = {'a': 1, 'b': 2, 'b': '3'}
# print(dict['b'])
# # '3'
# # dict
# # {'a': 1, 'b': '3'}

import  requests
import  pprint
import time
###################登陆接口！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
url="https://rcapi.hesiling.com"

new_time = time.strftime('%Y%m%d%H%M%S',time.localtime())  # 定义时间戳变量
socket_token='7b00c9fa-6593-669a-0aea-c428e3f3b919-1553755542934'

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

for name in r_1.json():
    # name = 'token'
    if name=='token':
        print("登陆测试pass!!!!!!!")
        break
else:
    print("登陆测试fail!!!!!!")


# ###############获取用户的全部资料--------------------------------------
hearders_2={
"Content-Type":"application/json",
"socket-token":socket_token,
"Authorization":LOG_token
}




# EstOrg={
#     'name': 'handsome_kun',
#     'parent_id': '0',
#     # 'mobile': '13333333333'
#
# }
# EstablishOrg=requests.post(url+'/api/manage/v1/organization',headers=hearders_2,json=EstOrg)
# # pprint.pprint(EstablishOrg.json())

#********************获取组织机构列表
GetOrg=requests.get(url+'/api/manage/v1/organization',headers=hearders_2)
# pprint.pprint(GetOrg.json())
ZZZ=GetOrg.json()
ThisOrg=ZZZ['data'][0]['children'][-1]['id']
print(ThisOrg)


#******删除创建的组织机构
DelOrg=requests.delete(url+'/api/manage/v1/organization/'+ThisOrg,headers=hearders_2)
pprint.pprint(DelOrg.json())
