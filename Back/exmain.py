from flask import Flask, render_template, request, redirect, json
import pymysql

class Maria:
    def __init__(self):
        self.user = input('Insert username :')
        self.password = getpass('Insert password :')
        self.connect = pymysql.connect(host = 'localhost',
                                  port = 3306,
                                  user = self.wap,
                                  password = self.password,
                                  db = 'wap',
                                  charset = 'utf8mb4')
        self.sql = sql()

    def excute(sql):
        cursor = self.connect.cursor()
        cursor.excute(sql)
        self.connect.commit()

    def s_excute(sql):
        cursor = self.connect.cursor()
        cursor.excute(sql)
        return cursor.fetchall()

    def search(data):
        self.excute(self.sql.search(data))


app = Flask(__name__)

data_id = 0
reply_id = 0

@app.route('/')
@app.route('/boardList.html')

#def aaa:
 #   maria.search(request.data())

def list():
    with db.cursor() as cursor:
        sql = '''
            CREATE TABLE post(
                Data_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                Store VARCHAR(10) NOT NULL,
                Product VARCHAR(10) NOT NULL,
                Content VARCHAR(20) NOT NULL,
                Price INT NOT NULL,
                Start_Date VARCHAR(10) NULL,
                End_Date VARCHAR(10) NOT NULL,
                Password INT NOT NULL,
                PRIMARY KEY(Data_id),
                );'''

            #CREATE TABLE replies(
             #   Reply_Id INT PRIMARY KEY,
              #  Reply VARCHAR(20) IS NOT NULL.
               # Num INT IS NOT NULL
                #);
    class sql:
        def sql_search(data):
            return f'SELECT * FROM post WHERE Product == {data['product']} OR Store == {data['store']}'

        def sql_search_re(data):
            return f'SELECT * FROM replies WHERE Reply_Id == {data['reply_id']}'

        cursor.execute(sql)  # 실행하기
    db.commit()  # DB에 Complete
    #finally:
        #db.close()  # DB 연결 닫기
    #db show 함수

    #'''try:
     #   with db.cursor() as cursor:
      #      sql = 'SHOW CREATE TABLE post
       #     cursor.execute(sql)
        #db.commit()
        #print(cursor.rowcount)
    #finally:
     #   db.close()'''



    #data_list = [{"store": "상호명", "product": "상품", "content": "내용", "price": "가격", "start": "시작", "end": "종료"}, {"store": "상호명", "product": "상품", "content": "내용", "price": "가격", "start": "시작", "end": "종료"}]

    return render_template('boardList.html')

@app.route('/boardList.html?searchType=<search_type>&searchText=<search_text>')
def search():
    #db 리스트에서 검색 {search_type(키): search_text(값)} 일치하면 가져오기
    try:
        with db.cursor() as cursor:
            sql = 'SELECT * FROM post WHERE Product == product OR Store == store'  #보류
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

    finally:
        db.close()

    return render_template('boardList.html') #data_list


@app.route('/boardWriteForm.html')
def write_form():
    return render_template('boardWriteForm.html')

@app.route('/write', methods=['POST'])
def register():
    if request.method == 'POST':
        global data_id
        data_id += 1
        store = request.form["store"]
        product = request.form["product"]
        content = request.form["content"]
        price = request.form["price"]
        startdate = request.form["start"]
        enddate = request.form["end"]
        password = request.form["password"]

        x = {"data_id": data_id, "store": store, "product": product, "content": content, "price": price, "startdate": startdate, "enddate": enddate, "password": password}
        y = json.dumps(x, ensure_ascii=False)
        try:
            with db.cursor() as cursor:
                sql = f"INSERT INTO post (Data_id, Store, Product, Content, Price, Start_Date, End_Date, Password) VALUES ({data_id}, store, product, content, price, start, end, password)"
                cursor.execute(sql)
                db.commit()

        with db.cursor() as cursor:
            sql = 'INSERT INTO replies (Reply_id, Num, Reply) VALUES (reply_id, num, reply)'
            cursor.execute(sql)
            db.commit()
            print(cursor.lastrowid)
    finally:
        db.close()

    return redirect('/boardView.html/'+str(data_id))

@app.route('/boardView.html/<int:data_id>')
def view(data_id):

    try:
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
    finally:
        db.close()

    return render_template('boardView.html', ) #json

@app.route('/boardModifyForm.html/<data_id>')
def modify_form():
    try:
        with db.cursor() as cursor:
            sql = 'SELECT * FROM post WHERE Data_Id = data_id ORDER BY End LIMIT 20'
            cursor.execute(sql)
            datas = cursor.fetchall()
            for data in datas:
                print(data)

        with db.cursor() as cursor:
            sql = 'SELECT * FROM replies WHERE Reply_Id = data_id ORDER BY End LIMIT 20'
            cursor.execute(sql)
            datas = cursor.fetchall()
            for data in datas:
                print(data)
    finally:
        db.close()

    return render_template('boardModifyForm.html')

@app.route('/modify')
def modify():
    if request.method == 'POST':
        data_id = request.form["id"]
        store = request.form["store"]
        product = request.form["product"]
        content = request.form["content"]
        price = request.form["price"]
        startdate = request.form["start"]
        enddate = request.form["end"]
        password = request.form["password"]

        x = {"data_id": data_id, "store": store, "product": product, "content": content, "price": price, "startdate": startdate, "enddate": enddate, "password": password}
        y = json.dumps(x, ensure_ascii=False)

        #db 데이터 수정(id, password 그대로)
        try:
            with db.cursor() as cursor:
                sql = 'UPDATE post set Data_Id = data_id WHERE Data_id = data_id AND password = password(password)'
                cursor.execute(sql)
            db.commit()
            print(cursor.rowcount)
        finally:
            db.close()

    return redirect('/boardView.html/'+str(data_id))

@app.route('/delete1', methods=['POST']) # 글 삭제
def delete1():
    data_id = request.form["id"]
    password = request.form["password"]

    try:
        with db.cursor() as cursor:
            sql = 'DELETE FROM post WHERE Data_id = data_id AND password = password(password)'
            cursor.execute(sql)
        db.commit()
        print(cursor.rowcount)
    finally:
        db.close()

    return render_template('boardList.html')

@app.route('/reply', methods=['POST'])
def reply():
    global reply_id
    reply_id += 1
    data_id = request.form["data_id"]
    reply = request.form["reply"]
    reply_password = request.form["password"]

    x = {"reply_id": reply_id, "data_id": data_id, "reply": reply, "reply_password": reply_password}
    y = json.dumps(x, ensure_ascii=False)

    #db 데이터 읽기(보류)

    return redirect('/boardView.html/'+str(data_id))

@app.route('/delete2') # 댓글 삭제
def delete2():
    data_id = request.form["data_id"]
    reply_id = request.form["reply_id"]
    reply_password = request.form["reply_password"]

    x = {"data_id": data_id, "reply_id": reply_id, "reply_password": reply_password}
    y = json.dumps(x, ensure_ascii=False)

    #db 데이터 읽기(보류)
    #json 데이터 일치 여부 확인
        #db 데이터 삭제

    return redirect('/boardView.html/'+str(data_id))

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=80)
