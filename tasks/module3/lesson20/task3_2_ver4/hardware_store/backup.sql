CREATE TABLE item(
    item_id serial primary key,
    title varchar(250),
    price numeric,
    info text,
    photo varchar(250)
);

CREATE TABLE cart(
    id serial primary key,
    item_id int,
    quantity smallint
);

INSERT INTO item(title,price,info,photo) VALUES
             ('Смартфон Samsung Galaxy S25',93999,'Флагманский смартфон с мощным процессором и отличной камерой.','samsung_galaxy_s25.jpg'),
             ('Ноутбук HONOR MagicBook X14',37999,'Легкий и производительный ноутбук для работы и творчества.','honor_magicbook_x14.jpg'),
             ('Наушники Marshall Major V',17999,'Беспроводные наушники с шумоподавлением и премиальным звуком.','marshall_major_v.jpg'),
             ('Смарт-часы Xiaomi Watch S4',15999,'Современные умные часы с функциями для здоровья и фитнеса.','xiaomi_watch_s4.jpg'),
             ('Планшет HONOR Pad V9',59999,'Мощный планшет для профессиональной работы и творчества.','honor_pad_v9.jpg'),
             ('Экшн-камера SJCAM SJ10',23599,'Экшн-камера для фотографии и видеосъемки в сложных условиях.','sjcam_sj10.jpg');

