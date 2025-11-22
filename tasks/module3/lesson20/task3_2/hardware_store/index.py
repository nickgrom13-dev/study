import os

from connect_db import *

from flask import Flask, render_template, request, redirect, session, jsonify

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    """Главная страница"""
    #Проверяем наличие имени пользователя в сеансе, если его нет, то загружаем страницу авторизации
    if 'username' in session :
        if 'role_id' in session:
            #Из сессии получаем id роли пользователя
            role_id = session.get('role_id')

            #Если id роли равен 1(admin), то загружаем главную страницу администратора
            if role_id == 1:
                #Получаем данные всех заказов пользователей
                order_items = get_all_user_orders()

                #Загружаем главную страницу для администратора, передаем в нее данные заказов,
                # скрываем в меню ссылку на страницу Контакты
                return render_template('admin.html', hide_contacts = True, order_items = order_items)

            #Получаем список всех товаров
            data = get_items()

            if 'cart_id' in session:
                #Получаем из сессии id корзины авторизованного пользователя
                cart_id = session.get('cart_id')

                #Получаем количество единиц товаров из корзины пользователя
                count_cart = get_count_cart(cart_id)
            else:
                count_cart = 0

            #Обновляем главную страницу в случае успешного добавления товара в корзину с доп. параметрами
            if 'success' in request.args and request.args['success']:
                return render_template('index.html', success = True, items = data, count_cart = count_cart)

            # Загружаем главную страницу в случае успешного оформления заказа с доп. параметрами
            if 'success_order' in request.args and request.args['success_order']:
                return render_template('index.html', success = True, success_order = True, items = data, count_cart = count_cart)

            #Загружаем главную страницу для пользователя
            return render_template('index.html', items = data, count_cart = count_cart)

    return redirect('login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Страница авторизации"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        #Проверяем данные авторизации, введенные пользователем
        #В случае успешной авторизации, загружаем главную страницу пользователя
        if check_account(username, password):
            user_data = get_user_data(username)
            if user_data:
                session['username'] = username
                session['role_id'] = user_data['role_id']
                session['name'] = user_data['first_name']
                session['cart_id'] = user_data['cart_id']
                return redirect('/')
            return "Ошибка авторизации"
        else:
            return 'Неверное имя пользователя или пароль'

    return render_template('login.html')

@app.route('/logout')
def logout():
    """Выход из системы"""
    #Удаляем данные сессии после выхода из пользователя из личного кабинета
    session.pop('username', None)
    session.pop('role_id', None)
    session.pop('name', None)
    session.pop('cart_id', None)
    return redirect('login')

@app.route('/contacts')
def contacts():
    """Страница контактов"""
    return render_template('contacts.html')

@app.route('/add_to_cart')
def add_to_cart():
    """Добавить товар в корзину"""
    #Получаем из параметров id товара, который нужно добавить в корзину
    item_id = request.args.get('item_id')
    if item_id and item_id.isdigit():
        item_id = int(item_id)

        #Получаем из сессии id корзины пользователя, в которую нужно добавить товар
        cart_id = session.get('cart_id')

        #Получаем данные из корзины пользователя по добавляемому товару
        item = get_cart_item(item_id, cart_id)

        #Если товар существует, то на 1 увеличиваем количество, иначе добавляем товар
        if item:
            update_cart_item(item_id, cart_id, '+')
        else:
            add_item_to_cart(item_id, cart_id)
        # подтверждаем изменения
        connection.commit()

        #Загружаем главную страницу с параметром успешного добавления товара success=True
        return redirect('/?success=True',code = 302)
    return 'Ошибка'

@app.route('/cart')
def cart():
    """Страница корзины"""
    #Получаем из сессии id корзины пользователя, которую нужно отобразить
    cart_id = session.get('cart_id')

    #Получаем данные товаров, добавленных в корзину
    cart_items = get_cart_items(cart_id)
    is_not_empty = len(cart_items)

    #Получаем общую сумму всех единиц товаров в корзине
    total_sum_cart = get_total_sum_cart(cart_id)

    #Загружаем страницу корзины
    return render_template('cart.html', cart_items = cart_items, total_sum_cart = total_sum_cart, is_not_empty = is_not_empty)

@app.route('/increase_quantity')
def increase_quantity():
    """Увеличить количество товара в корзине на 1"""
    try:
        # Получаем из параметров id товара, у которого в корзине нужно увеличить количество на 1
        item_id = request.args.get('item_id')
        if item_id and item_id.isdigit():
            item_id = int(item_id)

            # Получаем из сессии id корзины пользователя, в которой нужно увеличить количество товара
            cart_id = session.get('cart_id')

            # Получаем данные из корзины пользователя по товару, у которого увеличиваем количество
            item = get_cart_item(item_id, cart_id)
            if item:
                #Обновляем количество единиц товара в корзине (увеличиваем)
                update_cart_item(item_id, cart_id, '+')
                # подтверждаем изменения
                connection.commit()

                #Получаем обновленные данные (товара и общей суммы)
                updated_item = get_cart_item(item_id, cart_id)
                total_sum = get_total_sum_cart(cart_id)

                # Возвращаем JSON для AJAX
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return jsonify({
                        'success': True, #статус успешного изменения
                        'item_id': item_id, #id товара
                        'new_quantity': updated_item['quantity'], #новое количество
                        'item_sum': updated_item['sum'], #новая сумма по товару
                        'total_sum': total_sum['total_sum'], #новая общая сумма
                        'deleted': False #флажок удаления строки из страницы
                    })

        # Если это не AJAX запрос, обновляем страницу корзины
        if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
            return redirect('/cart')

        return jsonify({'success': False, 'error': 'Ошибка обновления'})

    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'success': False, 'error': str(e)})
        return f'Ошибка!<br>{e}'

