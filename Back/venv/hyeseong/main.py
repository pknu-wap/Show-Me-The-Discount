from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('메인페이지.html')

@app.route('/글쓰기', methods = ['POST'])
def write():
    return render_template('글쓰기페이지.html')

if __name__ == '__main__':
    app.run(debug = True)
