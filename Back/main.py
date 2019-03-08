from flask import Flask, render_template, request, redirect, json

app = Flask(__name__)

data_id = 0
reply_id = 0

@app.route('/')
@app.route('/boardList.html')
def list():
    #db 데이터 읽기
    data = {"store": "상호명", "product": "상품", "content": "내용", "price": "가격", "start": "행사 시작", "end": "행사 종료"}

    data1 = json.dumps(data, ensure_ascii=False).encode('utf8')

    return render_template('boardList.html', data1 = data1) #json

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
        y = json.dumps(x)

    #db 데이터 삽입

    return redirect('/boardView.html/'+str(data_id))

@app.route('/boardView.html/<int:data_id>')
def view(data_id):

    #db 데이터 읽기

    return render_template('boardView.html') #json

@app.route('/boardModifyForm.html')
def modify_form():
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
        y = json.dumps(x)

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
    y = json.dumps(x)

    #db 데이터 삽입

    return redirect('/boardView.html/'+str(data_id))

@app.route('/delete2') # 댓글 삭제
def delete2():
    data_id = request.form["data_id"]
    reply_id = request.form["reply_id"]
    reply_password = request.form["reply_password"]

    x = {"data_id": data_id, "reply_id": reply_id, "reply_password": reply_password}
    y = json.dumps(x)

    #db 데이터 읽기
    #json 데이터 일치 여부 확인
        #db 데이터 삭제

    return redirect('/boardView.html/'+str(data_id))

if __name__ == '__main__':
    app.run(debug = True)
