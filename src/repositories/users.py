from settings import DB_CONFIG
import psycopg2
        
def get_user_pwd(username):
    print("Получение информации о паролях...")
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT password_hash, access_level FROM users WHERE username = %s", (username,))
            return cur.fetchone()