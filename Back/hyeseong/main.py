from flask import Flask, render_template, request
import request

app = Flask(__name__)

@app.route('/')
def main_page():
    #db
    return render_template('boardList.html')

'''@app.route('/')
def main_get(f=None):
    return render_template('boardWriteForm.html', f=f)'''

'''@app.route('/')
def css_file():
    return redirect(url_for('static', filename='CSS.css'))'''

@app.route('/boardWriteForm.html')
def write():
    return render_template('boardWriteForm.html')

@app.route('/boardList.html')
def list():
    return render_template('boardList.html')

@app.route('/modify')

@app.route('/comment')

@app.route('/pass_data_to_db')

@app.route('/pass_data_to_front')
def front():
    x = dictionary데이터 #db에서 가져온 데이터
    y = json.dumps(x)
    return y

if __name__ == '__main__':
    app.run(debug = True)
