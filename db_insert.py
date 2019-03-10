import pymysql

#db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='wap', charset='utf8')
db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     password = '123',
                     db = 'wap',
                     charest = 'utf8mb4',
                     cursorclass = pymysql.cursors.DictCursor)
app = Flask(__name__)

@app.route("/get-reg")
def login():
    return render_template('reg.html')

@app.route('/save-post', methods = ['POST', 'GET'])
def signUp():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

print("INSERT, SELECT, UPDATE, DELETE")
value = input("select option : ")

def func(value):
    if value == 'INSERT':
        try:
            with db.cursor() as cursor:
                sql = """INSERT INTO post (Data_id, store, product, content, price, startdate, enddate, password)
                        VALUES (%d, %s, %s, %s, %d, %s, %s, %d)"""
                cursor.execute(sql)
                db.commit()

            with db.cursor() as cursor:
                sql = 'INSERT INTO replies (reply_id, num, reply) VALUES (%d, %d, %s)'
                cursor.execute(sql)
                db.commit()
                print(cursor.lastrowid)

    elif value == 'SELECT':
        with db.cursor() as cursor:
            sql = 'SELECT * FROM post WHERE Data_Id = data_id'
            cursor.execute(sql)
            datas = cursor.fetchall()
                for data in datas:
                    print(data)

        with db.cursor() as cursor:
            sql = 'SELECT * FROM replies WHERE Reply_Id = data_id'
            cursor.execute(sql)
            datas = cursor.fetchall()
                for data in datas:
                    print(data)

    elif value == 'update':
        with db.cursor() as cursor:
            sql = 'UPDATE post set Data_Id = data_id WHERE data_id = %d' %
            cursor.execute(sql)
        db.commit()
        print(cursor.rowcount)

    elif value == 'delete':
        with db.cursor() as cursor:
            sql = 'DELETE FROM post WHERE Data_id = data_id'
            cursor.execute(sql)
        db.commit()
        print(cursor.rowcount)

        finally:
            db.close()

if __name__ == "__main__":
    app.run()