@app.route('/decrease_quantity')
def decrease_quantity():
    """Уменьшить количество товара в корзине на 1"""
    try:
        # Получаем из параметров id товара, у которого в корзине нужно уменьшить количество на 1
        item_id = request.args.get('item_id')
        if item_id and item_id.isdigit():
            item_id = int(item_id)

            # Получаем из сессии id корзины пользователя, в которой нужно уменьшить количество товара
            cart_id = session.get('cart_id')

            # Получаем данные из корзины пользователя по товару, у которого уменьшаем количество
            item = get_cart_item(item_id, cart_id)

            if item:
                # Обновляем количество единиц товара в корзине
                # Если количество единиц товара больше 1, то уменьшаем его
                # иначе удаляем товар из корзины
                deleted = False
                if item['quantity'] > 1:
                    update_cart_item(item_id, cart_id, '-')
                else:
                    delete_cart_item(item_id, cart_id)
                    deleted = True
                # подтверждаем изменения
                connection.commit()

                #Получаем обновленные данные (товара и общей суммы)
                total_sum = get_total_sum_cart(cart_id)

                # Если товар не удален, получаем его данные
                if not deleted:
                    updated_item = get_cart_item(item_id, cart_id)
                    item_sum = updated_item['sum']
                    new_quantity = updated_item['quantity']
                else:
                    item_sum = 0
                    new_quantity = 0

                # Возвращаем JSON для AJAX
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return jsonify({
                        'success': True, #статус успешного изменения
                        'item_id': item_id, #id товара
                        'new_quantity': new_quantity, #новое количество
                        'item_sum': item_sum, #новая сумма по товару
                        'total_sum': total_sum['total_sum'], #новая общая сумма
                        'deleted': deleted #флажок удаления строки из страницы
                    })

        # Если это не AJAX запрос, обновляем страницу корзины
        if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
            return redirect('/cart')

        return jsonify({'success': False, 'error': 'Ошибка обновления'})

    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'success': False, 'error': str(e)})
        return f'Ошибка!<br>{e}'

@app.route('/order')
def order():
    """Переместить товары из корзины в заказы"""
    #Получаем из параметров общую сумму корзины
    total_sum = request.args.get('total_sum')
    if total_sum:
        total_sum = float(total_sum.replace(" ", ""))

        # Получаем из сессии id корзины пользователя, по которой нужно оформить заказ
        cart_id = session.get('cart_id')

        #Добавляем общую информацию по заказу
        order_data = add_order(cart_id, total_sum)

        #Добавляем детализацию заказа в разрезе товаров
        cart_items = get_cart_items(cart_id)
        for cart_item in cart_items:
            add_order_details(order_data['order_id'], cart_item['item_id'], cart_item['quantity'], cart_item['price'])

        #Очищаем корзину после формирования заказа
        delete_cart(cart_id)
        # подтверждаем изменения
        connection.commit()

        #Загружаем главную страницу
        return redirect('/?success_order=True',code = 302)
    return 'Ошибка!<br>Не передан параметр "total_sum"'


def check_account(username, password):
    """Проверка логина и пароля"""
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    users = cursor.fetchall()
    for user in users:
        if username == user['username'] and password == user['user_password']:
            return True
    return False

def get_user_data(username):
    """Получить данные пользователя"""
    sql = f"""
            SELECT u.user_id, r.role_id, u.first_name, c.cart_id 
            FROM users AS u 
            INNER JOIN user_roles AS u_r ON u.user_id = u_r.user_id
            INNER JOIN roles AS r ON u_r.role_id = r.role_id
            LEFT JOIN carts AS c ON c.user_id = u.user_id
            WHERE u.username = '{username}'
        """
    cursor.execute(sql)
    user = cursor.fetchone()
    return user

