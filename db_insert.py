import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='wap', charset='utf8')

print("INSERT : 입력, SELECT : 검색, UPDATE : 변경, DELETE : 삭제 ")
value = input("옵션을 선택하시오: ")

def func(value):
    if value == 'INSERT':
        try:
            with db.cursor() as cursor:
                sql = 'INSERT INTO post (data_id, store, product, content, price, startdate, enddate, password)' \
                      ' VALUES (%d, %s, %s, %s, %d, %s, %s, %d)'
                cursor.execute(sql, data)
                db.commit()

            with db.cursor() as cursor:
                sql = 'INSERT INTO replies (reply_id, num, reply) VALUES (%d, %d, %s)'
                cursor.execute(sql, )
                db.commit()
                print(cursor.lastrowid)

    elif value == 'SELECT':
        with db.cursor() as cursor:
            sql = 'SELECT store, products, content, startdate, enddate FROM post WHERE data_id = 1234'
            cursor.execute(sql)
            datas = cursor.fetchall()
                for data in datas:
                    print(data)

        with db.cursor() as cursor:
            sql = 'SELECT reply_id, replyContent, replyTime FROM replies WHERE data_id = 1234'
            cursor.execute(sql)
            datas = cursor.fetchall()
                for data in datas:
                    print(data)

    elif value == 'update':
        with db.cursor() as cursor:
            sql = 'UPDATE post SET  = %s WHERE data_id = %d'
            cursor.execute(sql, ('wap', '123'))
        db.commit()
        print(cursor.rowcount)

    elif value == 'delete':
        with db.cursor() as cursor:
            sql = 'DELETE FROM post WHERE data_id = %d'
            cursor.execute(sql, ('wap','123'))
        db.commit()
        print(cursor.rowcount)

        finally:
            db.close()



