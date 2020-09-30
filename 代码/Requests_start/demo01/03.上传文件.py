'''
个人中心——上传头像
'''



# url="http://www.httpbin.org/post"
# file_path="C:\Users\Administrator\PycharmProjects\xnggd\xiaoniao\bg.png"
# with open(file_path,mode="rb") as f:
#     #二元组："name":file_tuple ("file")
#     file={"bg.png":(file_path,f)}
#     #三元组：
#     # file={"bg.png":(file_path,f,"image/png")}
#     r=requests.post(url,files=file)
#     print(r.text)


# 上传多个文件
import requests
url="http://www.httpbin.org/post"
file_path1=r"F:\test.png"
file_path2=r"F:\test.txt"
with open(file_path1,mode='rb') as f1:
    with open(file_path2,mode='r',encoding='UTF-8') as f2:
        files={"test.png":(file_path1,f1,"image/png"),
                "test.txt":(file_path2,f2,"text/plain")}
        r=requests.post(url,files=files)
        print(r.text)

#
# file_path2=r"C:\Users\Administrator\PycharmProjects\xnggd\xiaoniao\bg.png"
# with open(file_path2,mode='rb') as f2:
#     r=requests.post(url,data=f2)
#     print(r.text)


