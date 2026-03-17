import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
with open("data.txt", "r") as file:
    text = file.read()

chunks = text.split(".")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(chunks)

st.title("🤖 AI Document Chatbot")

query = st.text_input("Ask a question:")

if query:
    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, X)
    index = similarity.argmax()

    st.subheader("Answer:")
    st.write(chunks[index])