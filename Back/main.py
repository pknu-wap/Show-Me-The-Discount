from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('boardList.html')

@app.route('/boardWriteForm.html')
def write_form():
    return render_template('boardWriteForm.html')

@app.route('/boardView.html/<id>', methods=['POST'])
def register(id):
    if request.method == 'POST':
        id = request.form["id"]
        store = request.form["store"]
        product = request.form["product"]
        content = request.form["content"]
        price = request.form["price"]
        startdate = request.form["start"]
        enddate = request.form["end"]
        password = request.form["password"]
        #db
        return redirect('/boardView.html/'+id)

'''@app.route('/json_data.txt', methods=['POST', 'GET'])
def json():
    if request.method == 'POST':
        print(request.headers.get('product'))
        #db
        return jsonify(request.headers.get('product'))
    elif request.method == 'GET':
        return jsonify(request.headers.get('product'))'''

@app.route('/boardList.html', methods=['GET'])
def list():
    #db
    return render_template('boardList.html')

@app.route('/boardView.html/<id>')
def view1(id):
    post_id = request.args.get('id')
    #db
    return redirect(url_for('view2', id=id))

@app.route('/boardView.html/')
def view2(id):
    '''dict = {id : '1', product : '상품'}
    return jsonify(dict)'''
    #db
    return render_template('boardView', )

@app.route('/boardModifyForm.html')
def modify():
    return render_template('boardModifyForm.html')

if __name__ == '__main__':
    app.run(debug = True)
