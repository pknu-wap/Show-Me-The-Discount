import pymysql

db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     password = '123',
                     db = 'wap',
                     charest = 'utf8mb4'
                     cursorclass=pymysql.cursors.DictCursor
                     )
                     
def dbInit():
    with db.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS wap;")
    db.commit();
    with db.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS post(Data_id INT UNSIGNED NOT NULL AUTO_INCREMENT,Store VARCHAR(10) NOT NULL,Product VARCHAR(10) NOT NULL,Content VARCHAR(400) NOT NULL,Price INT NOT NULL,Start_Date VARCHAR(10) NULL,End_Date VARCHAR(10) NOT NULL,Password VARCHAR(32) NOT NULL,PRIMARY KEY(Data_id),);")
    db.commit()
    with db.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS replies(Reply_Id INT PRIMARY KEY,Data_Id INT,Reply VARCHAR(20) IS NOT NULL,addTime DATETIME IS NOT NULL,password VARCHAR(32) NOT NULL);")
    db.commit()

def dbClose():
    db.close()

def dbSearch(query):
    if len(query)==0 :
        with db.cursor() as cursor:
            sql = 'SELECT * FROM post ORDER BY End LIMIT 20'
            cursor.execute(sql)
        return cursor.fetchall()
    else :
        with db.cursor() as cursor:
            sql = 'SELECT * FROM post WHERE Product == %s OR Store == %s'
            cursor.execute(sql,[query,query])
        return cursor.fetchall()
        
def dbNewPost(Store,Product,Content,Price,Start_Date,End_date,Password):
    with db.cursor() as cursor:
        sql = "INSERT INTO post (Store, Product, Content, Price, Start_Date, End_Date, Password) VALUES (%s,%s,%s,%s,%s,%s,password(%s))"
        cursor.excute(sql,[Store,Product,Content,Price,Start_Date,End_date,Password])
    db.commit()
    with db.cursor() as cursor:
        sql="SELECT LAST_INSERT_ID();"
        cursor.execute(sql)
    return cursor.fetchall()

def dbUpdatePost(post_id,Store,Product,Content,Price,Start_Date,End_date,Password):
    with db.cursor() as cursor:
        sql="UPDATE post SET Store=%s,Product=%s,Content=%s,Price=%s,Start_Date=%s,End_Date=%s WHERE Post_id=%s AND password(%s)"
        cursor.execute(sql,[Store,Product,Content,Price,Start_Date,End_date,post_id,Password])
    db.commit()
    return True

def dbRemovePost(post_id,Password):
    with db.cursor() as cursor:
        sql="DELETE FROM post WHERE Data_id = %s AND password = password(%s)"
        cursor.execute(sql,[post_id,Password])
    db.commit()
    return True

def dbGetPost(post_id):
    with db.cursor() as cursor:
        sql="SELECT * FROM post WHERE Data_Id=%s"
        cursor.execute(sql,post_id)
        post=cursor.fetchall()
    with db.cursor() as cursor:
        sql="SELECT * FROM replies where Data_Id=%s ORDER BY NUM"
        cursor.execute(sql,[post_id])
        replies=cursor.fetchall()
    data["post"]=post
    data["replies"]=replies
    return data

def dbNewReply(Data_id,reply,addTime,Password):
    with db.cursor() as cursor:
        sql = "INSERT INTO replies (Data_Id,Reply,addTime, pssword) VALUES (%s,%s,%s,password(%s))"
        cursor.excute(sql,[Data_id,reply,addTime,Password])
    db.commit()
    with db.cursor() as cursor:
        sql="SELECT LAST_INSERT_ID();"
        cursor.execute(sql)
    return cursor.fetchall()

def dbRemoveReply(replyId,Password):
    with db.cursor() as cursor:
        sql = "DELETE FROM replies WHERE replyId = %s AND password=password(%s)"
        cursor.execute(sql,[replyId,Password])
    db.commit()
    return True
    


if __name__=="__main__":
    dbInit()
    print(dbSearch())
    postId=dbNewPost("GS25", "딸기우유","2+1","1300원","2019-01-01","2019-02-01","1234")
    print(postId)
    print(dbUpdatePost(postId,"GS25", "딸기우유","2+1","1300원","2019-01-01","2019-02-01","1234"))
    print(dbRemovePost(postId,"1234"))
    dbGetPost(postId)
    replyId=dbNewReply(postId,"댓글","2019-03-12 16:43:20","1234")
    dbRemoveReply(replyId,"1234")
    dbClose()