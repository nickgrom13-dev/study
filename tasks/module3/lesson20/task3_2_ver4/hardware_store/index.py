from connect_db import *

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    data = get_items()
    count_cart = get_count_cart()
    if 'success' in request.args and request.args['success']:
        return render_template('index.html',success = True,items = data, count_cart = count_cart)
    return render_template('index.html', items = data, count_cart = count_cart)

@app.route('/contacts')
def contacts():
    count_cart = get_count_cart()
    return render_template('contacts.html', count_cart = count_cart)

@app.route('/add_cart')
def add_cart():
    id = request.args.get('id')
    if id.isdigit():
        id = int(id)
        sql = f'SELECT * FROM cart where item_id = {id}'
        cursor.execute(sql)
        item = cursor.fetchone()
        #Если товар существует, то на 1 увеличиваем количество
        if item:
            sql_update = f'UPDATE cart SET quantity = quantity + 1 where item_id = {id}'
            cursor.execute(sql_update)
        else:
            sql_insert = f'INSERT INTO cart(item_id,quantity) VALUES({id},1)'
            cursor.execute(sql_insert)
        # подтверждаем изменения
        connection.commit()
        return redirect('/?success=True',code = 302)
    return 'Ошибка!'

def get_items():
    sql = "select * from item"
    cursor.execute(sql)
    return cursor.fetchall()

def get_count_cart():
    sql = "select sum(quantity) as count from cart"
    cursor.execute(sql)
    return cursor.fetchone()

if __name__ == '__main__':
    app.run(debug = True,host = '127.0.0.1',port = 8081)

