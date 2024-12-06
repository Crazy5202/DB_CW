import streamlit as st
from repositories.monsters import get

def main():
    st.title("Монстры")
    data = get()
    st.dataframe(data, use_container_width=True, hide_index=True)

if __name__ == "__main__":
    main()