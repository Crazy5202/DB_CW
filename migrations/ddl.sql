-- таблица с биомами
CREATE TABLE "biomes"(
    "biome_id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "biomes" ADD PRIMARY KEY("biome_id");

COMMENT ON TABLE biomes IS 'Информация о биомах';

COMMENT ON COLUMN biomes.biome_id IS 'Уникальный идентификатор биома';

COMMENT ON COLUMN biomes.name IS 'Название биома';


-- таблица с травами
CREATE TABLE "herbs"(
    "herb_id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "biome_id" INTEGER NOT NULL
);
ALTER TABLE
    "herbs" ADD PRIMARY KEY("herb_id");

COMMENT ON TABLE herbs IS 'Информация о травах';

COMMENT ON COLUMN herbs.herb_id IS 'Уникальный идентификатор травы';

COMMENT ON COLUMN herbs.name IS 'Название травы';

COMMENT ON COLUMN herbs.biome_id IS 'Идентификатор биома, в котором встречается трава';


-- таблица с монстрами
CREATE TABLE "monsters"(
    "monster_id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "xp" INTEGER NOT NULL,
    "hp" INTEGER NOT NULL,
    "biome_id" INTEGER NOT NULL
);
ALTER TABLE
    "monsters" ADD PRIMARY KEY("monster_id");

COMMENT ON TABLE monsters IS 'Информация о монстрах';

COMMENT ON COLUMN monsters.monster_id IS 'Уникальный идентификатор монстра';

COMMENT ON COLUMN monsters.name IS 'Название монстра';

COMMENT ON COLUMN monsters.xp IS 'Опыт за монстра';

COMMENT ON COLUMN monsters.hp IS 'Количество ХП монстра';

COMMENT ON COLUMN monsters.biome_id IS 'Идентификатор биома, в котором встречается монстр';


-- таблица с частями монстров
CREATE TABLE "parts"(
    "part_id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "monster_id" INTEGER NOT NULL
);
ALTER TABLE
    "parts" ADD PRIMARY KEY("part_id");

COMMENT ON TABLE parts IS 'Информация о частях монстров';

COMMENT ON COLUMN parts.part_id IS 'Уникальный идентификатор части монстра';

COMMENT ON COLUMN parts.name IS 'Название части монстра';

COMMENT ON COLUMN parts.monster_id IS 'Идентификатор монстра, с которого срезается часть';


-- таблица с поселениями
CREATE TABLE "settlements"(
    "set_id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "settlements" ADD PRIMARY KEY("set_id");

COMMENT ON TABLE settlements IS 'Информация о поселениях';

COMMENT ON COLUMN settlements.set_id IS 'Уникальный идентификатор поселения';

COMMENT ON COLUMN settlements.name IS 'Название поселения';


-- таблица с продавцами
CREATE TABLE "vendors"(
    "vendor_id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "set_id" INTEGER NOT NULL
);
ALTER TABLE
    "vendors" ADD PRIMARY KEY("vendor_id");

COMMENT ON TABLE vendors IS 'Информация о торговцах';

COMMENT ON COLUMN vendors.vendor_id IS 'Уникальный идентификатор торговцах';

COMMENT ON COLUMN vendors.name IS 'Имя торговца';

COMMENT ON COLUMN vendors.set_id IS 'Идентификатор поселения, в котором живёт торговец';


-- таблица со спиртом
CREATE TABLE "alcohols"(
    "alc_id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "alcohols" ADD PRIMARY KEY("alc_id");

COMMENT ON TABLE alcohols IS 'Информация о спирте';

COMMENT ON COLUMN alcohols.alc_id IS 'Уникальный идентификатор спирта';

COMMENT ON COLUMN alcohols.name IS 'Название спирта';


-- таблица со сделками
CREATE TABLE "trades"(
    "trade_id" SERIAL NOT NULL,
    "vendor_id" INTEGER NOT NULL,
    "alc_id" INTEGER NOT NULL,
    "cost" INTEGER NOT NULL
);
ALTER TABLE
    "trades" ADD PRIMARY KEY("trade_id");

COMMENT ON TABLE trades IS 'Информация о сделках';

COMMENT ON COLUMN trades.trade_id IS 'Уникальный идентификатор сделки';

COMMENT ON COLUMN trades.vendor_id IS 'Идентификатор торговца';

COMMENT ON COLUMN trades.alc_id IS 'Идентификатор спирта';

COMMENT ON COLUMN trades.cost IS 'Цена покупки спирта у продавца';


-- таблица с зельями
CREATE TABLE "potions"(
    "id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "effect" TEXT NOT NULL,
    "duration" INTEGER NOT NULL,
    "toxicity" INTEGER NOT NULL,
    "charges" INTEGER NOT NULL,
    "herb_id" INTEGER NOT NULL,
    "part_id" INTEGER NOT NULL,
    "alc_id" INTEGER NOT NULL
);
ALTER TABLE
    "potions" ADD PRIMARY KEY("id");

COMMENT ON TABLE potions IS 'Информация о зельях';

COMMENT ON COLUMN potions.id IS 'Уникальный идентификатор зелья';

COMMENT ON COLUMN potions.name IS 'Название зелья';

COMMENT ON COLUMN potions.effect IS 'Эффект зелья';

COMMENT ON COLUMN potions.duration IS 'Длительность зелья';

COMMENT ON COLUMN potions.toxicity IS 'Токсичность зелья';

COMMENT ON COLUMN potions.charges IS 'Число применений зелья';

COMMENT ON COLUMN potions.herb_id IS 'Уникальный идентификатор травы';

COMMENT ON COLUMN potions.part_id IS 'Уникальный идентификатор части монстра';

COMMENT ON COLUMN potions.alc_id IS 'Уникальный идентификатор спирта';


-- добавления зависимостей (приколы drawSQL)
ALTER TABLE
    "trades" ADD CONSTRAINT "trades_alc_id_foreign" FOREIGN KEY("alc_id") REFERENCES "alcohols"("alc_id");
ALTER TABLE
    "monsters" ADD CONSTRAINT "monsters_biome_id_foreign" FOREIGN KEY("biome_id") REFERENCES "biomes"("biome_id");
ALTER TABLE
    "trades" ADD CONSTRAINT "trades_vendor_id_foreign" FOREIGN KEY("vendor_id") REFERENCES "vendors"("vendor_id");
ALTER TABLE
    "parts" ADD CONSTRAINT "parts_monster_id_foreign" FOREIGN KEY("monster_id") REFERENCES "monsters"("monster_id");
ALTER TABLE
    "herbs" ADD CONSTRAINT "herbs_biome_id_foreign" FOREIGN KEY("biome_id") REFERENCES "biomes"("biome_id");
ALTER TABLE
    "potions" ADD CONSTRAINT "potions_part_id_foreign" FOREIGN KEY("part_id") REFERENCES "parts"("part_id");
ALTER TABLE
    "potions" ADD CONSTRAINT "potions_herb_id_foreign" FOREIGN KEY("herb_id") REFERENCES "herbs"("herb_id");
ALTER TABLE
    "potions" ADD CONSTRAINT "potions_alc_id_foreign" FOREIGN KEY("alc_id") REFERENCES "alcohols"("alc_id");
ALTER TABLE
    "vendors" ADD CONSTRAINT "vendors_set_id_foreign" FOREIGN KEY("set_id") REFERENCES "settlements"("set_id");


-- таблица пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    access_level INTEGER NOT NULL
);