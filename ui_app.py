import streamlit as st
import requests

st.title("AI-Powered SQL Query Optimizer")

query = st.text_area("Enter SQL query")
table_size = st.number_input("Estimated Table Size", min_value=1)
index_present = st.checkbox("Index Present")
joins = st.number_input("Number of Joins", min_value=0)

if st.button("Predict Performance"):
    res = requests.post("https://<your-backend-url>/predict", json={
        "query": query,
        "table_size": table_size,
        "index_present": index_present,
        "joins": joins
    })
    st.json(res.json())

if st.button("Suggest Optimization"):
    res = requests.post("https://<your-backend-url>/suggest", json={
        "query": query,
        "table_size": table_size,
        "index_present": index_present,
        "joins": joins
    })
    st.markdown(res.json().get("suggestion", "No suggestion"))
