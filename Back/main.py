from flask import Flask, render_template, request, redirect, json

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('boardList.html')

@app.route('/boardWriteForm.html')
def write_form():
    return render_template('boardWriteForm.html')

@app.route('/boardView.html', methods=['POST'])
def register():
    if 'id' in locals():
        id +=1
        store = request.form["store"]
        product = request.form["product"]
        content = request.form["content"]
        price = request.form["price"]
        startdate = request.form["start"]
        enddate = request.form["end"]
        password = request.form["password"]
    else :
        id = 1
        store = request.form["store"]
        product = request.form["product"]
        content = request.form["content"]
        price = request.form["price"]
        startdate = request.form["start"]
        enddate = request.form["end"]
        password = request.form["password"]
        #글번호(id) 지정

    x = {"id": id, "store": store, "product": product, "content": content, "price": price, "startdate": startdate, "enddate": enddate, "password": password}
    y = json.dumps(x)
    #db 데이터 삽입
    return redirect('/boardView.html/'+str(id))

@app.route('/boardView.html/<int:id>')
def view(id):
    #db 데이터 읽기
    return render_template('boardView.html') #json

#@app.route('/')
@app.route('/boardList.html')
def list():
    #db
    x = '{"id": 1, "store": STORE, "product": PRODUCT, "content": CONTENT, "price": PRICE, "startdate": STARTDATE, "enddate": ENDDATE}' #TEST
    return x
    #return render_template('boardList.html')

@app.route('/boardModifyForm.html')
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
    return render_template('boardModifyForm.html')

if __name__ == '__main__':
    app.run(debug = True)
