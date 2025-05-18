import streamlit as st
from pages import potion_tip, potions, herbs, monsters, trades, adm_users
from services.password import check_wrapper
from services.redis_funcs import Redis, redis_listener, set, get, delete, exists
from services.security import make_token
import threading

st.set_page_config(layout="wide")

if 'logged' not in st.session_state:
    st.session_state['logged'] = 0

USER_TABLE = {
    "Главная": potion_tip,
    "Зелья": potions,
    "Травы": herbs,
    "Монстры": monsters,
    "Покупка спирта": trades
}

ADMIN_TABLE = {
    "Пользователи": adm_users
}

channel_name1 = "login"
channel_name2 = "logout"

if 'redis' not in st.session_state:
    st.session_state.redis = Redis()

if 'listener_started' not in st.session_state:
    thread = threading.Thread(target=redis_listener, args=[[channel_name1, channel_name2]], daemon=True)
    thread.start()
    st.session_state.listener_started = True

def publish_channel(channel_name, message):
    st.session_state.redis.publish(channel_name, message)

def add_token():
    print("\nТокен добавляется в кэш")
    set(st.session_state.username, make_token(st.session_state.username))
    print(f"Существует после добавления: {exists(st.session_state.username)}\n")

def delete_token():
    print(f"\nТокен {get(st.session_state.username)} удаляется из кэша")
    delete(st.session_state.username)
    print(f"Существует после удаления: {exists(st.session_state.username)}\n")

def main():
    if st.session_state['logged'] == 0:
        st.write("Войдите в аккаунт!")
        username = st.text_input("ЛОГИН:")
        password = st.text_input("ПАРОЛЬ:")
        send = st.button("ВОЙТИ")
        if send:
            if username and password:
                check_res = check_wrapper(username, password)
                if (check_res == 0):
                    st.write("Неверные данные!")
                else:
                    st.session_state.username = username

                    add_token()

                    publish_channel(channel_name1, f"Пользователь {st.session_state.username} вошёл в систему")
                    
                    st.session_state['logged'] = check_res
                    st.rerun()
            else:
                st.write("Одно из полей не заполнено!")
    elif st.session_state['logged'] == 1:
        unlog = st.sidebar.button("ВЫЙТИ")
        if unlog:
            publish_channel(channel_name2, f"Пользователь {st.session_state.username} вышел из системы")
            delete_token()
            st.session_state['logged'] = 0
            st.rerun()
        st.sidebar.title("Навигация")
        page = st.sidebar.radio("Выберите таблицу", list(USER_TABLE.keys()))
        USER_TABLE[page].main()
    elif st.session_state['logged'] == 2:
        unlog = st.sidebar.button("ВЫЙТИ")
        if unlog:
            publish_channel(channel_name2, f"Пользователь {st.session_state.username} вышел из системы")
            delete_token()

            st.session_state['logged'] = 0
            st.rerun()
        adm_users.main()

if __name__ == "__main__":
    main()