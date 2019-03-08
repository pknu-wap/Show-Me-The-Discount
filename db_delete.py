import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='wap', charset='utf8')

try:
    with db.cursor() as cursor:
        sql = 'DELETE FROM post WHERE data_id = %d'
        cursor.execute(sql, ('my@test.com',))
    db.commit()
    print(cursor.rowcount)
finally:
    db.close()