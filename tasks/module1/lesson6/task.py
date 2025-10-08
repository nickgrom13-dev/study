"""1) Создать список словарей. Каждый словарь - это товар.
У товара есть свойства:id, title, price.
2) Сделать админку для управления товарами на основе телефонной книги.
Должна быть возможность - вывести все товары, получить информацию о товаре
по названию, удалить товар, изменить цену товара при указании названия товара.
Перед запуском команд для администратора, нужно запросить логин и пароль.
Информация с логином и паролем для админов хранится в виде списка словарей
users = [{"login":"admin","pass":"123"}, {..............}]
3*) Сделать корзину покупок. Это отдельный список словарей, но изначально пустой.
Товар корзины отличается от товара каталога, в нем хранятся товары
в виде: id товара и количество добавленных в корзину товаров"""

#Список пользователей-администраторов
users = [{"login":"admin","pass":"123"},
         {"login":"admin2","pass":"456"},
         {"login":"admin3","pass":"789"}]

#Список товаров
goods = [{"id":1, "title":"Колбаса", "price":345},
         {"id":2, "title":"Молоко", "price":90},
         {"id":3, "title":"Хлеб", "price":40}]

#Список покупок
purchases = []

def check_admin()->bool:
    """Проверяет учетные данные пользователя"""
    login = input("Введите логин:\n")
    password = input("Введите пароль:\n")
    find_user = {"login": login, "pass": password}
    if find_user not in users:
        print("Ошибка авторизации. Пользователя с указанными логином и паролем не существует.")
        return False
    return True

def check_number(value:str)->bool:
    """Проверяет корректность введенных числовых значений"""
    if not value.isdigit():
        print("Введено нечисловое значение")
        return False
    return True

def format_print_dict(dictionary:dict)->None:
    """Форматированный вывод словаря"""
    for key, value in dictionary.items():
        print(f"{key} - {value}", end="\t\t")
    print(f"\n{"*" * 50}")

def show_goods()->None:
    """Выводит список всех товаров"""
    if len(goods) == 0:
        print("Пустой список товаров")
    for good in goods:
        format_print_dict(good)

def add_good()->None:
    """Добавляет новый товар в список товаров"""
    if check_admin():
        id_good = input("Введите номер (id) товара\n")
        if check_number(id_good):
            found_goods = get_found_goods("id", id_good, goods)
            if len(found_goods) == 0:
                title_good = input("Введите наименование (title) товара\n").capitalize()
                found_goods = get_found_goods("title", title_good, goods)
                if len(found_goods) == 0:
                    price_good = input("Введите цену (price) товара\n")
                    if check_number(price_good):
                        goods.append({"id":int(id_good), "title":title_good, "price":int(price_good)})
                        print(f"Товар добавлен:\nid - {id_good}\t\ttitle "
                              f"- {title_good}\t\tprice - {price_good}\n{"*" * 50}")
                else:
                    print(f'Товар с наименование (title) "{title_good}" уже есть в списке')
            else:
                print(f'Товар с номером (id) "{id_good}" уже есть в списке')

def get_found_goods(find_key:str, find_value:str, goods_list:list)->list:
    """Поиск товаров по ключу и значению"""
    found_goods = []
    find_value = find_value.capitalize() if find_key == "title" else int(find_value)
    for good in goods_list:
        for key, value in good.items():
            if isinstance(value, str):
                value = value.capitalize()
            if key == find_key and value == find_value:
                found_goods.append(goods_list.index(good))
                break
    return found_goods

def remove_good()->None:
    """Удаляет товар из списка товаров"""
    if check_admin():
        title_good = input("Введите наименование (title) товара\n").capitalize()
        found_goods = get_found_goods("title", title_good, goods)
        if len(found_goods) > 0:
            for found_good in found_goods:
                #Перед удалением товара, удалим этот товар из списка покупок
                found_purchases = get_found_goods("id", goods[found_good]["id"], purchases)
                for found_purchase in found_purchases:
                    purchases.pop(found_purchase)
                print("Товар удален:")
                format_print_dict(goods.pop(found_good))
        else:
            print(f'По наименованию (title) "{title_good}" не найдено ни одного товара')


