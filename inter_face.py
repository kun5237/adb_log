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
# print(type(hearders_2['Authorization']))
r_2=requests.get(url+"/api/manage/v1/profile",
                 headers=hearders_2)
#pprint.pprint(r_2.json())
A=r_2.json()
# B=A.text.split("{}")

if  A["data"]["hb_num"]==2:
    print("获取用户的资料接口PASS")
else:
    print('''返回的正确码为：''',A["data"]["hb_num"])



#--------------设备面板数据测试
r_3=requests.get(url+'/api/manage/v1/machine/operating_data',headers=hearders_2)
# pprint.pprint(r_3.json())
r_panduan=r_3.json()
if r_panduan['data']['comingSoonNum']==0:
    print("页面展示面板显示正常")
else:
    print('''正确的输入数据为''',r_panduan['data']['comingSoonNum'])

#==============获取组织机构列表===========
r_4=requests.get(url+'/api/manage/v1/organization',headers=hearders_2)
# pprint.pprint(r_4.json())
rr=r_4.json()
# r_4.text
if rr['data'][0]['id']==0:
    print("获取组织机构列表PASS")
else:
    print("this is require")

######写入txt文件
# file_text=r'C:\Users\言真信息\Desktop\1.txt'
# fo=open(file_text,'w')
# fo.write(r_4.text)

#-----------------------获取H5内容管理
r_5=requests.get(url+'/api/manage/v1/content?page=1&size=20&kind=1&type=1&folder_id=0',headers=hearders_2)
pprint.pprint(r_5.json())
# r_5_rtn=r_5.json()
# if  r_5_rtn['data'][0]['g_first_name']==0:
#     print("获取H5内容管理PASS")
# else:
#     print("测试不通过")

#------------------------发布时，获取短信验证码
get_code=requests.post(url+'/api/manage/v1/safe/sendMsg',headers=hearders_2)
# pprint.pprint(get_code.json())
check_msg=get_code.json()

try:
    if  check_msg['msg']=='短信发送成功':
        print("短信发送成功")

except KeyError as results:
    print("短信发送失败，请检查是否连续点击发送短信，捕获到一个异常",results)


all_getjie={
    "device_code": "H18BB265BB2EB",
	"status": 1
}
###
def A():
    r_6=requests.post(url+'/api/app/v3/update_machine_status',headers=hearders_2,json=all_getjie)
    print(r_6.json())

# a=0
# opopop=10
# while a<opopop:
#     A()
#     a+=1
#     if a>10:
#         break
#
# print(a)

#==============================清除全部组织机构
r_6=requests.delete(url+'/api/manage/v1/organization/all',headers=hearders_2)
panduan=r_6.json()
if panduan['error']=='请先解绑设备':
    print('清除组织机构pass')
else:
    print("此接口错误，请检查，此接口提示信息为：：",panduan['error'])

#*******************************创建设备分组
fenzu={
"name": new_time,
"parent_id": "0"

}
r_7=requests.post(url+'/api/manage/v1/group',headers=hearders_2,json=fenzu)
r_7_panduan=r_7.json()
if r_7_panduan['msg']=='创建成功':
    print("创建设备分组PASS")
else:
    print("设备分组创建出现错误,提示信息为：：：",r_7_panduan['msg'])


#**************************创建标签
Tag={
    'name':new_time
}
NewTag=requests.post(url+'/api/manage/v1/tag',headers=hearders_2,json=Tag)
pprint.pprint(NewTag.json())

#**************************获取标签列表
GetTag=requests.get(url+"/api/manage/v1/tag",headers=hearders_2)
# pprint.pprint(GetTag.json())
ZY=GetTag.json()
ChooseTag=ZY['data'][-1]['id']
print(ZY['data'][-1]['id'])

#**************************删除刚刚创建的标签
DelTag=requests.delete(url+"/api/manage/v1/tag"+'/'+ChooseTag,headers=hearders_2)
pprint.pprint(DelTag.json())


#************************新建组织机构
EstOrg={
    'name': 'handsome_kun'+new_time,
    'parent_id': '0',
    # 'mobile': '13333333333'

}
EstablishOrg=requests.post(url+'/api/manage/v1/organization',headers=hearders_2,json=EstOrg)
pprint.pprint(EstablishOrg.json())

#********************获取组织机构列表
GetOrg=requests.get(url+'/api/manage/v1/organization',headers=hearders_2)
# pprint.pprint(GetOrg.json())
ZZZ=GetOrg.json()
ThisOrg=ZZZ['data'][0]['children'][-1]['id']
print(ThisOrg)


#******删除创建的组织机构
DelOrg=requests.delete(url+'/api/manage/v1/organization/'+ThisOrg,headers=hearders_2)
pprint.pprint(DelOrg.json())