def get_items():
    """Получить товары"""
    sql = "SELECT * FROM items"
    cursor.execute(sql)
    return cursor.fetchall()

def get_count_cart(cart_id):
    """Получить общее количество единиц товаров в корзине"""
    sql = f"SELECT COALESCE(SUM(quantity), 0) AS count FROM cart_items WHERE cart_id = {cart_id}"
    cursor.execute(sql)
    return cursor.fetchone()

def get_total_sum_cart(cart_id):
    """Получить общую сумму в корзине"""
    sql = f"""
                SELECT COALESCE(SUM(i.price * c.quantity), 0) AS total_sum 
                FROM cart_items AS c INNER JOIN items AS i on c.item_id = i.item_id 
                WHERE c.cart_id = {cart_id}
            """
    cursor.execute(sql)
    return cursor.fetchone()

def get_cart_items(cart_id):
    """Получить данные товаров, добавленных в корзину"""
    sql = f"""
                SELECT row_number() OVER(ORDER BY i.title nulls last) AS row_number, i.title, 
                i.price, c.quantity, i.price * c.quantity AS sum, i.item_id 
                FROM cart_items AS c 
                INNER JOIN items AS i ON i.item_id = c.item_id 
                WHERE c.cart_id = {cart_id}
            """
    cursor.execute(sql)
    return cursor.fetchall()

def get_cart_item(item_id, cart_id):
    """Получить данные товара из корзины"""
    sql = f"""
            SELECT i.title, i.price, c.quantity, i.price * c.quantity AS sum, i.item_id 
            FROM cart_items AS c 
            INNER JOIN items AS i ON c.item_id = i.item_id  
            WHERE c.item_id = {item_id} AND c.cart_id = {cart_id}
        """
    cursor.execute(sql)
    return cursor.fetchone()

def update_cart_item(item_id, cart_id, operation):
    """Обновить количество единиц товара в корзине"""
    sql_update = f"""
                    UPDATE cart_items SET quantity = quantity {operation} 1 
                    WHERE item_id = {item_id} AND cart_id = {cart_id}
                """
    cursor.execute(sql_update)

def add_item_to_cart(item_id, cart_id):
    """Добавить товар в корзину"""
    sql_insert = f"INSERT INTO cart_items(cart_id, item_id, quantity) VALUES({cart_id}, {item_id}, 1)"
    cursor.execute(sql_insert)

def delete_cart_item(item_id, cart_id):
    """Удалить товар из корзины"""
    sql_delete = f"DELETE FROM cart_items WHERE item_id = {item_id} AND cart_id = {cart_id}"
    cursor.execute(sql_delete)

def delete_cart(cart_id):
    """Очистить корзину пользователя"""
    sql_delete = f"DELETE FROM cart_items WHERE cart_id = {cart_id}"
    cursor.execute(sql_delete)

def get_all_user_orders():
    """Получить данные по заказам всех пользователей"""
    sql = f"""
                SELECT row_number() OVER(ORDER BY o.order_date nulls last) AS row_number,
                o.order_date, u.username, CONCAT(u.last_name,' ',u.first_name) AS user_fio, 
                u.phone, u.email, i.title, o_i.price, o_i.quantity, o_i.price * o_i.quantity AS sum
                FROM users AS u
                INNER JOIN carts AS c ON u.user_id = c.user_id
                INNER JOIN orders AS o ON c.cart_id = o.cart_id
                INNER JOIN order_items AS o_i ON o.order_id = o_i.order_id
                INNER JOIN items AS i ON o_i.item_id = i.item_id
                ORDER BY o.order_date                      
            """
    cursor.execute(sql)
    return cursor.fetchall()

def add_order(cart_id, total_sum):
    """Добавить данные по оформленному заказу"""
    sql_insert = f"INSERT INTO orders(cart_id, total_sum) VALUES({cart_id}, {total_sum}) RETURNING order_id"
    cursor.execute(sql_insert)
    return cursor.fetchone()

def add_order_details(order_id, item_id, quantity, price):
    """Добавить детализацию оформленного заказа по товарам"""
    sql_insert = f"""
                    INSERT INTO order_items(order_id, item_id, quantity, price) 
                    VALUES({order_id}, {item_id}, {quantity}, {price})
                """
    cursor.execute(sql_insert)

if __name__ == '__main__':
    app.run(debug = True,host = '127.0.0.1',port = 8081)
