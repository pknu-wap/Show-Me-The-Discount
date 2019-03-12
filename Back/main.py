from flask import Flask, render_template, request, redirect, json
import pymysql, cust_db

app = Flask(__name__)

data_id = 0
reply_id = 0

cust_db.dbInit()

@app.route('/')
@app.route('/boardList.html')
def list():

    data=cust_db.dbSearch("")
    data_list = []
    for temp in data :
        data_id = temp[0]
        store = temp[1]
        product = temp[2]
        content = temp[3]
        price = temp[4]
        start = temp[5]
        end = temp[6]
        password = temp[7]
        data_list.append({"data_id": data_id, "store": store, "product": product, "content": content, "price": price, "start": start, "end": end})

    return render_template('boardList.html', data1 = data_list)

@app.route('/boardList.html?searchType=<search_type>&searchText=<search_text>')
def search():

    data = cust_db.dbSearch(search_text)
    data_list=[]
    for temp in data :
        data_id = temp[0]
        store = temp[1]
        product = temp[2]
        content = temp[3]
        price = temp[4]
        start = temp[5]
        end = temp[6]
        password = temp[7]
        data_list.append({"data_id": data_id, "store": store, "product": product, "content": content, "price": price, "start": start, "end": end})

    return render_template('boardList.html', data1 = data_list) #data_list


@app.route('/boardWriteForm.html')
def write_form():
    return render_template('boardWriteForm.html')

@app.route('/write', methods=['POST'])
def register():
    if request.method == 'POST':

        store = request.form["store"]
        product = request.form["product"]
        content = request.form["content"]
        price = request.form["price"]
        start = request.form["start"]
        end = request.form["end"]
        password = request.form["password"]
    data_id = cust_db.NewPost(store,product,content,price,start,end,password)

    return redirect('/boardView.html/'+str(data_id))

@app.route('/boardView.html/<int:data_id>')
def view(data_id):

    data = cust_db.dbGetPost(data_id)
    data_id = data["post"][0][0]
    store = data["post"][0][1]
    product = data["post"][0][2]
    content = data["post"][0][3]
    price = data["post"][0][4]
    start = data["post"][0][5]
    end = data["post"][0][6]
    password = data["post"][0][7]

    data1 = {"data_id": data_id, "store": store, "product": product, "content": content, "price": price, "start": start, "end": end}

    return render_template('boardView.html', data1 = data1) #json

@app.route('/boardModifyForm.html/<data_id>')
def modify_form():

    data = cust_db.dbGetPost(post_id) #view랑 똑같이
    data_id = data["post"][0][0]
    store = data["post"][0][1]
    product = data["post"][0][2]
    content = data["post"][0][3]
    price = data["post"][0][4]
    start = data["post"][0][5]
    end = data["post"][0][6]
    password = data["post"][0][7]

    data1 = {"data_id": data_id, "store": store, "product": product, "content": content, "price": price, "start": start, "end": end}

    return render_template('boardModifyForm.html', data1 = data1) #redirect id

@app.route('/modify')
def modify():

    data = cust_db.UpdatePost(post_id,Store,Product,Content,Price,Start_Date,End_date,Password)
    data_id = data["post"][0][0]
    store = data["post"][0][1]
    product = data["post"][0][2]
    content = data["post"][0][3]
    price = data["post"][0][4]
    start = data["post"][0][5]
    end = data["post"][0][6]
    password = data["post"][0][7]

    data1 = {"data_id": data_id, "store": store, "product": product, "content": content, "price": price, "start": start, "end": end}

    return redirect('/boardView.html/'+str(data_id))

@app.route('/delete1', methods=['POST']) # 글 삭제
def delete1():
    data_id = request.form["id"]
    password = request.form["password"]

    data = cust_db.RemovePost(data_id,password)

    return render_template('boardList.html')

@app.route('/reply', methods=['POST'])
def reply():
    data_id = request.form["data_id"]
    reply = request.form["reply"]
    reply_password = request.form["password"]

    data = cust_db.NewReply(data_id,reply,reply_password)

    return redirect('/boardView.html/'+str(data_id))

@app.route('/delete2') # 댓글 삭제
def delete2():
    data_id = request.form["data_id"]
    reply_id = request.form["reply_id"]
    reply_password = request.form["reply_password"]

    data = cust_db.RemoveReply(reply_id,reply_password)

    return redirect('/boardView.html/'+str(data_id))

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=80)
