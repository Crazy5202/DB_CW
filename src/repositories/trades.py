from settings import DB_CONFIG
import psycopg2
from pandas import DataFrame

def get():
    #print("Получение информации о продаже спирта...")
    query = """select
            alcohols.name as alc_name,
            cost,
            vendors.name,
            settlements.name
        from
            (alcohols
        join trades
                using (alc_id))
        join (vendors
        join settlements
                using (set_id))
                using (vendor_id)
        order by
            alc_name,
            cost"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return DataFrame(cur.fetchall(), columns = ["Название", "Цена", "Имя продавца", "Местонахождение"])