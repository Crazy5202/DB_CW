-- Вставка данных в таблицу biomes
INSERT INTO "biomes" ("name") VALUES
('Горы'),
('Вода'),
('Лес');

-- Вставка данных в таблицу mutants
INSERT INTO "mutants" ("name", "type", "hp", "biome_id") VALUES
('Виверна', 'Драконид', 1000, 1),
('Утопец', 'Трупоед', 300, 2),
('Леший', 'Реликт', 800, 3);

-- Вставка данных в таблицу parts
INSERT INTO "parts" ("name", "mutant_id") VALUES
('Крыло виверны', 1),
('Глаз утопца', 2),
('Кора лешего', 3);

-- Вставка данных в таблицу herbs
INSERT INTO "herbs" ("name", "biome_id") VALUES
('Белый мирт', 1),
('Крушина', 2),
('Лесная хризантема', 3);

-- Вставка данных в таблицу alcohols
INSERT INTO "alcohols" ("name") VALUES
('Алкагест'),
('Краснолюдский спирт'),
('Махакамский спирт');

-- Вставка данных в таблицу settlements
INSERT INTO "settlements" ("name") VALUES
('Новиград'),
('Белый Сад'),
('Оксенфурт');

-- Вставка данных в таблицу vendors
INSERT INTO "vendors" ("name", "set_id") VALUES
('Оливер', 1),
('Эльза', 2),
('Штепан', 3);

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
('Эликсир Ласточка', 'Восстановление здоровья', 180, 25, 3, 1, 1, 3),
('Гром', 'Увеличение урона', 300, 20, 2, 2, 2, 1),
('Черная кровь', 'Отравляет вампиров', 200, 30, 1, 3, 3, 2);