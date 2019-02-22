from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main_page():
    #db
    return render_template('boardList.html')

'''@app.route('/')
def css_file():
    return redirect(url_for('static', filename='CSS.css'))'''

@app.route('/boardWriteForm.html')
def write():
    return render_template('boardWriteForm.html')

@app.route('/boardProcess.html', methods = ['POST'])
def process():
    if request.method == "POST":
        result = request.form
        #db

        return #등록 알림창, 페이지 이동

@app.route('/boardList.html')
def list():
    return render_template('boardList.html')

@app.route('/boardView.html')
def view():
    post_id = request.args.get("글번호")
    #db
    return render_template('boardView.html')

@app.route('/boardModifyForm.html')

if __name__ == '__main__':
    app.run(debug = True)
