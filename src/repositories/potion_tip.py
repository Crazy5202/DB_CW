from settings import DB_CONFIG
import psycopg2
from pandas import DataFrame

def get_potion_names():
    print("Запрос к таблице зелий...")
    query = """select
            id,
            name
        from
            potions"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

def get(potion):
    print("Получение всей информации по зелью...")
    query = f"""with get_herbs as (
        select
                    herb_id,
            herbs.name as herb,
            biomes.name as herb_biome
        from
            herbs
        join biomes on
            herbs.biome_id = biomes.biome_id
        ),
        get_monsters as (
        select
                    part_id,
                    parts.name as part_name,
            monsters.name as monster,
            biomes.name as monster_biome
        from
            parts
        join monsters
                using (monster_id)
        join
                    biomes on
            monsters.biome_id = biomes.biome_id
        ),
        get_alc as (
        select
            distinct on
            (alcohols.name)
                    alc_id,
                    alcohols.name as alc,
            vendors.name as vendor,
            settlements.name as set
            ,
            cost
        from
            (alcohols
        join trades
                using (alc_id))
        join (vendors
        join settlements
                using (set_id))
                using (vendor_id)
        order by
            alc,
            cost asc 
        )

        select herb, herb_biome, part_name, monster, monster_biome, alc, vendor, set, cost
        from potions join get_herbs using (herb_id) join get_alc using (alc_id) join get_monsters using (part_id)
        where potions.name = '{potion}'"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()