-- Вставка данных в таблицу biomes
INSERT INTO "biomes" ("name") VALUES
('Горы'),
('Вода'),
('Лес');

-- Вставка данных в таблицу herbs
INSERT INTO "herbs" ("name", "biome_id") VALUES
('Белый мирт', 1),
('Крушина', 2),
('Лесная хризантема', 3);

-- Вставка данных в таблицу monsters
INSERT INTO "monsters" ("name", "xp", "hp", "biome_id") VALUES
('Леший', 200, 800, 3),
('Утопец', 60, 300, 2),
('Виверна', 300, 1000, 1);

-- Вставка данных в таблицу parts
INSERT INTO "parts" ("name", "monster_id") VALUES
('Крыло виверны', 3),
('Глаз утопца', 2),
('Кора лешего', 1);

-- Вставка данных в таблицу settlements
INSERT INTO "settlements" ("name") VALUES
('Белый Сад'),
('Новиград'),
('Оксенфурт');

-- Вставка данных в таблицу vendors
INSERT INTO "vendors" ("name", "set_id") VALUES
('Оливер', 2),
('Эльза', 1),
('Штепан', 3);

-- Вставка данных в таблицу alcohols
INSERT INTO "alcohols" ("name") VALUES
('Алкагест'),
('Краснолюдский спирт'),
('Махакамский спирт');

-- Вставка данных в таблицу trades
INSERT INTO "trades" ("vendor_id", "alc_id", "cost") VALUES
(1, 1, 50),
(1, 2, 40),
(1, 3, 30),

(2, 1, 40),
(2, 2, 30),
(2, 3, 50),

(3, 1, 30),
(3, 2, 50),
(3, 3, 40);

-- Вставка данных в таблицу potions
INSERT INTO "potions" ("name", "effect", "duration", "toxicity", "charges", "herb_id", "part_id", "alc_id") VALUES
('Ласточка', 'Восстановление здоровья', 180, 25, 3, 2, 1, 3),
('Гром', 'Увеличение урона', 300, 20, 2, 3, 2, 1),
('Черная кровь', 'Отравляет вампиров', 200, 30, 1, 1, 3, 2);

--вставка админа и обычного пользователя
INSERT INTO "users" ("username", "password_hash", "access_level") VALUES
('admin', '$2b$12$804NG.bhwQkDVrvNytO8.ua9C6gJFUYQbeMLBASE2ig7XL0lEVqTK', 2),
('user', '$2b$12$804NG.bhwQkDVrvNytO8.ua9C6gJFUYQbeMLBASE2ig7XL0lEVqTK', 1);