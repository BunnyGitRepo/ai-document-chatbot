import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🤖 AI Document Chatbot")
st.write("Upload a document and ask questions about it.")
st.divider()

uploaded_file = st.file_uploader("📄 Upload your document", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")

    # Split text into chunks
    chunks = text.split(".")

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(chunks)

    query = st.text_input("💬 Ask a question:")

    if query:
        with st.spinner("🤖 Thinking..."):
            query_vec = vectorizer.transform([query])
            similarity = cosine_similarity(query_vec, X)
            index = similarity.argmax()

            st.subheader("✅ Answer:")
            st.write(chunks[index])