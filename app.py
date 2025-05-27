import streamlit as st
from index_and_retrieve import search
from compose_response import summarize_chunks, compose_final_response

st.set_page_config(page_title="Travel Guide Chatbot", layout="wide")
st.title("🧳 Travel Guide Chatbot")

query = st.text_input("Enter your travel question:")

if query:
    with st.spinner("Retrieving and generating response..."):
        chunks = search(query)
        summary = summarize_chunks(chunks)
        response = compose_final_response(summary)

        st.subheader("✈ Recommendation")
        st.write(response)

        with st.sidebar:
            st.markdown("### 🔍 Agent Logs")
            st.write("Chunks Retrieved:")
            st.write(chunks)
            st.write("Summary:")
            st.write(summary)