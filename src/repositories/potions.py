from settings import DB_CONFIG
import psycopg2
from pandas import DataFrame

def get():
    #print("Получение информации о зельях...")
    query = """select
            potions.name,
            effect,
            duration,
            toxicity,
            charges,
            herbs.name,
            parts.name,
            alcohols.name
        from
            potions
        join parts
                using (part_id)
        join herbs
                using (herb_id)
        join alcohols
                using (alc_id)"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return DataFrame(cur.fetchall(), columns = ["Название", "Эффект", "Длительность", "Токсичность", "Применения", "Трава", "Часть монстра", "Спирт"])