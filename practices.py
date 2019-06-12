import  re

f0= open(r'C:\Users\Lenovo\Desktop\2.txt','r',encoding='utf-8')
target='''D/JzLog   ( 5117): main[presenter.MainPresenter.parseCmd(-1)]:MainPresenter : 执行指令：5\n'''
line = f0.readlines()
for one in line:
    # print(line)
    # print(one)
    if one==target:
        print("pass")
        break

else:
        print("false")
