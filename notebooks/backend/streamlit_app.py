import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.set_page_config(
    page_title="RAG Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 RAG Assistant")
st.write("Ask a question about your documents.")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question.strip():
        try:
            response = requests.post(
                f"{API_URL}/query",
                json={"question": question}
            )

            if response.status_code == 200:
                data = response.json()

                st.subheader("Answer")
                st.write(data["answer"])

                st.subheader("Sources")

                for source in data["sources"]:
                    st.write(
                        f"📄 {source['source']} — Page {source['page']}"
                    )

            else:
                st.error(f"API Error: {response.status_code}")

        except requests.exceptions.ConnectionError:
            st.error(
                "Could not connect to the RAG API. "
                "Make sure FastAPI is running."
            )
    else:
        st.warning("Please enter a question.")