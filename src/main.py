import streamlit as st
from pages import potions, herbs, monsters, trades
        
TABLES = {
    "Зелья": potions,
    "Травы": herbs,
    "Монстры": monsters,
    "Покупка спирта": trades
}

def main():
    st.set_page_config(layout="wide")
    st.sidebar.title("Навигация")
    page = st.sidebar.radio("Выберите таблицу", list(TABLES.keys()))
    TABLES[page].main()

if __name__ == "__main__":
    main()