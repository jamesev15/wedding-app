import os
import streamlit as st
from pymongo.mongo_client import MongoClient

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

uri = f"mongodb+srv://{username}:{password}@wedding-cluster.sqkmc.mongodb.net/?retryWrites=true&w=majority&appName=wedding-cluster"

client = MongoClient(uri)


def get_gifts():
    collection = client["wedding"]["jjgifts"]
    return collection.find()

@st.dialog("Confirma tu elección")
def update_gift(item, state_key, status: bool):
    st.write(f"Tu elección: {item}")
    senders = st.text_input("Quién eligió este regalo?: ")
    if st.button("Confirmar"):
        collection = client["wedding"]["jjgifts"]

        collection.update_one(
            {"uuid": state_key},  # Filter
            {"$set": {"reserved": status}}  # Update operation
        )
        st.rerun()
    elif st.button("Elegir otro regalo"):
        st.session_state[state_key] = "Libre 🟢"
        st.rerun()
