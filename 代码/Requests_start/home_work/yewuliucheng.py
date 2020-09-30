import requests
#1.用例1，投资人，reg注册
url="http://192.168.150.222:8081/futureloan/mvc/api/member/loginreg"
account={"mobilephone":"18089269982","pwd":"123456"}
r=requests.post(url,data=account)
assert r.status_code=="10001"
print(r.text)
#2.用例2，借款人
url="http://192.168.150.222:8081/futureloan/mvc/api/member/loginreg"
account={"mobilephone":"18089269981","pwd":"123456"}
r=requests.post(url,data=account)
assert r.status_code=="10001"
print(r.text)
#3.获取用户列表
url="http://192.168.150.222:8081/futureloan/mvc/api/member/list"
r=requests.post(url)
assert r.status_code=="10001"
print(r.text)
#4.投资人登陆
url="http://192.168.150.222:8081/futureloan/mvc/api/member/login"
account={"mobilephone":"18089269982","pwd":"123456"}
r=requests.post(url,data=account)
assert r.status_code=="10001"
print(r.text)
#5.借款人登陆
url="http://192.168.150.222:8081/futureloan/mvc/api/member/login"
account={"mobilephone":"18089269981","pwd":"123456"}
r=requests.post(url,data=account)
assert r.status_code=="10001"
print(r.text)
#6.投资人充值
url="http://192.168.150.222:8081/futureloan/mvc/api/member/recharge"
chongzhi={"mobilephone":"18089269982","amount":"10000"}
r=requests.post(url,data=chongzhi)
assert r.status_code=="10001"
print(r.text)
#7.借款人新增项目
url="http://192.168.150.222:8081/futureloan/mvc/api/loan/add"
xinzeng={"membeiId":123,"title":"demo","amount":500,"loanRate":18,"loanTerm":6,"loanDateType":0,"repaymemtWay":1,"biddingDays":5}
r=requests.post(url,data=xinzeng)
assert r.status_code=="10001"
#8.获取标列表
url="http://192.168.150.222:8081/futureloan/mvc/api/loan/getLoanList"

r=requests.post(url)
assert r.status_code=="10001"
print(r.text)
#9.平台人员审核1-运营人员审核（初审）
url="http://192.168.150.222:8081/futureloan/mvc/api/loan/audit"
shenhejieduan={"id":1,"status":2}
r=requests.post(url,data=shenhejieduan)
assert r.status_code=="10001"
print(r.text)
#10.平台人员审核2-运营主管审核（复审）
url="http://192.168.150.222:8081/futureloan/mvc/api/loan/audit"
shenhejieduan={"id":1,"status":3}
r=requests.post(url,data=shenhejieduan)
assert r.status_code=="10001"
print(r.text)
#11.运营总监审核（投标中状态）
url="http://192.168.150.222:8081/futureloan/mvc/api/loan/audit"
shenhejieduan={"id":1,"status":4}
r=requests.post(url,data=shenhejieduan)
assert r.status_code=="10001"
print(r.text)
#12.投资满标
url="http://192.168.150.222:8081/futureloan/mvc/api/loan/audit"
touzi={"memberId":1,"password":"1234567","loanId":123,"amount":500}
r=requests.post(url,data=touzi)
assert r.status_code=="10001"
#13.获取投资记录
url="http://192.168.150.222:8081/futureloan/mvc/api/invest/getInvestsByMemberId"
touziren={"memberId":1}
r=requests.post(url,data=touziren)
assert r.status_code=="10001"
#14.获取标的投资记录
url="http://192.168.150.222:8081/futureloan/mvc/api/invest/getInvestsByLoanId"
biaotouzi={"loanId":1}
r=requests.post(url,data=biaotouzi)
assert r.status_code=="10001"
#15.生成借款人回款计划
url="http://192.168.150.222:8081/futureloan/mvc/api/loan/generateRepayments"
para={"id":1}
r=requests.get(url,params=para)
assert r.status_code=="10001"



