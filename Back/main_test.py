from flask import Flask, render_template, request, redirect, json, url_for

app = Flask(__name__)

data_id = 0
reply_id = 0

@app.route('/')
@app.route('/boardList.html')
def list():

    data_list = [{"data_id": 1, "store" : "GS25", "product" : "딸기우유",  "content" : "2+1", "price" :"1300", "start" : "2019-01-01", "end" : "2019-02-01"},
                {"data_id": 2, "store" : "CU", "product" : "신라면컵",  "content" : "2+1", "price" :"1000", "start" : "2019-01-01", "end" : "2019-02-01"},
                {"data_id": 3, "store" : "올리브영", "product" : "올리브",  "content" : "1+1", "price" :"30000", "start" : "2019-01-01", "end" : "2020-02-01"},
                {"data_id": 4, "store" : "GS25", "product" : "초코우유",  "content" : "1+1", "price" :"1500", "start" : "2019-01-01", "end" : "2019-02-01"},
                {"data_id": 5, "store" : "GS25", "product" : "딸기우유",  "content" : "2+1", "price" :"1300", "start" : "2019-01-01", "end" : "2019-02-01"},
                {"data_id": 6, "store" : "CU", "product" : "신라면컵",  "content" : "2+1", "price" :"1000", "start" : "2019-01-01", "end" : "2019-02-01"},
                {"data_id": 7, "store" : "올리브영", "product" : "올리브",  "content" : "1+1", "price" :"30000", "start" : "2019-01-01", "end" : "2020-02-01"},
                {"data_id": 8, "store" : "GS25", "product" : "초코우유",  "content" : "1+1", "price" :"1500", "start" : "2019-01-01", "end" : "2019-02-01"},
                {"data_id": 9, "store" : "GS25", "product" : "딸기우유",  "content" : "2+1", "price" :"1300", "start" : "2019-01-01", "end" : "2019-02-01"},
                {"data_id": 10, "store" : "CU", "product" : "신라면컵",  "content" : "2+1", "price" :"1000", "start" : "2019-01-01", "end" : "2019-02-01"},
                {"data_id": 11, "store" : "올리브영", "product" : "올리브",  "content" : "1+1", "price" :"30000", "start" : "2019-01-01", "end" : "2020-02-01"},
                {"data_id": 12, "store" : "GS25", "product" : "초코우유",  "content" : "1+1", "price" :"1500", "start" : "2019-01-01", "end" : "2019-02-01"}
                ]

    return render_template('boardList.html', data1 = data_list)

@app.route('/boardList.html?searchType=<search_type>&searchText=<search_text>')
def search():

    #db 리스트에서 검색 {search_type(키): search_text(값)} 일치하면 가져오기

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
        start = request.form["start"]
        end = request.form["end"]
        password = request.form["password"]
        # 시작 날짜 반드시 입력

        x = {"data_id": data_id, "store": store, "product": product, "content": content, "price": price, "start": start, "end": end, "password": password}
        y = json.dumps(x, ensure_ascii=False)

    #return redirect('/boardView.html/'+str(data_id))
    return redirect(url_for('.view', data_id = data_id, store = store, product = product, content = content, price = price, start = start, end = end, password = password))

@app.route('/boardView.html/<data_id>/<store>/<product>/<content>/<price>/<start>/<end>/<password>')
def view(data_id, store, product, content, price, start,end,password):
    #data_id = request.form["data_id"]

    x = {"data_id": data_id, "store": store, "product": product, "content": content, "price": price, "start": start, "end": end, "password": password}

    test_data = [x]
    test_reply = [{"string": "댓글 남김"}]
    return render_template('boardView.html', data1 = test_data, reply1 = test_reply)

@app.route('/boardModifyForm.html/<int:data_id>')
def modify_form(data_id):
    test_data = [{"data_id": 1, "store" : "GS25", "product" : "딸기우유",  "content" : "2+1", "price" :"1300", "start" : "2019-01-01", "end" : "2019-02-01"}]
    return render_template('boardModifyForm.html', data1 = test_data)

@app.route('/boardModifyForm.html/modify/<int:data_id>', methods=['POST'])
def modify(data_id):
    if request.method == 'POST':
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

    return redirect('/boardView.html/'+str(data_id))

@app.route('/boardModifyForm.html/delete1/<int:data_id>', methods=['POST']) # 글 삭제
def delete1(data_id):
    password = request.form["password"]

    return redirect(url_for('list'))

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
