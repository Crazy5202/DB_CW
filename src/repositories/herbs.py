from settings import DB_CONFIG
import psycopg2
from pandas import DataFrame

def get():
    #print("Получение информации о травах...")
    query = """select
            herbs.name as herb,
            biomes.name as biome
        from
            herbs
        join biomes on
            herbs.biome_id = biomes.biome_id"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return DataFrame(cur.fetchall(), columns = ["Трава", "Местность"])