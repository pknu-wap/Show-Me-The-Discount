import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='wap', charset='utf8')

try:
    with db.cursor() as cursor:
        sql = 'SELECT store, products, content, startdate, enddate FROM post WHERE id = 1234'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

    with db.cursor() as cursor:
        sql = 'SELECT reply_id, replyContent, replyTime FROM replies WHERE data_id = 1234'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    db.close()