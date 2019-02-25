from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main_page():
    #db
    return render_template('boardList.html')

@app.route('/boardWriteForm.html')
def write():
    return render_template('boardWriteForm.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        store = request.form['store']
        product = request.form['product']
        content = request.form['content']
        price = request.form['price']
        startdate = request.form['startdate']
        enddate = request.form['enddate']
        password = request.form['password']
        return redirect(url_for('view', ))

@app.route('/boardList.html')
def list():
    return render_template('boardList.html')

@app.route('/boardView.html')
def view():
    post_id = request.args.get('글번호')
    #db
    return render_template('boardView.html')

@app.route('/boardModifyForm.html')
def modify():
    return render_template('boardModifyForm.html')

if __name__ == '__main__':
    app.run(debug = True)
