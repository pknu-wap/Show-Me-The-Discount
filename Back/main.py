from flask import Flask, render_template, request, redirect, json

app = Flask(__name__)

id = 0

@app.route('/')
@app.route('/boardList.html')
def list():

    #db 데이터 읽기

    return render_template('boardList.html') #json

@app.route('/boardWriteForm.html')
def write_form():
    return render_template('boardWriteForm.html')

@app.route('/write', methods=['POST'])
def register():
    if request.method == 'POST':
        global id
        id += 1
        store = request.form["store"]
        product = request.form["product"]
        content = request.form["content"]
        price = request.form["price"]
        startdate = request.form["start"]
        enddate = request.form["end"]
        password = request.form["password"]

        x = {"id": id, "store": store, "product": product, "content": content, "price": price, "startdate": startdate, "enddate": enddate, "password": password}
        y = json.dumps(x)

    #db 데이터 삽입

    return redirect('/boardView.html/'+str(id))

@app.route('/boardView.html/<int:id>')
def view(id):

    #db 데이터 읽기

    return render_template('boardView.html') #json

@app.route('/boardModifyForm.html')
def modify_form():
    return render_template('boardModifyForm.html')

@app.route('/modify')
def modify():
    if request.method == 'POST':
        id = request.form["id"]
        store = request.form["store"]
        product = request.form["product"]
        content = request.form["content"]
        price = request.form["price"]
        startdate = request.form["start"]
        enddate = request.form["end"]
        password = request.form["password"]

        x = {"id": id, "store": store, "product": product, "content": content, "price": price, "startdate": startdate, "enddate": enddate, "password": password}
        y = json.dumps(x)

    #db 데이터 수정

    return redirect('/boardView.html/'+str(id))

@app.route('/delete1')
def delete():
    #db 데이터 읽기
    #비밀번호 일치 여부 확인

        #db 데이터 삭제

    return render_template('boardList.html')

if __name__ == '__main__':
    app.run(debug = True)
