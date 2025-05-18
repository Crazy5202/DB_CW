import streamlit as st
import repositories.potion_tip

@st.cache_data
def get_products() -> dict[str, str]:
    #print("Получение названий зелий...")
    potions = repositories.potion_tip.get_potion_names()
    return {potion[1]: potion[0] for potion in potions}

def main():
    st.title("Справка по получению ингредиентов для зелий!")
    potion_dict = get_products()
    selected_potion = st.selectbox("Выберите зелье:", potion_dict.keys())
    button = st.button("Нажмите чтобы вывести результат!")
    if button:
        result = repositories.potion_tip.get(selected_potion)[0]
        text = f"""Нужно растение {result[0]}, растущее в регионе {result[1]}.  
        \nНужна часть {result[2]} монстра {result[3]}, обитающего в регионе {result[4]}.  
        \nНужно купить {result[5]}, дешевле всего у торговца {result[6]} в поселении {result[7]} за {result[8]} золотых."""
        st.write(text)
        

if __name__ == "__main__":
    main()