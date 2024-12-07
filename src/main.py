import streamlit as st
from pages import potion_tip, potions, herbs, monsters, trades, adm_users
from services.password import check_wrapper

st.set_page_config(layout="wide")

if 'logged' not in st.session_state:
    st.session_state['logged'] = 2

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
                    st.session_state['logged'] = check_res
                    st.rerun()
            else:
                st.write("Одно из полей не заполнено!")
    elif st.session_state['logged'] == 1:
        unlog = st.sidebar.button("ВЫЙТИ")
        if unlog:
            st.session_state['logged'] = 0
            st.rerun()
        st.sidebar.title("Навигация")
        page = st.sidebar.radio("Выберите таблицу", list(USER_TABLE.keys()))
        USER_TABLE[page].main()
    elif st.session_state['logged'] == 2:
        unlog = st.sidebar.button("ВЫЙТИ")
        if unlog:
            st.session_state['logged'] = 0
            st.rerun()
        st.sidebar.title("Навигация")
        page = st.sidebar.radio("Выберите таблицу", list(ADMIN_TABLE.keys()))
        ADMIN_TABLE[page].main()

if __name__ == "__main__":
    main()