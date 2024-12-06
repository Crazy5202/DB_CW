import streamlit as st
from repositories.trades import get

def main():
    st.title("Спирт")
    data = get()
    st.dataframe(data, use_container_width=True)

if __name__ == "__main__":
    main()