from flask import Flask, render_template, request, redirect, json
import pymysql.cursors

app = Flask(__name__)

db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     password = '123',
                     db = 'wap',
                     charset = 'utf8')

data_id = 0
reply_id = 0

@app.route('/')
@app.route('/boardList.html')
def list():
    #db 데이터 읽기

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
    finally:
        db.close()

    data_list = [{"store": "상호명", "product": "상품", "content": "내용", "price": "가격", "start": "시작", "end": "종료"}, {"store": "상호명", "product": "상품", "content": "내용", "price": "가격", "start": "시작", "end": "종료"}]

    return render_template('boardList.html', data1 = data_list)

@app.route('/boardList.html?searchType=<search_type>&searchText=<search_text>')
def search():
    #db 데이터 검색 {searchType: searchText}

    return render_template('boardList.html', ) #data_list

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

    #db 데이터 삽입

    return redirect('/boardView.html/'+str(data_id))

@app.route('/boardView.html/<int:data_id>')
def view(data_id):

    #db 데이터 읽기

    return render_template('boardView.html', ) #json

@app.route('/boardModifyForm.html')
def modify_form():
    #db 데이터 읽기
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

    #db 데이터 읽기(id)
    #json password 일치 여부 확인
        #db 데이터 수정(id, password 그대로)

    return redirect('/boardView.html/'+str(data_id))

@app.route('/delete1', methods=['POST']) # 글 삭제
def delete1():

    #db 데이터 읽기
    #json password 일치 여부 확인

        #db 데이터 삭제

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

    #db 데이터 삽입

    return redirect('/boardView.html/'+str(data_id))

@app.route('/delete2') # 댓글 삭제
def delete2():
    data_id = request.form["data_id"]
    reply_id = request.form["reply_id"]
    reply_password = request.form["reply_password"]

    x = {"data_id": data_id, "reply_id": reply_id, "reply_password": reply_password}
    y = json.dumps(x, ensure_ascii=False)

    #db 데이터 읽기
    #json 데이터 일치 여부 확인
        #db 데이터 삭제

    return redirect('/boardView.html/'+str(data_id))

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=80)
