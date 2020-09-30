import pymysql
class Mysql_do:
    def connect(self,db):
        #db={"ip":"192.168.150.52","port":"3306","name":"future","user":"root","pwd":"123456"}
        ip=db["ip"]
        port=db["port"]
        name=db["name"]
        user=db["user"]
        pwd=db["pwd"]
        try:
            conn=pymysql.connect(host=ip,port=int(port),user=user,password=pwd,charset='utf8',database=name)
            print(f"连接数据库{ip}:{port}成功")
            return conn
        except Exception as e:
            print(f"连接数据库异常，异常信息为{e}")
    def execute(self,conn,sql):
        try:
            cursor=conn.cursor()#获取游标
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            print(f"执行sql语句")
        except Exception as e:
            print(f"执行sql语句异常，异常信息为{e}")
 
    def disconnect(self,conn):
        try:
            conn.close()
        except Exception as e:
            print(f"断开数据库异常")
if __name__ == "__main__":
    db={"ip":"192.168.150.52","port":"3306","name":"apple","user":"root","pwd":"123456"}
    mysql=Mysql_do()
    conn=mysql.connect(db)
    print(conn)
    mysql.execute(conn,"delete from member where Mobilephone='18066668889';")
    mysql.execute(conn,"delete from member where Mobilephone='18066668888';")
