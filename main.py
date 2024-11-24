import streamlit as st
import pandas as pd
from db import get_gifts, update_gift

st.title("Amor en Detalles para July y James 🎁 👰🤵")

st.header("Instrucciones 📝")

st.text('- Si deseas regalarnos alguno de los detalles listados, entonces cambia el estado de "Libre" 🟢 a "Reservado" ⛔')
st.text("- Si no encuentras el regalo perfecto en nuestra lista, no te preocupes. También puedes hacernos un regalo económico, que será igual de apreciado 🌟")


def on_state_change(state_key):
    new_state = st.session_state[state_key]
    status = True if new_state == "Reservado 🔴" else False
    update_gift(state_key, status)

data = get_gifts()

df = pd.DataFrame(data)

st.markdown("---")
for index, row in df.iterrows():
    col1, col2 = st.columns([3, 2], vertical_alignment="bottom")
    with col1:
        st.write(f"\n{row['gift']}")
    with col2:
        new_state = st.selectbox(
            "",
            ["Libre 🟢", "Reservado 🔴"],
            index=0 if row["reserved"] == False else 1,
            key=row["uuid"],
            on_change=on_state_change,
            args=(row["uuid"], )
        )
    st.markdown("---")
