import pymysql
from datetime import datetime
db = pymysql.connect(host = 'localhost',
                     user = 'wap',
                     password = '123',
                     db = 'wap',
                     charset = 'utf8'
                     )
                     
def dbInit():
    with db.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS wap;")
    db.commit();
    with db.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS post(post_id INT PRIMARY KEY AUTO_INCREMENT,store VARCHAR(10) NOT NULL,product VARCHAR(10) NOT NULL,content VARCHAR(400) NOT NULL,price INT NOT NULL,start_date VARCHAR(10) NULL,end_date VARCHAR(10) NOT NULL,password VARCHAR(32) NOT NULL);")
    db.commit()
    with db.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS replies(reply_id INT PRIMARY KEY AUTO_INCREMENT,post_id INT,reply VARCHAR(400) NOT NULL,add_time DATETIME NOT NULL,password VARCHAR(32) NOT NULL);")
    db.commit()

def dbClose():
    db.close()

def dbSearch(query):
    if len(query)==0 :
        with db.cursor() as cursor:
            sql = 'SELECT * FROM post ORDER BY end_date LIMIT 20'
            cursor.execute(sql)
        return cursor.fetchall()
    else :
        with db.cursor() as cursor:
            sql = 'SELECT * FROM post WHERE product == %s OR store == %s'
            cursor.execute(sql,[query,query])
        return cursor.fetchall()
        
def dbNewPost(Store,Product,Content,Price,Start_Date,End_date,Password):
    with db.cursor() as cursor:
        sql = "INSERT INTO post (store, product, content, price, start_date, end_date, password) VALUES (%s,%s,%s,%s,%s,%s,password(%s))"
        cursor.execute(sql,[Store,Product,Content,Price,Start_Date,End_date,Password])
    db.commit()
    with db.cursor() as cursor:
        sql="SELECT LAST_INSERT_ID();"
        cursor.execute(sql)
    return cursor.fetchall()

def dbUpdatePost(post_id,Store,Product,Content,Price,Start_Date,End_date,Password):
    with db.cursor() as cursor:
        sql="UPDATE post SET store=%s,product=%s,content=%s,price=%s,start_date=%s,end_date=%s WHERE post_id=%s AND password(%s)"
        cursor.execute(sql,[Store,Product,Content,Price,Start_Date,End_date,post_id,Password])
    db.commit()
    return True

def dbRemovePost(post_id,Password):
    with db.cursor() as cursor:
        sql="DELETE FROM post WHERE post_id = %s AND password = password(%s)"
        cursor.execute(sql,[post_id,Password])
    db.commit()
    return True

def dbGetPost(post_id):
    data=dict()
    with db.cursor() as cursor:
        sql="SELECT * FROM post WHERE post_id=%s"
        cursor.execute(sql,post_id)
        post=cursor.fetchall()
    with db.cursor() as cursor:
        sql="SELECT * FROM replies where post_id=%s ORDER BY add_time"
        cursor.execute(sql,[post_id])
        replies=cursor.fetchall()
    data["post"]=post
    data["replies"]=replies
    return data

def dbNewReply(post_id,reply,Password):
    with db.cursor() as cursor:
        sql = "INSERT INTO replies (post_id,Reply,add_time, password) VALUES (%s,%s,%s,password(%s))"
        cursor.execute(sql,[post_id,reply,datetime.now(),Password])
    db.commit()
    with db.cursor() as cursor:
        sql="SELECT LAST_INSERT_ID();"
        cursor.execute(sql)
    return cursor.fetchall()

def dbRemoveReply(replyId,Password):
    with db.cursor() as cursor:
        sql = "DELETE FROM replies WHERE reply_id = %s AND password=password(%s)"
        cursor.execute(sql,[replyId,Password])
    db.commit()
    return True
    


if __name__=="__main__":
    dbInit()
    print(dbSearch(""))
    postId=dbNewPost("GS25", "딸기우유","2+1","1300원","2019-01-01","2019-02-01","1234")
    print(postId)
    print(dbUpdatePost(postId,"GS25", "딸기우유","2+1","1300원","2019-01-01","2019-02-01","1234"))
    print(dbRemovePost(postId,"1234"))
    dbGetPost(postId)
    replyId=dbNewReply(postId,"댓글","1234")
    dbRemoveReply(replyId,"1234")
    dbClose()