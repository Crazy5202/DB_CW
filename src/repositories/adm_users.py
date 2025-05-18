from settings import DB_CONFIG
import psycopg2
from pandas import DataFrame

def get_user_pwd(username):
    #print("Получение информации о пароле пользователя...")
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT password_hash, access_level FROM users WHERE username = %s", (username,))
            return cur.fetchone()

def get_users():
    #print("Получение информации о всех пользователях...")
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
    #print("Добавление пользователя...")
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
    #print("Проверка на существование лог-таблицы...")
    query1 = """select
        exists(
            select
                1
            from
                pg_class
            where
                relname = 'log')"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query1)
            res = cur.fetchone()[0]
            return res
        
def init_trigger():
    #print("Создание триггера...")
    create_log_query = """
        CREATE TABLE IF NOT EXISTS log (
            id SERIAL PRIMARY KEY,
            username_change VARCHAR(255) NOT NULL,
            action VARCHAR(255) NOT NULL,
            action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """
    create_function_query = """
        CREATE OR REPLACE FUNCTION log_user_insert()
        RETURNS TRIGGER AS $$
        BEGIN
            INSERT INTO log (username_change, action) VALUES (NEW.username, 'Создан');
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
    """
    create_function_query_2 = """
        CREATE OR REPLACE FUNCTION log_user_delete()
        RETURNS TRIGGER AS $$
        BEGIN
            INSERT INTO log (username_change, action) VALUES (OLD.username, 'Удалён');
            RETURN OLD;
        END;
        $$ LANGUAGE plpgsql;
    """
    create_trigger_query = """
        CREATE TRIGGER after_user_insert
        AFTER INSERT ON users
        FOR EACH ROW
        EXECUTE FUNCTION log_user_insert();
    """
    create_trigger_query_2 = """
        CREATE TRIGGER after_user_delete
        AFTER DELETE ON users
        FOR EACH ROW
        EXECUTE FUNCTION log_user_delete();
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        conn.autocommit = True
        with conn.cursor() as cur:
        
            cur.execute(create_log_query)

            cur.execute(create_function_query)

            cur.execute(create_function_query_2)

            cur.execute(create_trigger_query)

            cur.execute(create_trigger_query_2)
    
def get_user_log():
    #print("Получение информации о действиях со списком пользователей...")
    query = """select
            username_change, action, action_time 
        from
            log"""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return DataFrame(cur.fetchall(), columns=["Пользователь", "Действие", "Время добавления"])
        
def get_user_names():
    #print("Запрос к таблице пользователей...")
    query = """select
            id,
            username
        from
            users
        where
            username != 'admin'
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()
        
def delete_user(username):
    #print("Удаление пользователя...")
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            try:
                query = """
                    DELETE FROM users
                    WHERE username = %s
                """
                cur.execute(query, (username,))
                conn.commit()
                return True
            except:
                return False