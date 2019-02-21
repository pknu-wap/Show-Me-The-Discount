from flask import Flask, render_template, request
import request

app = Flask(__name__)

'''@app.route('/')
def main_page():
    return render_template('메인페이지.html')'''

@app.route('/')
def main_get(f=None):
    return render_template('boardWriteForm.html', f=f)

'''@app.route('/')
def css_file():
    return redirect(url_for('static', filename='CSS.css'))'''

@app.route('/register', methods=['POST']) #boardWriteForm.html
def register(f=None):
    if request.method == 'POST':
        temp1 = request.form['f'] #f가 json?
        temp2 = json.loads(x) #json->python dictionary
        return temp2 #혹은 render_template

@app.route('/pass_data_to_db')


@app.route('/pass_data_to_front')
def front():
    x = dictionary데이터 #db에서 가져온 데이터
    y = json.dumps(x)
    return y

if __name__ == '__main__':
    app.run(debug = True)
