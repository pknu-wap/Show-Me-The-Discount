from flask import Flask, render_template, request, json, jsonify

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('boardList.html')

@app.route('/boardWriteForm.html')
def write_form():
    return render_template('boardWriteForm.html')

@app.route('/register', methods=['POST'])
def register():
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
        #db
        return redirect('/boardView.html'+id)

@app.route('/boardView.html/<int:id>')
def view(id):
    #post_id = request.args.get('id')
    #db
    return render_template('boardView.html')

@app.route('/boardList.html', methods=['GET'])
def list():
    #db
    return render_template('boardList.html')

'''@app.route('/boardView.html/')
def view2(id):
    dict = {id : '1', product : '상품'}
    return jsonify(dict)
    #db
    return render_template('boardView', )'''

@app.route('/boardModifyForm.html')
def modify():
    return render_template('boardModifyForm.html')

if __name__ == '__main__':
    app.run(debug = True)
