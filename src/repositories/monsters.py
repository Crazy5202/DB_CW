from settings import DB_CONFIG
import psycopg2
from pandas import DataFrame

def get():
    #print("Получение информации о монстрах...")
    query = """select
            monsters.name,
            monsters.xp,
            monsters.hp,
            parts.name,
            biomes.name
        from
            monsters
        join parts on
            monsters.monster_id = parts.monster_id
        join biomes on
            biomes.biome_id = monsters.biome_id"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return DataFrame(cur.fetchall(), columns = ["Имя", "Опыт", "Здоровье", "Трофей", "Местность"])