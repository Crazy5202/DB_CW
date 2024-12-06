import streamlit as st
from repositories.potions import get

def main():
    st.title("Зелья")
    data = get()
    st.dataframe(data, use_container_width=True)

if __name__ == "__main__":
    main()