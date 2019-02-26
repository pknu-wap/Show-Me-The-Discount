from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def main_page():
    #db
    return render_template('boardList.html')

@app.route('/boardWriteForm.html')
def write_form():
    return render_template('boardWriteForm.html')

@app.route('/json_data.txt', methods=['POST', 'GET'])
def json():
    if request.method == 'POST':
        print(request.headers.get('product'))
    #db
        return jsonify(request.headers.get('product'))
    elif request.method == 'GET':
        return jsonify(request.headers.get('product'))

@app.route('/boardList.html', methods=['GET'])
def list():

    return render_template('boardList.html')

@app.route('/boardView.html')
def view1():
    #post_id = request.args.get('글번호')
    return render_template('boardView.html')

@app.route('/boardView.html/')
def view2():
    dict = {id : '1', product : '상품'}
    return jsonify(dict)

@app.route('/boardModifyForm.html')
def modify():
    return render_template('boardModifyForm.html')

if __name__ == '__main__':
    app.run(debug = True)
