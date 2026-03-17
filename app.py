from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load file
with open("data.txt", "r") as file:
    text = file.read()

chunks = text.split(".")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(chunks)

print("AI Document Chatbot Ready! Type 'exit' to quit.\n")

while True:
    query = input("Ask a question: ")

    if query.lower() == "exit":
        break

    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, X)
    index = similarity.argmax()

    print("\nAnswer:", chunks[index], "\n")