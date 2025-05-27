import streamlit as st
from src.rag_chain import build_chain

st.set_page_config(page_title="Codeine + CYP2D6 Chatbot")
st.title("💊 Codeine + CYP2D6 PGx Chatbot")

query = st.text_input("Ask a clinical question:")

if query:
    chain = build_chain()
    result = chain.run(query)
    st.write(result)
