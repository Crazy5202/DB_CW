import streamlit as st
from repositories.adm_users import get_users, init_trigger, get_user_log, check_exist, add_user
from services.password import hash_password

if 'trigger' not in st.session_state:
    st.session_state['trigger'] = 0

per = check_exist()

if per == True:
    st.session_state['trigger'] = 1

def main():
    st.title("Пользователи")
    st.dataframe(get_users(), use_container_width=True, hide_index=True)

    username = st.text_input("Имя нового пользователя:")
    password = st.text_input("Пароль:")
    access_level = st.radio("Уровень доступа:", [1, 2])
    add_user_btn = st.button("Добавить пользователя")

    if add_user_btn:
        if username and password:
            add_status = add_user(username, hash_password(password), access_level)
            if (add_status == False):
                st.write("Ошибка добавления! Проверьте имя пользователя на уникальность!")
            else:
                st.rerun()
        else:
            st.write("Все поля должны быть заполнены!")

    if st.session_state['trigger'] == 0:
        trigger_button = st.button("Включить триггер")
        if trigger_button:
            init_trigger()
            st.session_state['trigger'] = 1
            st.rerun()
    else:
        st.write("История добавлений для пользователей:")
        st.dataframe(get_user_log(), use_container_width=True, hide_index=True)


if __name__ == "__main__":
    main()