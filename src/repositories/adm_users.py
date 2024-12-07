from settings import DB_CONFIG
import psycopg2
from pandas import DataFrame

def get_user_pwd(username):
    print("Получение информации о пароле пользователя...")
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT password_hash, access_level FROM users WHERE username = %s", (username,))
            return cur.fetchone()

def get_users():
    print("Получение информации о всех пользователях...")
    query = """select
            username,
            password_hash,
            access_level
        from
            users"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return DataFrame(cur.fetchall(), columns = ["Логин", "Хэш пароля", "Уровень доступа (1-2)"])
        
def add_user(username, hashed_password, access_level):
    print("Добавление пользователя...")
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            try:
                query = """
                    INSERT INTO users (username, password_hash, access_level)
                    VALUES (%s, %s, %s)
                """
                cur.execute(query, (username, hashed_password, access_level))
                conn.commit()
                return True
            except:
                return False

def check_exist():
    print("Проверка на существование лог-таблицы...")
    query1 = """select
        exists(
            select
                1
            from
                pg_class
            where
                relname = 'log')"""
    query2 = """select
        exists(
        select
            *
        from
            information_schema.tables
        where
            table_schema = 'public'
            and 
        table_name = 'log'
    )"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query1)
            res = cur.fetchone()[0]
            return res
        
def init_trigger():
    print("Создание триггера...")
    create_log_query = """
        CREATE TABLE IF NOT EXISTS log (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """
    create_function_query = """
        CREATE OR REPLACE FUNCTION log_user_insert()
        RETURNS TRIGGER AS $$
        BEGIN
            INSERT INTO log (user_id) VALUES (NEW.id);
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
    """
    create_trigger_query = """
        CREATE TRIGGER after_user_insert
        AFTER INSERT ON users
        FOR EACH ROW
        EXECUTE FUNCTION log_user_insert();
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        conn.autocommit = True
        with conn.cursor() as cur:
        
            cur.execute(create_log_query)

            cur.execute(create_function_query)

            cur.execute(create_trigger_query)
    
def get_user_log():
    print("Получение информации о действиях со списком пользователей...")
    query = """select
            *
        from
            log"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return DataFrame(cur.fetchall())