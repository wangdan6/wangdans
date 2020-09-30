from jinrongzonghe.caw.mysql_do import Mysql_do
class DbOp:
    def delete_user(self,db,mobilephone):
        
        mysql=Mysql_do()
        conn=mysql.connect(db)
        print(conn)
        mysql.execute(conn,f"delete from member where Mobilephone={mobilephone};")
        mysql.disconnect(db)