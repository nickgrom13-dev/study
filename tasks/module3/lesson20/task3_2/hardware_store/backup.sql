CREATE TABLE roles(
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(250) NOT NULL,
    description TEXT
);

CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    user_password VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    last_name VARCHAR(250) NOT NULL,
    first_name VARCHAR(250) NOT NULL
);

CREATE TABLE user_roles(
    user_id INTEGER NOT NULL,
    role_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(role_id) ON DELETE CASCADE
);

CREATE TABLE items(
    item_id SERIAL PRIMARY KEY,
    title VARCHAR(250) NOT NULL UNIQUE,
    price NUMERIC NOT NULL,
    description TEXT,
    photo VARCHAR(250)
);

CREATE TABLE carts(
    cart_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE cart_items(
    cart_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    PRIMARY KEY (cart_id, item_id),
    FOREIGN KEY (cart_id) REFERENCES carts(cart_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES items(item_id) ON DELETE CASCADE
);

CREATE TABLE orders(
    order_id SERIAL PRIMARY KEY,
    cart_id INTEGER NOT NULL,
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total_sum NUMERIC NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES carts(cart_id) ON DELETE CASCADE
);

CREATE TABLE order_items(
    order_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    price NUMERIC NOT NULL,
    PRIMARY KEY (order_id, item_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES items(item_id) ON DELETE CASCADE
);


INSERT INTO roles(role_name, description) VALUES
('admin', 'Администратор системы'),
('user', 'Обычный пользователь');

INSERT INTO users(username, user_password, phone, email, last_name, first_name) VALUES
('ivan_ivanov', 'ivan123', '+79221112233', 'ivan.ivanov@example.ru', 'Иванов', 'Иван'),
('petr_petrov', 'petr123', '+79044445566', 'petr.petrov@example.ru', 'Петров', 'Петр'),
('anna_annova', 'anna123', '+79287778899', 'anna.annova@example.ru', 'Аннова', 'Анна');

INSERT INTO user_roles(user_id, role_id) VALUES
(1, 1), -- Иван - admin
(2, 2), -- Петр - user
(3, 2); -- Анна - moderator

INSERT INTO items(title, price, description, photo) VALUES
             ('Смартфон Samsung Galaxy S25',93999,'Флагманский смартфон с мощным процессором и отличной камерой.','samsung_galaxy_s25.jpg'),
             ('Ноутбук HONOR MagicBook X14',37999,'Легкий и производительный ноутбук для работы и творчества.','honor_magicbook_x14.jpg'),
             ('Наушники Marshall Major V',17999,'Беспроводные наушники с шумоподавлением и премиальным звуком.','marshall_major_v.jpg'),
             ('Смарт-часы Xiaomi Watch S4',15999,'Современные умные часы с функциями для здоровья и фитнеса.','xiaomi_watch_s4.jpg'),
             ('Планшет HONOR Pad V9',59999,'Мощный планшет для профессиональной работы и творчества.','honor_pad_v9.jpg'),
             ('Экшн-камера SJCAM SJ10',23599,'Экшн-камера для фотографии и видеосъемки в сложных условиях.','sjcam_sj10.jpg');

INSERT INTO carts(user_id) VALUES
             (2), -- Петр
             (3); -- Анна