def show_info_good()->None:
    """Выводит информацию по определенному товару"""
    title_good = input("Введите наименование (title) товара\n").capitalize()
    found_goods = get_found_goods("title", title_good, goods)
    if len(found_goods) > 0:
        print(f'По наименованию (title) "{title_good}" в количестве {len(found_goods)} ед. '
              f'найдены следующие товары:')
        for found_good in found_goods:
            format_print_dict(goods[found_good])
    else:
        print(f'По наименованию (title) "{title_good}" не найдено ни одного товара')

def change_price_good()->None:
    """Меняет цену у определенного товара"""
    if check_admin():
        title_good = input("Введите наименование (title) товара\n").capitalize()
        found_goods = get_found_goods("title", title_good, goods)
        if len(found_goods) > 0:
            new_price = input(f'Введите новую цену для товара "{title_good}"\n')
            if check_number(new_price):
                for found_good in found_goods:
                    goods[found_good]["price"] = int(new_price)
                print(f'У товара с наименованием (title) "{title_good}" установлена '
                      f'новая цена (price) {new_price}\n{"*" * 50}')
        else:
            print(f'По наименованию (title) "{title_good}" не найдено ни одного товара')

def show_purchases()->None:
    """Показывает список покупок в корзине"""
    if len(purchases) == 0:
        print("Пустая корзина покупок")
    for purchase in purchases:
        format_print_dict(purchase)

def add_purchase()->None:
    """Добавляет покупку в корзину"""
    title_good = input("Введите наименование (title) товара\n").capitalize()
    found_goods = get_found_goods("title", title_good, goods)
    if len(found_goods) > 0:
        for found_good in found_goods:
            purchase = {"id":goods[found_good]["id"]}
            while 1:
                good_count = input("Введите количество товара\n")
                if check_number(good_count):
                    purchase["count"] = int(good_count)
                    purchases.append(purchase)
                    print(f"Товар добавлен в корзину:\nid - {goods[found_good]["id"]}\t\ttitle "
                          f"- {title_good}\t\tcount - {good_count}\n{"*" * 50}")
                    break
    else:
        print(f'По наименованию (title) "{title_good}" не найдено ни одного товара')

def remove_purchase()->None:
    """Удаляет покупку из корзины"""
    title_good = input("Введите наименование (title) товара\n").capitalize()
    found_goods = get_found_goods("title", title_good, goods)
    if len(found_goods) > 0:
        for found_good in found_goods:
            found_purchases = get_found_goods("id", goods[found_good]["id"], purchases)
            for found_purchase in found_purchases:
                print("Покупка удалена:")
                format_print_dict(purchases.pop(found_purchase))
    else:
        print(f'По наименованию (title) "{title_good}" не найдено ни одного товара')

while 1:
    command = input("Выберите пункт меню:\n"
                    "1) Вывести список всех товаров\n"
                    "2) Добавить товар\n"
                    "3) Удалить товар\n"
                    "4) Получить информацию о товаре\n"
                    "5) Изменить цену товара\n"
                    "6) Вывести корзину покупок\n"
                    "7) Добавить покупку в корзину\n"
                    "8) Удалить покупку из корзины\n"
                    "9) Очистить корзину\n"
                    "10) Выход\n")

    match command:
        case "1":
            show_goods()
        case "2":
            add_good()
        case "3":
            remove_good()
        case "4":
            show_info_good()
        case "5":
            change_price_good()
        case "6":
            show_purchases()
        case "7":
            add_purchase()
        case "8":
            remove_purchase()
        case "9":
            purchases.clear()
            print("Корзина очищена")
        case "10":
            break
        case _:
            print(f'Введен несуществующий пункт меню "{command}"')
